import sys
import time
from math import ceil

from flask_definitions import *
import requests
from logic.time_handler import get_time

global steam_api_key


def steam_login_function():
    try:
        steam_session_token = request.args.get('token')
        appid = 555440
        response = requests.get(
            'https://api.steampowered.com/ISteamUserAuth/AuthenticateUserTicket/v1/?key={}&ticket={}&appid={}'.format(
                steam_api_key, steam_session_token, appid))
        if response.json() == {"response": {"error": {"errorcode": 102, "errordesc": "Ticket for other app"}}}:
            appid = 854040
            response = requests.get(
                'https://api.steampowered.com/ISteamUserAuth/AuthenticateUserTicket/v1/?key={}&ticket={}&appid={}'.format(
                    steam_api_key, steam_session_token, appid))
            steamid = response.json()["response"]["params"]["steamid"]
            logger.graylog_logger(level="info", handler="steam_login",
                                  message="User {} logged in with SOFTLAUNCH".format(steamid))
            return jsonify({"status": "error"})

        steamid = response.json()["response"]["params"]["steamid"]
        # owner_id = response.json()["response"]["params"]["result"]["ownersteamid"]  # This is providerId

        userid, token = mongo.user_db_handler(steamid)
        current_time, expire_time = get_time()

        logger.graylog_logger(level="info", handler="steam_login", message="User {} logged in".format(steamid))
        # Read: Doc -> AUTH
        # You can copy and paste the JSON from the Auth Doc here. If you don't have a steam api key.
        # The Client does not validate this and just uses it.

        # if acc younger than cur + 1209600 ban
        user_data_response = requests.get(f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={steam_api_key}&steamids={steamid}")
        # {"response": {"players": [{"steamid": "76561199124885528", "communityvisibilitystate": 1, "profilestate": 1, "personaname": "FocusriteLP", "commentpermission": 2, "profileurl": "https://steamcommunity.com/profiles/76561199124885528/", "avatar": "https://avatars.steamstatic.com/267a6647071c7c5ff28744edbd852894b0e89d64.jpg", "avatarmedium": "https://avatars.steamstatic.com/267a6647071c7c5ff28744edbd852894b0e89d64_medium.jpg", "avatarfull": "https://avatars.steamstatic.com/267a6647071c7c5ff28744edbd852894b0e89d64_full.jpg", "avatarhash": "267a6647071c7c5ff28744edbd852894b0e89d64", "personastate": 0}]}}}
        user_data = user_data_response.json()["response"]["players"][0]
        logger.graylog_logger(level="info", handler="steam_login", message=user_data)
        if user_data["communityvisibilitystate"] == 3:
            timecreated = user_data["timecreated"]
            if timecreated > current_time + 1209600:
                logger.graylog_logger(level="info",
                                      handler="steam_login",
                                      message=f"User {steamid} got banned for ban evasion.")
                mongo.write_data_with_list(login=userid,
                                           login_steam=False,
                                           items_dict={"is_banned": True,
                                                       "ban_reason": "Ban evasion detected.",
                                                       "ban_start": current_time,
                                                       "ban_expire": 1893459600})

        # get_challenge_ids_from_inventory(userid)
        return jsonify({"preferredLanguage": "en", "friendsFirstSync": {"steam": True}, "fixedMyFriendsUserPlatformId":
            {"steam": True}, "id": userid, "provider": {"providerId": steamid, "providerName": "steam", "userId":
            userid}, "providers": [{"providerName": "steam", "providerId": steamid}], "friends": [], "triggerResults":
                            {"success": [], "error": []}, "tokenId": userid, "generated": current_time,
                        "expire": expire_time,
                        "userId": userid, "token": token})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="steam_login", message=e)


