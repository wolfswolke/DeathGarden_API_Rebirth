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
    try:
        data = request.get_json()
        logger.graylog_logger(level="info", handler="logging_gameDataAnalytics", message=data)
        return jsonify({"status": "success"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_gameDataAnalytics", message=e)


@app.route("/api/v1/gameDataAnalytics/batch", methods=["POST"])
def analytics_batch_post():
    check_for_game_client()
    try:
        data = request.get_json()
        logger.graylog_logger(level="info", handler="logging_gameDataAnalyticsBatch", message=data)
        return jsonify({"status": "success"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_gameDataAnalyticsBatch", message=e)


@app.route("/api/v1/me/richPresence", methods=["POST"])
def me_rich_presence():
    check_for_game_client()
    try:
        logger.graylog_logger(level="info", handler="logging_meRichPresence", message=request.get_json())
        return jsonify({"status": "success"})
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
        return jsonify({"status": "success"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_crashreporter_CheckReport", message=e)
