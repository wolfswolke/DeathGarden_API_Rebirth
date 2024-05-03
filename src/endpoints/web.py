from flask_definitions import *
from logic.queue_handler import matchmaking_queue


@app.route('/', methods=["GET"])
def index():
    check_for_game_client("soft")
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


@app.route('/favicon.ico')
def favicon():
    check_for_game_client("soft")
    try:
        return send_from_directory(os.path.join(app.root_path, 'image'), 'favicon.ico',
                                   mimetype='image/vnd.microsoft.icon')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-favicon", message=e)


@app.route('/apple-touch-icon.png')
def apple_touch_icon():
    check_for_game_client("soft")
    try:
        return send_from_directory(os.path.join(app.root_path, 'image'), 'apple-touch-icon.png',
                                   mimetype='image/vnd.microsoft.icon')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-apple_touch_icon", message=e)


@app.route('/android-chrome-192x192.png')
def android_chrome_192x192():
    check_for_game_client("soft")
    try:
        return send_from_directory(os.path.join(app.root_path, 'image'), 'android-chrome-192x192.png',
                                   mimetype='image/vnd.microsoft.icon')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-android-chrome-192x192", message=e)


@app.route('/android-chrome-256x256.png')
def android_chrome_256x256():
    check_for_game_client("soft")
    try:
        return send_from_directory(os.path.join(app.root_path, 'image'), 'android-chrome-256x256.png',
                                   mimetype='image/vnd.microsoft.icon')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-android-chrome-256x256", message=e)


@app.route('/browserconfig.xml')
def browserconfig():
    check_for_game_client("soft")
    try:
        return send_from_directory(os.path.join(app.root_path, 'image'), 'browserconfig.xml')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-browserconfig", message=e)


@app.route('/favicon-16x16.png')
def favicon_16x16():
    check_for_game_client("soft")
    try:
        return send_from_directory(os.path.join(app.root_path, 'image'), 'favicon-16x16.png',
                                   mimetype='image/vnd.microsoft.icon')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-favicon-16x16", message=e)


@app.route('/favicon-32x32.png')
def favicon_32x32():
    check_for_game_client("soft")
    try:
        return send_from_directory(os.path.join(app.root_path, 'image'), 'favicon-32x32.png',
                                   mimetype='image/vnd.microsoft.icon')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-favicon-32x32", message=e)


@app.route('/favicon.png')
def favicon_png():
    check_for_game_client("soft")
    try:
        return send_from_directory(os.path.join(app.root_path, 'image'), 'favicon.png',
                                   mimetype='image/vnd.microsoft.icon')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-favicon", message=e)


@app.route('/mstile-150x150.png')
def mstile_150x150():
    check_for_game_client("soft")
    try:
        return send_from_directory(os.path.join(app.root_path, 'image'), 'mstile-150x150.png',
                                   mimetype='image/vnd.microsoft.icon')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-mstile-150x150", message=e)


@app.route('/safari-pinned-tab.svg')
def safari_pinned_tab():
    check_for_game_client("soft")
    try:
        return send_from_directory(os.path.join(app.root_path, 'image'), 'safari-pinned-tab.svg',
                                   mimetype='image/svg+xml')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-safari-pinned-tab", message=e)


@app.route('/site.webmanifest')
def site_webmanifest():
    check_for_game_client("soft")
    try:
        return send_from_directory(os.path.join(app.root_path, 'image'), 'site.webmanifest')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-site.webmanifest", message=e)


@app.route('/apple-touch-icon-precomposed.png')
def apple_touch_icon_precomposed():
    check_for_game_client("soft")
    try:
        return send_from_directory(os.path.join(app.root_path, 'image'), 'favicon.png',
                                   mimetype='image/vnd.microsoft.icon')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-apple-touch-icon-precomposed", message=e)


@app.route('/apple-touch-icon-120x120.png')
def apple_touch_icon_120x120():
    check_for_game_client("soft")
    try:
        return send_from_directory(os.path.join(app.root_path, 'image'), 'favicon.png',
                                   mimetype='image/vnd.microsoft.icon')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-apple-touch-icon-120x120", message=e)