def get_init_or_get_groups(userid, request_data):
    data = {}
    skip_progression_groups = request_data["data"]["skipProgressionGroups"]
    skip_metadata_groups = request_data["data"]["skipMetadataGroups"]
    if not skip_progression_groups:
        Progression_HunterGroupA = mongo.get_data_with_list(login=userid, login_steam=False,
                                                            items={"HunterGroupA"})
        Progression_HunterGroupB = mongo.get_data_with_list(login=userid, login_steam=False,
                                                            items={"HunterGroupB"})
        Progression_HunterGroupC = mongo.get_data_with_list(login=userid, login_steam=False,
                                                            items={"HunterGroupC"})
        Progression_HunterGroupD = mongo.get_data_with_list(login=userid, login_steam=False,
                                                            items={"HunterGroupD"})
        Progression_RunnerGroupA = mongo.get_data_with_list(login=userid, login_steam=False,
                                                            items={"RunnerGroupA"})
        Progression_RunnerGroupB = mongo.get_data_with_list(login=userid, login_steam=False,
                                                            items={"RunnerGroupB"})
        Progression_RunnerGroupC = mongo.get_data_with_list(login=userid, login_steam=False,
                                                            items={"RunnerGroupC"})
        Progression_RunnerGroupD = mongo.get_data_with_list(login=userid, login_steam=False,
                                                            items={"RunnerGroupD"})
        Progression_RunnerGroupE = mongo.get_data_with_list(login=userid, login_steam=False,
                                                            items={"RunnerGroupE"})
        Progression_RunnerGroupF = mongo.get_data_with_list(login=userid, login_steam=False,
                                                            items={"RunnerGroupF"})
        RunnerProgression = mongo.get_data_with_list(login=userid, login_steam=False,
                                                     items={"RunnerProgression"})
        HunterProgression = mongo.get_data_with_list(login=userid, login_steam=False,
                                                     items={"HunterProgression"})
        PlayerProgression = mongo.get_data_with_list(login=userid, login_steam=False,
                                                     items={"PlayerProgression"})

        # 'HunterGroupD': {
        #                 'prestige': 0,
        #                 'experience': {
        #                     'level': 1,
        #                     'experienceToReach': 5403,
        #                     'currentExperience': 0
        #                 },
        #                 'Equipment': [],
        #                 'EquippedPerks': [],
        #                 'EquippedPowers': [],
        #                 'EquippedWeapons': [],
        #                 'EquippedBonuses': [],
        #                 'pickedChallenges': []

        data["progressionGroups"] = [
            {
                "version": 10,
                "objectId": "HunterGroupA",
                "data": {
                    "experience": Progression_HunterGroupA["HunterGroupA"]["experience"],
                    "metadata": [

                    ]
                },
                "schemaVersion": 1
            },
            {
                "version": 2,
                "objectId": "HunterGroupB",
                "data": {
                    "experience": Progression_HunterGroupB["HunterGroupB"]["experience"],
                    "metadata": [

                    ]
                },
                "schemaVersion": 1
            },
            {
                "version": 2,
                "objectId": "HunterGroupC",
                "data": {
                    "experience": Progression_HunterGroupC["HunterGroupC"]["experience"],
                    "metadata": [

                    ]
                },
                "schemaVersion": 1
            },
            {
                "version": 2,
                "objectId": "HunterGroupD",
                "data": {
                    "experience": Progression_HunterGroupD["HunterGroupD"]["experience"],
                    "metadata": [

                    ]
                },
                "schemaVersion": 1
            },
            {
                "version": 2,
                "objectId": "HunterProgression",
                "data": {
                    "experience": HunterProgression["HunterProgression"]["experience"],
                    "metadata": [

                    ]
                },
                "schemaVersion": 1
            },
            {
                "version": 2,
                "objectId": "PlayerProgression",
                "data": {
                    "experience": PlayerProgression["PlayerProgression"]["experience"],
                    "metadata": [

                    ]
                },
                "schemaVersion": 1
            },
            {
                "version": 646,
                "objectId": "RunnerGroupA",
                "data": {
                    "experience": Progression_RunnerGroupA["RunnerGroupA"]["experience"],
                    "metadata": [

                    ]
                },
                "schemaVersion": 1
            },
            {
                "version": 2,
                "objectId": "RunnerGroupB",
                "data": {
                    "experience": Progression_RunnerGroupB["RunnerGroupB"]["experience"],
                    "metadata": [

                    ]
                },
                "schemaVersion": 1
            },
            {
                "version": 2,
                "objectId": "RunnerGroupC",
                "data": {
                    "experience": Progression_RunnerGroupC["RunnerGroupC"]["experience"],
                    "metadata": [

                    ]
                },
                "schemaVersion": 1
            },
            {
                "version": 36,
                "objectId": "RunnerGroupD",
                "data": {
                    "experience": Progression_RunnerGroupD["RunnerGroupD"]["experience"],
                    "metadata": [

                    ]
                },
                "schemaVersion": 1
            },
            {
                "version": 3229,
                "objectId": "RunnerGroupE",
                "data": {
                    "experience": Progression_RunnerGroupE["RunnerGroupE"]["experience"],
                    "metadata": [

                    ]
                },
                "schemaVersion": 1
            },
            {
                "version": 7,
                "objectId": "RunnerGroupF",
                "data": {
                    "experience": Progression_RunnerGroupF["RunnerGroupF"]["experience"],
                    "metadata": [

                    ]
                },
                "schemaVersion": 1
            },
            {
                "version": 235,
                "objectId": "RunnerProgression",
                "data": {
                    "experience": RunnerProgression["RunnerProgression"]["experience"],
                    "metadata": [

                    ]
                },
                "schemaVersion": 1
            }
        ]
    if not skip_metadata_groups:
        data["metadataGroups"] = []

        last_played_faction = mongo.get_data_with_list(login=userid, login_steam=False, items={"last_played_faction"})
        tutorial_completed = mongo.get_data_with_list(login=userid, login_steam=False, items={"tutorial_completed"})
        last_runner = mongo.get_data_with_list(login=userid, login_steam=False, items={"last_runner"})
        last_hunter = mongo.get_data_with_list(login=userid, login_steam=False, items={"last_hunter"})
        hasPlayedDeathGarden1 = mongo.get_data_with_list(login=userid, login_steam=False,
                                                         items={"hasPlayedDeathGarden1"})
        characterCumulativeExperience = mongo.get_data_with_list(login=userid, login_steam=False,
                                                                 items={"ProfileMetaData"})["ProfileMetaData"][
            "characterCumulativeExperience"]

        Runner_List = ["RunnerGroupA", "RunnerGroupB", "RunnerGroupC", "RunnerGroupD", "RunnerGroupE", "RunnerGroupF"]
        Hunter_List = ["HunterGroupA", "HunterGroupB", "HunterGroupC", "HunterGroupD"]

        data["metadataGroups"] = [
            {
                "version": 342,
                "objectId": "PlayerMetadata",
                "data": {
                    "lastPlayedFaction": last_played_faction["last_played_faction"],
                    "shouldPlayWithoutContextualHelp": tutorial_completed["tutorial_completed"],
                    "lastPlayedRunnerId": {
                        "tagName": last_runner["last_runner"]
                    },
                    "lastPlayedHunterId": {
                        "tagName": last_hunter["last_hunter"]
                    },
                    "hasPlayedDeathGarden1": hasPlayedDeathGarden1["hasPlayedDeathGarden1"]
                },
                "schemaVersion": 1
            },
            {
                "version": 2,
                "objectId": "HunterMetadata",
                "data": [
                ],
                "schemaVersion": 1
            },
            {
                "version": 804,
                "objectId": "ProfileMetadata",
                "data": {
                    "characterCumulativeExperience": characterCumulativeExperience
                },
                "schemaVersion": 1
            },
            {
                "version": 2,
                "objectId": "RunnerMetadata",
                "data": [
                ],
                "schemaVersion": 1
            }
        ]

        for group in Runner_List + Hunter_List:
            group_data = mongo.get_data_with_list(login=userid, login_steam=False, items={group})[group]
            equippedPerks = group_data["EquippedPerks"]
            equippedWeapons = group_data["EquippedWeapons"]
            equipment = group_data["Equipment"]
            equippedBonuses = group_data["EquippedBonuses"]
            equippedPowers = group_data["EquippedPowers"]
            prestige = group_data["prestige"]
            pickedChallenges = group_data["pickedChallenges"] # Removed because Challenges are still broken.
            characterId = group_data["characterId"]
            equippedConsumables = group_data["equippedConsumables"]

            data["metadataGroups"].append({
                "version": 3,
                "objectId": group,
                "data": {
                    "equippedPerks": equippedPerks,
                    "equippedWeapons": equippedWeapons,
                    "equipment": equipment,
                    "equippedBonuses": equippedBonuses,
                    "pickedChallenges": [],
                    "equippedConsumables": equippedConsumables,
                    "characterId": characterId,
                    "equippedPowers": equippedPowers,
                    "prestigeLevel": prestige
                },
                "schemaVersion": 1
            })

    data["rewards"] = []
    return data


