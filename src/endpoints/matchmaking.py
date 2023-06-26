import json
import os
from datetime import datetime

from flask_definitions import *
import uuid

@app.route("/api/v1/config/MATCH_MAKING_REGIONS/raw", methods=["GET"])
def match_making_regions_raw():
    get_remote_ip()
    try:
        # print(request.json)
        return jsonify(["EU", "US", "AP"])
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        print(e)


@app.route("/api/v1/queue/info", methods=["GET"])
def queue_info():
    # ?category=Steam-te-23ebf96c-27498-ue4-7172a3f5&gameMode=Default&region=US&countA=1&countB=5
    get_remote_ip()
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
    get_remote_ip()
    print("DEBUG: queue called")
    print(request.json)
    userid = request.json.get("userId")
    category = request.json.get("category")
    rank = request.json.get("rank")
    side = request.json.get("side")
    latencies = request.json.get("latencies")
    additional_user_ids = request.json.get("additionalUserIds")
    check_only = request.json.get("checkOnly")
    game_mode = request.json.get("gameMode")
    region = request.json.get("region")
    count_a = request.json.get("countA")
    count_b = request.json.get("countB")
    epoch = datetime.now().timestamp()
    match_id = uuid.uuid4()
    user = request.cookies.get("bhvrSession")

    file_name = "session.match"
    folder_path = os.path.join(app.root_path, "match_ids", user)
    file_path = os.path.join(folder_path, file_name)

    if folder_path:
        match_data = json.load(open(file_path, "r"))
        return_val = {"status": "WaitingForPlayers", "QueueData":
            {"Position": 1, "ETA": 1, "Stable": True, "SizeA": count_a, "SizeB": count_b},
                        "MatchData": match_data}
        return jsonify(return_val)

    try:
        print("Responded to queue api call POST")
        logger.graylog_logger(level="info", handler="logging_queue", message=request.get_json())
        return jsonify({"status": "WaitingForPlayers", "QueueData":
            {"Position": 10, "ETA": 1000, "Stable": True, "SizeA": count_a, "SizeB": count_b},
                        "MatchData": {"MatchId": match_id, "Category": category, "Rank": rank,
                                      "CreationDateTime": epoch, "ExcludeFriends": False,
                                      "ExcludeClanMembers": False, "Status": "WaitingForPlayers", "Creator": userid,
                                      "Players": [userid], "SideA": [], "SideB": [userid], "CustomData": {}, "Props": {},
                                      "Schema": 11122334455666}})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_queue", message=str(e))


@app.route("/api/v1/match/create", methods=["POST", "GET"])
def match_create():
    # {'category': 'Steam-te-18f25613-36778-ue4-374f864b', 'region': 'US', 'playersA': [],
    # 'playersB': ['00658d11-2dfd-41e8-b6d2-2462e8f3aa47', '95041085-e7e4-4759-be3d-e72c69167578',
    # '0385496c-f0ae-44d3-a777-26092750f39c'],
    # 'props': {'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_Demo.MatchConfig_Demo'}, 'latencies': []}
    get_remote_ip()

    if request.method == "POST":
        print("DEBUG CREATE MATCH")
        print(request.json)
        userid = request.cookies.get("bhvrSession")
        category = request.json.get("category")
        match_id = str(uuid.uuid4())
        rank = request.json.get("rank")
        epoch = datetime.now().timestamp()
        players_a = request.json.get("playersA")
        players_b = request.json.get("playersB")
        props = request.json.get("props")
        player_list = []

        player_list.append(players_b)
        player_list.append(players_a)

        file_name = "session.match"

        data = {"MatchId": match_id, "Category": category, "Rank": rank,
                "CreationDateTime": epoch, "ExcludeFriends": False,
                "ExcludeClanMembers": False, "Status": "WaitingForPlayers", "Creator": userid,
                "Players": player_list, "SideA": players_a, "SideB": players_b, "CustomData": {}, "Props": props,
                "Schema": 11122334455666}

        for user_list in player_list:
            for user in user_list:
                user = str(user)
                folder_path = os.path.join(app.root_path, "match_ids", user)
                file_path = os.path.join(folder_path, file_name)
                os.makedirs(folder_path, exist_ok=True)
                json.dump(data, open(file_path, "w"), indent=4)
        data = jsonify(data)
        data.set_cookie("match_id", match_id)
        return data


@app.route("/api/v1/extensions/progression/playerEndOfMatch", methods=["POST"])
def progression_player_end_of_match():
    get_remote_ip()
    try:
        print("Responded to progression player end of match api call POST")
        logger.graylog_logger(level="info", handler="logging_playerEndOfMatch", message=request.get_json())
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_playerEndOfMatch", message=e)
