import uuid
from logic.time_handler import get_time
from logic.logging_handler import logger


class QueueData:
    def __init__(self, side):
        self.side = side


class Session:
    def __init__(self, userid, clientIds):
        self.userid = userid
        self.clientIds = clientIds


class QueuedPlayer:
    def __init__(self, userId, side, lastCheckedForMatch):
        self.userId = userId
        self.side = side
        self.lastCheckedForMatch = lastCheckedForMatch


class Lobby:
    def __init__(self, isReady, host, nonHosts, id, isPrepared, hasStarted):
        self.isReady = isReady
        self.host = host
        self.nonHosts = nonHosts
        self.id = id
        self.isPrepared = isPrepared
        self.hasStarted = hasStarted


class KilledLobby:
    def __init__(self, id, reason, killedTime):
        self.id = id
        self.reason = reason
        self.killedTime = killedTime


class MatchmakingQueue:
    def __init__(self):
        self.openLobbies = []
        self.killedLobbies = []
        self.queuedPlayers = []

    def queuePlayer(self, side, userId):
        try:
            queuedPlayer = QueuedPlayer(userId, side,
                                        get_time())
            self.queuedPlayers.append(queuedPlayer)
        except Exception as e:
            logger.graylog_logger(level="error", handler="matchmaking_queuePlayer", message=e)

    def getQueuedPlayer(self, userid):
        try:
            for i, queuedPlayer in enumerate(self.queuedPlayers):
                if queuedPlayer.userId == userid:
                    return queuedPlayer, i
            return None, -1
        except Exception as e:
            logger.graylog_logger(level="error", handler="matchmaking_getQueuedPlayer", message=e)
            return None

    def getQueueStatus(self, side, userid):
        try:
            queuedPlayer, index = self.getQueuedPlayer(userid)
            if not queuedPlayer:
                return {}
            if side == 'B':
                if self.openLobbies:
                    for openLobby in self.openLobbies:
                        if not openLobby.isReady or openLobby.hasStarted:
                            continue
                        if len(openLobby.nonHosts) < 4:
                            openLobby.nonHosts.append(queuedPlayer)
                            self.queuedPlayers.pop(index)
                            return self.createQueueResponseMatched(openLobby.host.userId, openLobby.id,
                                                                   userid)

                else:
                    return {
                        "queueData": {
                            "ETA": -10000,
                            "position": 0,
                            "sizeA": 0,
                            "sizeB": 1,
                        },
                        "status": "QUEUED",
                    }
            else:
                matchId = self.genMatchUUID()
                lobby = Lobby(False, queuedPlayer, [], matchId, False, False)
                self.openLobbies.append(lobby)
                return self.createQueueResponseMatched(userid, matchId)
        except Exception as e:
            logger.graylog_logger(level="error", handler="matchmaking_getQueueStatus", message=e)
            return None

    def removePlayerFromQueue(self, userid):
        _, index = self.getQueuedPlayer(userid)
        if index != -1:
            self.queuedPlayers.pop(index)

    def getLobbyById(self, id):
        for i, lobby in enumerate(self.openLobbies):
            if lobby.id == id:
                return lobby, i
        return None, -1

    def getKilledLobbyById(self, id):
        for killedLobby in self.killedLobbies:
            if killedLobby.id == id:
                return killedLobby
        return None

    def registerMatch(self, matchId, sessionSettings):
        lobby, _ = self.getLobbyById(matchId)
        if lobby:
            lobby.isReady = True
            lobby.sessionSettings = sessionSettings
            return self.createMatchResponse(matchId)

    def deleteMatch(self, matchId):
        lobby, index = self.getLobbyById(matchId)
        if lobby:
            self.openLobbies.pop(index)
            killedLobby = KilledLobby(lobby.id, lobby.reason, get_time())
            self.killedLobbies.append(killedLobby)

    def isOwner(self, matchId, userid):
        lobby, _ = self.getLobbyById(matchId)
        return lobby and lobby.host.userid == userid

    def deleteOldMatches(self):
        current_time = get_time()
        for i in range(len(self.killedLobbies) - 1, -1, -1):
            if self.killedLobbies[i].killedTime < current_time - 5 * 60 * 1000:
                self.killedLobbies.pop(i)

    def createMatchResponse(self, matchId, killed=False):
        try:
            lobby = self.getLobbyById(matchId)[0] or self.getKilledLobbyById(matchId)
            if not lobby:
                return {}
            return {
                "category": "Steam-te-18f25613-36778-ue4-374f864b",
                "churn": 0,
                "creationDateTime": get_time(),
                "creator": lobby.host.userId,
                "customData": {
                    "SessionSettings": lobby.sessionSettings or "",
                },
                "geolocation": {},
                "matchId": matchId,
                "props": {
                    "countA": 1,
                    "countB": 4,
                    "EncryptionKey": "Rpqy9fgpIWrHxjJpiwnJJtoZ2hbUZZ4paU+0n4K/iZI=",
                    "gameMode": "None",
                    "platform": "Windows",
                },
                "rank": 1,
                "reason": lobby.reason or "",
                "schema": 3,
                "sideA": [lobby.host.userId],
                "sideB": [player.userId for player in lobby.nonHosts],
                "skill": {
                    "continent": "NA",
                    "country": "US",
                    "latitude": 0,
                    "longitude": 0,
                    "rank": 20,
                    "rating": {
                        "rating": 1500,
                        "RD": 347.4356,
                        "volatility": 0.06,
                    },
                    "regions": {
                        "good": ["us-east-1"],
                        "ok": ["us-east-1"],
                    },
                    "version": 2,
                    "x": 20,
                },
                "status": "KILLED" if killed else "OPENED",
                "version": 2,
            }
        except Exception as e:
            logger.graylog_logger(level="error", handler="matchmaking_createMatchResponse", message=e)

    def createQueueResponseMatched(self, creatorId, matchId, joinerId=None):
        try:
            return {
                "status": "MATCHED",
                "matchData": {
                    "category": "Steam-te-18f25613-36778-ue4-374f864b",
                    "churn": 0,
                    "creationDateTime": get_time(),
                    "creator": creatorId,
                    "customData": {},
                    "geolocation": {},
                    "matchId": matchId,
                    "props": {
                        "countA": 1,
                        "countB": 4,
                        "EncryptionKey": "Rpqy9fgpIWrHxjJpiwnJJtoZ2hbUZZ4paU+0n4K/iZI=",
                        "gameMode": "None",
                        "platform": "Windows",
                    },
                    "rank": 1,
                    "reason": "",
                    "schema": 3,
                    "sideA": [creatorId],
                    "sideB": [joinerId] if joinerId else [],
                    "skill": {
                        "continent": "NA",
                        "country": "US",
                        "latitude": 0,
                        "longitude": 0,
                        "rank": 20,
                        "rating": {
                            "rating": 1500,
                            "RD": 347.4356,
                            "volatility": 0.06,
                        },
                        "regions": {
                            "good": ["us-east-1"],
                            "ok": ["us-east-1"],
                        },
                        "version": 2,
                        "x": 20,
                    },
                    "status": "CREATED",
                    "version": 1,
                },
            }
        except Exception as e:
            logger.graylog_logger(level="error", handler="matchmaking_createQueueResponseMatched", message=e)

    def getSession(self, userid):
        try:
            for lobby in self.openLobbies:
                if lobby.host.userId == userid:
                    return Session(lobby.host.userId, [player.userId for player in lobby.nonHosts])
                for player in lobby.nonHosts:
                    if player.userId == userid:
                        return Session(lobby.host.userId, [player.userId for player in lobby.nonHosts])
            return None
        except Exception as e:
            logger.graylog_logger(level="error", handler="getSession", message=e)

    def genMatchUUID(self):
        return str(uuid.uuid4())


matchmaking_queue = MatchmakingQueue()
