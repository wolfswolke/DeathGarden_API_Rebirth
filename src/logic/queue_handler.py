import uuid
import random
from logic.time_handler import get_time
from logic.logging_handler import logger


def random_game_mode():
    MatchConfig_SLU_DownTown = {"gameMode": "4b4bbb82b85e662e5121233ae06f9b1c-Default",
                                "MatchConfiguration": "/Game/Configuration/MatchConfig/MatchConfig_SLU_DownTown.MatchConfig_SLU_DownTown"} # broken

    MatchConfig_Demo_HarvestYourExit_1v5 = {"gameMode": "789c81dfb11fe39b7247c7e488e5b0d4-Default",
                                           "MatchConfiguration": "/Game/Configuration/MatchConfig/MatchConfig_Demo_HarvestYourExit_1v5.MatchConfig_Demo_HarvestYourExit_1v5"}
    MatchConfig_Demo = {"gameMode": "08d2279d2ed3fba559918aaa08a73fa8-Default",
                        "MatchConfiguration": "/Game/Configuration/MatchConfig/MatchConfig_Demo.MatchConfig_Demo"}
    MatchConfig_ARC_Fortress = {'gameMode': 'd071fb6678668246d6d999c9892c2a60-Default',
                                'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_ARC_Fortress.MatchConfig_ARC_Fortress'}

    MatchConfig_ARC_BlastFurnace = {'gameMode': '4cb782397d46fc432d10bdc24538097a-Default',
                                    'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_ARC_BlastFurnace.MatchConfig_ARC_BlastFurnace'}
    MatchConfig_ARC_BlastFurnace_2Hunters = {'gameMode': '1760f0a98f85cf53b6011b322cad1586-Default',
                                             'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_ARC_BlastFurnace_2Hunters.MatchConfig_ARC_BlastFurnace_2Hunters'}
    MatchConfig_ARC_Expedition = {'gameMode': '3d9c3d09116d982ec7d631ae38e4628b-Default',
                                  'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_ARC_Expedition.MatchConfig_ARC_Expedition'}
    MatchConfig_ARC_Expedition_2Hunters = {'gameMode': 'a79946d18164f1b8b8589c81778ab15e-Default',
                                           'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_ARC_Expedition_2Hunters.MatchConfig_ARC_Expedition_2Hunters'}
    MatchConfig_ARC_ScrapYard = {'gameMode': 'd4e84bc42020d2daa92cf141b5f545b4-Default',
                                 'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_ARC_ScrapYard.MatchConfig_ARC_ScrapYard'}
    MatchConfig_ARC_ScrapYard_2Hunters = {'gameMode': 'cd9986d916859aa8e1ec4c5bac41d0e8-Default',
                                          'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_ARC_ScrapYard_2Hunters.MatchConfig_ARC_ScrapYard_2Hunters'}
    MatchConfig_CAV_All = {'gameMode': 'fac37036b5799852e499ce02dd716914-Default',
                           'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_CAV_All.MatchConfig_CAV_All'}  # Broken
    MatchConfig_CAV_All_2Hunters = {'gameMode': '3f1052dc0058bf795ad24f4d292b57f9-Default',
                                    'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_CAV_All_2Hunters.MatchConfig_CAV_All_2Hunters'}
    MatchConfig_Custom = {'gameMode': '401cc719864f3e7dade5291ea1399469-Default',
                          'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_Custom.MatchConfig_Custom'}
    MatchConfig_CustomMatch = {'gameMode': 'e3744bb4acbc0e5dc107e999c6132f18-Default',
                               'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_CustomMatch.MatchConfig_CustomMatch'}
    MatchConfig_Demo_2v10_4Needles = {'gameMode': 'b844f2e112df38cb1696c10012aa2976-Default',
                                      'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_Demo_2v10_4Needles.MatchConfig_Demo_2v10_4Needles'}
    MatchConfig_Demo_2v10_5Needles = {'gameMode': '5ecd49c3b64a089717e0e604bd32a76a-Default',
                                      'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_Demo_2v10_5Needles.MatchConfig_Demo_2v10_5Needles'}
    MatchConfig_Demo_2v8_4Needles = {'gameMode': 'fe29231c7bdcc6e2bc4d1891e8b9decd-Default',
                                     'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_Demo_2v8_4Needles.MatchConfig_Demo_2v8_4Needles'}
    MatchConfig_Demo_2v8_5Needles = {'gameMode': 'cfe80d8e2d9a5d1aefeac4ac5d2de3ac-Default',
                                     'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_Demo_2v8_5Needles.MatchConfig_Demo_2v8_5Needles'}
    MatchConfig_Demo_HarvestYourExit = {'gameMode': 'd4f962f287d04cb6fd266ac2b2e7705e-Default',
                                        'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_Demo_HarvestYourExit.MatchConfig_Demo_HarvestYourExit'}

    MatchConfig_DES_City = {'gameMode': 'b05564a0712a62ebe5dd2228333c9237-Default',
                            'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_DES_City.MatchConfig_DES_City'}
    MatchConfig_DES_City_2Hunters = {'gameMode': 'a0fdf9ce92261dcc5492f353b62f34f3-Default',
                                     'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_DES_City_2Hunters.MatchConfig_DES_City_2Hunters'}
    MatchConfig_DES_Fortress = {'gameMode': 'b63232e2c852823ac87bae2367edf875-Default',
                                'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_DES_Fortress.MatchConfig_DES_Fortress'}
    MatchConfig_DES_Fortress_2Hunters = {'gameMode': 'e3b6d0d277c8f36dffc0bb9f51e057c0-Default',
                                         'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_DES_Fortress_2Hunters.MatchConfig_DES_Fortress_2Hunters'}
    MatchConfig_DES_GoldRush = {'gameMode': '4b12293b22fdef0a6d2f2b21a79fa9b1-Default',
                                'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_DES_GoldRush.MatchConfig_DES_GoldRush'}
    MatchConfig_DES_GoldRush_2v10_5Needles = {'gameMode': '1a80bd0f2cec80a7a18ae6f605de788b-Default',
                                              'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_DES_GoldRush_2v10_5Needles.MatchConfig_DES_GoldRush_2v10_5Needles'}
    MatchConfig_DES_Mayan = {'gameMode': '86006559cbf3f749a73c7095f06c566c-Default',
                             'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_DES_Mayan.MatchConfig_DES_Mayan'}
    MatchConfig_DES_Mayan_2v10_5Needles = {'gameMode': '4e2d42e4448ea91914a67b60487b691f-Default',
                                           'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_DES_Mayan_2v10_5Needles.MatchConfig_DES_Mayan_2v10_5Needles'}
    MatchConfig_DES_Oilfield = {'gameMode': '7fcd68d7493bf41e57c1b9b68502a43d-Default',
                                'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_DES_Oilfield.MatchConfig_DES_Oilfield'}
    MatchConfig_DES_Oilfield_2Hunters = {'gameMode': '06dffbe8772084ece87a6c73eaf48df8-Default',
                                         'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_DES_Oilfield_2Hunters.MatchConfig_DES_Oilfield_2Hunters'}
    MatchConfig_JUN_Fortress = {'gameMode': 'b32306ecddb7a60fbbb91a872d4f15fe-Default',
                                'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_JUN_Fortress.MatchConfig_JUN_Fortress'}
    MatchConfig_JUN_Fortress_2Hunters = {'gameMode': '23eea0d20f661b516666d1151aad8718-Default',
                                         'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_JUN_Fortress_2Hunters.MatchConfig_JUN_Fortress_2Hunters'}
    MatchConfig_NewMaps = {'gameMode': 'ad4d7af5763ab472800abbe73f7d2740-Default',
                           'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_NewMaps.MatchConfig_NewMaps'}
    MatchConfig_PRM_Special = {'gameMode': 'bdf7473d4b23baae7e13a6c2c46c5094-Default',
                               'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_PRM_Special.MatchConfig_PRM_Special'}
    MatchConfig_RUI_All = {'gameMode': '027b541cfcaa4ab088dab234a02e81d3-Default',
                           'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_RUI_All.MatchConfig_RUI_All'}
    MatchConfig_RUI_All_2Hunters = {'gameMode': 'de1bb601c3dab35e896d0366da563445-Default',
                                    'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_RUI_All_2Hunters.MatchConfig_RUI_All_2Hunters'}
    MatchConfig_WA_Cemetery = {'gameMode': '9af69a666badf6b443628f7f80c58445-Default',
                               'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_WA_Cemetery.MatchConfig_WA_Cemetery'}
    MatchConfig_WA_Cemetery_2Hunters = {'gameMode': '59f81208123d114050207c04d1e9af3f-Default',
                                        'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_WA_Cemetery_2Hunters.MatchConfig_WA_Cemetery_2Hunters'}
    MatchConfig_WA_Rivers = {'gameMode': '33cbc6d506de6c85a5eead04f5a57c92-Default',
                             'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_WA_Rivers.MatchConfig_WA_Rivers'}
    MatchConfig_WA_Rivers_2Hunters = {'gameMode': 'feac811fdef1d1a2f2fc26b3c99205fd-Default',
                                      'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_WA_Rivers_2Hunters.MatchConfig_WA_Rivers_2Hunters'}

    list_of_game_modes = [MatchConfig_Demo, MatchConfig_Demo_HarvestYourExit_1v5, MatchConfig_ARC_Fortress,
                          MatchConfig_CustomMatch, MatchConfig_Demo_2v8_4Needles, MatchConfig_DES_City_2Hunters]
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
            eta_data = {
                "queueData": {
                    "ETA": -10000,
                    "position": 0,
                    "sizeA": 0,
                    "sizeB": 1
                },
                "status": "QUEUED"
            }

            queuedPlayer, index = self.getQueuedPlayer(userId)
            if not queuedPlayer:
                return {}
            if side == 'B':
                if self.openLobbies:
                    for openLobby in self.openLobbies:
                        if not openLobby.isReady or openLobby.hasStarted or openLobby.status == "CLOSED":
                            if openLobby.last_host_check < get_time()[0] - 15:
                                self.openLobbies.pop(self.openLobbies.index(openLobby))
                                logger.graylog_logger(level="info", handler="matchmaking_getQueueStatus", message="Lobby killed due to host not checking in")
                                return eta_data
                            if openLobby.host == userId:
                                self.openLobbies.pop(self.openLobbies.index(openLobby))
                                logger.graylog_logger(level="info", handler="matchmaking_getQueueStatus", message="Killed broken lobby Host on Side RUNNER.")
                                return eta_data
                    for openLobby in self.openLobbies:
                        if not openLobby.isReady or openLobby.hasStarted or openLobby.status == "CLOSED":
                            continue
                        if userId in openLobby.nonHosts:
                            data = self.createQueueResponseMatched(openLobby.host, openLobby.id, userId,
                                                                   matchConfig=openLobby.matchConfig)
                            self.queuedPlayers.pop(index)
                            return data
                        if len(openLobby.nonHosts) < 5:
                            if additional_user_ids:
                                open_slots = 5 - len(openLobby.nonHosts)
                                queued_player_count = 1 + len(additional_user_ids)
                                if queued_player_count <= open_slots:
                                    for user_id in additional_user_ids:
                                        if user_id not in openLobby.nonHosts:
                                            openLobby.nonHosts.append(user_id)
                                else:
                                    continue
                            openLobby.nonHosts.append(queuedPlayer)
                            self.queuedPlayers.pop(index)
                            data = self.createQueueResponseMatched(openLobby.host, openLobby.id, userId, matchConfig=openLobby.matchConfig)
                            if data:
                                return data
                            else:
                                return eta_data
                        else:
                            logger.graylog_logger(level="debug", handler="matchmaking_getQueueStatus",
                                                  message=f"Len Non Hosts >= 3 for {openLobby.id}")
                            return eta_data
                    logger.graylog_logger(level="debug", handler="matchmaking_getQueueStatus",message="No Open Lobbies fit the criteria.")
                    return eta_data

                else:
                    return eta_data
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
            if not lobby:
                lobby = self.getKilledLobbyById(matchId)

            if killed:
                lobby.status = "KILLED"
            current_timestamp, expiration_timestamp = get_time()
            if lobby.last_host_check < get_time()[0] - 15:
                self.openLobbies.pop(self.openLobbies.index(lobby))
                logger.graylog_logger(level="info", handler="matchmaking_createMatchResponse",
                                      message="Lobby killed due to host not checking in")
                return
            host = lobby.host
            if type(host) == QueuedPlayer:
                host = host.userId
            non_host = []
            for item in lobby.nonHosts:
                if type(item) == QueuedPlayer:
                    non_host.append(item.userId)
                else:
                    non_host.append(item)
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
