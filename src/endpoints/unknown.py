import requests
import werkzeug.exceptions
from flask import Response

from flask_definitions import *


# Do NOT change Result to ANYTHING or Add anything before it. Game will crash. Doesnt mean it 100% works tho XD
@app.route("/<game_version_unsanitized>/catalog", methods=["GET"])
def catalog_get(game_version_unsanitized):
    game_version = sanitize_input(game_version_unsanitized)
    check_for_game_client("strict")
    session_cookie = request.cookies.get("bhvrSession")
    userid = session_manager.get_user_id(session_cookie)
    if game_version == "dev030":
        output = json.load(open(os.path.join(app.root_path, "json", "catalog", "dev030", "catalog.json"), "r"))
        return jsonify(output)
    elif game_version == "2.11.2-1574441597":
        output = json.load(open(os.path.join(app.root_path, "json", "catalog", "te-18f25613-36778-ue4-374f864b", "catalog.json"), "r"))
        return jsonify(output)
    else:
        return jsonify({"message": "Unknown game version"}), 404


@app.errorhandler(404)
def debug_404(e):
    user_ip = check_for_game_client("remote")
    try:
        if request.json:
            response_json = sanitize_input(request.json)
        else:
            response_json = "None"
    except werkzeug.exceptions.UnsupportedMediaType:
        response_json = "None"
    if request.path:
        response_path = sanitize_input(request.path)
    else:
        response_path = "None"
    if request.endpoint:
        response_endpoint = sanitize_input(request.endpoint)
    else:
        response_endpoint = "None"
    logger.graylog_logger(level="error", handler="404-handler", message=f"<Path: {response_path}> "
                                                                        f"<Endpoint: {response_endpoint}>"
                                                                        f"<Methode: {sanitize_input(request.method)}>"
                                                                        f"<JSON: {response_json}>"
                                                                        f"<IP: {user_ip}>")

    return jsonify({"message": "Endpoint not found"}), 404


@app.errorhandler(500)
def debug_500(e):
    check_for_game_client("soft")
    if request.path:
        response_path = sanitize_input(request.path)
    else:
        response_path = "None"
    if request.endpoint:
        response_endpoint = sanitize_input(request.endpoint)
    else:
        response_endpoint = "None"
    if not e:
        e = "None"
    try:
        if request.json:
            response_json = sanitize_input(request.json)
        else:
            response_json = "None"
    except werkzeug.exceptions.UnsupportedMediaType:
        response_json = "None"

    response_method = request.method
    user_ip = check_for_game_client("remote")
    logger.graylog_logger(level="error", handler="500-handler", message=f"<Path: {response_path}> "
                                                                        f"<Endpoint: {response_endpoint}>"
                                                                        f"<Methode: {response_method}>"
                                                                        f"<JSON: {response_json}>"
                                                                        f"<IP: {user_ip}>"
                                                                        f"<Error: {e}>")
    print(e)
    return jsonify({"message": "Internal Server Error"}), 500


@app.route("/nice ports,/Trinity.txt.bak", methods=["GET"])
def trinity():
    # For NMAP Scans
    abort(404)
