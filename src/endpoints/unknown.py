from flask_definitions import *


# Do NOT change Result to ANYTHING or Add anything before it. Game will crash. Doesnt mean it 100% works tho XD
@app.route("/<game_version>/catalog", methods=["GET"])
def catalog_get(game_version):
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    try:
        output = json.load(open(os.path.join(app.root_path, "json", "catalog", game_version, "catalog.json"), "r"))
        return jsonify(output)

    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="catalog", message=e)


@app.errorhandler(404)
def debug_404(e):
    check_for_game_client("soft")
    logger.graylog_logger(level="error", handler="404-handler", message=f"Path: {request.path} Endpoint: {request.endpoint}")
    print(e)
    return jsonify({"message": "Endpoint not found"}), 404
