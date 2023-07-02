from flask_definitions import *


# Do NOT change Result to ANYTHING or Add anything before it. Game will crash. Doesnt mean it 100% works tho XD
@app.route("/<game_version>/catalog", methods=["GET"])
def catalog_get(game_version):
    print("Game Version of Catalog: " + game_version)
    get_remote_ip()
    try:
        output = json.load(open(os.path.join(app.root_path, "json", "catalog", game_version, "catalog.json"), "r"))
        return jsonify(output)

    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="catalog", message=e)


@app.errorhandler(404)
def debug_404():
    logger.graylog_logger(level="error", handler="404-handler", message=f"Path: {request.path} Endpoint: {request.endpoint}")
    return jsonify({"message": "Endpoint not found"}), 404
