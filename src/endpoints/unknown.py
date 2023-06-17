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
        logger.graylog_logger(level="error", handler="unknown_catalog", message=str(e))


@app.errorhandler(404)
def debug_404(e):
    print("##################################################################################")
    print("DEBUG 404")
    print("##################################################################################")
    print('HTTP Headers:')
    for header in request.headers:
        print(f'{header[0]}: {header[1]}')

    print('Cookies:')
    for key, value in request.cookies.items():
        print(f'{key}: {value}')

    print('Endpoint: ', request.endpoint)
    print('Path: ', request.path)
    print('Method: ', request.method)

    if request.json:
        print('JSON Payload:')
        print(request.json)

    print("##################################################################################")
    return jsonify({"status": "error", "code": 404})
