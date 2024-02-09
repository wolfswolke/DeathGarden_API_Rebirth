import uuid
import random
from logic.time_handler import get_time
from logic.logging_handler import logger


def random_game_mode():
    MatchConfig_SLU_DownTown = {"gameMode": "4b4bbb82b85e662e5121233ae06f9b1c-Default",
                                "MatchConfiguration": "/Game/Configuration/MatchConfig/MatchConfig_SLU_DownTown.MatchConfig_SLU_DownTown"}

    MatchConfig_Demo_HarvestYourExit_1v5 = {"gameMode": "789c81dfb11fe39b7247c7e488e5b0d4-Default",
                                           "MatchConfiguration": "/Game/Configuration/MatchConfig/MatchConfig_Demo_HarvestYourExit_1v5.MatchConfig_Demo_HarvestYourExit_1v5"}
    MatchConfig_Demo = {"gameMode": "08d2279d2ed3fba559918aaa08a73fa8-Default",
                        "MatchConfiguration": "/Game/Configuration/MatchConfig/MatchConfig_Demo.MatchConfig_Demo"}

    list_of_game_modes = [MatchConfig_Demo, MatchConfig_Demo_HarvestYourExit_1v5]
    return random.choice(list_of_game_modes)



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
    def __init__(self, isReady, host, nonHosts, id, isPrepared, hasStarted, status, MatchConfig, last_host_check):
        self.isReady = isReady
        self.host = host
        self.nonHosts = nonHosts
        self.id = id
        self.isPrepared = isPrepared
        self.hasStarted = hasStarted
        self.status = status
        self.matchConfig = MatchConfig
        self.last_host_check = last_host_check


class KilledLobby:
    def __init__(self, id, reason, killedTime, host):
        self.id = id
        self.reason = reason
        self.killedTime = killedTime
        self.host = host


