import json
import os
from datetime import datetime

from logic.time_handler import get_time
from logic.queue_handler import matchmaking_queue
from flask_definitions import *


@app.route("/api/v1/config/MATCH_MAKING_REGIONS/raw", methods=["GET"])
def match_making_regions_raw():
    check_for_game_client("strict")
    try:
        return jsonify(["EU"])
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="matchmaking_RegionsRAW", message=e)


@app.route("/api/v1/queue/info", methods=["GET"])
def queue_info():
    try:
        # ?category=Steam-te-23ebf96c-27498-ue4-7172a3f5&gameMode=Default&region=US&countA=1&countB=5
        check_for_game_client("strict")
        session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
        userid = session_manager.get_user_id(session_cookie)

        # USER BAN CHECK
        try:
            u_data = mongo.get_data_with_list(login=userid, login_steam=False, items={"is_banned"})["is_banned"]
            if u_data:
                return jsonify({"message": "User is banned", "status": "error"}), 401
        except Exception as e:
            logger.graylog_logger(level="error", handler="extension_progression_init_or_get_groups", message=e)
            return jsonify({"status": "error"})

        category = sanitize_input(request.args.get("category"))
        game_mode = sanitize_input(request.args.get("gameMode"))
        region = sanitize_input(request.args.get("region"))
        count_a = request.args.get("countA")  # Hunter Count
        count_b = request.args.get("countB")  # Runner Count
        side = sanitize_input(request.args.get("side", ""))
        session = matchmaking_queue.getSession(userid)
        if not side:
            return jsonify({"A": {"Size": 1, "ETA": 100, "stable": True}, "B": {"Size": 5, "ETA": 100, "stable": True},
                            "SizeA": count_a, "SizeB": count_b})

        if side not in ["A", "B"]:
            return jsonify({"message": "Invalid side parameter"}), 400

        response_data = matchmaking_queue.getQueueStatus(side, session, region)
        return jsonify(response_data)
        # return jsonify({"A": {"Size": 1, "ETA": 100, "stable": True}, "B": {"Size": 5, "ETA": 100, "stable": True}, "SizeA": count_a, "SizeB": count_b})
    except TimeoutError:
        return jsonify({"status": "TimeoutError"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="queue_info", message=e)


@app.route("/api/v1/queue", methods=["POST"])
def queue():
    # {"category":"Steam-te-18f25613-36778-ue4-374f864b","rank":1,"side":"B","latencies":[],"additionalUserIds":[],
    # "checkOnly":false,"gameMode":"08d2279d2ed3fba559918aaa08a73fa8-Default","region":"US","countA":1,"countB":5}
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    # USER BAN CHECK
    try:
        u_data = mongo.get_data_with_list(login=userid, login_steam=False, items={"is_banned"})["is_banned"]
        if u_data:
            return jsonify({"message": "User is banned", "status": "error"}), 401
    except Exception as e:
        logger.graylog_logger(level="error", handler="extension_progression_init_or_get_groups", message=e)
        return jsonify({"status": "error"})

    category = sanitize_input(request.json.get("category"))
    rank = request.json.get("rank")
    side = sanitize_input(request.json.get("side"))
    latencies = sanitize_input("latencies")
    additional_user_ids = request.json.get("additionalUserIds")
    check_only = request.json.get("checkOnly")  # False = Searching. True = Is searching and waiting for match
    game_mode = sanitize_input(request.json.get("gameMode"))
    region = sanitize_input(request.json.get("region"))
    count_a = request.json.get("countA")
    count_b = request.json.get("countB")
    if additional_user_ids:
        logger.graylog_logger(level="info",
                              handler="logging_queue",
                              message=f"User {userid} is queueing for {category} in "
                                      f"{region} with {count_a} hunters and {count_b} "
                                      f"runners and these additional Users {additional_user_ids}")
    else:
        logger.graylog_logger(level="info", handler="logging_queue",
                              message=f"User {userid} is queueing for {category} in {region} with "
                                      f"{count_a} hunters and {count_b} runners")
    try:
        if not check_only:
            matchmaking_queue.queuePlayer(side=side, userId=userid)
            if additional_user_ids:
                for user in additional_user_ids:
                    matchmaking_queue.queuePlayer(side=side, userId=user)

            response_data = {
                "queueData": {
                    "ETA": -10000,
                    "position": 0,
                    "sizeA": 1 if side == "A" else 0,
                    "sizeB": 1 if side == "B" else 0,
                    "stable": False,
                },
                "status": "QUEUED",
            }
            return jsonify(response_data)

        else:
            response_data = matchmaking_queue.getQueueStatus(side, userid, region, game_mode=game_mode,
                                                             version=category)
            return jsonify(response_data)

    except Exception as e:
        logger.graylog_logger(level="error", handler="queue", message=e)
        return jsonify({"message": "Internal Server Error"}), 500


#    if region == "DEV":
#        all_users = [userid]
#        if additional_user_ids:
#            all_users.append(additional_user_ids)
#        return jsonify(
#            {"status": "MATCHED", "QueueData": {"Position": 0, "ETA": 0, "Stable": False, "SizeA": 1, "SizeB": 4},
#             "MatchData": {"MatchId": spoofed_match_id, "Category": category, "Rank": rank,
#                           "CreationDateTime": epoch, "ExcludeFriends": False,
#                           "ExcludeClanMembers": False, "Status": "CREATED",
#                           "Creator": userid,
#                           "Players": [all_users],
#                           "SideA": [userid],
#                           "SideB": [additional_user_ids], "CustomData": {},
#                           "Props": {"isDedicated": False, "gameMode": "08d2279d2ed3fba559918aaa08a73fa8-Default",
#                                     'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_Demo.MatchConfig_Demo'},
#                           "Schema": 11122334455666}})
#    else:
#        return {"status": "QUEUED", "queueData": {"ETA": -10000, "position": 0, "stable": False}}
# eta, position = match_manager.find_eta_and_position(data["_match_uuid"])


@app.route("/api/v1/queue/cancel", methods=["POST"])
def cancel_queue():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    try:
        matchmaking_queue.removePlayerFromQueue(userid)
    except Exception as e:
        logger.graylog_logger(level="error", handler="queue", message=e)
        return jsonify({"message": "Internal Server Error"}), 500

    return "", 204


@app.route("/api/v1/match/<matchid_unsanitized>", methods=["GET"])
def match(matchid_unsanitized):
    matchid = sanitize_input(matchid_unsanitized)
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)
    try:
        response_data = matchmaking_queue.createMatchResponse(matchId=matchid, userId=userid)
        # logger.graylog_logger(level="debug", handler="match", message=response_data)
        if response_data == "null" or response_data is None:
            logger.graylog_logger(level="error", handler="match", message=f"MatchResponse is null for MatchID: {matchid}")
            return {
                "Category": "Steam-te-18f25613-36778-ue4-374f864b",
                "creationDateTime": 0,
                "creator": None,
                "customData": {
                },
                "MatchId": matchid,
                "props": {
                    "countA": 0,
                    "countB": 0,
                    "gameMode": None,
                    "MatchConfiguration": None,
                    "platform": "Windows",
                },
                "rank": 1,
                "Schema": 3,
                "sideA": [],
                "sideB": [],
                "Players": [],
                "status": "Destroyed"
            }
            # response_data = matchmaking_queue.getKilledLobbyById(matchid)
            # logger.graylog_logger(level="debug", handler="match", message=response_data)
        return jsonify(response_data)
    except Exception as e:
        logger.graylog_logger(level="error", handler="match", message=e)
        return jsonify({"message": "Internal Server Error"}), 500