# This works
@app.route("/api/v1/auth/provider/steam/login", methods=["POST"])
def steam_login():
    # Read Doc\SteamAuth.md for more information
    ip = check_for_game_client("soft")
    user_agent = sanitize_input(request.headers.get('User-Agent'))
    request_token = sanitize_input(request.args.get('token'))
    if user_agent.startswith("TheExit/++UE4+Release-4.2"):
        if request_token == "140000007B7B7B7B02000000E3FA3952010010017B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B":
            userid, token = mongo.user_db_handler("Debug_session")
            current_time, expire_time = get_time()
            return_val = jsonify({"preferredLanguage": "en", "friendsFirstSync": {"steam": True},
                                  "fixedMyFriendsUserPlatformId":
                                      {"steam": True}, "id": userid,
                                  "provider": {"providerId": userid, "providerName": "steam", "userId":
                                      userid}, "providers": [{"providerName": "steam", "providerId": userid}],
                                  "friends": [],
                                  "triggerResults":
                                      {"success": [], "error": []}, "tokenId": userid, "generated": current_time,
                                  "expire": expire_time,
                                  "userId": userid, "token": token})
            session_cookie = session_manager.create_session(userid)
            return_val.set_cookie("bhvrSession", session_cookie)
            return return_val
        try:

            return_val = steam_login_function()
            session_cookie = session_manager.create_session(return_val.json["id"])
            print(f"Logged in with token: {session_cookie}", file=sys.stderr)
            return_val.set_cookie("bhvrSession", session_cookie)
            return return_val
        except Exception as e:
            logger.graylog_logger(level="error", handler="steam_login", message=e)
            abort(401, "Unauthorized")

    elif user_agent.startswith("game=TheExit, engine=UE4, version="):
        return_val = steam_login_function()
        session_cookie = session_manager.create_session(return_val.json["id"])
        return_val.set_cookie("bhvrSession", session_cookie)
        return return_val

    else:
        logger.graylog_logger(level="error", handler="steam_login", message={"text": "Access denied to User Agent",
                                                                             "User-Agent": user_agent, "IP": ip})
        abort(401, "Unauthorized")


# Dont know if this works
@app.route("/api/v1/modifierCenter/modifiers/me", methods=["GET"])
def modifiers():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    data = mongo.get_data_with_list(login=userid, login_steam=False,
                                    items={"steamid", "token"})

    token = data["token"]
    steamid = data["steamid"]
    try:
        return jsonify({"Modifiers": []})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="modifiers_me", message=e)


@app.route("/api/v1/modifierCenter/modifiers/<userid>", methods=["GET"])
def modifiers_userid(userid):
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    steamid, token = mongo.get_data_with_list(login=userid, login_steam=False,
                                              items={"token", "steamid"})
    try:
        # todo TEMP REMOVE
        users_with_dg1 = [
            "76561198129051713",
            "76561198076387733",
            "76561197960308924",
            "76561198838605143",
            "76561198375755382",
            "76561198190942526",
            "76561198085931811",
            "76561198804479305",
            "76561197987790181",
            "76561198051757391",
            "76561197987310750",
            "76561198811124309",
            "76561198275831683",
            "76561198331700778",
            "76561198064369535",
            "76561198069250881",
            "76561198059448904",
            "76561198143207619",
            "76561198069014976",
            "76561198140796510",
            "76561199169781285",
            "76561198124949660"
        ]
        data = mongo.get_data_with_list(login=userid, login_steam=False, items={"steamid", "hasPlayedDeathGarden1"})
        if not data["hasPlayedDeathGarden1"]:
            if data["steamid"] in users_with_dg1:
                mongo.write_data_with_list(login=userid, login_steam=False,
                                           items_dict={"hasPlayedDeathGarden1": True})
        return jsonify({"Modifiers": []})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="modifiers_me", message=e)


# This works
@app.route("/moderation/check/username", methods=["POST"])
def moderation_check_username():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    try:
        request_var = request.get_json()
        userid = sanitize_input(request_var["userId"])
        username = sanitize_input(request_var["username"])
        if userid == "d7662a88-72f4-4279-a985-c2c6ac0a8404":
            return jsonify({"List": [{"UserId": userid, "PlayerName": "DEV: HEX: Dino Nuggies"}]})
        return jsonify({
            "PlayerName": username,
            "UserId": userid
        })
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="moderation_check_username", message=e)


# Doesn't work
# OG DG Endpoint
@app.route("/api/v1/progression/experience", methods=["POST"])
def progression_experience():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    try:
        logger.graylog_logger(level="info", handler="user_handling_progression_experience", message=request.get_json())
        return jsonify({"List": [
            {"ObjectId": "PlayerProgression", "SchemaVersion": 11122233344, "Version": 11122233345,
             "Data": {"ObjectId": "PlayerProgression", "Experience": 100, "Version": 1}},
            {"ObjectId": "RunnerProgression", "SchemaVersion": 11122233345, "Version": 11122233345,
             "Data": {"ObjectId": "Runner.Smoke", "Experience": 100, "Version": 1}},
            {"ObjectId": "RunnerProgression", "SchemaVersion": 11122233346, "Version": 11122233346,
             "Data": {"ObjectId": "Runner.Ghost", "Experience": 100, "Version": 1}},
            {"ObjectId": "RunnerProgression", "SchemaVersion": 11122233346, "Version": 11122233346,
             "Data": {"ObjectId": "Runner.Ink", "Experience": 100, "Version": 1}},
            {"ObjectId": "RunnerProgression", "SchemaVersion": 11122233346, "Version": 11122233346,
             "Data": {"ObjectId": "Runner.Sawbones", "Experience": 100, "Version": 1}},
            {"ObjectId": "RunnerProgression", "SchemaVersion": 11122233346, "Version": 11122233346,
             "Data": {"ObjectId": "Runner.Switch", "Experience": 100, "Version": 1}},
            {"ObjectId": "RunnerProgression", "SchemaVersion": 11122233346, "Version": 11122233346,
             "Data": {"ObjectId": "Runner.Dash", "Experience": 100, "Version": 1}},
            {"ObjectId": "HunterProgression", "SchemaVersion": 11122233346, "Version": 11122233346,
             "Data": {"ObjectId": "Hunter.Inquisitor", "Experience": 100, "Version": 1}},
            {"ObjectId": "HunterProgression", "SchemaVersion": 11122233346, "Version": 11122233346,
             "Data": {"ObjectId": "Hunter.Stalker", "Experience": 100, "Version": 1}},
            {"ObjectId": "HunterProgression", "SchemaVersion": 11122233346, "Version": 11122233346,
             "Data": {"ObjectId": "Hunter.Poacher", "Experience": 100, "Version": 1}},
            {"ObjectId": "HunterProgression", "SchemaVersion": 11122233346, "Version": 11122233346,
             "Data": {"ObjectId": "Hunter.Mass", "Experience": 100, "Version": 1}}
        ]})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="progression_experience", message=e)