@app.route('/images/icons/fugue/tick-circle.png')
def tick_circle():
    try:
        return send_from_directory(os.path.join(app.root_path, 'image'), 'tick-circle.png',
                                   mimetype='image/vnd.microsoft.icon')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-tick-circle-png", message=e)


@app.route("/debug", methods=["Get"])
def debug_root():
    check_for_game_client("soft")
    endpoint_descriptions = {
        '/debug/user': 'Endpoint to debug user information'}

    endpoint_list = []
    for endpoint, description in endpoint_descriptions.items():
        endpoint_list.append(f'<li>{endpoint}: {description}</li>')

    endpoints_html = '<ul>' + ''.join(endpoint_list) + '</ul>'
    return f'<h1>Debug Endpoints:</h1>{endpoints_html}'


@app.route('/debug/user/', methods=['GET'], defaults={'steamid_unsanitized': None})
@app.route('/debug/user/<steamid_unsanitized>', methods=['GET'])
def debug_user(steamid_unsanitized):
    steamid = sanitize_input(steamid_unsanitized)
    if steamid is None:
        return render_template('debug/user.html', is_id_set=False, id_not_found=True)

    user_data = mongo.get_debug(steamid=steamid)

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
        userId=user_data.get('userId'),
        account_xp=user_data.get('account_xp'),
        prestige_xp=user_data.get('prestige_xp'),
        is_banned=user_data.get('is_banned'),
        ban_reason=user_data.get('ban_reason'),
        ban_start=user_data.get('ban_start'),
        ban_expire=user_data.get('ban_expire'),
        special_unlocks=user_data.get('special_unlocks'),
        finished_challanges=user_data.get('finished_challanges'),
        open_challanges=user_data.get('open_challanges'),
        unread_msg_ids=user_data.get('unread_msg_ids')
    )


@app.route("/debug/mirrors/write", methods=["POST", "GET"])
def debug_mirrors_write():
    check_for_game_client("soft")
    try:
        if request.method == "POST":
            try:
                api_token = sanitize_input(request.cookies.get("api_token"))
                if api_token is None:
                    return jsonify({"status": "error", "message": "No api token found"}, 401)
                if api_token not in allowed_tokens:
                    return jsonify({"status": "error", "message": "Invalid api token"}), 401
                steam_user_id = sanitize_input(request.json.get("steamid"))
                data_b = request.json.get("data")

                if not data_b:
                    return jsonify({"status": "error", "message": "No data found."}), 400

                if not steam_user_id:
                    return jsonify({"status": "error", "message": "No Steamid found."}), 400

                logger.graylog_logger(level="info", handler="logging_debug_mirror_write",
                                      message={"IP": check_for_game_client("remote"), "steamid": steam_user_id, "data": data_b})

                return_val = mongo.write_data_with_list(login=steam_user_id, login_steam=True, items_dict=data_b)

                if return_val is None:
                    return jsonify({"status": "error", "message": "There was a error on our End. "
                                                                  "Please try again later."}), 400

                return jsonify({"status": "success", "message": "Data written."}), 200

            except TimeoutError:
                return jsonify({"status": "error"})
            except Exception as e:
                logger.graylog_logger(level="error", handler="logging_debug_mirror_write", message=e)
        if request.method == "GET":
            return jsonify({"message": "Endpoint not found"}), 404
    except Exception as e:
        logger.graylog_logger(level="error", handler="web_debug_mirrors", message=e)


