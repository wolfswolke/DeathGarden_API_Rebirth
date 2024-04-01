import hashlib
import os
import threading
import uuid
import random
from collections import Counter
from logic.time_handler import get_time
from logic.logging_handler import logger

mirrors_match_status = ["None", "NoMatch", "Created", "Creating", "DelayedCreation", "Opened", "Completed", "Timedout",
                        "Closing", "Closed", "Killing", "Killed", "Destroyed"]


def random_game_mode(match_config=None):
    if match_config:
        md5 = hashlib.md5(match_config.encode('utf-8')).hexdigest()
        return {'gameMode': f'{md5}-Default',
                'MatchConfiguration': match_config}

    MatchConfig_SLU_DownTown = {"gameMode": "4b4bbb82b85e662e5121233ae06f9b1c-Default",
                                "MatchConfiguration": "/Game/Configuration/MatchConfig/MatchConfig_SLU_DownTown.MatchConfig_SLU_DownTown"}  # broken

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
                               'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_CustomMatch.MatchConfig_CustomMatch'}  # Broken
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
                                     'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_DES_City_2Hunters.MatchConfig_DES_City_2Hunters'}  # Broken
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

    high_probability = [MatchConfig_WA_Rivers, MatchConfig_WA_Cemetery, MatchConfig_DES_Oilfield] * 3
    normal_probability = [MatchConfig_ARC_BlastFurnace, MatchConfig_DES_Mayan, MatchConfig_ARC_Expedition] * 2
    low_probability = [MatchConfig_RUI_All, MatchConfig_ARC_Fortress]
    probability_list = high_probability + normal_probability + low_probability
    return random.choice(probability_list)


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
    def __init__(self, isReady, host, nonHosts, id, isPrepared, hasStarted, status, MatchConfig, last_host_check,
                 is_private=False):
        self.isReady = isReady
        self.host = host
        self.nonHosts = nonHosts
        self.id = id
        self.isPrepared = isPrepared
        self.hasStarted = hasStarted
        self.status = status
        self.matchConfig = MatchConfig
        self.last_host_check = last_host_check
        self.is_private = is_private


class KilledLobby:
    def __init__(self, id, reason, killedTime, lobby):
        self.id = id
        self.reason = reason
        self.killedTime = killedTime
        self.lobby = lobby


