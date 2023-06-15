from flask_definitions import *
import requests
from logic.mongodb_handler import mongo
from logic.time_handler import get_time

global steam_api_key, mongo_db, mongo_collection, mongo_host


def steam_login_function():
    try:
        steam_session_token = request.args.get('token')
        appid = 555440
        response = requests.get(
            'https://api.steampowered.com/ISteamUserAuth/AuthenticateUserTicket/v1/?key={}&ticket={}&appid={}'.format(
                steam_api_key, steam_session_token, appid))
        if response.json() == {"response":{"error":{"errorcode":102,"errordesc":"Ticket for other app"}}}:
            appid = 854040
            response = requests.get(
                'https://api.steampowered.com/ISteamUserAuth/AuthenticateUserTicket/v1/?key={}&ticket={}&appid={}'.format(
                    steam_api_key, steam_session_token, appid))

        steamid = response.json()["response"]["params"]["steamid"]
        # owner_id = response.json()["response"]["params"]["result"]["ownersteamid"]  # This is providerId

        userid, token = mongo.user_db_handler(steamid, mongo_host, mongo_db, mongo_collection)
        current_time, expire_time = get_time()

        logger.graylog_logger(level="info", handler="steam_login", message="User {} logged in".format(steamid))
        # Read: Doc -> AUTH
        # You can copy and paste the JSON from the Auth Doc here. If you don't have a steam api key.
        # The Client does not validate this and just uses it.
        return jsonify({"preferredLanguage": "en", "friendsFirstSync": {"steam": True}, "fixedMyFriendsUserPlatformId":
            {"steam": True}, "id": userid, "provider": {"providerId": steamid, "providerName": "steam", "userId":
            userid}, "providers": [{"providerName": "steam", "providerId": steamid}], "friends": [], "triggerResults":
                            {"success": [], "error": []}, "tokenId": userid, "generated": current_time,
                        "expire": expire_time,
                        "userId": userid, "token": token})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="steam_login", message=str(e))


@app.route("/api/v1/auth/provider/steam/login", methods=["POST"])
def steam_login():
    # Read Doc\SteamAuth.md for more information
    ip = get_remote_ip()
    user_agent = request.headers.get('User-Agent')
    print("####################################################")
    print("USER AGENT: " + user_agent)
    print("####################################################")

    if user_agent.startswith("TheExit/++UE4+Release-4.2"):
        try:
            return_val = steam_login_function()
            return_val.set_cookie("bhvrSession", return_val.json["id"])
            return return_val
        except Exception as e:
            logger.graylog_logger(level="error", handler="steam_login", message=str(e))
            abort(401, "Unauthorized")

    elif user_agent.startswith("game=TheExit, engine=UE4, version="):
        return_val = steam_login_function()
        return_val.set_cookie("bhvrSession", return_val.json["id"])
        return return_val

    else:
        logger.graylog_logger(level="error", handler="steam_login", message={"text": "Access denied to User Agent",
                                                                               "User-Agent": user_agent, "IP": ip})
        abort(401, "Unauthorized")


@app.route("/api/v1/modifierCenter/modifiers/me", methods=["GET"])
def modifiers():
    get_remote_ip()
    try:
        return jsonify({"status": "success", "modifiers": []})  # Don't know. Added as Placeholder.
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="modifiers_me", message=str(e))


@app.route("/moderation/check/username", methods=["POST"])
def moderation_check_username():
    get_remote_ip()
    try:
        request_var = request.get_json()
        print(str(request_var))
        userid = request_var["userId"]
        username = request_var["username"]
        logger.graylog_logger(level="info", handler="moderation_check_username", message=request.get_json())
        steamid, token = mongo.get_user_info(userId=userid, server=mongo_host, db=mongo_db, collection=mongo_collection)
        return jsonify({"Id": userid, "Token": token,
                        "Provider": {"ProviderName": username, "ProviderId": steamid}})  # CLIENT:{"userId": "ID-ID-ID-ID-SEE-AUTH",	"username": "Name-Name-Name"}
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="moderation_check_username", message=str(e))