@app.route("/debug/mirrors/get", methods=["POST"])
def debug_mirrors_get():
    check_for_game_client("soft")
    try:
        if request.method == "POST":
            try:
                api_token = sanitize_input(request.cookies.get("api_token"))
                if api_token is None:
                    return jsonify({"status": "error", "message": "No api token found"}, 401)
                if api_token not in allowed_tokens:
                    return jsonify({"status": "error", "message": "Invalid api token"}), 401
                steam_user_id = sanitize_input(request.json.get("steamid"))

                if not steam_user_id:
                    return jsonify({"status": "error", "message": "No Steamid found."}), 400

                # logger.graylog_logger(level="info", handler="logging_debug_mirror_read",
                #                      message={"IP": check_for_game_client("remote"), "steamid": steam_user_id})

                return_val = mongo.get_debug(steam_user_id)

                if return_val is None:
                    return jsonify({"status": "error", "message": "There was a error on our End. "
                                                                  "Please try again later."}), 400
                return_val.pop("_id")
                return jsonify({"Data": return_val}), 200

            except TimeoutError:
                return jsonify({"status": "error"})
            except Exception as e:
                logger.graylog_logger(level="error", handler="logging_debug_mirror_write", message=e)
        if request.method == "GET":
            return jsonify({"message": "Endpoint not found"}), 404
    except Exception as e:
        logger.graylog_logger(level="error", handler="web_debug_mirrors", message=e)


@app.route("/debug/mirrors/clear", methods=["POST"])
def debug_mirrors_clear():
    check_for_game_client("soft")
    try:
        if request.method == "POST":
            try:
                api_token = sanitize_input(request.cookies.get("api_token"))
                if api_token is None:
                    return jsonify({"status": "error", "message": "No api token found"}, 401)
                if api_token not in allowed_tokens:
                    return jsonify({"status": "error", "message": "Invalid api token"}), 401
                # logger.graylog_logger(level="info", handler="logging_debug_mirror_read",
                #                      message={"IP": check_for_game_client("remote"), "steamid": steam_user_id})

                return_val = matchmaking_queue.clear_queue()

                if return_val is None:
                    return jsonify({"status": "error", "message": "There was a error on our End. "
                                                                  "Please try again later."}), 400
                return jsonify({"status": "success", "message": "Queues Cleared."}), 200

            except TimeoutError:
                return jsonify({"status": "error"})
            except Exception as e:
                logger.graylog_logger(level="error", handler="logging_debug_mirror_write", message=e)
        if request.method == "GET":
            return jsonify({"message": "Endpoint not found"}), 404
    except Exception as e:
        logger.graylog_logger(level="error", handler="web_debug_mirrors", message=e)


@app.route('/updater/', methods=["GET"])
def updater_root():
    return render_template("updater.html")


@app.route("/updater/versions", methods=["GET"])
def updater_version():
    return jsonify({
        "script_version": 2,
        "pak_version": 1,
        "sig_version": 1
    })


@app.route("/updater/files/", methods=["GET"])
def updater_files():
    return jsonify({"Error": "Please read the Docs about this Endpoint."}), 400


@app.route("/updater/files/pak/", methods=["GET"])
def updater_pak():
    try:
        return send_from_directory(os.path.join(app.root_path, 'files'), 'TheExitRebirthBackendAPI-WindowsNoEditor_P.pak')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="web-updater-PAK", message=e)


@app.route("/updater/files/sig/", methods=["GET"])
def updater_sig():
    try:
        return send_from_directory(os.path.join(app.root_path, 'files'), 'TheExitRebirthBackendAPI-WindowsNoEditor_P.sig')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="web-updater-SIG", message=e)


@app.route("/updater/files/script/", methods=["GET"])
def updater_script():
    try:
        return send_from_directory(os.path.join(app.root_path, 'files'), 'TheExit-Rebirth-Updater.bat')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="web-updater-script", message=e)


@app.route("/debug/matchmaking", methods=["GET"])
@app.route("/debug/MatchMaking", methods=["GET"])
def debug_matchmaking():
    len_queue = matchmaking_queue.get_len_of_queue()
    len_killed_lobbies = matchmaking_queue.get_len_of_killed_lobbies()
    len_queued_runners = matchmaking_queue.get_len_of_queued_runners()
    len_queued_hunters = matchmaking_queue.get_len_of_queued_hunters()
    len_open_lobbies = matchmaking_queue.get_len_of_open_lobbies()

    lobby_data = matchmaking_queue.get_lobby_data()

    return render_template('debug/matchmaking.html',
                           len_queue=len_queue,
                           len_killed_lobbies=len_killed_lobbies,
                           len_queued_runners=len_queued_runners,
                           len_queued_hunters=len_queued_hunters,
                           len_open_lobbies=len_open_lobbies,
                           lobby_data=lobby_data)