class MatchmakingQueue:
    def __init__(self):
        self.openLobbies = []
        self.killedLobbies = []
        self.queuedPlayers = []
        self.matchmaking_lock = threading.Lock()

    def cleanup_queue_players(self):
        for i, player in enumerate(self.queuedPlayers):
            if player.lastCheckedForMatch < get_time()[0] - 15:
                self.queuedPlayers.pop(i)
                logger.graylog_logger(level="info", handler="cleanup_queue_players",
                                      message="Removed player from queue due to timeout.")

    def queuePlayer(self, side, userId):
        self.cleanup_queue_players()
        try:
            # Check if user is owner of broken lobby
            for openLobby in self.openLobbies:
                if openLobby.host == userId:
                    if openLobby.is_private:
                        continue
                    if not openLobby.hasStarted or not openLobby.status == "CLOSED":
                        self.openLobbies.pop(self.openLobbies.index(openLobby))
                        logger.graylog_logger(level="info", handler="matchmaking_queuePlayer",
                                              message="Killed broken lobby from queuePlayer")
            current_timestamp, expiration_timestamp = get_time()

            # check if user is already in queue
            if userId in [player.userId for player in self.queuedPlayers]:
                return
            queued_player = QueuedPlayer(userId, side,
                                         current_timestamp)
            if userId in [player.userId for player in self.queuedPlayers]:
                return
            logger.graylog_logger(level="debug", handler="matchmaking_queuePlayer", message=f"Queued Player {userId}")
            self.queuedPlayers.append(queued_player)
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
        with self.matchmaking_lock:
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

                self.cleanup_queue_players()
                for player in self.queuedPlayers:
                    if player.userId == userId:
                        player.lastCheckedForMatch = get_time()[0]

                queuedPlayer, index = self.getQueuedPlayer(userId)
                if not queuedPlayer:
                    return {}

                if os.environ['DEV'] == "true":
                    max_players_b = 5
                else:
                    max_players_b = 5
                # TEMP
                for openLobby in self.openLobbies:
                    if openLobby.is_private:
                        is_non_host = False
                        for user in openLobby.nonHosts:
                            if userId == user.userId:
                                is_non_host = True
                        if is_non_host:
                            data = self.createQueueResponseMatched(openLobby.host, openLobby.id, userId,
                                                                   matchConfig=openLobby.matchConfig)
                        elif userId == openLobby.host:
                            current_timestamp, expiration_timestamp = get_time()
                            gameMode = openLobby.matchConfig["gameMode"]
                            MatchConfiguration = openLobby.matchConfig["MatchConfiguration"]
                            countB = len(openLobby.nonHosts)
                            logger.graylog_logger(level="debug", handler="fu",
                                                  message=f"noHosts is {openLobby.nonHosts}")
                            users = []
                            for element in openLobby.nonHosts:
                                logger.graylog_logger(level="debug", handler="fu", message=f"ELEMENT {element}")
                            for user in openLobby.nonHosts:
                                users.append(user.userId)
                            if type(openLobby.host) == QueuedPlayer:
                                host = openLobby.host.userId
                            else:
                                host = openLobby.host
                            users_with_host = users.copy()
                            users_with_host.append(host)
                            logger.graylog_logger(level="debug",
                                                  handler="fu",
                                                  message=f"H: {host}, Useres: {users}, UWH: {users_with_host}, HID: {openLobby.host}")
                            return {
                                "status": "MATCHED",
                                "matchData": {
                                    "category": "Steam-te-18f25613-36778-ue4-374f864b",
                                    "creationDateTime": current_timestamp,
                                    "creator": openLobby.host,
                                    "customData": {},
                                    "matchId": openLobby.id,
                                    "props": {
                                        "countA": 1,
                                        "countB": countB,
                                        "gameMode": gameMode,
                                        "MatchConfiguration": MatchConfiguration,
                                        "platform": "Windows",
                                    },
                                    "rank": 1,
                                    "schema": 3,
                                    "sideA": [host],
                                    "sideB": users,
                                    "Players": users_with_host,
                                    "status": "CREATED"
                                },
                            }
                        else:
                            logger.graylog_logger(level="debug", handler="matchmaking_getQueueStatus",
                                                  message="ERROR???")
                        self.queuedPlayers.pop(index)
                        return data
                    else:
                        continue

                if side == 'B':
                    if self.openLobbies:
                        for openLobby in self.openLobbies:
                            if not openLobby.status == "CLOSED":
                                if openLobby.last_host_check < get_time()[0] - 15:
                                    self.openLobbies.pop(self.openLobbies.index(openLobby))
                                    logger.graylog_logger(level="info", handler="matchmaking_getQueueStatus",
                                                          message="Lobby killed due to host not checking in")
                                    return eta_data
                                if openLobby.host == userId:
                                    if openLobby.is_private:
                                        logger.graylog_logger(level="debug", handler="matchmaking_getQueueStatus",
                                                              message="Lobby is private CHECK 1")
                                        continue
                                    logger.graylog_logger(level="info", handler="matchmaking_getQueueStatus",
                                                          message=f"Kill lobby due to host not checking in: {openLobby.id}"
                                                                  f", index: {index}, val: "
                                                                  f"{self.openLobbies.index(openLobby)}")
                                    self.openLobbies.pop(self.openLobbies.index(openLobby))
                                    logger.graylog_logger(level="info", handler="matchmaking_getQueueStatus",
                                                          message="Killed broken lobby Host on Side RUNNER.")
                                    return eta_data
                        for openLobby in self.openLobbies:
                            if not openLobby.isReady or openLobby.hasStarted or openLobby.status == "CLOSED" or openLobby.status == "KILLED":
                                continue

                            # Private match logic
                            if openLobby.is_private:
                                logger.graylog_logger(level="debug", handler="matchmaking_getQueueStatus",
                                                      message="Lobby is private")
                                if userId in openLobby.nonHosts or userId == openLobby.host:
                                    data = self.createQueueResponseMatched(openLobby.host, openLobby.id, userId,
                                                                           matchConfig=openLobby.matchConfig, SessionSettings=openLobby.SessionSettings)
                                    self.queuedPlayers.pop(index)
                                    return data
                                else:
                                    continue
                            else:
                                logger.graylog_logger(level="debug", handler="matchmaking_getQueueStatus",
                                                      message="Lobby is NOT private")

                            if userId in openLobby.nonHosts:
                                data = self.createQueueResponseMatched(openLobby.host, openLobby.id, userId,
                                                                       matchConfig=openLobby.matchConfig, SessionSettings=openLobby.SessionSettings)
                                self.queuedPlayers.pop(index)
                                return data
                            if len(openLobby.nonHosts) < max_players_b:
                                logger.graylog_logger(level="debug", handler="matchmaking_getQueueStatus",
                                                      message=f"Len is {len(openLobby.nonHosts)}")
                                if additional_user_ids:
                                    open_slots = max_players_b - len(openLobby.nonHosts)
                                    queued_player_count = 1 + len(additional_user_ids)
                                    if queued_player_count <= open_slots:
                                        for user_id in additional_user_ids:
                                            if user_id not in openLobby.nonHosts:
                                                openLobby.nonHosts.append(user_id)
                                                additional_queuedPlayer, additional_index = self.getQueuedPlayer(
                                                    user_id)
                                                self.queuedPlayers.pop(additional_index)
                                    else:
                                        continue
                                openLobby.nonHosts.append(queuedPlayer)
                                self.queuedPlayers.pop(index)
                                data = self.createQueueResponseMatched(openLobby.host, openLobby.id, userId,
                                                                       matchConfig=openLobby.matchConfig,
                                                                       SessionSettings=openLobby.SessionSettings)
                                if data:
                                    return data
                                else:
                                    return eta_data
                            else:
                                logger.graylog_logger(level="debug", handler="matchmaking_getQueueStatus",
                                                      message=f"Len Non Hosts >= 3 for {openLobby.id}")
                                return eta_data
                        logger.graylog_logger(level="debug", handler="matchmaking_getQueueStatus",
                                              message="No Open Lobbies fit the criteria.")
                        return eta_data

                    else:
                        return eta_data
                else:
                    if self.openLobbies:
                        for openLobby in self.openLobbies:
                            if openLobby.is_private:
                                if userId == openLobby.host:
                                    data = self.createQueueResponseMatched(openLobby.host, openLobby.id, userId,
                                                                           matchConfig=openLobby.matchConfig, SessionSettings=openLobby.SessionSettings)
                                    self.queuedPlayers.pop(index)
                                    return data
                                else:
                                    continue
                            if openLobby.host == userId:
                                self.openLobbies.pop(self.openLobbies.index(openLobby))
                                logger.graylog_logger(level="info", handler="matchmaking_getQueueStatus",
                                                      message="Killed broken lobby")
                    matchId = self.genMatchUUID()
                    Match_Config = random_game_mode()
                    current_time = get_time()[0]
                    lobby = Lobby(isReady=False, host=queuedPlayer, nonHosts=[], id=matchId, isPrepared=False,
                                  hasStarted=False, status="OPENED", MatchConfig=Match_Config,
                                  last_host_check=current_time, is_private=False)
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

    def register_private_match(self, players_a, players_b, match_config):
        match_id = self.genMatchUUID()
        current_time = get_time()[0]
        Match_Config = random_game_mode(match_config)
        for player_a in players_a:
            self.queuePlayer("A", player_a)
        for player_b in players_b:
            self.queuePlayer("B", player_b)
        queuedPlayers = []
        for player_b in players_b:
            queuedPlayer, index = self.getQueuedPlayer(player_b)
            queuedPlayers.append(queuedPlayer)
            logger.graylog_logger(level="debug", handler="fu", message=f"QP {queuedPlayer}")
        logger.graylog_logger(level="debug", handler="fy", message=f"PA {players_a}, PB {players_b}, MC {Match_Config}")
        lobby = Lobby(isReady=False, host=players_a[0], nonHosts=queuedPlayers, id=match_id, isPrepared=False,
                      hasStarted=False, status="OPENED", MatchConfig=Match_Config, last_host_check=current_time,
                      is_private=True)
        self.openLobbies.append(lobby)
        return match_id, Match_Config

    def registerMatch(self, matchId, sessionSettings, userId):
        lobby, _ = self.getLobbyById(matchId)
        if lobby:
            lobby.host = userId
            lobby.isReady = True
            lobby.SessionSettings = sessionSettings
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
            killedLobby = KilledLobby(lobby.id, "killed_by_host", current_timestamp, lobby=lobby)
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
            if os.environ['DEV'] == "true":
                countA = 1
                countB = 5
            else:
                countA = 1
                countB = 5
            lobby_temp, id_temp = self.getLobbyById(matchId)
            if lobby_temp is None:
                logger.graylog_logger(level="debug", handler="createMatchResponse",
                                      message="Returning NONE in lobby_temp because TEMP none.")
                return
            if lobby_temp.host == userId:
                # lobby.last_host_check = get_time()[0] + 3
                self.openLobbies[id_temp].last_host_check = get_time()[0] + 3
            lobby, id = self.getLobbyById(matchId)
            if not lobby:
                lobby = self.getKilledLobbyById(matchId)

            if killed:
                lobby.status = "KILLED"
            current_timestamp, expiration_timestamp = get_time()
            if not lobby.isReady or lobby.hasStarted or lobby.status == "CLOSED":
                if lobby.last_host_check < get_time()[0] - 15:
                    self.openLobbies.pop(self.openLobbies.index(lobby))
                    logger.graylog_logger(level="info", handler="matchmaking_createMatchResponse",
                                          message="Lobby killed due to host not checking in, Returning NONE")
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
                SessionSettings = lobby.SessionSettings
            except:
                SessionSettings = ""
            gameMode = lobby.matchConfig["gameMode"]
            MatchConfiguration = lobby.matchConfig["MatchConfiguration"]
            if host == "147d48b8-6c71-456c-8c72-8d75cff31c51":
                sideA = []
                players = non_host
            else:
                players = [host] + non_host
                sideA = [host]
            return {
                "Category": "Steam-te-18f25613-36778-ue4-374f864b",
                "creationDateTime": current_timestamp,
                "creator": host,
                "customData": {
                    "SessionSettings": SessionSettings,
                },
                "MatchId": matchId,
                "props": {
                    "countA": countA,
                    "countB": countB,
                    "gameMode": gameMode,
                    "MatchConfiguration": MatchConfiguration,
                    "platform": "",
                    "EncryptionKey": "fZ6lAM3Y3XNNz5qH86cgUP6Q0Bh7\/Y72yQMfW\/9nh74=",
                },
                "skill": [],
                "reason": "",
                "region": "all",
                "geolocation": [],
                "version": 2,
                "churn": 0,
                "rank": 1,
                "Schema": 3,
                "sideA": sideA,
                "sideB": [player.userId for player in lobby.nonHosts],
                "Players": players,
                "status": lobby.status
            }
        except Exception as e:
            logger.graylog_logger(level="error", handler="matchmaking_createMatchResponse", message=e)

    def createQueueResponseMatched(self, creatorId, matchId, joinerId=None, region=None, matchConfig=None, SessionSettings=None):
        try:
            if os.environ['DEV'] == "true":
                countA = 1
                countB = 5
            else:
                countA = 1
                countB = 5
            current_timestamp, expiration_timestamp = get_time()
            gameMode = matchConfig["gameMode"]
            MatchConfiguration = matchConfig["MatchConfiguration"]
            if creatorId == "147d48b8-6c71-456c-8c72-8d75cff31c51":
                host = []
                players = ([joinerId] if joinerId else [])
            else:
                host = [creatorId]
                players = [creatorId] + ([joinerId] if joinerId else [])
            return {
                "status": "MATCHED",
                "matchData": {
                    "category": "Steam-te-18f25613-36778-ue4-374f864b",
                    "creationDateTime": current_timestamp,
                    "creator": creatorId,
                    "customData": {
                        "SessionSettings": SessionSettings
                    },
                    "matchId": matchId,
                    "props": {
                        "countA": countA,
                        "countB": countB,
                        "gameMode": gameMode,
                        "MatchConfiguration": MatchConfiguration,
                        "platform": "",
                        "EncryptionKey": "fZ6lAM3Y3XNNz5qH86cgUP6Q0Bh7\/Y72yQMfW\/9nh74=",
                    },
                    "rank": 1,
                    "schema": 3,
                    "skill": [],
                    "reason": "",
                    "region": "all",
                    "geolocation": [],
                    "version": 2,
                    "churn": 0,
                    "sideA": host,
                    "sideB": [joinerId] if joinerId else [],
                    "Players": players,
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
        open_lobbies = self.openLobbies
        for lobby in open_lobbies:
            match_id = lobby.id
            self.deleteMatch(match_id)
            logger.graylog_logger(level="info", handler="clear_queue",
                                  message=f"Killed lobby: {match_id} with CLEAR_QUEUE")
        return {"status": "success"}

    def get_len_of_queue(self):
        length = len(self.queuedPlayers)
        return int(length)

    def get_len_of_killed_lobbies(self):
        length = len(self.killedLobbies)
        return int(length)

    def get_len_of_queued_runners(self):
        length = len([player for player in self.queuedPlayers if player.side == "B"])
        return int(length)

    def get_len_of_queued_hunters(self):
        length = len([player for player in self.queuedPlayers if player.side == "A"])
        return int(length)

    def get_len_of_open_lobbies(self):
        length = len(self.openLobbies)
        return int(length)

    def get_lobby_data(self):
        return self.openLobbies


matchmaking_queue = MatchmakingQueue()