@app.route("/api/v1/match/<matchid_unsanitized>/Kill", methods=["PUT"])
def match_kill(matchid_unsanitized):
    matchid = sanitize_input(matchid_unsanitized)
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)
    try:
        lobby, _ = matchmaking_queue.getLobbyById(matchid)

        if lobby and matchmaking_queue.isOwner(matchid, userid):
            response_data = matchmaking_queue.createMatchResponse(matchId=matchid, killed=True)
            matchmaking_queue.deleteMatch(matchid)
            logger.graylog_logger(level="info", handler="match_kill", message=f"Killed Match: {matchid}"
                                                                              f"by User: {userid}")
            return jsonify(response_data)

        else:
            return jsonify({"message": "Unauthorized"}), 401

    except Exception as e:
        logger.graylog_logger(level="error", handler="match", message=e)
        return jsonify({"message": "Internal Server Error"}), 500


@app.route("/api/v1/match/<match_id_unsanitized>/register", methods=["POST"])
def match_register(match_id_unsanitized):
    try:
        check_for_game_client("strict")
        session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
        userid = session_manager.get_user_id(session_cookie)
        match_id = sanitize_input(match_id_unsanitized)

        logger.graylog_logger(level="info", handler="match_register",
                              message=f"User {userid} is registering to match {match_id}")

        data = request.json
        custom_data = data.get("customData", {})
        session_settings = custom_data.get("SessionSettings", "")

        response, private = matchmaking_queue.registerMatch(match_id, session_settings, userid)
        if private:
            return jsonify(response)

        if response:
            if use_discord:
                game_mode = response["props"]["gameMode"]
                if game_mode == "789c81dfb11fe39b7247c7e488e5b0d4-Default":
                    game_mode = "Default"
                elif game_mode == "08d2279d2ed3fba559918aaa08a73fa8-Default":
                    game_mode = "Default"
                elif game_mode == "d071fb6678668246d6d999c9892c2a60-Default":
                    game_mode = "Default"
                elif game_mode == "e3744bb4acbc0e5dc107e999c6132f18-Default":
                    game_mode = "REMIX"
                elif game_mode == "a0fdf9ce92261dcc5492f353b62f34f3-Default":
                    game_mode = "4 Needles"
                else:
                    game_mode = "Default"
                # "KeysToMetaData": {
                #         "Map_WashingtonRuins_Name": "FIRST STRIKE",
                #         "Map_DesertMayan_Name": "DUST & BLOOD",
                #         "Map_WashingtonRivers_Name": "SALT CREEK",
                #         "Map_ArcticBlastFurnace_Name": "FIRE IN THE SKY",
                #         "Map_ArcticExpedition_Name": "DESPERATE EXPEDITION",
                #         "Map_WashingtonCemetary_Name": "TOMBSTONE",
                #         "Map_DesertGoldRush_Name": "GOLD RUSH",
                #         "Map_DesertOilField_Name": "BLOWOUT",
                #         "Map_WashingtonFortress_Name": "FOREST CITADEL",
                #         "Map_DesertFortress_Name": "LEGIONS REST",
                #         "Map_DesertCity_Name": "BARREN CITY",
                #         "Map_ArcticScrapYard_Name": "ARC SCRAPYARD",
                #         "Map_SlumsDownTown_Map": "CURFEW",
                #         "Map_ArcticBlastFurnace_2Hunters_Name": "FIRE IN THE SKY - 2 Hunters",
                #         "Map_ArcticExpedition_2Hunters_Name": "DESPERATE EXPEDITION - 2 Hunters",
                #         "Map_ArcticScrapYard_2Hunters_Name": "ARC SCRAPYARD - 2 Hunters",
                #         "Map_DesertCity_2Hunters_Name": "BARREN CITY - 2 Hunters",
                #         "Map_DesertFortress_2Hunters_Name": "LEGIONS REST - 2 Hunters",
                #         "Map_DesertGoldRush_2Hunters_Name": "GOLD RUSH - 2 Hunters",
                #         "Map_DesertMayan_2Hunters_Name": "DUST & BLOOD - 2 Hunters",
                #         "Map_DesertOilField_2Hunters_Name": "BLOWOUT - 2 Hunters",
                #         "Map_SlumsDownTown_2Hunters_Name": "CURFEW - 2 Hunters",
                #         "Map_WashingtonCemetary_2Hunters_Name": "TOMBSTONE - 2 Hunters",
                #         "Map_WashingtonFortress_2Hunters_Name": "FOREST CITADEL - 2 Hunters",
                #         "Map_WashingtonRivers_2Hunters_Name": "SALT CREEK - 2 Hunters",
                #         "Map_WashingtonRuins_2Hunters_Name": "FIRST STRIKE - 2 Hunters",
                #         "Map_DesertMayan_2v10_5Needles_Name": "DUST & BLOOD - 2 Hunters",
                #         "Map_DesertMayan_2v10_4Needles_Name": "DUST & BLOOD - 2 Hunters",
                #         "Map_DesertMayan_2v8_5Needles_Name": "DUST & BLOOD - 2 Hunters",
                #         "Map_DesertMayan_2v8_4Needles_Name": "DUST & BLOOD - 2 Hunters"
                #       }
                match_configuration = response["props"]["MatchConfiguration"]
                if match_configuration == "/Game/Configuration/MatchConfig/MatchConfig_Demo_HarvestYourExit_1v5.MatchConfig_Demo_HarvestYourExit_1v5":
                    match_configuration = "Harvest Your Exit 1v5"
                elif match_configuration == "/Game/Configuration/MatchConfig/MatchConfig_Demo.MatchConfig_Demo":
                    match_configuration = "Survival"
                elif match_configuration == "/Game/Configuration/MatchConfig/MatchConfig_ARC_Fortress.MatchConfig_ARC_Fortress":
                    match_configuration = "Arctic Fortress"
                elif match_configuration == "/Game/Configuration/MatchConfig/MatchConfig_CustomMatch.MatchConfig_CustomMatch":
                    match_configuration = "REMIX Deathgarden - Gold Rush"
                elif match_configuration == "/Game/Configuration/MatchConfig/MatchConfig_Demo_2v8_4Needles.MatchConfig_Demo_2v8_4Needles":
                    match_configuration = "Harvest Your Exit 4Needles"
                elif match_configuration == "/Game/Configuration/MatchConfig/MatchConfig_DES_City_2Hunters.MatchConfig_DES_City_2Hunters":
                    match_configuration = "Desert City 5 needles"
                elif match_configuration == "/Game/Configuration/MatchConfig/MatchConfig_WA_Rivers.MatchConfig_WA_Rivers":
                    match_configuration = "Salt Creek"
                elif match_configuration == "/Game/Configuration/MatchConfig/MatchConfig_WA_Cemetery.MatchConfig_WA_Cemetery":
                    match_configuration = "Tombstone"
                elif match_configuration == "/Game/Configuration/MatchConfig/MatchConfig_DES_Oilfield.MatchConfig_DES_Oilfield":
                    match_configuration = "Blowout"
                elif match_configuration == "/Game/Configuration/MatchConfig/MatchConfig_ARC_BlastFurnace.MatchConfig_ARC_BlastFurnace":
                    match_configuration = "Fire in the Sky"
                elif match_configuration == "/Game/Configuration/MatchConfig/MatchConfig_DES_Mayan.MatchConfig_DES_Mayan":
                    match_configuration = "Dust & Blood"
                elif match_configuration == "/Game/Configuration/MatchConfig/MatchConfig_ARC_Expedition.MatchConfig_ARC_Expedition":
                    match_configuration = "Desperate Expedition"
                elif match_configuration == "/Game/Configuration/MatchConfig/MatchConfig_RUI_All.MatchConfig_RUI_All":
                    match_configuration = "First Strike"
                elif match_configuration == "/Game/Configuration/MatchConfig/MatchConfig_DES_GoldRush.MatchConfig_DES_GoldRush":
                    match_configuration = "Gold Rush"
                elif match_configuration == "/Game/Configuration/MatchConfig/MatchConfig_JUN_Fortress.MatchConfig_JUN_Fortress":
                    match_configuration = "Forest Citadel"
                elif match_configuration == "/Game/Configuration/MatchConfig/MatchConfig_DES_Fortress.MatchConfig_DES_Fortress":
                    match_configuration = "Legions Rest"

                if dev_env == "false":
                    webhook_data = {
                        "content": "",
                        "embeds": [
                            {
                                "title": f"Match Registered",
                                "description": f"MatchID: {match_id} \n GameMode: {game_mode} \n MatchConfiguration: {match_configuration}",
                                "color": 7932020
                            }
                        ],
                        "attachments": []
                    }
                    try:
                        discord_webhook(url_list, webhook_data)
                    except Exception as e:
                        logger.graylog_logger(level="error", handler="discord_webhook_message", message=e)

            return jsonify(response)

        else:
            return jsonify({"message": "Match registration failed"}), 500

    except Exception as e:
        logger.graylog_logger(level="error", handler="match_register", message=e)
        return jsonify({"message": "Internal Server Error"}), 500