class MatchmakingQueue:
    def __init__(self):
        self.openLobbies = []
        self.killedLobbies = []
        self.queuedPlayers = []
        self.devs = ["a"]
        # "95041085-e7e4-4759-be3d-e72c69167578", "00658d11-2dfd-41e8-b6d2-2462e8f3aa47", "619d6f42-db87-4f3e-8dc9-3c9995613614"

    def queuePlayer(self, side, userId):
        try:
            current_timestamp, expiration_timestamp = get_time()
            queuedPlayer = QueuedPlayer(userId, side,
                                        current_timestamp)
            if userId in [player.userId for player in self.queuedPlayers]:
                return
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

    def getQueueStatus(self, side, userId, region, additional_user_ids=None):
        try:
            #if additional_user_ids:
            #    for additional_user_id in additional_user_ids:
            #        queuedPlayer, index = self.getQueuedPlayer(additional_user_id)

            queuedPlayer, index = self.getQueuedPlayer(userId)
            if not queuedPlayer:
                return {}
            if side == 'B':
                if self.openLobbies:
                    for openLobby in self.openLobbies:
                        if openLobby.last_host_check < get_time()[0] - 15:
                            self.openLobbies.pop(self.openLobbies.index(openLobby))
                            logger.graylog_logger(level="info", handler="matchmaking_getQueueStatus", message="Lobby killed due to host not checking in")
                        if openLobby.host == userId:
                            self.openLobbies.pop(self.openLobbies.index(openLobby))
                            logger.graylog_logger(level="info", handler="matchmaking_getQueueStatus", message="Killed broken lobby")
                    for openLobby in self.openLobbies:
                        if not openLobby.isReady or openLobby.hasStarted or openLobby.status == "CLOSED":
                            continue
                        if len(openLobby.nonHosts) < 5:
                            openLobby.nonHosts.append(queuedPlayer)
                            self.queuedPlayers.pop(index)
                            data = self.createQueueResponseMatched(openLobby.host, openLobby.id, userId, matchConfig=openLobby.matchConfig)
                            if data:
                                return data
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
                            logger.graylog_logger(level="debug", handler="matchmaking_getQueueStatus",
                                                  message=f"Len Non Hosts >= 3 for {openLobby.id}")
                            return {
                                "queueData": {
                                    "ETA": -10000,
                                    "position": 0,
                                    "sizeA": 0,
                                    "sizeB": 1,
                                },
                                "status": "QUEUED",
                            }
                    logger.graylog_logger(level="debug", handler="matchmaking_getQueueStatus",message="No Open Lobbies")
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
                if self.openLobbies:
                    for openLobby in self.openLobbies:
                        if openLobby.host == userId:
                            self.openLobbies.pop(self.openLobbies.index(openLobby))
                            logger.graylog_logger(level="info", handler="matchmaking_getQueueStatus",
                                                  message="Killed broken lobby")
                matchId = self.genMatchUUID()
                Match_Config = random_game_mode()
                current_time = get_time()[0]
                lobby = Lobby(isReady=False, host=queuedPlayer, nonHosts=[], id=matchId, isPrepared=False,
                              hasStarted=False, status="OPENED", MatchConfig=Match_Config, last_host_check=current_time)
                self.openLobbies.append(lobby)
                self.queuedPlayers.pop(index)
                return self.createQueueResponseMatched(userId, matchId, region=region, matchConfig=Match_Config)
        except Exception as e:
            logger.graylog_logger(level="error", handler="matchmaking_getQueueStatus", message=e)
            return None

    def removePlayerFromQueue(self, userid):
        _, index = self.getQueuedPlayer(userid)
        if index != -1:
            self.queuedPlayers.pop(index)

    def remove_player_from_match(self, matchId, userId):
        try:
            lobby, _ = self.getLobbyById(matchId)
            if lobby:
                for i, player in enumerate(lobby.nonHosts):
                    if player.userId == userId:
                        lobby.nonHosts.pop(i)
                        break
            return {"status": "success"}
        except Exception as e:
            logger.graylog_logger(level="error", handler="remove_player_from_match", message=e)
            return {"status": "error"}

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
            return self.createMatchResponse(matchId=matchId, userId=userId)

    def closeMatch(self, matchId):
        lobby, _ = self.getLobbyById(matchId)
        if lobby:
            lobby.status = "CLOSED"
            return self.createMatchResponse(matchId=matchId)

    def deleteMatch(self, matchId):
        lobby, index = self.getLobbyById(matchId)
        if lobby:
            self.openLobbies.pop(index)
            current_timestamp, expiration_timestamp = get_time()
            killedLobby = KilledLobby(lobby.id, "killed_by_host", current_timestamp, lobby.host)
            self.killedLobbies.append(killedLobby)

    def isOwner(self, matchId, userid):
        lobby, _ = self.getLobbyById(matchId)
        return lobby and lobby.host == userid

    def deleteOldMatches(self):
        current_time = get_time()
        for i in range(len(self.killedLobbies) - 1, -1, -1):
            if self.killedLobbies[i].killedTime < current_time - 5 * 60 * 1000:
                self.killedLobbies.pop(i)

    def createMatchResponse(self, matchId, killed=None, userId=None):
        try:
            if userId in self.devs:
                countA = 1
                countB = 1
            else:
                countA = 1
                countB = 5
            lobby_temp, id_temp = self.getLobbyById(matchId)
            if lobby_temp.host == userId:
                # lobby.last_host_check = get_time()[0] + 3
                self.openLobbies[id_temp].last_host_check = get_time()[0] + 3
            lobby, id = self.getLobbyById(matchId)
            logger.graylog_logger(level="info", handler="matchmaking_createMatchResponse", message=f"current_time: {get_time()[0]}")
            logger.graylog_logger(level="info", handler="matchmaking_createMatchResponse", message=f"last_host_check: {lobby.last_host_check}")
            if lobby.last_host_check < get_time()[0] - 15:
                self.openLobbies.pop(self.openLobbies.index(lobby))
                logger.graylog_logger(level="info", handler="matchmaking_createMatchResponse",
                                      message="Lobby killed due to host not checking in")
            if not lobby:
                lobby = self.getKilledLobbyById(matchId)
            host = lobby.host
            if type(host) == QueuedPlayer:
                host = host.userId
            non_host = []
            for item in lobby.nonHosts:
                if type(item) == QueuedPlayer:
                    non_host.append(item.userId)
                else:
                    non_host.append(item)

            if killed:
                lobby.status = "KILLED"
            current_timestamp, expiration_timestamp = get_time()
            try:
                sessionSettings = lobby.sessionSettings
            except:
                sessionSettings = ""
            gameMode = lobby.matchConfig["gameMode"]
            MatchConfiguration = lobby.matchConfig["MatchConfiguration"]

            return {
                "Category": "Steam-te-18f25613-36778-ue4-374f864b",
                "creationDateTime": current_timestamp,
                "creator": host,
                "customData": {
                    "SessionSettings": sessionSettings,
                },
                "MatchId": matchId,
                "props": {
                    "countA": countA,
                    "countB": countB,
                    "gameMode": gameMode,
                    "MatchConfiguration": MatchConfiguration,
                    "platform": "Windows",
                },
                "rank": 1,
                "Schema": 3,
                "sideA": [host],
                "sideB": [player.userId for player in lobby.nonHosts],
                "Players": [host] + non_host,
                "status": lobby.status
            }
        except Exception as e:
            logger.graylog_logger(level="error", handler="matchmaking_createMatchResponse", message=e)

    def createQueueResponseMatched(self, creatorId, matchId, joinerId=None, region=None, matchConfig=None):
        try:
            lobby, index = self.getLobbyById(matchId)
            self.openLobbies[index].last_host_check = get_time()[0] + 3
            if region:
                countA = 1
                countB = 1
            else:
                countA = 1
                countB = 5
            current_timestamp, expiration_timestamp = get_time()
            gameMode = matchConfig["gameMode"]
            MatchConfiguration = matchConfig["MatchConfiguration"]
            return {
                "status": "MATCHED",
                "matchData": {
                    "category": "Steam-te-18f25613-36778-ue4-374f864b",
                    "creationDateTime": current_timestamp,
                    "creator": creatorId,
                    "customData": {},
                    "matchId": matchId,
                    "props": {
                        "countA": countA,
                        "countB": countB,
                        "gameMode": gameMode,
                        "MatchConfiguration": MatchConfiguration,
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

    def clear_queue(self):
        self.queuedPlayers = []
        self.openLobbies = []
        self.killedLobbies = []
        return {"status": "success"}


matchmaking_queue = MatchmakingQueue()
