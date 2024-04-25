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
        get_challenge_ids_from_inventory(userid)
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
            pickedChallenges = group_data["pickedChallenges"]
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
                    "pickedChallenges": pickedChallenges,
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
        {'quantity': 1, 'objectId': '69055D534DF27180C4B36CAB4B651054', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '5A2DD3F6433AB83A725513B868D240CF', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '5D230967452FEEE13F1CA780F580E889', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'F42C5B4148F22D29DA976BA8667964F4', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '51E112D1407DC2F33CD6C98B31E1F1BD', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'C9C6D40A4D6A6A5748D5C0A17763C9C1', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '5DA9F0DE40A95322DC5453A4F85B7B2B', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '38E5F7F241E2BA1177419BB312FC1ACE', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '1A09DB19434DA733AAD3D9B5B1929CD4', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '320652184E1A719DEF1D3C9395EE7344', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '9FCAAC9143A827E79DC179B762B1E520', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '274EB0B34AB39E468BFA878F7E87465B', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '04FC953E40A601200FA1C181A0D3C913', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'D495BCB543F2D005B559C888E4BF2B3B', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'F05493F04CF30636487243B5776882D6', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'CAA84E294F02ECF88B08FB96E481194D', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '1258297B4BCBFB39628E22A58C77EA87', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'A858CAF640A824508A028D89AFC44366', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '78C4B6734B7C9DD1D2488EBA8EB5A7E4', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '6340FA564B0C4E692AD174BB743607F5', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '75A9B5A34CD7815B6D77248506897122', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '5681640F41DF9BEF0659C3A951BFC01B', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '25BF0927456349471A1C77A852342246', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '60542B19472C7AACEABFAA83D8112ACA', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '105AE7CE41DBBBE92EEBFBB32FDFEC20', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'FD1F569B450C253D3EC750A68A9A177A', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'E30FA007473CD2472AE5798B679DA419', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '5889E8B1404109B1D4623B9DD2057608', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '2F3693A4473188D2787CC899A70DC563', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '9B34059A4199ACBEE46BB4B0472E7CC3', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '4886DDC446B96FEE1255D6A2AB114B0D', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '7037D4804CB9931A4DDF23A35E321775', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'C215B81F4E42196103ECE98949892499', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '0C6D2A4648B95C2264312783F977F211', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '0FA5CBDA402FB9FCC8B56CAE69202061', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '08E1B04246C86826FA5FBE9B8030EB01', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'B7287C204907B7DDFC7D0EA0B8252E60', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '9281A7AB4EE28B4FB6341886DFD50391', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '9281A7AB4EE28B4FB6341886DFD50391', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '47FCA62C449C01963D2293A422A41CF3', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '3D3C4F024308BA7C67306783902EECAB', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '7899428947342326CE6B3B83021529E8', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'BFC78D3E4DEFDB5C6369A7B0EF5260C9', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '00CE22624386379A86512A9500B41ABC', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '97D7970A47CDE0451384D098E7E4A681', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '2046082F4049FFABD5A933A4559B3AE0', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'DE624DB646B9EEAA7CBDFF9A62D96293', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '48072EAA49C83C6F387236955B3C7B6E', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '1B51D59C47F565A20E743BA187B83642', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '2732AE1E44D10CF38EE2BE9A5927AA6F', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'B83A141A45FB8D96D48A5185CD607AA3', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'F7B0756043C628036D038BBED754E89A', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '759E44DD469C284175C2D6A1AB0B0FA7', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '56B7B6F6473712D0B7A2F992BB2C16CD', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '234FFD464C55514B6C1E738645993CAA', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'C300E3A84E571D549E014B9051A18BE8', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '755D4DFE40DA1512B01E3D8CFF3C8D4D', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '38A4EF8140822E498B2FD196B757F7AD', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'CCA2272D408ED95387F017BED437FF9A', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'C50FFFBF4686613182F45890651797CE', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'EF96A20249884D437B87A6A4BDE81B7F', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '606129DC45AB9D16B69E2FA5C99A9835', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '0398A38946C5FD3871B10A9E6B4B2BEC', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'B83713F044EED4FB220F2F9337AD14A2', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '4F563EB64882529F0CC42397CCCCB4A4', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '9373067D4895DE2C33EFBA8711F6E1D6', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'D91835664F2FAD7765BCF78B18CA9082', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'AA25DA8543EDF88C233713B438B43365', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'EB90A75F44EA4D821B385EA00B45E1BE', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '305F597C424FDD0A0A6B2BB6CF5CC542', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'D14477DA4ED69E001DC36ABCEA0B42BC', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '08DC38B6470A7A5B0BA025B96279DAA8', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '5159591743CBF0B57EC6FEB3341960D6', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '89A14A794CD70E50ADFEB497B89E4381', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '738CFAEB44A48BF6DA5F109C50068BE3', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '6BE28177483A89CF00B2FD839726ACE1', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '4431395744543533907B099952F81510', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '1069E6DF40AB4CAEF2AF03B4FD60BB22', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '5B6E31EA4E175EB002243D8942832223', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '334A7F0D417F3922E34BBDA4A66A5334', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'CC59BE294499B62827A639949AB3C2A3', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '3BB3C4774D87712BF8F6388F14E48FB2', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'B95774E641C37130DAE2F0A6C5E82C38', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '667EF1B74448A67A2E1B5EB74B2DBA66', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '7CE5AFBF459102E5728DCDAA6F88C0F1', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '2DBF9B114B82A63940936396CBA68BCD', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '10A8C667458016646E2EFA9452E3141A', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '08DC38B6470A7A5B0BA025B96279DAA8', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '5159591743CBF0B57EC6FEB3341960D6', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '364665404243311408F6A0BD4DCE05BD', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '307A0B13417737DED675309F8B978AB8', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '791F12E047DA9E26E246E3859C3F587E', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '8A5BF2274640C2F23EF3C996A6F6404D', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '1069E6DF40AB4CAEF2AF03B4FD60BB22', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '5CBD38644EA136989CB0E3BBF4A8E54B', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '321B9FA34B4497CA94F1CDB007735A57', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '525F6BE644576B3832ED77A10193F8A3', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'F01A992E429392A4F839FD93C25B34DB', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '9109796A49930831B017B3994A9F22EA', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'C814E8904A7C9D9A2F2594A3153E77A0', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '3C9D2E0A44ED015979667DBA4F080B49', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'AA00BB584A47234168A63D9F14C4C4E8', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '7A541DCB4F04DAB2E10FAB84395BB967', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '08DC38B6470A7A5B0BA025B96279DAA8', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '0703E3634B0E4409623E2D8C06B14C79', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '6562B26B48C9C791C82A3EAE344EBEE1', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '0606F8464D4C7EB70601CC84C50BCAC6', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '172080544A05F838E2473790FDF4873A', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '3D377249421D35F0F750578919A7E210', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '1069E6DF40AB4CAEF2AF03B4FD60BB22', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '0C06E9B5426B42D8C09C6B926938329D', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '44DD11E54FF689A553D297AB4FC1A7B2', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'E6448020488885E9F3D1FDBA8A70EBBF', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'AD900FC94C6608A4F88E8B8A87402F0F', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'BE1C0D4C4CE0861122BE22B2736D9091', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'F2768C4541C8262EFF4922B372AB7306', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'C8AF3D534973F82FADBB40BDA96F9DCD', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '4E171BD14FF98ED43A7AFAB57FE55578', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '109BC5904DC1272D70822EBA79CC85B1', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '54B3EF794FCB0643C4644FA15BEF31D5', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '487DEBE247818A01797AF5B3FD04C2B2', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'BA470A974C8EEC39D7248F91F3ABFACD', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '6A45DC544903218CEC18D4B7A27CEE51', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '1EBB7B3043BED679F382B087C0D6DE56', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '92CC1AC04868D1F9A99E6EA35BCDAD56', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '97501DEF493625107AEDCAAB2ADEDF4B', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '2BD43A50459BD9094DADC49A0F5F2551', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'C8AF3D534973F82FADBB40BDA96F9DCD', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '272369C042147225E364CFA42947859F', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'E13EA0CF46EE94F27F75BFAAD48D29D1', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'CEE62C37472E49AF36BC2A9809EEF2AD', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '487DEBE247818A01797AF5B3FD04C2B2', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '733A624F49F34D4659C084A4325D3202', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'B782F75E4A250FBD58BED0AAA2F9B4B0', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '2F282A504F9D04B0E3E8089CDAAC31FC', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '540DB1914938D04F524DC9850A325B21', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '48C47A4341B0E3E001F3D18537658D40', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '366DFB0841631FE3A1F4FE9BF814CF2C', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'C8AF3D534973F82FADBB40BDA96F9DCD', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '62AF95414827D3B29B9DFD97D54F1E95', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '261144CC43A9F74A60506AB0335B23B2', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '92B767F442A89C87CC3C9CB5D279D6EA', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '487DEBE247818A01797AF5B3FD04C2B2', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'F201BA114D675F8B62879199B3E5BEC9', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '81688A484ADDF511C219C89DF3B2CE4F', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '5DD486354855AEA9825B79AE6E306C82', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'C619BC1049C2C0FAC3907A914FD26469', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '350B26074604529237BF0CB22B60A9B8', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '04650B23493C386FA87E48947D26D79F', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'C8AF3D534973F82FADBB40BDA96F9DCD', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '23744B06493AE1220576529C4DB530B1', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'CE235B2C497B4381DA1742BA22999128', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'F91593E346415A85CFD0ED9CEBFBBDEA', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '487DEBE247818A01797AF5B3FD04C2B2', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '6B1B9949479BFD2B75E137AFFF3DBBD4', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '54526C4A4FF83835E02711B308AA80F5', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '5C4F9FC84B0CAE9CF00423A6768AEA23', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '24D5F6164191358D93B8E5BDFFE763F1', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '3B3BC3704395FAF545A97CBF8F601901', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '611F4DCB4A5C38EC4E423DB512CD9DC6', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'F055513D48AACBAC280B2AA00A984180', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '5998C1C548AB7BDA80C87295F2764C5D', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '7902D836470BBB49DE9B9D97F17C9DB5', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '08DC38B6470A7A5B0BA025B96279DAA8', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '5159591743CBF0B57EC6FEB3341960D6', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '50D3005B437066E4C4D99F9397CF1B0B', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '973C9176404A29F926D13BACB76A2425', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '1098BEE241B1515B44013A87EDB16BDC', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'EDB6D6B742023AE61AD8718CAC073C0E', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '1069E6DF40AB4CAEF2AF03B4FD60BB22', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '84DBF7B141246372690AFBA436B51C30', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '642E3BFA4F89698DD59E64AC133E266B', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '74C21FF949E644AF2231CDB796E9386E', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '0743E9B44190283D81A76480701EB07E', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '20FF1865462FD26B0253A08F18EFAA10', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'E4892E8A495FFB38F90729A1C97F3AC9', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'C8AF3D534973F82FADBB40BDA96F9DCD', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '492232504161420C872A0F82FC16ACDB', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '1E08AFFA485E92BAFF2C1BB85CEFB81E', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '1F5CD9004224C56746D81991AA40448A', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '487DEBE247818A01797AF5B3FD04C2B2', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'F6C3C02843F4DBA84109A0BF2D607DC2', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '97F3953347EE8BE10A29D39E3C4F0D1E', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'B3F3E6D84078F1DAE3C95AB5BFDEE945', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'BE23A8F14E783C51E662DCADD9AA76FF', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '6A8FA1C845AE1D7576BD87A53F7ED4A4', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'C7A898A44F208F9F85CE75969A98242D', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': 'C8AF3D534973F82FADBB40BDA96F9DCD', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '0E262D7A47567BE03A49ABA756FC1482', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '8EFCD5CC464EBFE1B7B03A984563710A', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '336D01F84D412B0D0D38F39311CA8D64', 'lastUpdateAt': 1574612664},
        {'quantity': 1, 'objectId': '487DEBE247818A01797AF5B3FD04C2B2', 'lastUpdateAt': 1574612664}
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
                challenge_data = new_challenge_handler.get_progression_batch(challenge,
                                                                                        userid, db_challenge_dict)
            else:
                challenge_data = new_challenge_handler.get_progression_batch(challenge,
                                                                                        userid, db_challenge_dict)

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
