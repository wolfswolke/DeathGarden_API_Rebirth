import json
import os
from datetime import datetime

from logic.match_manager import match_manager
from logic.queue_handler import matchmaking_queue
from flask_definitions import *
import uuid


@app.route("/api/v1/config/MATCH_MAKING_REGIONS/raw", methods=["GET"])
def match_making_regions_raw():
    check_for_game_client("strict")
    try:
        return jsonify(["EU", "US", "AP", "DEV"])
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
        category = sanitize_input(request.args.get("category"))
        game_mode = sanitize_input(request.args.get("gameMode"))
        region = sanitize_input(request.args.get("region"))
        count_a = request.args.get("countA") # Hunter Count
        count_b = request.args.get("countB") # Runner Count
        side = sanitize_input(request.args.get("side", ""))
        session = matchmaking_queue.getSession(userid)
        if region == "DEV":
            return jsonify({"A": {"Size": 1, "ETA": 100, "stable": True}, "B": {"Size": 5, "ETA": 100, "stable": True},
                            "SizeA": count_a, "SizeB": count_b})
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
    spoofed_match_id = "0051681e-72ce-46f0-bda2-752e471d0d08"
    epoch = datetime.now().timestamp()

    logger.graylog_logger(level="info", handler="logging_queue_DUMP", message=request.get_json())

    logger.graylog_logger(level="info", handler="logging_queue",
                          message=f"User {userid} is queueing for {category} in {region} with {count_a} hunters and {count_b} runners")
    if region == "DEV":
        all_users = [userid]
        if additional_user_ids:
            all_users.append(additional_user_ids)
        return jsonify(
            {"status": "MATCHED", "QueueData": {"Position": 0, "ETA": 0, "Stable": False, "SizeA": 1, "SizeB": 4},
             "MatchData": {"MatchId": spoofed_match_id, "Category": category, "Rank": rank,
                           "CreationDateTime": epoch, "ExcludeFriends": False,
                           "ExcludeClanMembers": False, "Status": "CREATED",
                           "Creator": userid,
                           "Players": [all_users],
                           "SideA": [userid],
                           "SideB": [additional_user_ids], "CustomData": {},
                           "Props": {"isDedicated": False, "gameMode": "08d2279d2ed3fba559918aaa08a73fa8-Default",
                                     'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_Demo.MatchConfig_Demo'},
                           "Schema": 11122334455666}})
    try:
        queue_data = side, check_only
        if not check_only:
            matchmaking_queue.queuePlayer(side=side, userId=userid)

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
            response_data = matchmaking_queue.getQueueStatus(side, userid, region)
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
    if matchid == "0051681e-72ce-46f0-bda2-752e471d0d08":
        return jsonify({"MatchId": matchid, "Category": "Steam-te-18f25613-36778-ue4-374f864b", "Rank": 1})
    try:
        response_data = matchmaking_queue.createMatchResponse(matchid)
        logger.graylog_logger(level="debug", handler="match", message=response_data)
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
            response_data = matchmaking_queue.createMatchResponse(matchid, killed=True)
            matchmaking_queue.deleteMatch(matchid)
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

        response = matchmaking_queue.registerMatch(match_id, session_settings, userid)

        if response:
            return jsonify(response)

        else:
            return jsonify({"message": "Match registration failed"}), 500

    except Exception as e:
        logger.graylog_logger(level="error", handler="match_register", message=e)
        return jsonify({"message": "Internal Server Error"}), 500


@app.route("/api/v1/match/<match_id_unsanitized>/Quit", methods=["PUT"])
def match_quit(match_id_unsanitized):
    try:
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

            return "", 204

        else:
            return jsonify({"message": "Match not found"}), 404

    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_queue", message=e)
        return jsonify({"status": "ERROR"}), 500


