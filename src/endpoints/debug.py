from flask_definitions import *
from logic.time_handler import get_time

from logic.mongodb_handler import mongo


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


@app.route("/debug/user/", methods=["Get"])
def debug_user():
    if request.args.get('steamid') is None:
        return jsonify({'error': 'No steamid. Please call with ?steamid=<steamID64>'}), 400
    steam_id = request.args.get('steamid')
    user_data = mongo.get_debug(steamid=steam_id, server=mongo_host, db=mongo_db, collection=mongo_collection)
    if user_data.get('status') == 'error':
        return jsonify(user_data), 400
    user_data['_id'] = str(user_data.get('_id'))
    steamid = user_data.get('steamid')
    userId = user_data.get('userId')
    eula = user_data.get('eula')
    xp = user_data.get('xp')
    currency_blood_cells = user_data.get('currency_blood_cells')
    currency_iron = user_data.get('currency_iron')
    currency_ink_cells = user_data.get('currency_ink_cells')
    unlocked_items = user_data.get('unlocked_items')
    return_data = {"steamid": steamid, "userId": userId, "eula": eula, "xp": xp, "currency_blood_cells": currency_blood_cells, "currency_iron": currency_iron, "currency_ink_cells": currency_ink_cells, "unlocked_items": unlocked_items}
    return jsonify(return_data)


@app.route("/debug/time", methods=["Get"])
def debug_time():
    current_time, expire_time = get_time()
    return jsonify({'current_time': current_time, 'expire_time': expire_time})