@app.route("/api/v1/progression/experience", methods=["POST"])
def progression_experience():
    get_remote_ip()
    try:
        # graylog_logger(request.get_json(), "info")
        return jsonify({'groupExperiences': [{'objectId': 'PlayerProgression', 'experience': 0.57, 'version': 1},
                                             {'objectId': 'RunnerProgression', 'experience': 0.555, 'version': 1},
                                             {'objectId': 'HunterProgression', 'experience': 0.67, 'version': 1}]})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="progression_experience", message=str(e))


@app.route("/api/v1/extensions/challenges/getChallenges", methods=["POST"])
def challenges_get_challenges():
    get_remote_ip()
    try:
        print("Responded to challenges get challenges api call POST")
        logger.graylog_logger(level="info", handler="challenges_get_challenges", message=request.get_json())
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="getChallanges", message=str(e))


@app.route("/api/v1/inventories", methods=["GET"])
def inventories():
    get_remote_ip()
    try:
        print("Responded to inventories api call GET")
        print(request.cookies.get('bhvrSession'))
        userid = request.cookies.get('bhvrSession')
        return jsonify({"code": 200, "message": "OK", "data": {"playerId": userid, "inventory": []}})
        return jsonify({"code":200,"message":"OK","data":{"playerId":userid,"inventory":[{"objectId":"Runner.Ink","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Runner.Ghost","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Runner.Smoke","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Runner.Sawbones","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Runner.Switch","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Runner.Dash","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Hunter.Stalker","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Hunter.Poacher","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Hunter.Inquisitor","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Hunter.Mass","quantity":1,"lastUpdateAt":1665866946},{"objectId":"HairColor.White","quantity":1,"lastUpdateAt":1665866946},{"objectId":"HairColor.Red","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Class.Hunter","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Class.HunterTypeA","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Class.HunterTypeB","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Class.HunterTypeC","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Class.HunterTypeD","quantity":1,"lastUpdateAt":1665866946},{"objectId":"HairColor.Auburn","quantity":1,"lastUpdateAt":1665866946},{"objectId":"HairColor.Black","quantity":1,"lastUpdateAt":1665866946},{"objectId":"HairColor.Brown","quantity":1,"lastUpdateAt":1665866946},{"objectId":"HairColor.Blond","quantity":1,"lastUpdateAt":1665866946},{"objectId":"HairColor.Gray","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Class.Runner","quantity":1,"lastUpdateAt":1665866946},{"objectId":"ClassVariation.HT.ShortRange","quantity":1,"lastUpdateAt":1665866946},{"objectId":"ClassVariation.HT.MediumRange","quantity":1,"lastUpdateAt":1665866946},{"objectId":"ClassVariation.HT.LongRange","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Gender","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Gender.Male","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Gender.Female","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Weapon","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Weapon.ICR","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Weapon.BareFist","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Weapon.Bow","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Weapon.EmptyHands","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Mod.NPI","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Mod.Bow","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Consumable","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Consumable.AmmoPack","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Consumable.MedPack","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Consumable.RepairKit","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Color.Blue","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Color.Green","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Color.Yellow","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Color.Orange","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Color.Red","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Color.Purple","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Color.Pink","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Color.White","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Accessory","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Accessory.Armour","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Accessory.Bonus","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Accessory.Wargear1","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Accessory.Wargear2","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Accessory.Perk","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Accessory.Trinket","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Accessory.CaptureKey","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Accessory.Standard","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Accessory.JumpPack","quantity":1,"lastUpdateAt":1665866946},{"objectId":"RewardBox","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Ability","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Ability.Fade","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Ability.SpawnTurret","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Ability.Supercharge","quantity":1,"lastUpdateAt":1665866946},{"objectId":"DifficultyLevel.Normal","quantity":1,"lastUpdateAt":1665866946},{"objectId":"DifficultyLevel.Hard","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Warlord","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Role.AutonomousProxy","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Role.SimulatedProxy","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Markable","quantity":1,"lastUpdateAt":1665866946},{"objectId":"LifeTimeOwner","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Revealable","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Weapon.AssaultRifle","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Mod.Assaultrifle.Top","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Mod.Assaultrifle.Front","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Mod.Assaultrifle.Rear","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Mod.Assaultrifle.Muzzle","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Mod.Assaultrifle.Sight","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Mod.Assaultrifle.Handle","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Mod.Assaultrifle.Ammo","quantity":1,"lastUpdateAt":1665866946},{"objectId":"SkinTone","quantity":1,"lastUpdateAt":1665866946},{"objectId":"SkinTone.Expresso","quantity":1,"lastUpdateAt":1665866946},{"objectId":"SkinTone.Cocoa","quantity":1,"lastUpdateAt":1665866946},{"objectId":"SkinTone.Mocha","quantity":1,"lastUpdateAt":1665866946},{"objectId":"SkinTone.Toffee","quantity":1,"lastUpdateAt":1665866946},{"objectId":"SkinTone.Dolce","quantity":1,"lastUpdateAt":1665866946},{"objectId":"SkinTone.Chai","quantity":1,"lastUpdateAt":1665866946},{"objectId":"SkinTone.Honey","quantity":1,"lastUpdateAt":1665866946},{"objectId":"SkinTone.Caramel","quantity":1,"lastUpdateAt":1665866946},{"objectId":"SkinTone.Latte","quantity":1,"lastUpdateAt":1665866946},{"objectId":"SkinTone.Peaches","quantity":1,"lastUpdateAt":1665866946},{"objectId":"SkinTone.Creme","quantity":1,"lastUpdateAt":1665866946},{"objectId":"SkinTone.Milk","quantity":1,"lastUpdateAt":1665866946},{"objectId":"WeaponType.ShortRange","quantity":1,"lastUpdateAt":1665866946},{"objectId":"WeaponType.MediumRange","quantity":1,"lastUpdateAt":1665866946},{"objectId":"WeaponType.LongRange","quantity":1,"lastUpdateAt":1665866946},{"objectId":"HairColor","quantity":1,"lastUpdateAt":1665866946},{"objectId":"UnverifiedAsset","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Ability.Stun","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Censored","quantity":1,"lastUpdateAt":1665866946},{"objectId":"Accessory.Consumable","quantity":1,"lastUpdateAt":1665866946}]}})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="inventories", message=str(e))


