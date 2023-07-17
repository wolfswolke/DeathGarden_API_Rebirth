import json
import os
from datetime import datetime

from logic.match_manager import match_manager
from flask_definitions import *
import uuid


@app.route("/api/v1/config/MATCH_MAKING_REGIONS/raw", methods=["GET"])
def match_making_regions_raw():
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    try:
        return jsonify(["EU", "US", "AP", "DEV"])
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="matchmaking_RegionsRAW", message=e)


@app.route("/api/v1/queue/info", methods=["GET"])
def queue_info():
    # ?category=Steam-te-23ebf96c-27498-ue4-7172a3f5&gameMode=Default&region=US&countA=1&countB=5
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    category = request.args.get("category")
    game_mode = request.args.get("gameMode")
    region = request.args.get("region")
    count_a = request.args.get("countA") # Hunter Count
    count_b = request.args.get("countB") # Runner Count
    return jsonify({"A": {"Size": 1, "ETA": 100, "stable": True}, "B": {"Size": 5, "ETA": 100, "stable": True}, "SizeA": count_a, "SizeB": count_b})


@app.route("/api/v1/queue", methods=["POST"])
def queue():
    # {"category":"Steam-te-18f25613-36778-ue4-374f864b","rank":1,"side":"B","latencies":[],"additionalUserIds":[],
    # "checkOnly":false,"gameMode":"08d2279d2ed3fba559918aaa08a73fa8-Default","region":"US","countA":1,"countB":5}
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404

    category = request.json.get("category")
    rank = request.json.get("rank")
    side = request.json.get("side")
    latencies = request.json.get("latencies")
    additional_user_ids = request.json.get("additionalUserIds")
    check_only = request.json.get("checkOnly")  # False = Searching. True = Is searching and waiting for match
    game_mode = request.json.get("gameMode")
    region = request.json.get("region")
    count_a = request.json.get("countA")
    count_b = request.json.get("countB")
    spoofed_match_id = "0051681e-72ce-46f0-bda2-752e471d0d08"
    epoch = datetime.now().timestamp()

    session_cookie = request.cookies.get("bhvrSession")
    if not session_cookie:
        return jsonify({"message": "Endpoint not found"}), 404
    userid = session_manager.get_user_id(session_cookie)

    logger.graylog_logger(level="info", handler="logging_queue",
                          message=f"User {userid} is queueing for {category} in {region} with {count_a} hunters and {count_b} runners")

    # return {"status":"QUEUED","queueData":{"ETA":-10000,"position":0,"stable":False}}
    # else:
    #   # check here if more than one User is in the Queue and create a Match.
    #    return {"status":"QUEUED","queueData":{"ETA":-8000,"position":0,"stable":False}}

    # data = match_manager.find_match_id_from_user(user_id)
    # if data is None:
    #    print("No match found")
    #    # PlaceHolder for If User not in private match

    tmp = {"status": "MATCHED", "queueData": {"ETA": 0, "position": 0, "stable": False},
           "matchData": {"matchId": "asdasdassdasd-ddddd-asdasd-asdas-bfbfbfbfb", "schema": 3,
                         "category": "oman-100372-dev:None:Windows::us-east-1:1:4:0:G:2", "rank": 1, "geolocation": {},
                         "creationDateTime": 10101010101, "status": "CREATED",
                         "creator": "asdasdasdasdasdasdasd", "customData": {}, "version": 1,
                         "skill": {"longitude": 1.1, "latitude": 1.1, "rank": 20,
                                   "rating": {"rating": 11111, "RD": 111.1111, "volatility": 1.11}, "countries": ["AT"],
                                   "x": 20, "isSuspicious": False, "isProtected": False, "version": 2}, "churn": 0,
                         "props": {"countA": 1,
                                   "countB": 4, "gameMode": "None", "platform": "Windows", "isDedicated": False},
                         "reason": "", "sideA": ["asdasdasdasdasdasdasd"],
                         "sideB": ["dsadasdasdasdasdasddsa"],
                         "playerHistory": ["asdasdasdasdasdasdasd",
                                           "dsadasdasdasdasdasddsa"]}}
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
    else:
        return {"status": "QUEUED", "queueData": {"ETA": -10000, "position": 0, "stable": False}}
    # eta, position = match_manager.find_eta_and_position(data["_match_uuid"])


