from flask_definitions import *
from logic.time_handler import get_time


@app.route("/debug/", methods=["Get"])
def debug_root():
    endpoint_descriptions = {
        '/debug/user': 'Endpoint to debug user information',
        '/debug/time': 'Endpoint to debug Epoch Time'}

    endpoint_list = []
    for endpoint, description in endpoint_descriptions.items():
        endpoint_list.append(f'<li>{endpoint}: {description}</li>')

    endpoints_html = '<ul>' + ''.join(endpoint_list) + '</ul>'
    return f'<h1>Debug Endpoints:</h1>{endpoints_html}'


@app.route("/debug/time", methods=["Get"])
def debug_time():
    current_time, expire_time = get_time()
    return jsonify({'current_time': current_time, 'expire_time': expire_time})