@app.route("/api/v1/extensions/challenges/getChallenges", methods=["POST"])
def challenges_get_challenges():
    # client: {"data":{"userId":"619d6f42-db87-4f3e-8dc9-3c9995613614","challengeType":"Daily"}}
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    # Removed because Challenges are still broken.
    return jsonify({"status": "error"})

    try:
        response = request.get_json()
        challenge_type = sanitize_input(response["data"]["challengeType"])
        if challenge_type == "Weekly":
            return_data = new_challenge_handler.get_time_based_challenges(challenge_type="Weekly", userid=userid)
        elif challenge_type == "Daily":
            return_data = new_challenge_handler.get_time_based_challenges(challenge_type="Daily", userid=userid)
        else:
            logger.graylog_logger(level="error", handler="getChallenges",
                                  message=f"Unknown challenge type {challenge_type}")
            return jsonify({"status": "error"})
        return jsonify({"challenges": return_data})

    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="getChallenges", message=e)


@app.route("/api/v1/extensions/challenges/executeChallengeProgressionOperationBatch", methods=["POST"])
def challenges_execute_challenge_progression_operation_batch():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    user_id = session_manager.get_user_id(session_cookie)
    # {
    #    "data":{
    #       "userId":"d7662a88-72f4-4279-a985-c2c6ac0a8404",
    #       "operations":[
    #          {
    #             "challengeId":"0E7912E34B0F76F06A54769371A1615A",
    #             "operationName":"complete"
    #          },
    #          {
    #             "challengeId":"EFAB89E6465D1163D62A07B11048F2B6",
    #             "operationName":"save",
    #             "operationData":{
    #                "className":"ChallengeProgressionCounter",
    #                "value":1,
    #                "schemaVersion":1
    #             }
    #          },
    #          {
    #             "challengeId":"AAD05B9D46471DC811BBE0BA91916AB7",
    #             "operationName":"save",
    #             "operationData":{
    #                "className":"ChallengeProgressionCounter",
    #                "value":1,
    #                "schemaVersion":1
    #             }
    #          },
    #          {
    #             "challengeId":"0E7912E34B0F76F06A54769371A1615A",
    #             "operationName":"save",
    #             "operationData":{
    #                "className":"ChallengeProgressionCounter",
    #                "value":1,
    #                "schemaVersion":1
    #             }
    #          },
    #          {
    #             "challengeId":"87A39D494DF78A55D012B4BCA091E043",
    #             "operationName":"save",
    #             "operationData":{
    #                "className":"ChallengeProgressionCounter",
    #                "value":39,
    #                "schemaVersion":1
    #             }
    #          }
    #       ]
    #    }
    # }

    try:
        data = request.get_json()
        userId = data["data"]["userId"]
        operations = data["data"]["operations"]
        error_list = []
        for operation in operations:
            challenge_id = operation["challengeId"]
            operation_name = operation["operationName"]
            if operation_name == "complete":
                ret = new_challenge_handler.update_challenge(userId, challenge_id, completed=True)
                #ret = update_progression_batch(challenge_id, userId, complete=True)
                if ret:
                    wallet = mongo.get_data_with_list(login=userId, login_steam=False,
                                                      items={"currency_blood_cells", "currency_iron",
                                                             "currency_ink_cells"})
                    currency_blood_cells = wallet["currency_blood_cells"]
                    currency_iron = wallet["currency_iron"]
                    currency_ink_cells = wallet["currency_ink_cells"]
                    currency_iron = currency_iron + 340
                    currency_ink_cells = currency_ink_cells + 340
                    currency_blood_cells = currency_blood_cells + 340
                    mongo.write_data_with_list(login=userId, login_steam=False,
                                               items_dict={"currency_blood_cells": currency_blood_cells,
                                                           "currency_iron": currency_iron,
                                                           "currency_ink_cells": currency_ink_cells})
                    pass
                else:
                    error_list.append(challenge_id)
            elif operation_name == "save":
                operation_data = operation["operationData"]
                value = operation_data["value"]
                ret = new_challenge_handler.update_challenge(userId, challenge_id, value=value)
                # DEV NOTE: "/Engine/" is a placeholder if SAVE and if HARDCODED
                if ret:
                    pass
                else:
                    error_list.append(challenge_id)
            else:
                logger.graylog_logger(level="error", handler="executeChallengeProgressionOperationBatch",message=f"Unknown operation {operation_name}")
        if error_list:
            logger.graylog_logger(level="error", handler="executeChallengeProgressionOperationBatch", message=f"Error while saving challenges for {userId} with challenge_ids {error_list}")
        return "", 204
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_executeChallengeProgressionOperationBatch",
                              message=e)