@app.route("/api/v1/match/<matchid>", methods=["GET"])
def match(matchid):
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    if matchid == "0051681e-72ce-46f0-bda2-752e471d0d08":
        return jsonify({"matchId": matchid, "schema": 3,
                        "category": "Steam-te-18f25613-36778-ue4-374f864b",
                        "geolocation": {}, "creationDateTime": datetime.now().timestamp(),
                        "status": "OPENED",
                        "creator": "00658d11-2dfd-41e8-b6d2-2462e8f3aa47",
                        "customData": {
                            "SessionSettings": "AAAAJDYxOWQ2ZjQyLWRiODctNGYzZS04ZGM5LTNjOTk5NTYxMzYxNAAAAAAAAAAAAAAAYwAAAGMAAAAAAQAAAAEAAQEAAAAAAAAAAAAKAAAAB01hcE5hbWUGAAAAA21hcAIAAAAQQ1VTVE9NU0VBUkNISU5UMgHRD3M7AgAAAAhnYW1lTW9kZQYAAAAoMDhkMjI3OWQyZWQzZmJhNTU5OTE4YWFhMDhhNzNmYTgtRGVmYXVsdAIAAAAOUHJvamVjdFZlcnNpb24GAAAAHnRlLTE4ZjI1NjEzLTM2Nzc4LXVlNC0zNzRmODY0YgIAAAAQQ1VTVE9NU0VBUkNISU5UMQEAAAABAgAAAAdNYXhSYW5rAQAAAAECAAAAB01pblJhbmsBAAAAAQIAAAAQTWlycm9yc1Nlc3Npb25JZAYAAAAkMDA1MTY4MWUtNzJjZS00NmYwLWJkYTItNzUyZTQ3MWQwZDA4AgAAAAxQbGF0Zm9ybU5hbWUGAAAABVN0ZWFtAgAAABFQbGF0Zm9ybVNlc3Npb25JZAYAAAAsMXx8NzY1NjExOTkxNjk3ODEyODU6Nzc3N3wxMDk3NzUyNDI5MDM4OTYwOTgC"}
                           , "version": 2, "churn": 0, 'props':
                            {"gameMode": "08d2279d2ed3fba559918aaa08a73fa8-Default",
                             'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_Demo.MatchConfig_Demo'},
                        "reason": "", "SideA": ["619d6f42-db87-4f3e-8dc9-3c9995613614"],
                        "SideB": ["00658d11-2dfd-41e8-b6d2-2462e8f3aa47"]})
    else:
        json_dict = match_manager.find_json_with_match_id(matchid)
        return jsonify({"matchId": matchid, "schema": 3,
                        "category": json_dict["category"],
                        "geolocation": {}, "creationDateTime": json_dict["time_created"],
                        "status": "OPENED",
                        "creator": json_dict["creator"],
                        "customData": json_dict["custom_data"], "version": 2, "churn": 0,
                        "props": {"countA": 1, "countB": 4,
                                  "gameMode": "None",
                                  "platform": "Windows",
                                  "isDedicated": False},
                        "reason": "", "sideA": [json_dict["players_side_a"]],
                        "sideB": [json_dict["players_side_b"]]})


@app.route("/api/v1/match/<matchid>/Kill", methods=["PUT"])
def match_kill(matchid):
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    logger.graylog_logger(level="info", handler="match_kill", message=f"Match {matchid} has been killed")
    return jsonify({"status": "OK"})


@app.route("/api/v1/match/<match_id>/register", methods=["POST"])
def match_register(match_id):
    try:
        check = check_for_game_client("strict")
        if not check:
            return jsonify({"message": "Endpoint not found"}), 404
        custom_data = request.get_json("customData")
        if custom_data["sessionSettings"]:
            session_settings = custom_data["sessionSettings"]

        session_cookie = request.cookies.get("bhvrSession")
        if not session_cookie:
            return jsonify({"message": "Endpoint not found"}), 404
        userid = session_manager.get_user_id(session_cookie)

        logger.graylog_logger(level="info", handler="match_register",
                              message=f"User {userid} is registering to match {match_id}")
        return jsonify({"status": "OK"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="match_register", message=e)
        return jsonify({"status": "ERROR"})


@app.route("/api/v1/match/<match_id>/Quit", methods=["PUT"])
def match_quit(match_id):
    try:
        check = check_for_game_client("strict")
        if not check:
            return jsonify({"message": "Endpoint not found"}), 404

        session_cookie = request.cookies.get("bhvrSession")
        if not session_cookie:
            return jsonify({"message": "Endpoint not found"}), 404
        userid = session_manager.get_user_id(session_cookie)

        logger.graylog_logger(level="info", handler="logging_queue",
                              message=f"User {userid} is quieting match {match_id}")
        return jsonify({"status": "OK"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_queue", message=e)
        return jsonify({"status": "ERROR"})


@app.route("/api/v1/match/create", methods=["POST"])
def match_create():
    # {'category': 'Steam-te-18f25613-36778-ue4-374f864b', 'region': 'US', 'playersA': [],
    # 'playersB': ['00658d11-2dfd-41e8-b6d2-2462e8f3aa47', '95041085-e7e4-4759-be3d-e72c69167578',
    # '0385496c-f0ae-44d3-a777-26092750f39c'],
    # 'props': {'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_Demo.MatchConfig_Demo'},
    # 'latencies': []}
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404

    session_cookie = request.cookies.get("bhvrSession")
    if not session_cookie:
        return jsonify({"message": "Endpoint not found"}), 404
    userid = session_manager.get_user_id(session_cookie)

    category = request.json.get("category")
    rank = request.json.get("rank")
    players_a = request.json.get("playersA")
    players_b = request.json.get("playersB")
    props = request.json.get("props")

    match_id = match_manager.create_match(request.json)
    epoch = datetime.now().timestamp()
    player_list = [players_b, players_a]

    data = {"MatchId": match_id, "Category": category, "Rank": rank,
            "CreationDateTime": epoch, "ExcludeFriends": False,
            "ExcludeClanMembers": False, "Status": "WaitingForPlayers", "Creator": userid,
            "Players": player_list, "SideA": players_a, "SideB": players_b, "CustomData": {}, "Props": props,
            "Schema": 11122334455666}
    return jsonify(data)


@app.route("/api/v1/extensions/progression/playerEndOfMatch", methods=["POST"])
def progression_player_end_of_match():
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    try:
        logger.graylog_logger(level="info", handler="matchmaking_playerEndOfMatch", message=request.get_json())
        return jsonify("", 204)
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="matchmaking_playerEndOfMatch", message=e)


@app.route("/file/<game_version>/<seed>/<map_name>", methods=["POST", "GET"])
def file_gold_rush(seed, map_name, game_version):
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404

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
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    try:
        logger.graylog_logger(level="info", handler="logging_matchmaking_Event", message=request.get_json())
        return jsonify({"status": "success"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_matchmaking_Event", message=e)

