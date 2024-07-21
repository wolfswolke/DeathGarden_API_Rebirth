import uuid

from flask_definitions import *


def json_log_validator(data):
    cleaned_str = data.decode('utf8')
    # base_str = cleaned_str.replace('\n', '')
    cleaned_str = cleaned_str.replace('://', '-')
    cleaned_str = cleaned_str.replace('"https', 'https')
    # cleaned_str = cleaned_str.replace('""', '"')
    cleaned_str = cleaned_str.replace('\\', '\\\\')
    cleaned_str = cleaned_str.replace(u"\u000D", "")  # Carriage Return
    cleaned_str = cleaned_str.replace(u"\u000A", "")  # Line Feed
    cleaned_str = cleaned_str.replace(u"\u0009", "")  # Horizontal Tab
    cleaned_str = cleaned_str.replace('{""', "{")
    cleaned_str = cleaned_str.replace('"":', ":")
    cleaned_str = cleaned_str.replace('"url"', "url")
    cleaned_str = cleaned_str.replace('"endpoints"', "endpoints")
    cleaned_str = cleaned_str.replace('"}],', "}]")
    cleaned_str = cleaned_str.replace('"group"', "group")
    cleaned_str = cleaned_str.replace('"cf-nel"', "cf-nel")
    cleaned_str = cleaned_str.replace('"max_age"', "max_age")
    cleaned_str = cleaned_str.replace('"report_to"', "report_to")
    cleaned_str = cleaned_str.replace('"success_fraction"', "success_fraction")
    cleaned_str = cleaned_str.replace('":443"', ":443")
    return cleaned_str


@app.route("/metrics/client/event", methods=["POST"])
def receive_event():
    check_for_game_client()
    try:
        data = request.get_json()
        logger.graylog_logger(level="info", handler="logging_client_Event", message=data)
        return "", 204
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_client_Event", message=e)


@app.route("/metrics/httplog/event", methods=["POST"])
def metrics_httplog_event():
    check_for_game_client()
    try:
        data = request.get_json()
        logger.graylog_logger(level="info", handler="logging_httplog_Event", message=data)
        return "", 204
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_httplog_Event", message=e)


@app.route("/api/v1/gameDataAnalytics", methods=["POST"])
def analytics_post():
    check_for_game_client()
    rand_record_id = uuid.uuid4()
    try:
        data = request.get_json()
        logger.graylog_logger(level="info", handler="logging_gameDataAnalytics", message=data)
        return jsonify({
            "RecordId": f"{rand_record_id}"
        })
    except TimeoutError:
        return jsonify({
            "FailedPutCode": 1,
            "RequestResponse": [
                {
                    "RecordId": f"{rand_record_id}",
                }
            ]
        })
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_gameDataAnalytics", message=e)
        return jsonify({
            "FailedPutCode": 1,
            "RequestResponse": [
                {
                    "RecordId": f"{rand_record_id}",
                }
            ]
        })


@app.route("/api/v1/gameDataAnalytics/batch", methods=["POST"])
def analytics_batch_post():
    check_for_game_client()
    try:
        data = request.get_json()
        item_count = len(data["body"])
        data = []
        for item in range(item_count):
            rand_record_id = uuid.uuid4()
            data.append({
                "RecordId": f"{rand_record_id}"
            })
        return jsonify(
            {
                "FailedPutCount": 0,
                "RequestResponses": data
            }
        )
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_gameDataAnalyticsBatch", message=e)


@app.route("/api/v1/me/richPresence", methods=["POST"])
def me_rich_presence():
    check_for_game_client()
    session_cookie = request.cookies.get("bhvrSession")
    session_manager.extend_session(session_cookie)
    user_id = session_manager.get_user_id(session_cookie)
    if "gameState" not in request.get_json():
        request.get_json()["gameState"] = "BOOT"

    try:
        rich_presence_handler.update_presence(user_id, request.get_json()["userType"], request.get_json()["gameState"])
        return "", 204
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_meRichPresence", message=e)


@app.route("/metrics/server/event", methods=["POST"])
def metrics_server_event():
    check_for_game_client()
    try:
        logger.graylog_logger(level="info", handler="logging_server_Event", message=request.get_json())
        return "", 204
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_server_Event", message=e)


@app.route("/crashreport/unreal/CrashReporter/CheckReport", methods=["POST"])
def crashreporter_check_report():
    check_for_game_client()
    try:
        # TODO: Add Crashreporter
        # Ngl i think it doesnt even care what it gets here...
        # It Pings, Sends something like "UE4CC-Windows-AB720C3F412E0FF7280F73BBB64245AB_0003"
        # and then uploads the crashreport to bugsplat
        return jsonify({"status": "success", "stackKeyId": -1, "crashId": 2011, "messageId": -1})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_crashreporter_CheckReport", message=e)


@app.route("/gameservers.dev", methods=["POST"])
def gameservers_dev():
    try:
        check_for_game_client("strict")
        req = request.get_data()
        cleaned_str = json_log_validator(req)
        try:
            data = json.loads(cleaned_str)
            logger.graylog_logger(level="info", handler="logging_gameservers_dev", message=data)
        except Exception as e:
            logger.graylog_logger(level="error", handler="logging_gameservers_dev", message=e)
            return jsonify({"status": "error"}), 500
        return "", 204
    except TimeoutError:
        return jsonify({"status": "error"}), 500
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_gameservers_dev", message=e)
        return jsonify({"status": "error"}), 500


@app.route("/gameservers.uat", methods=["POST"])
def gameservers_uat():
    try:
        check_for_game_client("strict")
        req = request.get_data()
        cleaned_str = json_log_validator(req)
        try:
            data = json.loads(cleaned_str)
            logger.graylog_logger(level="info", handler="logging_gameservers_uat", message=data)
        except Exception as e:
            logger.graylog_logger(level="error", handler="logging_gameservers_uat", message=e)
            return jsonify({"status": "error"}), 500
        return "", 204
    except TimeoutError:
        return jsonify({"status": "error"}), 500
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_gameservers_uat", message=e)
        return jsonify({"status": "error"}), 500


@app.route("/gameservers.live", methods=["POST"])
def gameservers_live():
    try:
        check_for_game_client("strict")
        req = request.get_data()
        cleaned_str = json_log_validator(req)
        try:
            data = json.loads(cleaned_str)
            logger.graylog_logger(level="info", handler="logging_gameservers_live", message=data)
        except Exception as e:
            logger.graylog_logger(level="error", handler="logging_gameservers_live", message=e)
            return jsonify({"status": "error"}), 500
        return "", 204
    except TimeoutError:
        return jsonify({"status": "error"}), 500
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_gameservers_live", message=e)
        return jsonify({"status": "error"}), 500
