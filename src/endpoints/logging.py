import uuid

from flask_definitions import *


@app.route("/metrics/client/event", methods=["POST"])
def receive_event():
    check_for_game_client()
    try:
        data = request.get_json()
        logger.graylog_logger(level="info", handler="logging_client_Event", message=data)
        return jsonify({"status": "success"})
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
        return jsonify({"status": "success"})
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
        return jsonify({"status": "success"})
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
        return jsonify({"status":"success","stackKeyId":-1,"crashId":2011,"messageId":-1})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_crashreporter_CheckReport", message=e)