@app.route("/api/v1/inventories", methods=["GET"])
def inventories():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    base_inventory = [
        {'quantity': 1, 'objectId': '56B7B6F6473712D0B7A2F992BB2C16CD', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '234FFD464C55514B6C1E738645993CAA', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '755D4DFE40DA1512B01E3D8CFF3C8D4D', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'CCA2272D408ED95387F017BED437FF9A', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '606129DC45AB9D16B69E2FA5C99A9835', 'lastUpdateAt': 1574612664},

    ]
    deathgarden_1_inventory = [
        {'quantity': 1, 'objectId': 'FD93572C4CF2DFD134E6D9A90252F665', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'C645C7AC405B3D8AF8E73B946875F0AE', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'DADB36D34727AD788367D58873AB2106', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '428EE16F4F00056E576CC29ED83B8DAB', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '996863814494FF8C7B9531A7478FE762', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'BEF2872E4B3188B43B77EA9DCDFDE0AE', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'C0F44BF0417ACA353D0B8E8A26B1B1AB', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '0EB2781D45D950C6525B8CA308811AA3', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '0FDDDD6A45C0856D0B3EA785B1F508BC', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'D60E21A84EADE0E910DF2FAD7D382699', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'E59F6A1E4513039087919CA078090BFB', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'EF96A20249884D437B87A6A4BDE81B7F', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '2B011E8F46C37F900F8D40A9A73782EB', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '6A7E87AC403EF62B151C27A051B2E373', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'F4B0185D41460D68A0CF7D9A00ACB6E7', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '7474DFFE4A04B58BA12954B430637120', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '29447D464334997ECF872F8B08FDC442', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '2837D67046DAE1E3BE4E749A51BB555B', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'EF8E713B41CA7626D83D39BF05600FA4', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '34918BAF4507ECE322853D8D6DFE81D4', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '755D4DFE40DA1512B01E3D8CFF3C8D4D', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'B35F363447360EC17BE1BD92D827E08B', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '0ADDB41F4216A32D8F1853BAB25D20F2', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'DF5E3FD049902AB5DC1B3C8E22625AAF', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'E501095545F87E64AAFC74A04F1CFF5B', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'F9D4700D47DC559C7CCE11800F3A318A', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '6FF69DEE4FBC9CE82CC2818EE7864EAB', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '03175A2941AB8800F4CAF39ADCDDC663', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '7E2AB46D4BA6F40F03BA768A6F31DB17', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '8968BDBD4AB5F7017A446BB78416EB29', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '97CD4AEA444D6BD2CD218E92B7B12A33', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '098612FC4A3C827849BB55A59C2BC258', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '40E89D554CD74E398E5BAF86369E7C81', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '4302DF13418EC9BE3C8E119F390AACE2', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '865A380D485284B3C5A9409E04C22551', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '3EF7ED3449B8EA4E19BEDFBD100B1DFA', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '0600201B48B6E1F0B583039E01F8E909', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'C300E3A84E571D549E014B9051A18BE8', 'lastUpdateAt': 1574612664}

    ]

    try:
        page = request.args.get('page', default=0, type=int)
        limit = request.args.get('limit', default=500, type=int)
        items = mongo.get_data_with_list(login=userid, login_steam=False, items={"inventory"})
        for item in items["inventory"]:
            base_inventory.append({"quantity": 1, "objectId": item, "lastUpdateAt": 1574612664})

        hasPlayedDeathGarden1 = mongo.get_data_with_list(login=userid, login_steam=False, items={"hasPlayedDeathGarden1"})["hasPlayedDeathGarden1"]
        if hasPlayedDeathGarden1:
            for item in deathgarden_1_inventory:
                base_inventory.append(item)

        if page == 0:
            return jsonify({
                "code": 200,
                "message": "OK",
                "data": {
                    "playerId": "userid",
                    "inventory": base_inventory,
                }
            })
        elif page == 1:
            return jsonify({"Code": 200, "Message": "OK", "Data": {"PlayerId": userid, "Inventory": [
                {"ObjectId": "C1672541-4A4B16B9-AD557C9E-E865D113", "Quantity": 1, "LastUpdateAt": 1687377305}
            ], "NextPage": 0}})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="inventories", message=e)


# idk if this works
@app.route("/api/v1/players/me/splinteredstates/ProgressionGroups", methods=["GET"])
def progression_groups():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)
    try:
        #  This is the real code but need to build this first
        # return jsonify({"UserId": userid, "StateName": "Fstring", "Segment": "Fstring", "ObjectId": "Fstring",
        #                "Version": 1111, "schemaVersion": 1111, "Data": {}})
        return jsonify({"List": [{"ObjectId": "C50FFFBF-46866131-82F45890-651797CE",
                                  "SchemaVersion": 11111111,
                                  "Version": 11111111,
                                  "Data":
                                      [{"Level": 5, "Ratio": 0.111}]},
                                 {"ObjectId": "755D4DFE-40DA1512-B01E3D8C-FF3C8D4D",
                                  "SchemaVersion": 11111111,
                                  "Version": 11111111,
                                  "Data":
                                      [{"Level": 5, "Ratio": 0.111}]}
                                 ]})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="ProgressionGroups", message=e)


# This works
@app.route("/api/v1/players/ban/status", methods=["GET"])
def ban_status():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    try:
        ban_data = mongo.get_data_with_list(login=userid, login_steam=False,
                                            items={"is_banned", "ban_reason", "ban_start", "ban_expire"})
        if ban_data is None:
            return jsonify({"status": "error"})
        elif ban_data["is_banned"]:
            return jsonify({"IsBanned": ban_data["is_banned"], "BanInfo": {"BanPeriod": 10,
                                                                           "BanReason": ban_data["ban_reason"],
                                                                           "BanStart": ban_data["ban_start"],
                                                                           "BanEnd": ban_data["ban_expire"],
                                                                           "Confirmed": False, "Pending": False}})
        elif not ban_data["is_banned"]:
            return jsonify({"IsBanned": ban_data["is_banned"], "BanInfo": {"BanPeriod": 0,
                                                                           "BanReason": "None",
                                                                           "BanStart": 0,
                                                                           "BanEnd": 0,
                                                                           "Confirmed": False, "Pending": False}})
        else:
            return jsonify({"status": "error"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="ban_status", message=e)


# broken. no need to fix... OG DG endpoint. Not needed.
@app.route("/api/v1/players/ban/getbaninfo", methods=["GET"])
def get_ban_info():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    try:
        return jsonify({"BanPeriod": None, "BanReason": None, "BanStart": None, "BanEnd": None,
                        "Confirmed": False})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="ban_status", message=e)


