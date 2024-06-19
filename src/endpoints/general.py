from flask_definitions import *
import os

from logic.mongodb_handler import mongo
from logic.time_handler import get_date_and_time


@app.route("/gamenews/messages", methods=["GET"])
def gamenews():
    check_for_game_client("strict")
    session_cookie = request.cookies.get("bhvrSession")
    userid = session_manager.get_user_id(session_cookie)

    # /gamenews/messages?
    # sortDesc=true
    # gameVersion=0
    # platform=PC
    # language=EN
    # messageType=InGameNews
    # faction=Runner
    # playerLevel=1
    # The game saves watched game news here: C:\Users\User\AppData\Local\TheExit\Saved\Config\WindowsNoEditor\GameUserSettings.ini
    # In this Format: GameNewsViews=(("1", 4),("2", 1),("3", 1),("4", 1))
    # The first number is the ID of the news, the second number is the amount of times the news window was opened
    try:
        sort_desc = sanitize_input(request.args.get('sortDesc'))
        gameVersion = sanitize_input(request.args.get('gameVersion'))
        platform = sanitize_input(request.args.get('platform'))
        language = sanitize_input(request.args.get('language'))
        messageType = sanitize_input(request.args.get('messageType'))
        faction = sanitize_input(request.args.get('faction'))
        playerLevel = sanitize_input(request.args.get('playerLevel'))
        if dev_env == "true":
            output = json.load(open(os.path.join(app.root_path, "json", "placeholders", "dev_gamenews.json"), "r"))
            return jsonify(output)
        output = json.load(open(os.path.join(app.root_path, "json", "placeholders", "gamenews.json"), "r"))
        return jsonify(output)
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-Game-News", message=e)