@app.route("/api/v1/match/<match_id_unsanitized>/Quit", methods=["PUT"])
def match_quit(match_id_unsanitized):
    try:
        # todo If OWNER Crash -> Runner sends QUIT acknowledge when players less then 2
        check_for_game_client("strict")
        session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
        userid = session_manager.get_user_id(session_cookie)
        match_id = sanitize_input(match_id_unsanitized)

        logger.graylog_logger(level="info", handler="logging_queue",
                              message=f"User {userid} is quitting match {match_id}")

        lobby, _ = matchmaking_queue.getLobbyById(match_id)

        if lobby:
            if matchmaking_queue.isOwner(match_id, userid):
                matchmaking_queue.deleteMatch(match_id)
            else:
                matchmaking_queue.removePlayerFromQueue(userid)
                matchmaking_queue.remove_player_from_match(match_id, userid)

            return "", 204

        else:
            return jsonify({"message": "Match not found"}), 404

    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_queue", message=e)
        return jsonify({"status": "ERROR"}), 500


@app.route("/api/v1/match/<match_id_unsanitized>/Close", methods=["PUT"])
def close_lobby(match_id_unsanitized):
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)
    match_id = sanitize_input(match_id_unsanitized)

    try:
        lobby, _ = matchmaking_queue.getLobbyById(match_id)

        if lobby:
            if matchmaking_queue.isOwner(match_id, userid):
                #matchmaking_queue.deleteMatch(match_id)
                #return "", 204
                # set lobby.status to "Closed"
                matchmaking_queue.closeMatch(match_id)
                data = matchmaking_queue.createMatchResponse(matchId=match_id, killed=False, userId=userid)
                return jsonify(data), 200
            else:
                return jsonify({"message": "Unauthorized"}), 401

        else:
            return jsonify({"message": "Match not found"}), 404

    except Exception as e:
        logger.graylog_logger(level="error", handler="close_lobby", message=e)
        return jsonify({"message": "Internal Server Error"}), 500


