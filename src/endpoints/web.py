from flask_definitions import *
from logic.mongodb_handler import mongo


@app.route('/', methods=["GET"])
def index():
    check_for_game_client()
    return render_template("index.html")


@app.route('/robots.txt', methods=["GET"])
def robots():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route('/.well-known/security.txt', methods=["GET"])
def security():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route('/.well-known/gpc.json', methods=["GET"])
def gpc():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route('/.well-known/dnt-policy.txt', methods=["GET"])
def dnt():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route('/debug/user/', methods=['GET'], defaults={'steamid': None})
@app.route('/debug/user/<steamid>', methods=['GET'])
def debug_user(steamid):
    if steamid is None:
        return render_template('debug/user.html', is_id_set=False, id_not_found=True)

    user_data = mongo.get_debug(steamid=steamid, server=mongo_host, db=mongo_db, collection=mongo_collection)

    if user_data is None:
        return render_template('debug/user.html', is_id_set=True, id_not_found=False, steam_id=steamid)

    return render_template(
        'debug/user.html',
        is_id_set=True,
        is_not_found=False,
        steam_id=user_data.get('steamid'),
        eula=user_data.get('eula'),
        currency_blood_cells=user_data.get('currency_blood_cells'),
        currency_ink_cells=user_data.get('currency_ink_cells'),
        currency_iron=user_data.get('currency_iron'),
        unlocked_items=user_data.get('unlocked_items'),
        userId=user_data.get('userId'),
        account_xp=user_data.get('account_xp'),
        runner_xp=user_data.get('runner_xp'),
        hunter_xp=user_data.get('hunter_xp'),
        is_banned=user_data.get('is_banned'),
        ban_reason=user_data.get('ban_reason'),
        ban_start=user_data.get('ban_start'),
        ban_expire=user_data.get('ban_expire'),
        special_unlocks=user_data.get('special_unlocks'),
        finished_challanges=user_data.get('finished_challanges'),
        open_challanges=user_data.get('open_challanges')
    )


@app.route("/debug/mirrors", methods=["POST", "GET"])
def debug_mirrors_write():
    check_for_game_client("soft")
    try:
        if request.method == "POST":
            try:
                api_token = request.cookies.get("api_token")
                if api_token is None:
                    return jsonify({"status": "error", "message": "No api token found"}, 401)
                else:
                    if api_token in allowed_tokens:

                        steam_user_id = request.json.get("steamid")
                        data_b = request.json.get("data")

                        if data_b or steam_user_id:
                            return_val = mongo.write_data_with_list(steamid=steam_user_id, items_dict=data_b, server=mongo_host, db=mongo_db,
                                                   collection=mongo_collection)
                            if return_val == None:
                                return jsonify({"status": "error", "message": "Error."}, 400)
                            else:
                                return jsonify({"status": "success", "message": "Data written."}, 200)
                        else:
                            return jsonify({"status": "error", "message": "No data or Steamid found."}, 400)
                    else:
                        return jsonify({"status": "error", "message": "Invalid api token"}, 401)

            except TimeoutError:
                return jsonify({"status": "error"})
            except Exception as e:
                logger.graylog_logger(level="error", handler="logging_debug_mirror_write", message=e)
        if request.method == "GET":
            return jsonify({"message": "Endpoint not found"}), 404
    except Exception as e:
        logger.graylog_logger(level="error", handler="web_debug_mirrors", message=e)