@app.route("/api/v1/players/me/splinteredstates/ProgressionGroups", methods=["GET"])
def progression_groups():
    get_remote_ip()
    try:
        print("Responded to progression groups api call GET")
        return jsonify({"status": "success", "progressionGroups": [1]})  # Don't know. Added as Placeholder.
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="ProgressionGroups", message=str(e))


@app.route("/api/v1/players/ban/status", methods=["GET"])
def ban_status():
    get_remote_ip()
    try:
        print("Responded to ban status api call GET")
        return jsonify({"BanPeriod": 33464688741, "BanReason": "TEST", "BanStart": 1592247140, "BanEnd": 33464688740,
                        "Confirmed": True, "Pending": False})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="ban_status", message=str(e))


@app.route("/api/v1/wallet/currencies", methods=["GET"])
def wallet_currencies():
    get_remote_ip()
    try:
        print("Responded to wallet currencies api call GET")
        return jsonify({"currencies": "EUR"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="currencies", message=str(e))


@app.route("/api/v1/players/me/splinteredstates/TheExit_Achievements", methods=["GET"])
def achievements_get():
    get_remote_ip()
    try:
        return jsonify({"gameName":"Deathgarden: BLOODHARVEST","achievements":
            [{"apiname":"EFAB89E6465D1163D62A07B11048F2B6","achieved":1,"unlocktime":1587140058},
             {"apiname":"2CAEBB354D506D7C43B941BC1DA775A0","achieved":1,"unlocktime":1586792410},
             {"apiname":"E51981B946BEE3D45C5C41B2FCFF310B","achieved":1,"unlocktime":1586788872},
             {"apiname":"AAD05B9D46471DC811BBE0BA91916AB7","achieved":1,"unlocktime":1586788872},
             {"apiname":"BA2D4A5445CB70276A8F5D9E1AFCE080","achieved":1,"unlocktime":1586788872}],"success":True})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="Achievment_handler", message=str(e))


@app.route("/api/v1/messages/count", methods=["GET"])
def messages_count():
    get_remote_ip()
    try:
        return jsonify({"count": 0})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="messages_count", message=str(e))