@app.route("/api/v1/match/create", methods=["POST"])
def match_create():
    # {'category': 'Steam-te-18f25613-36778-ue4-374f864b',
    # 'region': 'US',
    # 'playersA': [],
    # 'playersB': ['00658d11-2dfd-41e8-b6d2-2462e8f3aa47', '95041085-e7e4-4759-be3d-e72c69167578',
    # '0385496c-f0ae-44d3-a777-26092750f39c'],
    # 'props': {'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_Demo.MatchConfig_Demo'},
    # 'latencies': []}
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    category = sanitize_input(request.json.get("category"))
    region = sanitize_input(request.json.get("region"))
    players_a = request.json.get("playersA")
    players_b = request.json.get("playersB")
    props = request.json.get("props")["MatchConfiguration"]

    # match_send = matchmaking_queue.createQueueResponseMatched(userid, matchid, joinerId=players_a)
    epoch = datetime.now().timestamp()
    player_list = []
    for player in players_a:
        player_list.append(player)
    for player in players_b:
        player_list.append(player)
    matchid, Match_Config = matchmaking_queue.register_private_match(players_a=players_a, players_b=players_b, match_config=props, version=category)
    users = players_a.copy()
    users.append(players_b)
    current_time = get_time()[0]
    countB = len(players_b)
    # Test new data
    # MatchId FString
    # Category FString
    # Rank FString
    # CreationDateTime double
    # ExcludeFriends bool
    # ExcludeClanMembers bool
    # Status FString
    # Reason FString
    # Creator FString
    # Players TARRAY FString
    # SideA TARRAY FString
    # SideB TARRAY FString
    # CustomData TARRAY Json
    # Props TARRAY Json
    # Schema double
    data = {
        "MatchId": matchid,
        "Category": category,
        "Rank": 1,
        "CreationDateTime": epoch,
        "ExcludeFriends": False,
        "ExcludeClanMembers": False,
        "Status": "NoMatch",
        "Reason": "",
        "Creator": userid,
        "Players": player_list,
        "SideA": players_a,
        "SideB": players_b,
        "CustomData": {},
        "Props": props,
        "Schema": 3
    }
    # Status:
    # None
    # NoMatch
    # Created
    # Creating
    # DelayedCreation
    # Opened
    # Completed
    # Timedout
    # Closing
    # Closed
    # Killing
    # Killed
    # Destroyed
    return jsonify(data)