# This works
@app.route("/api/v1/wallet/currencies", methods=["GET"])
def wallet_currencies():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    try:
        currencies = mongo.get_data_with_list(login=userid, login_steam=False,
                                              items={"currency_blood_cells", "currency_iron", "currency_ink_cells"})
        return jsonify({"List": [{"Currency": "CurrencyA", "Balance": currencies["currency_iron"],
                                  "CurrencyGroup": "SoftCurrencyGroup", "LastRefillTimeStamp": "1684862187"},
                                 {"Currency": "CurrencyB", "Balance": currencies["currency_blood_cells"],
                                  "CurrencyGroup": "SoftCurrencyGroup", "LastRefillTimeStamp": "1684862187"},
                                 {"Currency": "CurrencyC", "Balance": currencies["currency_ink_cells"],
                                  "CurrencyGroup": "SoftCurrencyGroup", "LastRefillTimeStamp": "1684862187"},
                                 {"Currency": "HARD_CURRENCY", "Balance": 6969,
                                  "CurrencyGroup": "HardCurrencyGroup", "LastRefillTimeStamp": "1684862187"},
                                 {"Currency": "PROGRESSION_CURRENCY", "Balance": 10000,
                                  "CurrencyGroup": "HardCurrencyGroup", "LastRefillTimeStamp": "1684862187"}]})
    except TypeError:
        return jsonify({"status": "error"})

    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="currencies", message=e)


# Does not work. Old DG endpoint. Not needed.
@app.route("/api/v1/wallet/currencies/PROGRESSION_CURRENCY", methods=["GET"])
def wallet_currencies_progression():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    try:
        return jsonify([{"Currency": 1, "Amount": 10}, {"Currency": 2, "Amount": 10}, {"Currency": 3, "Amount": 10}])
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="currencies", message=e)


# Dont know if this works. Dont think it does.
@app.route("/api/v1/players/me/splinteredstates/TheExit_Achievements", methods=["GET"])
def achievements_get():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    try:
        # I don't know how this fixes the console error but if it works for now idc...
        return jsonify({"UserId": userid,
                        "StateName": "Fstring",
                        "Segment": "FString",
                        "ObjectId": "",
                        "Version": 1,
                        "SchemaVersion": 1,
                        "Data": [
                            {
                                "ObjectId": "EFAB89E6465D1163D62A07B11048F2B6",
                                "Version": 11111111,
                                "SchemaVersion": 11111111,
                                "Data":
                                    {
                                        "Key": "Value"
                                    }
                            },
                            {
                                "ObjectId": "2CAEBB354D506D7C43B941BC1DA775A0",
                                "Version": 11111111,
                                "SchemaVersion": 11111111,
                                "Data":
                                    {
                                        "Key": "Value"
                                    }
                            },
                            {
                                "ObjectId": "E51981B946BEE3D45C5C41B2FCFF310B",
                                "Version": 11111111,
                                "SchemaVersion": 11111111,
                                "Data":
                                    {
                                        "Key": "Value"
                                    }
                            },
                            {
                                "ObjectId": "AAD05B9D46471DC811BBE0BA91916AB7",
                                "Version": 11111111,
                                "SchemaVersion": 11111111,
                                "Data":
                                    {
                                        "Key": "Value"
                                    }
                            },
                            {
                                "ObjectId": "BA2D4A5445CB70276A8F5D9E1AFCE080",
                                "Version": 11111111,
                                "SchemaVersion": 11111111,
                                "Data":
                                    {
                                        "Key": "Value"
                                    }
                            }
                        ]})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="Achievment_handler", message=e)


# Does not work
@app.route("/api/v1/messages/count", methods=["GET"])
def messages_count():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    try:
        flag = sanitize_input(request.args.get('flag'))
        if flag == "NEW":
            a = "a"
        else:
            logger.graylog_logger(level="debug", handler="messages_count", message=f"New message Count Flag {flag}")
        unread_message_ids = mongo.get_data_with_list(login=userid, login_steam=False, items={"unread_msg_ids"})
        if unread_message_ids["unread_msg_ids"] == "" or unread_message_ids is None:
            return jsonify({"Count": 0})
        else:
            length = len(unread_message_ids["unread_msg_ids"])
            return jsonify({"Count": length})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="messages_count", message=e)


@app.route("/api/v1/messages/list", methods=["GET", "DELETE"])
def messages_list():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    try:
        if request.method == "GET":
            limit = int(request.args.get("limit", 500))
            page = int(request.args.get("page", 1))

            unread_message_ids = mongo.get_data_with_list(login=userid, login_steam=False, items={"unread_msg_ids"})
            ids = []
            for items in unread_message_ids.get("unread_msg_ids", []):
                ids.append(str(items))

            json_file_path = os.path.join(app.root_path, "json", "placeholders", "messages.json")
            with open(json_file_path, "r") as json_file:
                data = json.load(json_file)

            messages = []
            for message_id in ids:
                messages.extend(data.get(message_id, []))

            total_messages = len(messages)

            if total_messages <= limit * page:
                pages = 0
            else:
                pages = ceil(total_messages / limit) - page

            start_idx = (page - 1) * limit
            end_idx = start_idx + limit
            messages_page = messages[start_idx:end_idx]

            return jsonify({"messages": messages_page, "NetPage": pages})

        elif request.method == "DELETE":
            return jsonify(""), 204
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="messages_list", message=str(e))

    return jsonify({"messages": [], "NetPage": 0})


