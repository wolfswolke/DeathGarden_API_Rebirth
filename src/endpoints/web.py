from flask_definitions import *
from logic.mongodb_handler import mongo


@app.route('/', methods=["GET"])
def index():
    get_remote_ip()
    print("Index Page")
    return render_template("index.html")


# @app.route('/debug/user/', methods=['GET'])
# def debug_user():
#     return debug_user(False)

@app.route('/debug/user/', methods=['GET'], defaults={'steamid': None})
@app.route('/debug/user/<steamid>', methods=['GET'])
def debug_user(steamid):
    if steamid is None:
        return render_template('debug/user.html', is_id_set=False, id_not_found=True)

    user_data = mongo.get_debug(steamid=steamid, server=mongo_host, db=mongo_db, collection=mongo_collection)

    if user_data is None:
        return render_template('debug/user.html', is_id_set=True, id_not_found=False, steam_id=steamid)

    return render_template(
        'debug/user.html',
        is_id_set=True,
        is_not_found=False,
        steam_id=request.args.get('steamid'),
        eula=user_data.get('eula'),
        currency_blood_cells=user_data.get('currency_blood_cells'),
        currency_ink_cells=user_data.get('currency_ink_cells'),
        currency_iron=user_data.get('currency_iron'),
        unlocked_items=user_data.get('unlocked_items'),
        userId=user_data.get('userId'),
        xp=user_data.get('xp')
    )