@app.route("/api/v1/extensions/progression/playerEndOfMatch", methods=["POST"])
def progression_player_end_of_match():
    # {
    #    "data":{
    #       "playerId":"00658d11-2dfd-41e8-b6d2-2462e8f3aa47",
    #       "faction":"Runner",
    #       "characterGroup":"RunnerGroupE",
    #       "playtime":547,
    #       "platform":"PC",
    #       "hasQuit":false,
    #       "characterState":"Escaped",
    #       "matchId":"A9B72FEC485695753C8181AE3168877B-1",
    #       "experienceEvents":[
    #          {
    #             "type":"MarkedSupplier",
    #             "amount":600
    #          },
    #          {
    #             "type":"ResourceLootBonus",
    #             "amount":510
    #          },
    #          {
    #             "type":"PlayTime",
    #             "amount":45
    #          },
    #          {
    #             "type":"FriendlyEffectBonus",
    #             "amount":975
    #          },
    #          {
    #             "type":"ResourceDepositBonus",
    #             "amount":3750
    #          },
    #          {
    #             "type":"GoldenCrateLootBonus",
    #             "amount":5
    #          },
    #          {
    #             "type":"EscapeBonus",
    #             "amount":1000
    #          },
    #          {
    #             "type":"ResourceEscapeBonus",
    #             "amount":20
    #          },
    #          {
    #             "type":"BloodModeEscapeBonus",
    #             "amount":100
    #          }
    #       ],
    #       "earnedCurrencies":[
    #          {
    #             "currencyName":"CurrencyA",
    #             "amount":617
    #          },
    #          {
    #             "currencyName":"CurrencyB",
    #             "amount":620
    #          },
    #          {
    #             "currencyName":"CurrencyC",
    #             "amount":619
    #          }
    #       ],
    #       "completedChallenges":[
    #          {
    #             "challengeId":"24CE65364362CB2A90C0E08876176937",
    #             "challengeType":"Challenge.Type.Progression"
    #          },
    #          {
    #             "challengeId":"B4B156CC47C8D987B9BDBEB910B12C9E",
    #             "challengeType":"Challenge.Type.Progression"
    #          },
    #          {
    #             "challengeId":"ECCBA78D4055676F9C17D79B9D5FA2D4",
    #             "challengeType":"Challenge.Type.Progression"
    #          }
    #       ]
    #    }
    # }
    #
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    # userid = session_manager.get_user_id(session_cookie)
    try:
        logger.graylog_logger(level="info", handler="matchmaking_playerEndOfMatch", message=request.get_json())
        data = request.get_json()["data"]
        userid = data["playerId"]
        characterGroup = data["characterGroup"]
        experience = 0
        for event in data["experienceEvents"]:
            experience += event["amount"]
        update_user_xp(userid, experience, characterGroup)
        user_wallet = mongo.get_data_with_list(login=userid, login_steam=False, items={"currency_iron",
                                                                                       "currency_blood_cells",
                                                                                       "currency_ink_cells"})
        CurrencyA = user_wallet["currency_iron"]
        CurrencyB = user_wallet["currency_blood_cells"]
        CurrencyC = user_wallet["currency_ink_cells"]
        wallet = []
        for currency in data["earnedCurrencies"]:
            if currency["currencyName"] == "CurrencyA":
                wallet.append({"Currency": "CurrencyA", "Amount": currency["amount"]})
                CurrencyA += currency["amount"]
            elif currency["currencyName"] == "CurrencyB":
                wallet.append({"Currency": "CurrencyB", "Amount": currency["amount"]})
                CurrencyB += currency["amount"]
            elif currency["currencyName"] == "CurrencyC":
                wallet.append({"Currency": "CurrencyC", "Amount": currency["amount"]})
                CurrencyC += currency["amount"]
        mongo.write_data_with_list(login=userid, login_steam=False, items_dict={"currency_iron": CurrencyA,
                                                                                "currency_blood_cells": CurrencyB,
                                                                                "currency_ink_cells": CurrencyC})
        # return jsonify({
        #             "Player": {
        #                 "InitialExperienceProgressions": [
        #                     FGMProgressionExperienceModel
        #                 ],
        #                 "NewExperienceProgressions": [
        #                     FGMProgressionExperienceModel
        #                 ],
        #                 "TotalEarnedCurrency": [
        #                     FCurrencyModel
        #                 ],
        #                 "Wallet": [
        #                     FCurrencyModel
        #                 ],
        #                 "Events": [
        #                     FGMExperienceEvent
        #                 ]
        #             }
        #         })

        # MirrorsExtModelProgressionPlayerEndOfMatchResponse
        # todo remove this test
        # Found in TheExit\Content\Configuration\Experience\PlayerEndOfMatchDataAsset.uasset
        # [
        #   {
        #     "Type": "GMPlayerEndOfMatchConfiguration",
        #     "Name": "PlayerEndOfMatchDataAsset",
        #     "Class": "UScriptClass'GMPlayerEndOfMatchConfiguration'",
        #     "Properties": {
        #       "PlayTimeRunnerXPBonus": 20,
        #       "PlayTimeRunnerXPFrequency": 60.0,
        #       "EscapeXpBonus": 1150,
        #       "ConstructDestructionXps": [
        #         {
        #           "ConstructClass": {
        #             "ObjectName": "BlueprintGeneratedClass'BP_Mine_C'",
        #             "ObjectPath": "TheExit/Content/Items/ItemTemplates/Powers/SpawnMine/BP_Mine.1"
        #           },
        #           "DestructionXp": 25
        #         },
        #         {
        #           "ConstructClass": {
        #             "ObjectName": "BlueprintGeneratedClass'BP_HT_Turret_Mount_C'",
        #             "ObjectPath": "TheExit/Content/PROPS/GamePlay/Turrets/HT_XX_Turret_Turret01/BP_HT_Turret_Mount.1"
        #           },
        #           "DestructionXp": 50
        #         }
        #       ],
        #       "RescueXpBonus": 460,
        #       "FriendlyEffectXpBonus": 60,
        #       "FriendlyEffectAssistXpBonus": 115,
        #       "ResourceDepositXpBonus": 75,
        #       "ResourceLootXpBonus": 15,
        #       "ResourceEscapeXpBonus": 40,
        #       "MarkedSupplierXpBonus": 15,
        #       "EscapingPlayXpBonus": 300,
        #       "EscapingPlayAssistXpBonus": 175,
        #       "DangerClosePlayXpBonus": 60,
        #       "LastManStandingXpBonus": 100,
        #       "BloodDeliveryMasterXpBonus": 575,
        #       "RunnerGoldenCrateLootXpBonus": 60,
        #       "HunterGoldenCrateLootXpBonus": 50,
        #       "PlayTimeHunterXPBonus": 5,
        #       "PlayTimeHunterXPFrequency": 60.0,
        #       "BloodModeEscapeXp": 100,
        #       "QuickExecutorXpBonus": 500,
        #       "DownedXpBonus": 400,
        #       "RingOutKillXpBonus": 500,
        #       "ExecutionXpBonus": 500,
        #       "MercyXpBonus": 500,
        #       "BleedOutXpBonus": 500,
        #       "DroneActivationXpBonus": 45,
        #       "DroneActivatedKillXpBonus": 45,
        #       "DroneDeactivatedKillXpBonus": 10,
        #       "HackingInteractionStartXpBonus": 20,
        #       "HackedInteractionEffectXpBonus": 50,
        #       "DroneRevealXpBonus": 10,
        #       "RagdollMinTravelDistance": 100.0,
        #       "RagdollTravelStepDistance": 50.0,
        #       "RagdollTravelXPBonusPerStep": 5,
        #       "RagdollTravelBaseXP": 5,
        #       "RagdollTravelMaxXP": 100,
        #       "HunterAttackDamageStep": 30,
        #       "SelfDeterminationConfigurations": [
        #         {
        #           "Key": {
        #             "TagName": "MatchGameMode.OneVsFive"
        #           },
        #           "Value": {
        #             "SelfDeterminationXpBonuses": [
        #               {
        #                 "Key": "1",
        #                 "Value": 300
        #               },
        #               {
        #                 "Key": "2",
        #                 "Value": 600
        #               },
        #               {
        #                 "Key": "3",
        #                 "Value": 1200
        #               },
        #               {
        #                 "Key": "4",
        #                 "Value": 2000
        #               },
        #               {
        #                 "Key": "5",
        #                 "Value": 5000
        #               }
        #             ]
        #           }
        #         },
        #         {
        #           "Key": {
        #             "TagName": "MatchGameMode.TwoVsTen"
        #           },
        #           "Value": {
        #             "SelfDeterminationXpBonuses": [
        #               {
        #                 "Key": "1",
        #                 "Value": 300
        #               },
        #               {
        #                 "Key": "2",
        #                 "Value": 600
        #               },
        #               {
        #                 "Key": "3",
        #                 "Value": 1200
        #               },
        #               {
        #                 "Key": "4",
        #                 "Value": 2000
        #               },
        #               {
        #                 "Key": "5",
        #                 "Value": 4000
        #               },
        #               {
        #                 "Key": "6",
        #                 "Value": 6000
        #               },
        #               {
        #                 "Key": "7",
        #                 "Value": 8000
        #               },
        #               {
        #                 "Key": "8",
        #                 "Value": 10000
        #               },
        #               {
        #                 "Key": "9",
        #                 "Value": 14000
        #               },
        #               {
        #                 "Key": "10",
        #                 "Value": 18000
        #               }
        #             ]
        #           }
        #         },
        #         {
        #           "Key": {
        #             "TagName": "None"
        #           },
        #           "Value": {
        #             "SelfDeterminationXpBonuses": [
        #               {
        #                 "Key": "1",
        #                 "Value": 300
        #               },
        #               {
        #                 "Key": "2",
        #                 "Value": 600
        #               },
        #               {
        #                 "Key": "3",
        #                 "Value": 1200
        #               },
        #               {
        #                 "Key": "4",
        #                 "Value": 2000
        #               },
        #               {
        #                 "Key": "5",
        #                 "Value": 5000
        #               }
        #             ]
        #           }
        #         }
        #       ]
        #     }
        #   }
        # ]

        return jsonify({
            "Player": {
                "InitialExperienceProgressions": [
                    {
                        "ObjectId": characterGroup,
                        "Level": 1,
                        "ExperienceToReach": 100000,
                        "CurrentExperience": 1
                    }
                ],
                "NewExperienceProgressions": [
                    {
                        "ObjectId": characterGroup,
                        "Level": 1,
                        "ExperienceToReach": 100000,
                        "CurrentExperience": experience
                    }
                ],
                "TotalEarnedCurrency": wallet,
                "Wallet": [
                    {
                        "Currency": "CurrencyA",
                        "Amount": CurrencyA
                    },
                    {
                        "Currency": "CurrencyB",
                        "Amount": CurrencyB
                    },
                    {
                        "Currency": "CurrencyC",
                        "Amount": CurrencyC
                    }
                ],
                "Events": []
            }
        })
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="matchmaking_playerEndOfMatch", message=e)