@app.route("/api/v1/messages/v2/markAs", methods=["POST"])
def messages_mark_as():
    try:
        check_for_game_client("strict")
        session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
        userid = session_manager.get_user_id(session_cookie)
        data = request.get_json()
        message_list = data["messageList"]
        if not message_list:
            mongo.write_data_with_list(login=userid, login_steam=False, items_dict={"unread_msg_ids": ""})
            return jsonify({"List": [{"Received": get_time(), "Success": True, "RecipientId": userid}]})
        if message_list[0]["recipientId"] == "3":
            # Moderation MSG -> Do not del (Request by miraak)
            return jsonify({"List": [{"Received": get_time(), "Success": True, "RecipientId": userid}]})
        message_id = message_list[0]["recipientId"]
        unread_messages = mongo.get_data_with_list(login=userid, login_steam=False, items={"unread_msg_ids"})
        unread_messages = unread_messages["unread_msg_ids"].split(",")
        unread_messages.remove(message_id)
        unread_messages = ",".join(unread_messages)
        data = {"unread_msg_ids": unread_messages}
        mongo.write_data_with_list(login=userid, login_steam=False, items_dict=data)
        current_timestamp, expiration_timestamp = get_time()
        return jsonify({"List": [{"Received": current_timestamp, "Success": True, "RecipientId": userid}]})
    except TimeoutError:
        return jsonify({"status": "Timeout error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="messages_mark_as", message=e)
        return jsonify({"status": "API error"})


@app.route("/moderation/check/chat", methods=["POST"])
def moderation_check_chat():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    try:
        # Request: FApiHttpCheckChatRequest
        data = request.get_json()
        userid = sanitize_input(data["userId"])
        language = sanitize_input(data["language"])
        message = sanitize_input(data["message"])
        return jsonify({"status": "success", "result": "OK"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="moderation_check_chat", message=e)


@app.route("/api/v1/extensions/progression/initOrGetGroups", methods=["POST"])
def extension_progression_init_or_get_groups():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    # USER BAN CHECK
    #try:
    #    u_data = mongo.get_data_with_list(login=userid, login_steam=False, items={"is_banned"})["is_banned"]
    #    if u_data:
    #        return jsonify({"message": "User is banned", "status": "error"}), 401
    #except Exception as e:
    #    logger.graylog_logger(level="error", handler="extension_progression_init_or_get_groups", message=e)
    #    return jsonify({"status": "error"})

    try:
        request_data = request.get_json()
        data = get_init_or_get_groups(userid, request_data)
        return jsonify(data)

    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_initOrGetGroups", message=e)


@app.route("/api/v1/extensions/progression/updateMetadataGroup", methods=["POST"])
def update_metadata_group():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)
    try:
        data = request.get_json()
        object_id = data["data"]["objectId"]
        version = data["data"]["version"]
        metadata = data["data"]["metadata"]
        try:
            metadata["pickedChallenges"] = []
        except KeyError:
            pass
        try:
            reason = data["data"]["reason"]
        except KeyError:
            reason = "SetLastPlayedCharacterId"

        if reason == "SetLastPlayedCharacterId" or reason == "SetLastPlayedFaction":

            last_played_faction = metadata["lastPlayedFaction"]
            last_played_runner_id = metadata["lastPlayedRunnerId"]["tagName"]
            last_played_hunter_id = metadata["lastPlayedHunterId"]["tagName"]
            should_play_without_contextual_help = metadata["shouldPlayWithoutContextualHelp"]
            try:
                has_played_death_garden_1 = metadata["hasPlayedDeathGarden1"]
            except KeyError:
                # old version of game
                has_played_death_garden_1 = False
            mongo.write_data_with_list(login=userid, login_steam=False,
                                       items_dict={"last_played_faction": last_played_faction,
                                                   "last_hunter": last_played_hunter_id,
                                                   "last_runner": last_played_runner_id,
                                                   "hasPlayedDeathGarden1": has_played_death_garden_1,
                                                   "tutorial_completed": should_play_without_contextual_help})
        elif reason == "OnCloseLoadoout" or reason == "Character dirty":
            # Write data to DB
            character_id = metadata["characterId"]
            prestige_level = metadata["prestigeLevel"]
            equipment = metadata["equipment"]
            equippedPerks = metadata["equippedPerks"]
            equippedPowers = metadata["equippedPowers"]
            equippedWeapons = metadata["equippedWeapons"]
            equippedBonuses = metadata["equippedBonuses"]
            equippedConsumables = metadata["equippedConsumables"]
            pickedChallenges = metadata["pickedChallenges"]

            # 'RunnerGroupC': {
            #                 'prestige': 0,
            #                 'experience': {
            #                     'level': 1,
            #                     'experienceToReach': 5403,
            #                     'currentExperience': 0
            #                 },
            #                 'Equipment': [],
            #                 'EquippedPerks': [],
            #                 'EquippedPowers': [],
            #                 'EquippedWeapons': [],
            #                 'EquippedBonuses': [],
            #                 'pickedChallenges': [],
            #                 'characterId': {"tagName":"Runner.Ghost"}
            object_data = mongo.get_data_with_list(login=userid, login_steam=False, items={object_id})

            database_dict = {object_id: {"prestige": prestige_level,
                                         "experience": object_data[object_id]["experience"],
                                         "Equipment": equipment,
                                         "EquippedPerks": equippedPerks,
                                         "EquippedPowers": equippedPowers,
                                         "EquippedWeapons": equippedWeapons,
                                         "EquippedBonuses": equippedBonuses,
                                         "pickedChallenges": pickedChallenges,
                                         "equippedConsumables": equippedConsumables,
                                         "characterId": character_id}}

            mongo.write_data_with_list(login=userid, login_steam=False, items_dict=database_dict)

        elif reason == "OnRequestCharacterOverrideEvent":
            try:
                new_challenge_handler.get_challenge_by_id()
                get_challenge_ids_from_inventory(userid)
            except Exception as e:
                logger.graylog_logger(level="error", handler="updateMetadataGroup", message=e)
            character_id = metadata["characterId"]
            prestige_level = metadata["prestigeLevel"]
            equipment = metadata["equipment"]
            equippedPerks = metadata["equippedPerks"]
            equippedPowers = metadata["equippedPowers"]
            equippedWeapons = metadata["equippedWeapons"]
            equippedBonuses = metadata["equippedBonuses"]
            equippedConsumables = metadata["equippedConsumables"]
            pickedChallenges = metadata["pickedChallenges"]
            object_data = mongo.get_data_with_list(login=userid, login_steam=False, items={object_id})

            database_dict = {object_id: {"prestige": prestige_level,
                                         "experience": object_data[object_id]["experience"],
                                         "Equipment": equipment,
                                         "EquippedPerks": equippedPerks,
                                         "EquippedPowers": equippedPowers,
                                         "EquippedWeapons": equippedWeapons,
                                         "EquippedBonuses": equippedBonuses,
                                         "pickedChallenges": pickedChallenges,
                                         "equippedConsumables": equippedConsumables,
                                         "characterId": character_id}}

            mongo.write_data_with_list(login=userid, login_steam=False, items_dict=database_dict)

        else:
            logger.graylog_logger(level="error", handler="updateMetadataGroup", message=f"New reason: {reason}")

        return jsonify({"userId": userid,
                        "stateName": "MetadataGroups",
                        "objectId": "PlayerMetadata",
                        "version": 343,
                        "schemaVersion": 1,
                        "data": data["data"]})

    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_updateMetadataGroup",
                              message=f"Json: {request.get_json()}")
        logger.graylog_logger(level="error", handler="logging_updateMetadataGroup", message=e)


# Should be correct see PDB 0.8.0
@app.route("/api/v1/extensions/inventory/unlockSpecialItems", methods=["POST"])
def inventory_unlock_special_items():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)
    data = request.get_json()["data"]["additionalSteamAppIds"]

    unlocked_items = []

    origin_sets_artbook_items = ["34918BAF4507ECE322853D8D6DFE81D4", "4302DF13418EC9BE3C8E119F390AACE2",
                                 "3EF7ED3449B8EA4E19BEDFBD100B1DFA", "40E89D554CD74E398E5BAF86369E7C81",
                                 "C645C7AC405B3D8AF8E73B946875F0AE", "6A7E87AC403EF62B151C27A051B2E373",
                                 "29447D464334997ECF872F8B08FDC442", "F4B0185D41460D68A0CF7D9A00ACB6E7"]
    dbd_items = ["4EDACCF844B8025FD89C7BAB6B0005A2", "9F54DE7A4E15935B503850A127B0A2A4"]
    terminator_set_items = ["EADE3240481E7372624FF2B186ADE4D8", "ED13D15E4439C1C19281D2AFDD4C5B96",
                            "5AC2450640153C86DF57FA84500DA45C", "361D68284314B8A0A9432D913C93C9C0",
                            "B42F8BA04A4294BAF95A4090E62F66BC", "1B00252A45A9206224ECE5816C99A2A3"]
    alienware_outfit_items = ["ADC2570E4BD4D9AD5FAB21B974B807EC", "D4D6E33D42EE0DDDA24DA983C70209EC",
                              "EAF477EC4CE75EACAE8E4ABE22AD8E4D", "996F45A64E6E2E7B2B72B9BABA86F86D"]
    hearts_and_minds_items = ["70A09B4348F9DA5B1EEF0786DB1911AC", "221B6B19499A30944F8F4A969EB2B83D"]

    user_inventory = mongo.get_data_with_list(login=userid, login_steam=False, items={"inventory"})

    writen_sets = mongo.get_data_with_list(login=userid, login_steam=False, items={"unlocked_special_item_ids"})["unlocked_special_item_ids"]
    if 872770 in data and 872770 not in writen_sets:
        unlocked_items.extend(origin_sets_artbook_items)
        writen_sets.append(872770)
    if 381210 in data and 381210 not in writen_sets:
        unlocked_items.extend(dbd_items)
        writen_sets.append(381210)
    if 1024660 in data and 1024660 not in writen_sets:
        unlocked_items.extend(terminator_set_items)
        writen_sets.append(1024660)
    if 1083130 in data and 1083130 not in writen_sets:
        unlocked_items.extend(alienware_outfit_items)
        writen_sets.append(1083130)
    if 920440 in data and 920440 not in writen_sets:
        unlocked_items.extend(hearts_and_minds_items)
        writen_sets.append(920440)
    for appid in data:
        if appid not in [872770, 381210, 1024660, 1083130, 920440]:
            logger.graylog_logger(level="error", handler="unknown_unlockSpecialItems",
                                  message=f"Unknown appid {appid} for user {userid}")

    for item in unlocked_items:
        if item not in user_inventory["inventory"]:
            user_inventory["inventory"].append(item)

    mongo.write_data_with_list(login=userid, login_steam=False, items_dict=user_inventory)
    if len(writen_sets) != 0:
        mongo.write_data_with_list(login=userid, login_steam=False, items_dict={"unlocked_special_item_ids": writen_sets})

    try:
        return jsonify({"unlockedItems": unlocked_items})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="unknown_unlockSpecialItems", message=e)


