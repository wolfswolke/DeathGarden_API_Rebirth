from flask_definitions import *


@app.route("/te-18f25613-36778-ue4-374f864b/catalog", methods=["GET"])
def catalog_get():
    get_remote_ip()
    try:
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        graylog_logger("API ERROR: " + str(e), "error")


@app.route("/api/v1/extensions/inventory/unlockSpecialItems", methods=["POST"])
def inventory_unlock_special_items():
    get_remote_ip()
    try:
        print("Responded to Inventory Unlock Special Items event api call POST")
        graylog_logger(request.get_json(), "info")
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        graylog_logger("API ERROR: " + str(e), "error")