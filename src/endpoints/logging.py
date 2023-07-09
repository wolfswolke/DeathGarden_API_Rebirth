from flask_definitions import *


@app.route("/metrics/client/event", methods=["POST"])
def receive_event():
    get_remote_ip()
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
    get_remote_ip()
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
    get_remote_ip()
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
    get_remote_ip()
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
    get_remote_ip()
    try:
        logger.graylog_logger(level="info", handler="logging_meRichPresence", message=request.get_json())
        return jsonify({"status": "success"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_meRichPresence", message=e)


@app.route("/metrics/server/event", methods=["POST"])
def metrics_server_event():
    get_remote_ip()
    try:
        logger.graylog_logger(level="info", handler="logging_server_Event", message=request.get_json())
        return jsonify({"status": "success"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_server_Event", message=e)


@app.route("/crashreport/unreal/CrashReporter/CheckReport", methods=["POST"])
def crashreporter_check_report():
    get_remote_ip()
    try:
        # TODO: Add Crashreporter
        return jsonify({"status": "success"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_crashreporter_CheckReport", message=e)


@app.route("/metrics/matchmaking/event", methods=["POST"])
def metrics_matchmaking_event():
    get_remote_ip()
    try:
        logger.graylog_logger(level="info", handler="logging_matchmaking_Event", message=request.get_json())
        return jsonify({"status": "success"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_matchmaking_Event", message=e)