@app.route("/api/v1/extensions/progression/resetCharacterProgressionForPrestige", methods=["POST"])
def reset_prestige():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)
    try:
        data = request.get_json()
        character_id = data["data"]["characterId"]
        logger.graylog_logger(level="info", handler="resetCharacterProgressionForPrestige", message=data)
        return jsonify({
            "IsCharacterItemsReset": False,
            "IsCharacterChallengesReset": False,
            "IsCharacterExperienceReset": False,
            "PrestigeLevel": 1,
            "Rewards": [
                {
                    "ItemRewards": [],
                    "CurrencyRewards": [
                        {
                            "Currency": "CurrencyA",
                            "Amount": 100
                        }
                    ],
                    "Costs": [
                        {
                            "Currency": "CurrencyA",
                            "Amount": 100
                        }
                    ]
                }
            ]
        })
        # ItemRewards: UCatalogItemAsset ARRAY
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="resetCharacterProgressionForPrestige", message=e)


@app.route("/api/v1/extensions/challenges/getChallengeProgressionBatch", methods=["POST"])
def challenges_get_challenge_progression_batch():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    user_id = session_manager.get_user_id(session_cookie)

    # Disabled because challenges still dont work and the new backend has it fixed already.
    return jsonify({"status": "error"})

    try:
        data = request.get_json()
        challenge_ids = data["data"]["challengeIds"]
        challenge_list = []
        userid = data["data"]["userId"]

        #moved this call to outside get_progression_batch to reduce the amount of database calls
        #change array to dict for quicker element access
        db_challenge = mongo.get_data_with_list(login=userid, login_steam=False, items={"challengeProgression"})[
            "challengeProgression"]
        db_challenge_dict = {}
        for challenge in db_challenge:
            #We do not want timestamp in our key otherwise duplicate weekly/daily challenges are created
            db_challenge_dict[challenge["challengeId"].split(":")[0]] = challenge

        for challenge in challenge_ids:
            challenge_data = None
            if ":" in challenge:
                challenge = challenge.split(":")[0]
            challenge_data = new_challenge_handler.get_progression_batch(challenge, userid, db_challenge_dict)


            if challenge_data:
                challenge_list.append(challenge_data)
            else:
                logger.graylog_logger(level="error", handler="logging_missing_challenge",
                                      message=f"Unknown challenge id {challenge}")

        response = {"progressionBatch": challenge_list}
        return jsonify(response)
        # return jsonify({"ProgressionBatch": challenge_list})
    except TimeoutError:
        return jsonify({"status": "error"})

    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_getChallengeProgressionBatch", message=e)