@app.route("/api/v1/extensions/progression/endOfMatch", methods=["POST"])
def progression_end_of_match():
    # todo Implement this fully

    # {
    #    "data":{
    #       "players":[
    #          {
    #             "playerId":"619d6f42-db87-4f3e-8dc9-3c9995613614",
    #             "faction":"Runner",
    #             "characterGroup":"RunnerGroupE",
    #             "platform":"PC",
    #             "hasQuit":false,
    #             "characterState":"Dead"
    #          },
    #          {
    #             "playerId":"95041085-e7e4-4759-be3d-e72c69167578",
    #             "faction":"Hunter",
    #             "characterGroup":"HunterGroupB",
    #             "platform":"PC",
    #             "hasQuit":false,
    #             "characterState":"InArena"
    #          },
    #          {
    #             "playerId":"00658d11-2dfd-41e8-b6d2-2462e8f3aa47",
    #             "faction":"Runner",
    #             "characterGroup":"RunnerGroupB",
    #             "platform":"PC",
    #             "hasQuit":false,
    #             "characterState":"Dead"
    #          }
    #       ],
    #       "dominantFaction":"Hunter",
    #       "matchId":"df9655d9-63ac-4dde-a9e9-129aaa249356"
    #    }
    # }

    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)
    try:
        players = []
        for player in request.get_json()["data"]["players"]:
            player = player["playerId"]
            response = {
                "playerId": player,
                # What could this struct be????
            }
        logger.graylog_logger(level="info", handler="matchmaking_endOfMatch", message=request.get_json())
        matchId = request.get_json()["data"]["matchId"]
        matchmaking_queue.deleteMatch(matchId)
        return jsonify({"Success": True})
    except TimeoutError:
        return jsonify({"Success": False})
    except Exception as e:
        logger.graylog_logger(level="error", handler="matchmaking_endOfMatch", message=e)
        return jsonify({"Success": False})


