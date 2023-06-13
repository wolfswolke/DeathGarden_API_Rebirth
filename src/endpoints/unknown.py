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
        graylog_logger(level="error", handler="unknown_catalog", message=str(e))


@app.route("/api/v1/extensions/inventory/unlockSpecialItems", methods=["POST"])
def inventory_unlock_special_items():
    get_remote_ip()
    try:
        print("Responded to Inventory Unlock Special Items event api call POST")
        graylog_logger(level="info", handler="unknown_unlockSpecialItems",
                       message=request.get_json())
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        graylog_logger(level="error", handler="unknown_unlockSpecialItems", message=str(e))
