import json
import os
from datetime import datetime

from logic.match_manager import match_manager
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
        logger.graylog_logger(level="error", handler="matchmaking_RegionsRAW", message=e)


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

    category = request.json.get("category")
    rank = request.json.get("rank")
    side = request.json.get("side")
    latencies = request.json.get("latencies")
    additional_user_ids = request.json.get("additionalUserIds")
    check_only = request.json.get("checkOnly") # False = Searching. True = Is searching and waiting for match
    game_mode = request.json.get("gameMode")
    region = request.json.get("region")
    count_a = request.json.get("countA")
    count_b = request.json.get("countB")
    user_id = request.cookies.get("bhvrSession")

    logger.graylog_logger(level="info", handler="logging_queue", message=f"User {user_id} is queueing for {category} in {region} with {count_a} hunters and {count_b} runners")

    # data = match_manager.find_match_id_from_user(user_id)
    # if data is None:
    #    print("No match found")
    #    # PlaceHolder for If User not in private match
    return {"status":"QUEUED","queueData":{"ETA":-10000,"position":0,"stable":False}}
    #eta, position = match_manager.find_eta_and_position(data["_match_uuid"])


@app.route("/api/v1/match/<matchid>", methods=["GET"])
def match(matchid):
    json_dict = match_manager.find_json_with_match_id(matchid)
    return jsonify({"matchId":matchid,"schema":3,
                    "category":json_dict["category"],
                    "geolocation":{},"creationDateTime":json_dict["time_created"],
                    "status":"OPENED",
                    "creator":json_dict["creator"],
                    "customData":json_dict["custom_data"],"version":2,"churn":0,"props":{"countA":1,"countB":4,
                                                                                         "gameMode":"None",
                                                                                         "platform":"Windows",
                                                                                         "isDedicated":False},
                    "reason":"","sideA":[json_dict["players_side_a"]],
                    "sideB":[json_dict["players_side_b"]]})


@app.route("/api/v1/match/create", methods=["POST"])
def match_create():
    # {'category': 'Steam-te-18f25613-36778-ue4-374f864b', 'region': 'US', 'playersA': [],
    # 'playersB': ['00658d11-2dfd-41e8-b6d2-2462e8f3aa47', '95041085-e7e4-4759-be3d-e72c69167578',
    # '0385496c-f0ae-44d3-a777-26092750f39c'],
    # 'props': {'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_Demo.MatchConfig_Demo'},
    # 'latencies': []}
    get_remote_ip()

    userid = request.cookies.get("bhvrSession")
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
    get_remote_ip()
    try:
        print("Responded to progression player end of match api call POST")
        logger.graylog_logger(level="info", handler="matchmaking_playerEndOfMatch", message=request.get_json())
        return jsonify("", 204)
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="matchmaking_playerEndOfMatch", message=e)