@app.route("/metrics/endofmatch/event", methods=["POST"])
def metrics_end_of_match_event():
    #
    # {
    # 	"matchId": "A9B72FEC485695753C8181AE3168877B-1",
    # 	"gameVersion": "te-f9b4768a-26590-ue4-cefc1aee",
    # 	"roundEvents": [
    # 		{
    # 			"round": 1,
    # 			"roundLength": 547,
    # 			"gamemode": "None",
    # 			"biomeName": "",
    # 			"randomSeed": 0,
    # 			"runnerCount": 2,
    # 			"hunterCount": 0,
    # 			"weather": "",
    # 			"supplierCounts": [],
    # 			"endOfRoundObjectiveState":
    # 			{
    # 				"bAreObjectivesCompleted": false,
    # 				"fullyCapturedObjectivesCount": 0,
    # 				"objectivesFilledCompartmentsCount": 0,
    # 				"progressionByObjective": []
    # 			},
    # 			"endOfRoundExitState":
    # 			{
    # 				"bAreExitOpened": true,
    # 				"openTime": 548.63604736328125,
    # 				"openReason": "HunterDomination",
    # 				"exitCoords": [
    # 					{
    # 						"x": -4371.796875,
    # 						"y": -7400,
    # 						"z": -400
    # 					},
    # 					{
    # 						"x": 3942.046875,
    # 						"y": 7000,
    # 						"z": -400
    # 					}
    # 				]
    # 			}
    # 		}
    # 	],
    # 	"runnerMatchAnalytics": [
    # 		{
    # 			"roundEvents": [
    # 				{
    # 					"caltrops": [],
    # 					"specialArrows": [],
    # 					"role": "PlayerRole.Support",
    # 					"state": "Escaped",
    # 					"suicideCount": 0,
    # 					"timeOfDeath": -1,
    # 					"rescueCount": 0,
    # 					"rescuedCount": 0,
    # 					"downedCount": 0,
    # 					"damageDealtToHunter": 0,
    # 					"damageDealtToMines": 0,
    # 					"damageDealtToTurrets": 0,
    # 					"damageDealtToDrones": 44,
    # 					"arenaObjectivesMarked": 0,
    # 					"resourceSuppliersMarked": 1,
    # 					"totalObjectsMarked": 1,
    # 					"murderPostRescueCount": 0,
    # 					"rescuedFromMurderPostCount": 0,
    # 					"sentToMurderPostCount": 0,
    # 					"hunterHitsCount": 0,
    # 					"unsecuredBloodCount": 0,
    # 					"bankedBloodCount": 0,
    # 					"round": 1,
    # 					"gamemode": "",
    # 					"country": "DE",
    # 					"gender": "Male",
    # 					"damageTaken": 0,
    # 					"headshotCount": 0,
    # 					"longestHeadshotDistance": -1,
    # 					"totalShotsFired": 3,
    # 					"supplierUsedCounts": [
    # 						{
    # 							"type": "SupplyCrate_AmmunitionPack_C",
    # 							"count": 3
    # 						},
    # 						{
    # 							"type": "SupplyCrate_WeaponParts_C",
    # 							"count": 1
    # 						},
    # 						{
    # 							"type": "BP_ResourceCrate_ResourceTypeB_C",
    # 							"count": 66
    # 						},
    # 						{
    # 							"type": "GoldenCrate_Unlimited_C",
    # 							"count": 1
    # 						}
    # 					],
    # 					"resourcesUsage": [
    # 						{
    # 							"type": "Resource.Ammo.ReserveEarned",
    # 							"amount": 34
    # 						},
    # 						{
    # 							"type": "Resource.NPIEarned",
    # 							"amount": 3
    # 						},
    # 						{
    # 							"type": "Resource.NPIExpended",
    # 							"amount": 3
    # 						},
    # 						{
    # 							"type": "Resource.ResourceCharge.TypeB.UnsecuredEarned",
    # 							"amount": 66
    # 						},
    # 						{
    # 							"type": "Resource.ResourceCharge.TypeB.UnsecuredExpended",
    # 							"amount": 56
    # 						},
    # 						{
    # 							"type": "Resource.ResourceCharge.TypeB.BankedEarned",
    # 							"amount": 56
    # 						},
    # 						{
    # 							"type": "Resource.Ammo.ClipExpended",
    # 							"amount": 2
    # 						}
    # 					],
    # 					"pingInformation":
    # 					{
    # 						"readCount": 108,
    # 						"average": 0,
    # 						"variance": 0,
    # 						"maximum": 0,
    # 						"minimum": 0
    # 					},
    # 					"crouchingTime": 18.294017791748047,
    # 					"capturingObjectivesTime": 0,
    # 					"holdingKeyTime": 0,
    # 					"keysDelivered": 0,
    # 					"objectsDestroyedCount": 1,
    # 					"perksChosen": [
    # 						"Shimmey",
    # 						"Ammo Opportunist"
    # 					],
    # 					"chatMessagesCounts": [],
    # 					"effectsAppliedCounts": [],
    # 					"customizationItems": [
    # 						{
    # 							"itemSlot": "Head",
    # 							"customizationItem": "Default Smoke Head"
    # 						},
    # 						{
    # 							"itemSlot": "Outfit",
    # 							"customizationItem": "Default Smoke Upperbody"
    # 						},
    # 						{
    # 							"itemSlot": "Lower Body Section",
    # 							"customizationItem": "Default Smoke Lowerbody"
    # 						},
    # 						{
    # 							"itemSlot": "Gauntlet",
    # 							"customizationItem": "Default Smoke Vambrace"
    # 						}
    # 					],
    # 					"customizationWeaponSkins": [],
    # 					"chaseAmount": 0,
    # 					"chaseAmountEscape": 0
    # 				}
    # 			],
    # 			"playerName": "HEX: Dino Nuggies",
    # 			"playerUniqueId": "619d6f42-db87-4f3e-8dc9-3c9995613614",
    # 			"playerSessionId": "71E8AFB54DFFCC83A69D3F80A5CBADD5"
    # 		},
    # 		{
    # 			"roundEvents": [
    # 				{
    # 					"caltrops": [],
    # 					"specialArrows": [],
    # 					"role": "PlayerRole.Support",
    # 					"state": "Escaped",
    # 					"suicideCount": 0,
    # 					"timeOfDeath": -1,
    # 					"rescueCount": 0,
    # 					"rescuedCount": 0,
    # 					"downedCount": 0,
    # 					"damageDealtToHunter": 0,
    # 					"damageDealtToMines": 0,
    # 					"damageDealtToTurrets": 0,
    # 					"damageDealtToDrones": 0,
    # 					"arenaObjectivesMarked": 5,
    # 					"resourceSuppliersMarked": 26,
    # 					"totalObjectsMarked": 31,
    # 					"murderPostRescueCount": 0,
    # 					"rescuedFromMurderPostCount": 0,
    # 					"sentToMurderPostCount": 0,
    # 					"hunterHitsCount": 0,
    # 					"unsecuredBloodCount": 0,
    # 					"bankedBloodCount": 0,
    # 					"round": 1,
    # 					"gamemode": "",
    # 					"country": "DE",
    # 					"gender": "Male",
    # 					"damageTaken": 0,
    # 					"headshotCount": 0,
    # 					"longestHeadshotDistance": -1,
    # 					"totalShotsFired": 76,
    # 					"supplierUsedCounts": [
    # 						{
    # 							"type": "SupplyCrate_AmmunitionPack_C",
    # 							"count": 3
    # 						},
    # 						{
    # 							"type": "SupplyCrate_WeaponParts_C",
    # 							"count": 2
    # 						},
    # 						{
    # 							"type": "BP_ResourceCrate_ResourceTypeB_C",
    # 							"count": 51
    # 						},
    # 						{
    # 							"type": "GoldenCrate_Unlimited_C",
    # 							"count": 1
    # 						}
    # 					],
    # 					"resourcesUsage": [
    # 						{
    # 							"type": "Resource.Ammo.ReserveEarned",
    # 							"amount": 34
    # 						},
    # 						{
    # 							"type": "Resource.Ammo.ClipExpended",
    # 							"amount": 35
    # 						},
    # 						{
    # 							"type": "Resource.NPIEarned",
    # 							"amount": 6
    # 						},
    # 						{
    # 							"type": "Resource.NPIExpended",
    # 							"amount": 6
    # 						},
    # 						{
    # 							"type": "Resource.ResourceCharge.TypeB.UnsecuredEarned",
    # 							"amount": 51
    # 						},
    # 						{
    # 							"type": "Resource.ResourceCharge.TypeB.UnsecuredExpended",
    # 							"amount": 50
    # 						},
    # 						{
    # 							"type": "Resource.ResourceCharge.TypeB.BankedEarned",
    # 							"amount": 50
    # 						}
    # 					],
    # 					"pingInformation":
    # 					{
    # 						"readCount": 110,
    # 						"average": 225,
    # 						"variance": 82.481819152832031,
    # 						"maximum": 268,
    # 						"minimum": 215
    # 					},
    # 					"crouchingTime": 13.677490234375,
    # 					"capturingObjectivesTime": 0,
    # 					"holdingKeyTime": 0,
    # 					"keysDelivered": 0,
    # 					"objectsDestroyedCount": 0,
    # 					"perksChosen": [
    # 						"Shimmey",
    # 						"Ammo Opportunist"
    # 					],
    # 					"chatMessagesCounts": [
    # 						{
    # 							"messageType": "IntelliCommsMsgNoChannel",
    # 							"messageCount": 3
    # 						},
    # 						{
    # 							"messageType": "IntelliCommsMsgFaction",
    # 							"messageCount": 23
    # 						}
    # 					],
    # 					"effectsAppliedCounts": [
    # 						{
    # 							"effectSource": "BP_Arrow_SmokeScreen_C",
    # 							"count": 39
    # 						}
    # 					],
    # 					"customizationItems": [
    # 						{
    # 							"itemSlot": "Head",
    # 							"customizationItem": "Default Smoke Head"
    # 						},
    # 						{
    # 							"itemSlot": "Outfit",
    # 							"customizationItem": "Default Smoke Upperbody"
    # 						},
    # 						{
    # 							"itemSlot": "Lower Body Section",
    # 							"customizationItem": "Default Smoke Lowerbody"
    # 						},
    # 						{
    # 							"itemSlot": "Gauntlet",
    # 							"customizationItem": "Default Smoke Vambrace"
    # 						}
    # 					],
    # 					"customizationWeaponSkins": [],
    # 					"chaseAmount": 0,
    # 					"chaseAmountEscape": 0
    # 				}
    # 			],
    # 			"playerName": "Miraak",
    # 			"playerUniqueId": "00658d11-2dfd-41e8-b6d2-2462e8f3aa47",
    # 			"playerSessionId": "B9BB33074498771555A3DBAF95D124CE"
    # 		},
    # 		{
    # 			"roundEvents": [
    # 				{
    # 					"caltrops": [],
    # 					"specialArrows": [],
    # 					"role": "",
    # 					"state": "Alive",
    # 					"suicideCount": 0,
    # 					"timeOfDeath": -1,
    # 					"rescueCount": 0,
    # 					"rescuedCount": 0,
    # 					"downedCount": 0,
    # 					"damageDealtToHunter": 0,
    # 					"damageDealtToMines": 0,
    # 					"damageDealtToTurrets": 0,
    # 					"damageDealtToDrones": 0,
    # 					"arenaObjectivesMarked": 0,
    # 					"resourceSuppliersMarked": 0,
    # 					"totalObjectsMarked": 0,
    # 					"murderPostRescueCount": 0,
    # 					"rescuedFromMurderPostCount": 0,
    # 					"sentToMurderPostCount": 0,
    # 					"hunterHitsCount": 0,
    # 					"unsecuredBloodCount": 0,
    # 					"bankedBloodCount": 0,
    # 					"round": 1,
    # 					"gamemode": "",
    # 					"country": "",
    # 					"gender": "",
    # 					"damageTaken": 0,
    # 					"headshotCount": 0,
    # 					"longestHeadshotDistance": -1,
    # 					"totalShotsFired": 0,
    # 					"supplierUsedCounts": [],
    # 					"resourcesUsage": [],
    # 					"pingInformation":
    # 					{
    # 						"readCount": 1,
    # 						"average": 0,
    # 						"variance": 0,
    # 						"maximum": 0,
    # 						"minimum": 0
    # 					},
    # 					"crouchingTime": 0,
    # 					"capturingObjectivesTime": 0,
    # 					"holdingKeyTime": 0,
    # 					"keysDelivered": 0,
    # 					"objectsDestroyedCount": 0,
    # 					"perksChosen": [],
    # 					"chatMessagesCounts": [],
    # 					"effectsAppliedCounts": [],
    # 					"customizationItems": [],
    # 					"customizationWeaponSkins": [],
    # 					"chaseAmount": 0,
    # 					"chaseAmountEscape": 0
    # 				}
    # 			],
    # 			"playerName": "",
    # 			"playerUniqueId": "",
    # 			"playerSessionId": ""
    # 		}
    # 	],
    # 	"hunterMatchAnalytics": [],
    # 	"hitDetectionErrorRate": 0,
    # 	"hitDetectionErrors": [],
    # 	"lobbyAnalytics": [],
    # 	"eventType": "Server"
    # }
    #
    check_for_game_client("strict")
    try:
        data = request.get_json()
        # Keys LV 1
        match_id = data["matchId"]
        game_version = data["gameVersion"]
        round_events = data["roundEvents"]
        runner_match_analytics = data["runnerMatchAnalytics"]
        hunter_match_analytics = data["hunterMatchAnalytics"]
        hit_detection_error_rate = data["hitDetectionErrorRate"]
        hit_detection_errors = data["hitDetectionErrors"]
        lobby_analytics = data["lobbyAnalytics"]
        event_type = data["eventType"]

        # Keys round_events
        round_events_item1 = round_events[0]
        round_value = round_events_item1["round"]
        round_length = round_events_item1["roundLength"]
        # gamemode = round_events_item1["gamemode"]
        biome_name = round_events_item1["biomeName"]
        random_seed = round_events_item1["randomSeed"]
        runner_count = round_events_item1["runnerCount"]
        hunter_count = round_events_item1["hunterCount"]
        weather = round_events_item1["weather"]
        supplier_counts = round_events_item1["supplierCounts"]
        end_of_round_objective_state = round_events_item1["endOfRoundObjectiveState"]
        end_of_round_exit_state = round_events_item1["endOfRoundExitState"]

        # Keys end_of_round_objective_state
        b_are_objectives_completed = end_of_round_objective_state["bAreObjectivesCompleted"]
        fully_captured_objectives_count = end_of_round_objective_state["fullyCapturedObjectivesCount"]
        objectives_filled_compartments_count = end_of_round_objective_state["objectivesFilledCompartmentsCount"]
        progression_by_objective = end_of_round_objective_state["progressionByObjective"]

        # Keys end_of_round_exit_state
        b_are_exit_opened = end_of_round_exit_state["bAreExitOpened"]
        open_time = end_of_round_exit_state["openTime"]
        open_reason = end_of_round_exit_state["openReason"]
        exit_coords = end_of_round_exit_state["exitCoords"]

        # keys exit_coords
        # Per Player XYZ

        # Keys runner_match_analytics
        # For all players in game LOOP Func
        roundEvents = runner_match_analytics[0]["roundEvents"]
        playerName = runner_match_analytics[0]["playerName"]
        playerUniqueId = runner_match_analytics[0]["playerUniqueId"]
        playerSessionId = runner_match_analytics[0]["playerSessionId"]

        # Keys hunter_match_analytics

        # Keys hit_detection_errors

        # Keys lobby_analytics

        logger.graylog_logger(level="info", handler="logging_endOfMatch_Event", message=data)
        return jsonify({"Success": True})
    except TimeoutError:
        return jsonify({"Success": False})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_endOfMatch_Event", message=e)