@app.route("/api/v1/config/VER_LATEST_CLIENT_DATA", methods=["GET"])
def config_ver_latest_client_data():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    try:
        return jsonify({"LatestSupportedVersion": "te-18f25613-36778-ue4-374f864b"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-ver-latest-data", message=e)


@app.route("/api/v1/utils/contentVersion/latest/<version>", methods=["GET"])
def content_version_latest(version):
    # V 2.2 = Alpha 2, V 2.11 = LIVE
    version_san = sanitize_input(version)
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    if version_san == "0":
        return jsonify({"LatestSupportedVersion": "dev030"}), 200
        # This is DEV Placeholder in the Config
    elif version_san == "2.0":
        return jsonify({"LatestSupportedVersion": "dev020"}), 200
    elif version_san == "2.2":
        return jsonify({"LatestSupportedVersion": "te-23ebf96c-27498-ue4-7172a3f5"}), 200
    elif version_san == "2.5":
        return jsonify({"LatestSupportedVersion": "te-40131b9e-33193-ue4-fbccc218"}), 200
    elif version_san == "2.11":
        return jsonify({"LatestSupportedVersion": "2.11.2-1574441597"}), 200
    elif version_san == "2.12":
        return jsonify({"LatestSupportedVersion": "balance111"}), 200
    elif version_san == "3.0":
        return jsonify({"LatestSupportedVersion": "dev030"}), 200

    try:
        print("Responded to content version api call GET")
        print(f"Version called by client: {version_san}")
        return jsonify({"LatestSupportedVersion": "te-40131b9e-33193-ue4-fbccc218"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-content-version", message=e)


@app.route("/api/v1/config/UseMirrorsMM_Steam",
           methods=["GET"])  # What is this even??? Maybe Use Matchmaking? Its only in old Versions tho...
def config_use_mirrors_mm_steam():
    check_for_game_client("strict")
    session_cookie = request.cookies.get("bhvrSession")
    userid = session_manager.get_user_id(session_cookie)

    try:
        return jsonify("false")
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-use-mirrors-mm-steam", message=e)


@app.route("/crashreport/unreal/CrashReporter/Ping", methods=["GET"])
def crashreporter_ping():
    check_for_game_client("soft")
    try:
        # potentialy {"status":"success","stackKeyId":-1,"crashId":1525,"messageId":-1}
        return "healthy"
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-crashreporter-ping", message=e)


@app.route("/tex", methods=["GET"])
def tex_get():
    check_for_game_client("soft")
    try:
        return jsonify({"current-event": {}, "status": {}, "id": "live", "message": "Warning msg 1"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-tex", message=e)


@app.route("/api/v1/healthcheck", methods=["GET"])
def healthcheck():
    check_for_game_client("soft")
    try:
        # return jsonify({"status": "success", "online": "true"})
        return jsonify({"Health": "Alive"})
        # {"Health": "Alive"}
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-healthcheck", message=e)


@app.route("/api/v1/services/tex/")
def services_tex():
    current_time = get_date_and_time()
    try:
        user_agent = request.headers.get('User-Agent')
        if "TheExit/++UE4+Release-4.21-CL-0 Windows/" in user_agent:
            # EStashboard [0 Up, 1 Down, 2 Warning, 3 Failed]
            # up, down, available
            return jsonify({
                "description": "The Exit - Live",
                "url": "https://api.zkwolf.com/api/v1/services/tex",
                "list": None,
                "current-event": {
                    "status": {
                        "description": "The service is up",
                        "level": "NORMAL",
                        "default": True,
                        "image": "https://api.zkwolf.com/images/icons/fugue/tick-circle.png",
                        "url": "https://api.zkwolf.com/api/v1/statuses/up",
                        "id": "up",
                        "name": "Up"
                    },
                    "url": "https://api.zkwolf.com/api/v1/services/tex/events/ahdzfnB1Ymxpc2hpbmctc3Rhc2hib2FyZHISCxIFRXZlbnQYgICAgMC1mwoM",
                    "timestamp": current_time,
                    "sid": "ahdzfnB1Ymxpc2hpbmctc3Rhc2hib2FyZHISCxIFRXZlbnQYgICAgMC1mwoM",
                    "message": "up",
                    "informational": False
                },
                "id": "tex",
                "name": "tex"
            })
        else:
            return {"current-event": {"status": {"id": "live"}, "message": ""}}  # Alpha 2 WARNING Msg text?!?!

    except TimeoutError:
        return jsonify({
            "description": "The Exit - Live",
            "url": "https://api.zkwolf.com/api/v1/services/tex",
            "list": None,
            "current-event": {
                "status": {
                    "description": "The service is maybe working",
                    "level": "ERROR",
                    "default": True,
                    "image": "https://api.zkwolf.com/images/icons/fugue/tick-circle.png",
                    "url": "https://api.zkwolf.com/api/v1/statuses/up",
                    "id": "available",
                    "name": "available"
                },
                "url": "https://api.zkwolf.com/api/v1/services/tex/events/ahdzfnB1Ymxpc2hpbmctc3Rhc2hib2FyZHISCxIFRXZlbnQYgICAgMC1mwoM",
                "timestamp": current_time,
                "sid": "ahdzfnB1Ymxpc2hpbmctc3Rhc2hib2FyZHISCxIFRXZlbnQYgICAgMC1mwoM",
                "message": "available",
                "informational": False
            },
            "id": "tex",
            "name": "tex"
        })
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-services-tex", message=e)
        return jsonify({
            "description": "The Exit - Live",
            "url": "https://api.zkwolf.com/api/v1/services/tex",
            "list": None,
            "current-event": {
                "status": {
                    "description": "The service is not working",
                    "level": "ERROR",
                    "default": False,
                    "image": "https://api.zkwolf.com/images/icons/fugue/tick-circle.png",
                    "url": "https://api.zkwolf.com/api/v1/statuses/up",
                    "id": "down",
                    "name": "down"
                },
                "url": "https://api.zkwolf.com/api/v1/services/tex/events/ahdzfnB1Ymxpc2hpbmctc3Rhc2hib2FyZHISCxIFRXZlbnQYgICAgMC1mwoM",
                "timestamp": current_time,
                "sid": "ahdzfnB1Ymxpc2hpbmctc3Rhc2hib2FyZHISCxIFRXZlbnQYgICAgMC1mwoM",
                "message": "down",
                "informational": False
            },
            "id": "tex",
            "name": "tex"
        })


@app.route("/api/v1/statuses/up", methods=["GET"])
def statuses_up():
    return jsonify({"description": "The service is up", "level": "NORMAL", "default": True,
                    "image": "https://api.zkwolf.com/images/icons/fugue/tick-circle.png",
                    "url": "https://api.zkwolf.com/api/v1/statuses/up", "id": "up", "name": "Up"})


@app.route("/api/v1/services/tex/events/ahdzfnB1Ymxpc2hpbmctc3Rhc2hib2FyZHISCxIFRXZlbnQYgICAgMC1mwoM", methods=["GET"])
def services_tex_events():
    try:
        current_time = get_date_and_time()
        return jsonify({
            "status": {
                "description": "The service is up",
                "level": "NORMAL",
                "default": True,
                "image": "https://api.zkwolf.com/images/icons/fugue/tick-circle.png",
                "url": "https://api.zkwolf.com/api/v1/statuses/up",
                "id": "up",
                "name": "Up"
            },
            "url": "https://api.zkwolf.com/api/v1/services/tex/events/ahdzfnB1Ymxpc2hpbmctc3Rhc2hib2FyZHISCxIFRXZlbnQYgICAgMC1mwoM",
            "timestamp": current_time,
            "sid": "ahdzfnB1Ymxpc2hpbmctc3Rhc2hib2FyZHISCxIFRXZlbnQYgICAgMC1mwoM",
            "message": "up",
            "informational": False
        })
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-services-tex-events", message=e)


@app.route("/api/v1/consent/eula2", methods=["PUT", "GET"])
def consent_eula():
    # todo Fix this
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    try:
        if request.method == "PUT":
            try:
                mongo.eula(userId=userid, get_eula=False)
                return jsonify({"Userid": userid, "ConsentList": [{"ConsentId": "eula2", "isGiven": True,
                                                                   "UpdatedDate": 1689714606, "AttentionNeeded": False,
                                                                   "LatestVersion": "eula2"}]})
            except TimeoutError:
                return jsonify({"status": "error"})
            except Exception as e:
                logger.graylog_logger(level="error", handler="general-consent-eula",
                                      message=f"Error in consent_eula: {e}")
        elif request.method == "GET":
            if not session_cookie:
                return jsonify({"message": "Not Authenticated"}), 401
            userid = session_manager.get_user_id(session_cookie)
            if userid == 401:
                return jsonify({"message": "Not Authenticated"}), 401
            is_given = mongo.get_data_with_list(login=userid, login_steam=False,
                                                items={"eula"})
            if is_given is None:
                return jsonify({"isGiven": False})
            if is_given["eula"]:
                return jsonify({
                    "ConsentId": "eula2",
                    "isGiven": True,
                    "UpdatedDate": 1689714606,
                    "AttentionNeeded": False,
                    "LatestVersion": {
                        "Label": "eula2",
                        "EntryDate": 1689714606
                    },
                    "Userid": userid
                })

            else:
                return jsonify({"isGiven": False})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-consent-eula", message=e)


@app.route("/api/v1/consent/eula", methods=["GET"])
def consent_eula0():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    try:
        output = json.load(open(os.path.join(app.root_path, "json", "eula.json"), "r"))
        return jsonify(output)
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-consent-eula0", message=e)


@app.route("/api/v1/consent/privacyPolicy", methods=["GET"])
def privacy_policy():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    try:
        output = json.load(open(os.path.join(app.root_path, "json", "eula.json"), "r"))
        return jsonify(output)
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-privacy-policy", message=e)


@app.route("/api/v1/extensions/leaderboard/getScores", methods=["GET", "POST"])
def leaderboard_get_scores():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    if request.method == "POST":
        logger.graylog_logger(level="info", handler="general-leaderboard-get-scores",
                              message=f"Leaderboard getScores: {request.get_json()}")
        data = json.load(open(os.path.join(app.root_path, "json", "placeholders", "leaderboard.json"), "r"))
        #data = json.load(open(os.path.join(app.root_path, "json", "placeholders", "WIP_LeaderBoard.json"), "r"))
        return jsonify(data)
    else:
        try:
            return jsonify({"data": []})
        except TimeoutError:
            return jsonify({"status": "error"})
        except Exception as e:
            logger.graylog_logger(level="error", handler="general-leaderboard-get-scores", message=e)


@app.route("/submit", methods=["POST"])
def submit():
    check = check_for_game_client("soft")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    return "Discarded=1"


@app.route("/api/v1/extensions/quitters/getQuitterState", methods=["POST"])
def get_quitter_state():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    try:
        logger.graylog_logger(level="info", handler="logging_getQuitterState", message=request.get_json())
        return jsonify({
            "strikeRefreshTime": 0,
            "quitMatchStreakPrevious": 0,
            "strikeLeft": 1,
            "stayedMatchStreak": 100,
            "stayedMatchStreakPrevious": 100,
            "hasQuitOnce": False,
            "quitMatchStreak": 0,
            "stayMatchStreakRewards": [
                {
                    "id": "CurrencyA",
                    "type": "currency",
                    "amount": 20
                }
            ]
        })
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_getQuitterState", message=e)


@app.route("/api/v1/feedback", methods=["POST"])
def feedback():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    try:
        # {
        #    "type":"PlayerReport",
        #    "entityId":"00658d11-2dfd-41e8-b6d2-2462e8f3aa47",
        #    "platformId":"PC",
        #    "reason":"GriefingToxicBehavior",
        #    "details":"TEST MSG 01",
        #    "gameSpecificData":{
        #       "matchId":"0e019267-b57c-4ca4-a429-78e851515027",
        #       "playerInfoList":[
        #          {
        #             "playerId":"88d55eca-37b9-4ac1-8c93-5d7a395175b4",
        #             "characterState":"InArena",
        #             "faction":"Hunter",
        #             "totalXpEarned":0,
        #             "playtimeInSec":231.60643005371094,
        #             "isReportedPlayer":false,
        #             "isReporterPlayer":false
        #          },
        #          {
        #             "playerId":"619d6f42-db87-4f3e-8dc9-3c9995613614",
        #             "characterState":"InArena",
        #             "faction":"Runner",
        #             "totalXpEarned":0,
        #             "playtimeInSec":231.60643005371094,
        #             "isReportedPlayer":false,
        #             "isReporterPlayer":true
        #          },
        #          {
        #             "playerId":"6220aa12-7dc4-4850-80f7-dd1ce8054204",
        #             "characterState":"InArena",
        #             "faction":"Runner",
        #             "totalXpEarned":25,
        #             "playtimeInSec":231.60643005371094,
        #             "isReportedPlayer":false,
        #             "isReporterPlayer":false
        #          },
        #          {
        #             "playerId":"00658d11-2dfd-41e8-b6d2-2462e8f3aa47",
        #             "characterState":"InArena",
        #             "faction":"Runner",
        #             "totalXpEarned":45,
        #             "playtimeInSec":231.60643005371094,
        #             "isReportedPlayer":true,
        #             "isReporterPlayer":false
        #          },
        #          {
        #             "playerId":"cc4240ba-d7fd-4dd5-a3b7-ed42002e13cc",
        #             "characterState":"InArena",
        #             "faction":"Runner",
        #             "totalXpEarned":15,
        #             "playtimeInSec":231.60643005371094,
        #             "isReportedPlayer":false,
        #             "isReporterPlayer":false
        #          },
        #          {
        #             "playerId":"0385496c-f0ae-44d3-a777-26092750f39c",
        #             "characterState":"InArena",
        #             "faction":"Runner",
        #             "totalXpEarned":0,
        #             "playtimeInSec":231.60643005371094,
        #             "isReportedPlayer":false,
        #             "isReporterPlayer":false
        #          }
        #       ]
        #    }
        # }

        # logger.graylog_logger(level="info", handler="logging_feedback", message=request.get_json())
        data = request.get_json()
        report_type = data["type"]
        entity_id = data["entityId"]
        reporter_steam = mongo.get_data_with_list(login=entity_id, login_steam=False, items={"steamid"})["steamid"]
        platform_id = data["platformId"]
        reason = data["reason"]
        details = data["details"]
        game_specific_data = data["gameSpecificData"]
        match_id = game_specific_data["matchId"]
        playerInfoList = game_specific_data["playerInfoList"]
        player_list = []
        for player in playerInfoList:
            steam_id = mongo.get_data_with_list(login=player["playerId"], login_steam=False, items={"steamid"})
            if steam_id:
                player_list.append(steam_id["steamid"])
        resp = {
            "content": "",
            "embeds": [
                {
                    "title": f"User {reporter_steam} reported.",
                    "description": f"Reported for {reason} \nReport Type {report_type}\nDetails: {details} \nMatch ID: {match_id} \nReporter: {reporter_steam}\nPlayers in Lobby:\n"
                                   f"{player_list[0]}\n"
                                   f"{player_list[1]}\n"
                                   f"{player_list[2]}\n"
                                   f"{player_list[3]}\n"
                                   f"{player_list[4]}\n"
                                   f"{player_list[5]}\n",
                    "color": 7932020
                }
            ],
            "attachments": []
        }
        discord_webhook(moderation_urls, resp)
        return jsonify({"status": "success"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_feedback", message=e)


@app.route("/api/v1/extensions/purchase/set", methods=["POST"])
def purchase_set():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    data = request.get_json()
    itemid = data["data"]["itemId"]
    currencygroup = data["data"]["currencyGroup"]
    # {
    #       "id": "D89AA4884C54121C007FC3B613A8DDE8",
    #       "displayName": "RN_FOG_SMOKE_Fullset_STR001_Winter01_Item_Hard_Winter",
    #       "initialQuantity": 0,
    #       "consumable": false,
    #       "consumptionReward": [],
    #       "defaultCost": [],
    #       "eventCostList": [],
    #       "metaData": {
    #         "gameplayTags": [
    #           "Customization.RN.FullSet",
    #           "Runner.Smoke"
    #         ],
    #         "requiredChallengesToComplete": [],
    #         "minPlayerLevel": 0,
    #         "minCharacterLevel": 0,
    #         "freeForUserCreatedAfter": 0,
    #         "freeForUserCreatedBefore": 0,
    #         "isUnbreakableFullset": false,
    #         "origin": "None",
    #         "quality": "Basic",
    #         "groupType": "",
    #         "followingItem": "",
    #         "prerequisiteItem": "",
    #         "autoUnlockItemIds": [],
    #         "bundleItems": [
    #           "248D60AC47F987E895AD65B722D8912B",
    #           "4C0728944310CD3252C500B2B39BD34F",
    #           "70A248D340C77F1E552282AB8D73EADA",
    #           "ACE0A0304A74F795A6466192FCBC7CBC"
    #         ],
    #         "rewardBundleItems": [],
    #         "itemAssignments": [],
    #         "prestigeLevelRewards": [],
    #         "bundlePartOf": "",
    #         "bundleDiscountPercent": 0
    #       },
    #       "unique": false,
    #       "nonSecure": false,
    #       "purchasable": false
    #     },

    # {"data":{"itemId":"D89AA4884C54121C007FC3B613A8DDE8","currencyGroup":"SoftCurrencyGroup"}}
    try:
        data = mongo.get_data_with_list(login=userid, login_steam=False,
                                        items={"inventory", "currency_blood_cells", "currency_iron",
                                               "currency_ink_cells"})
        inventory = data["inventory"]
        CurrencyB = int(data["currency_blood_cells"])
        CurrencyA = int(data["currency_iron"])
        CurrencyC = int(data["currency_ink_cells"])

        catalog = json.load(
            open(os.path.join(app.root_path, "json", "catalog", "te-18f25613-36778-ue4-374f864b", "catalog.json"), "r"))
        wallet = [
            {"Id": "CurrencyA", "Balance": CurrencyA, "Debited": 0},
            {"Id": "CurrencyB", "Balance": CurrencyB, "Debited": 0},
            {"Id": "CurrencyC", "Balance": CurrencyC, "Debited": 0}
        ]
        bought_items = [itemid]
        for item in catalog["result"]:
            if item["id"] == itemid:
                for sub_item in item["metaData"]["bundleItems"]:
                    bought_items.append(sub_item)
                    for new_catalog_query in catalog["result"]:
                        if new_catalog_query["id"] == sub_item:
                            for currency in new_catalog_query["defaultCost"]:
                                if currency["currencyId"] == "CurrencyA":
                                    wallet[0]["Debited"] += currency["price"]
                                    CurrencyA -= currency["price"]
                                elif currency["currencyId"] == "CurrencyB":
                                    wallet[1]["Debited"] += currency["price"]
                                    CurrencyB -= currency["price"]
                                elif currency["currencyId"] == "CurrencyC":
                                    wallet[2]["Debited"] += currency["price"]
                                    CurrencyC -= currency["price"]
                            break

        if CurrencyA < 0 or CurrencyB < 0 or CurrencyC < 0:
            return jsonify({"status": "error"}), 500
        logger.graylog_logger(level="debug", handler="logging_purchase_item",
                              message=f"bought_items: {bought_items}, user_inventory: {inventory}")
        inventory.extend(bought_items)
        mongo.write_data_with_list(login=userid, login_steam=False,
                                   items_dict={"inventory": inventory, "currency_blood_cells": CurrencyB,
                                               "currency_iron": CurrencyA, "currency_ink_cells": CurrencyC})

        return jsonify({
            "Cost": {"CurrencyId": "CurrencyB", "Price": CurrencyB},
            "NewBalance": [
                {"Currency": "CurrencyA", "Balance": CurrencyA,
                 "CurrencyGroup": "SoftCurrencyGroup", "LastRefillTimeStamp": "1684862187"},
                {"Currency": "CurrencyB", "Balance": CurrencyB,
                 "CurrencyGroup": "SoftCurrencyGroup", "LastRefillTimeStamp": "1684862187"},
                {"Currency": "CurrencyC", "Balance": CurrencyC,
                 "CurrencyGroup": "SoftCurrencyGroup", "LastRefillTimeStamp": "1684862187"},
                {"Currency": "HARD_CURRENCY", "Balance": 6969,
                 "CurrencyGroup": "HardCurrencyGroup", "LastRefillTimeStamp": "1684862187"},
                {"Currency": "PROGRESSION_CURRENCY", "Balance": 10000,
                 "CurrencyGroup": "HardCurrencyGroup", "LastRefillTimeStamp": "1684862187"}
            ],
            "PurchasedItems": ["itemid"],
            "RewardItems": bought_items,
        })
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_purchase_item", message=e)


@app.route("/api/v1/extensions/purchase/item", methods=["POST"])
def purchase_item():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    data = request.get_json()
    itemid = data["data"]["objectId"]
    oldquantity = data["data"]["oldQuantity"]
    wantedquantity = data["data"]["wantedQuantity"]
    currencygroup = data["data"]["currencyGroup"]

    try:
        logger.graylog_logger(level="info", handler="logging_purchase_item", message=request.get_json())
        data = mongo.get_data_with_list(login=userid, login_steam=False,
                                        items={"inventory", "currency_blood_cells", "currency_iron",
                                               "currency_ink_cells"})
        inventory = data["inventory"]
        CurrencyB = int(data["currency_blood_cells"])
        CurrencyA = int(data["currency_iron"])
        CurrencyC = int(data["currency_ink_cells"])

        catalog = json.load(
            open(os.path.join(app.root_path, "json", "catalog", "te-18f25613-36778-ue4-374f864b", "catalog.json"), "r"))
        wallet = []
        for item in catalog["result"]:
            if item["id"] == itemid:
                for currency in item["defaultCost"]:
                    if currency["currencyId"] == "CurrencyA":
                        wallet.append({"Id": "CurrencyA", "Balance": CurrencyA, "Debited": currency["price"]})
                        CurrencyA -= currency["price"]
                    elif currency["currencyId"] == "CurrencyB":
                        wallet.append({"Id": "CurrencyB", "Balance": CurrencyB, "Debited": currency["price"]})
                        CurrencyB -= currency["price"]
                    elif currency["currencyId"] == "CurrencyC":
                        wallet.append({"Id": "CurrencyC", "Balance": CurrencyC, "Debited": currency["price"]})
                        CurrencyC -= currency["price"]
                break
        if CurrencyA < 0 or CurrencyB < 0 or CurrencyC < 0:
            return jsonify({"status": "error"}), 500
        inventory.append(itemid)
        mongo.write_data_with_list(login=userid, login_steam=False,
                                   items_dict={"inventory": inventory, "currency_blood_cells": CurrencyB,
                                               "currency_iron": CurrencyA, "currency_ink_cells": CurrencyC})

        return jsonify({
            "PlayerId": userid,
            "ObjectId": itemid,
            "Quantity": 1,
            "RewardItems": [
                itemid
            ],
            "Wallet": wallet
        })
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_purchase_item", message=e)
