from flask_definitions import *

@app.route("/api/v1/config/MATCH_MAKING_REGIONS/raw", methods=["GET"])
def match_making_regions_raw():
    get_remote_ip()
    try:
        # print(request.json)
        return jsonify({"eServerResponded"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        print(e)