@app.route("/file/<game_version_unsanitized>/<seed_unsanitized>/<map_name_unsanitized>", methods=["POST", "GET"])
def file_gold_rush(seed_unsanitized, map_name_unsanitized, game_version_unsanitized):
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    game_version = sanitize_input(game_version_unsanitized)
    seed = sanitize_input(seed_unsanitized)
    map_name = sanitize_input(map_name_unsanitized)
    userid = session_manager.get_user_id(session_cookie)

    file_name = f"{game_version}_{seed}_{map_name}.raw"
    folder_path = os.path.join(app.root_path, "map_seeds")
    file_path = os.path.join(folder_path, file_name)
    os.makedirs(folder_path, exist_ok=True)

    if request.method == "GET":
        if os.path.isfile(file_path):
            with open(file_path, "rb") as files:
                data = files.read()
                return data

    if request.method == "POST":
        data = request.get_data()
        with open(file_path, "wb") as files:
            files.write(data)
        return {"status": "success"}


@app.route("/metrics/matchmaking/event", methods=["POST"])
def metrics_matchmaking_event():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    try:
        logger.graylog_logger(level="info", handler="logging_matchmaking_Event", message=request.get_json())
        # {
        # 	"playerId": "619d6f42-db87-4f3e-8dc9-3c9995613614",
        # 	"matchId": "",
        # 	"playerRole": "Leader",
        # 	"faction": "Runner",
        # 	"endState": "Cancelled",
        # 	"group": "Default",
        # 	"region": "EU",
        # 	"groupSize": 1,
        # 	"beginTime": 1707419672,
        # 	"endTime": 1707419822,
        # 	"eventType": "Client"
        # }

        endState = request.get_json()["endState"]
        if endState == "Cancelled":
            matchmaking_queue.removePlayerFromQueue(userid)
            return jsonify({"status": "success"})

        return "", 204
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_matchmaking_Event", message=e)


@app.route("/api/v1/match/<match_id_unsanitized>/user/<user_id>", methods=["DELETE"])
def remove_player_from_match(match_id_unsanitized, user_id):
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)
    match_id = sanitize_input(match_id_unsanitized)

    try:
        response = matchmaking_queue.remove_player_from_match(match_id, user_id)
        if response == {"status": "success"}:
            return "", 204
        else:
            return jsonify({"message": "Something is fucked"}), 500
    except Exception as e:
        logger.graylog_logger(level="error", handler="remove_player_from_match", message=e)
        return jsonify({"message": "Internal Server Error"}), 500
