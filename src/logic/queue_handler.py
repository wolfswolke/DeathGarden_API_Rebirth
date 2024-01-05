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

    def __repr__(self):
        return f"QueuedPlayer(userId={self.userId}, side={self.side}, lastCheckedForMatch={self.lastCheckedForMatch})"


class Lobby:
    def __init__(self, isReady, host, nonHosts, id, isPrepared, hasStarted):
        self.isReady = isReady
        self.host = host
        self.nonHosts = nonHosts
        self.id = id
        self.isPrepared = isPrepared
        self.hasStarted = hasStarted
        self.status = "OPENED"


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
            current_timestamp, expiration_timestamp = get_time()
            queuedPlayer = QueuedPlayer(userId, side,
                                        current_timestamp)
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

    def getQueueStatus(self, side, userId, region):
        try:
            queuedPlayer, index = self.getQueuedPlayer(userId)
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
                            return self.createQueueResponseMatched(openLobby.host, openLobby.id, userId)

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
                return self.createQueueResponseMatched(userId, matchId)
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

    def registerMatch(self, matchId, sessionSettings, userId):
        lobby, _ = self.getLobbyById(matchId)
        if lobby:
            lobby.host = userId
            lobby.isReady = True
            lobby.sessionSettings = sessionSettings
            return self.createMatchResponse(matchId)

    def closeMatch(self, matchId):
        lobby, _ = self.getLobbyById(matchId)
        if lobby:
            lobby.status = "CLOSED"
            return self.createMatchResponse(matchId)

    def deleteMatch(self, matchId):
        lobby, index = self.getLobbyById(matchId)
        logger.graylog_logger(level="info", handler="deleteMatch", message=f"Deleting Match: {matchId}")
        if lobby:
            self.openLobbies.pop(index)
            current_timestamp, expiration_timestamp = get_time()
            killedLobby = KilledLobby(lobby.id, "killed_by_host", current_timestamp)
            self.killedLobbies.append(killedLobby)

    def isOwner(self, matchId, userid):
        lobby, _ = self.getLobbyById(matchId)
        return lobby and lobby.host == userid

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
            host = lobby.host
            if killed:
                lobby.status = "KILLED"
            current_timestamp, expiration_timestamp = get_time()
            try:
                sessionSettings = lobby.sessionSettings
            except:
                sessionSettings = ""
            return {
                "Category": "Steam-te-18f25613-36778-ue4-374f864b",
                "creationDateTime": current_timestamp,
                "creator": host,
                "customData": {
                    "SessionSettings": sessionSettings,
                },
                "MatchId": matchId,
                "props": {
                    "countA": 1,
                    "countB": 4,
                    "EncryptionKey": "Rpqy9fgpIWrHxjJpiwnJJtoZ2hbUZZ4paU+0n4K/iZI=",
                    "gameMode": "4cb782397d46fc432d10bdc24538097a",
                    "platform": "Windows",
                },
                "rank": 1,
                "Schema": 3,
                "sideA": [host],
                "sideB": [player.userId for player in lobby.nonHosts],
                "Players": [host] + [player.userId for player in lobby.nonHosts],
                "status": lobby.status
            }
        except Exception as e:
            logger.graylog_logger(level="error", handler="matchmaking_createMatchResponse", message=e)

    def createQueueResponseMatched(self, creatorId, matchId, joinerId=None):
        try:
            current_timestamp, expiration_timestamp = get_time()
            return {
                "status": "MATCHED",
                "matchData": {
                    "category": "Steam-te-18f25613-36778-ue4-374f864b",
                    "creationDateTime": current_timestamp,
                    "creator": creatorId,
                    "customData": {},
                    "matchId": matchId,
                    "props": {
                        "countA": 1,
                        "countB": 5,
                        "EncryptionKey": "Rpqy9fgpIWrHxjJpiwnJJtoZ2hbUZZ4paU+0n4K/iZI=",
                        "gameMode": "4cb782397d46fc432d10bdc24538097a",
                        "platform": "Windows",
                    },
                    "rank": 1,
                    "schema": 3,
                    "sideA": [creatorId],
                    "sideB": [joinerId] if joinerId else [],
                    "Players": [creatorId] + ([joinerId] if joinerId else []),
                    "status": "CREATED"
                },
            }
        except Exception as e:
            logger.graylog_logger(level="error", handler="matchmaking_createQueueResponseMatched", message=e)

    def getSession(self, userid):
        try:
            for lobby in self.openLobbies:
                if lobby.host == userid:
                    return Session(lobby.host, [player.userId for player in lobby.nonHosts])
                for player in lobby.nonHosts:
                    if player.userId == userid:
                        return Session(lobby.host, [player.userId for player in lobby.nonHosts])
            return None
        except Exception as e:
            logger.graylog_logger(level="error", handler="getSession", message=e)

    def genMatchUUID(self):
        return str(uuid.uuid4())

    def remove_user_from_Match(self, matchId, userId):
        try:
            lobby, _ = self.getLobbyById(matchId)
            if lobby:
                if lobby.host == userId:
                    self.deleteMatch(matchId)
                else:
                    for i, player in enumerate(lobby.nonHosts):
                        if player.userId == userId:
                            lobby.nonHosts.pop(i)
                            break
            return {"status": "success"}
        except Exception as e:
            logger.graylog_logger(level="error", handler="remove_user_from_Match", message=e)
            return {"status": "error"}


matchmaking_queue = MatchmakingQueue()
