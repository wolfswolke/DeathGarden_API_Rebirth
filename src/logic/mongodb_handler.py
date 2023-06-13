import pymongo
import uuid
from logic.logging_handler import graylog_logger


def user_db_handler(steamid, server, db, collection):
    try:
        client = pymongo.MongoClient(server)
        db = client[db]
        collection = db[collection]

        existing_document = collection.find_one({'steamid': steamid})

        if existing_document:
            print(f"Document with steamid {steamid} already exists.")
            userId = existing_document['userId']
            token = existing_document['token']
            return userId, token
        else:
            userId = str(uuid.uuid4())
            token = str(uuid.uuid4())

            new_document = {
                'steamid': steamid,
                'userId': userId,
                'token': token
            }

            collection.insert_one(new_document)
            graylog_logger(level="info", handler="mongodb", message=f"New user added to database: {steamid}")
            return userId, token
    except Exception as e:
        graylog_logger(level="error", handler="mongodb", message=f"Error in mongodb_handler: {e}")
        return None, None