@app.route("/api/v1/match/create", methods=["POST"])
def match_create():
    # {'category': 'Steam-te-18f25613-36778-ue4-374f864b', 'region': 'US', 'playersA': [],
    # 'playersB': ['00658d11-2dfd-41e8-b6d2-2462e8f3aa47', '95041085-e7e4-4759-be3d-e72c69167578',
    # '0385496c-f0ae-44d3-a777-26092750f39c'],
    # 'props': {'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_Demo.MatchConfig_Demo'},
    # 'latencies': []}
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    category = sanitize_input(request.json.get("category"))
    rank = sanitize_input(request.json.get("rank"))
    players_a = request.json.get("playersA")
    players_b = request.json.get("playersB")
    props = request.json.get("props")

    matchid = matchmaking_queue.genMatchUUID()
    # match_send = matchmaking_queue.createQueueResponseMatched(userid, matchid, joinerId=players_a)
    epoch = datetime.now().timestamp()
    player_list = [players_b, players_a]

    data = {"MatchId": matchid, "Category": category, "Rank": rank,
            "CreationDateTime": epoch, "ExcludeFriends": False,
            "ExcludeClanMembers": False, "Status": "WaitingForPlayers", "Creator": userid,
            "Players": player_list, "SideA": players_a, "SideB": players_b, "CustomData": {}, "Props": props,
            "Schema": 11122334455666}
    return jsonify(data)


@app.route("/api/v1/extensions/progression/playerEndOfMatch", methods=["POST"])
def progression_player_end_of_match():
    # {"data":{"playerId":"619d6f42-db87-4f3e-8dc9-3c9995613614",
    # "faction":"Runner","characterGroup":"RunnerGroupE",
    # "playtime":79,"platform":"PC","hasQuit":false,"characterState":"Dead",
    # "matchId":"63203229-1cd7-42da-8821-540eb87536c1",
    # "experienceEvents":[{"type":"GardenFinale","amount":5}],"earnedCurrencies":[],"completedChallenges":[]}}
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)
    try:
        logger.graylog_logger(level="info", handler="matchmaking_playerEndOfMatch", message=request.get_json())
        return jsonify({"Player": {"Success": True}})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="matchmaking_playerEndOfMatch", message=e)


@app.route("/api/v1/extensions/progression/endOfMatch", methods=["POST"])
def progression_end_of_match():
    # todo Implent this fully

    # {"data":{"players":[
    # {"playerId":"619d6f42-db87-4f3e-8dc9-3c9995613614","faction":"Runner","characterGroup":"RunnerGroupE",
    # "platform":"PC","hasQuit":false,"characterState":"Dead"},
    # {"playerId":"95041085-e7e4-4759-be3d-e72c69167578","faction":"Hunter","characterGroup":"HunterGroupB",
    # "platform":"PC","hasQuit":false,"characterState":"InArena"},
    # {"playerId":"00658d11-2dfd-41e8-b6d2-2462e8f3aa47","faction":"Runner","characterGroup":"RunnerGroupB",
    # "platform":"PC","hasQuit":false,"characterState":"Dead"}],
    # "dominantFaction":"Hunter","matchId":"df9655d9-63ac-4dde-a9e9-129aaa249356"}}
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)
    try:
        players = []
        for player in request.get_json()["data"]["players"]:
            players.append({"PlayerId": player["playerId"]})
        logger.graylog_logger(level="info", handler="matchmaking_endOfMatch", message=request.get_json())
        return jsonify({"Players": [
            {},
            {}
        ]})
        sub_list = {"Level": 3, "Ratio": 0.4}
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="matchmaking_endOfMatch", message=e)



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
        return jsonify({"status": "success"})
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
        response = matchmaking_queue.remove_user_from_Match(match_id, user_id)
        if response == {"status": "success"}:
            return "", 204
        else:
            return jsonify({"message": "Internal Server Error"}), 500
    except Exception as e:
        logger.graylog_logger(level="error", handler="remove_player_from_match", message=e)
        return jsonify({"message": "Internal Server Error"}), 500