@app.route("/api/debug/MatchMaking", methods=["GET"])
def api_debug_matchmaking():
    len_queue = matchmaking_queue.get_len_of_queue()
    len_killed_lobbies = matchmaking_queue.get_len_of_killed_lobbies()
    len_queued_runners = matchmaking_queue.get_len_of_queued_runners()
    len_queued_hunters = matchmaking_queue.get_len_of_queued_hunters()
    len_open_lobbies = matchmaking_queue.get_len_of_open_lobbies()

    lobby_data = matchmaking_queue.get_lobby_data()
    lobby_return_data = []
    for item in lobby_data:
        # Hunters needs to be changed from STRING to LIST some day
        lobby_info = {
            "id": item.id,
            "Hunters": 1,
            "Runners": len(item.nonHosts),
            "status": item.status
        }
        lobby_return_data.append(lobby_info)

    return jsonify({
        "len_queue": len_queue,
        "len_killed_lobbies": len_killed_lobbies,
        "len_queued_runners": len_queued_runners,
        "len_queued_hunters": len_queued_hunters,
        "len_open_lobbies": len_open_lobbies,
        "lobby_data": lobby_return_data
    })


@app.route("/api/sha", methods=["GET"])
def api_sha():
    try:
        hashes = hash_handler.get_hash()
        return jsonify({"pak": hashes[0], "sig": hashes[1]})
    except Exception as e:
        logger.graylog_logger(level="error", handler="web-api-sha", message=e)
        return jsonify({"status": "error"}), 500


@app.route("/api/v1/upload", methods=["POST", "GET"])
def upload():
    check_for_game_client("soft")
    try:
        return jsonify({"status": "error", "message": "ENDPOINT WIP"}), 404
        if request.method == "POST":
            try:
                api_token = sanitize_input(request.headers.get("api_token"))
                if api_token is None:
                    return jsonify({"status": "error", "message": "No api token found"}), 401
                if api_token not in allowed_tokens:
                    return jsonify({"status": "error", "message": "Invalid api token"}), 401
                file = request.files['file']
                user_id = sanitize_input("test")
                if not user_id:
                    return jsonify({"status": "error", "message": "No User ID found."}), 400
                if not file:
                    return jsonify({"status": "error", "message": "No file found."}), 400
                file_id = file_handler.create_file(file, user_id)
                return jsonify({"status": "success", "file_id": file_id}), 200
            except TimeoutError:
                return jsonify({"status": "error"})
            except Exception as e:
                logger.graylog_logger(level="error", handler="web-upload", message=e)
        if request.method == "GET":
            return render_template("debug/upload.html")
    except Exception as e:
        logger.graylog_logger(level="error", handler="web-upload", message=e)


@app.route("/api/v1/download/<file_id>", methods=["GET"])
def download(file_id):
    check_for_game_client("soft")
    try:
        #file = file_handler.get_file(file_id)
        file = None
        if file is None:
           return jsonify({"status": "error", "message": "File not found."}), 404
        return file
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="web-download", message=e)


@app.route("/api/v1/metadata/<file_id>", methods=["GET"])
def metadata(file_id):
    check_for_game_client("soft")
    try:
        #metadata = file_handler.get_metadata(file_id)
        metadata_data = None
        if metadata_data is None:
            return jsonify({"status": "error", "message": "File not found."}), 404
        return jsonify(metadata_data)
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="web-metadata", message=e)


@app.route("/api/v1/sha256/<file_id>", methods=["GET"])
def sha256(file_id):
    check_for_game_client("soft")
    try:
        #sha256 = file_handler.get_file_sha256(file_id)
        sha256_data = None
        if sha256_data is None:
            return jsonify({"status": "error", "message": "File not found."}), 404
        return jsonify({"sha256": sha256_data})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="web-sha256", message=e)