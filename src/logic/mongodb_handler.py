import pymongo
import uuid
from logic.logging_handler import logger


class Mongo:
    def __init__(self):
        self.dyn_server = None
        self.dyn_db = None
        self.dyn_collection = None

    def user_db_handler(self, steamid, server, db, collection):
        self.dyn_server = server
        self.dyn_db = db
        self.dyn_collection = collection
        try:
            client = pymongo.MongoClient(self.dyn_server)
            self.dyn_db = client[self.dyn_db]
            self.dyn_collection = self.dyn_db[self.dyn_collection]

            existing_document = self.dyn_collection.find_one({'steamid': steamid})

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
                    'token': token,
                    'eula': False,
                    'account_xp': 0,
                    'prestige_xp': 0,
                    'runner_xp': 0,
                    'hunter_xp': 0,
                    'currency_blood_cells': 0,
                    'currency_iron': 0,
                    'currency_ink_cells': 0,
                    'unlocked_items': [],
                    'is_banned': False,
                    'ban_reason': "NoReasonGiven",
                    'ban_start': 2177449139,
                    'ban_expire': 253392484149,
                    'special_unlocks': [],
                    'finished_challanges': [],
                    'open_challanges': []
                }

                self.dyn_collection.insert_one(new_document)
                logger.graylog_logger(level="info", handler="mongodb", message=f"New user added to database: {steamid}")
                return userId, token
        except Exception as e:
            logger.graylog_logger(level="error", handler="mongodb_user_db_handler", message=e)
            return None, None

    def eula(self, userId, get_eula, server, db, collection):
        try:
            self.dyn_server = server
            self.dyn_db = db
            self.dyn_collection = collection
            client = pymongo.MongoClient(self.dyn_server)
            self.dyn_db = client[self.dyn_db]
            self.dyn_collection = self.dyn_db[self.dyn_collection]
            existing_document = self.dyn_collection.find_one({'userId': userId})
            if existing_document:
                if get_eula:
                    eula = existing_document['eula']
                    return eula
                else:
                    self.dyn_collection.update_one({'userId': userId}, {'$set': {'eula': True}})
                    return True
            else:
                return False
        except Exception as e:
            logger.graylog_logger(level="error", handler="mongodb_eula", message=e)
            return None, None

    def get_debug(self, steamid, server, db, collection):
        try:
            self.dyn_server = server
            self.dyn_db = db
            self.dyn_collection = collection
            client = pymongo.MongoClient(self.dyn_server)
            self.dyn_db = client[self.dyn_db]
            self.dyn_collection = self.dyn_db[self.dyn_collection]
            existing_document = self.dyn_collection.find_one({'steamid': steamid})
            if existing_document:
                return existing_document
            else:
                return None
        except Exception as e:
            logger.graylog_logger(level="error", handler="mongodb_get_debug", message=e)
            return {"status": "error", "message": "Error in mongodb_handler"}

    def get_data_with_list(self, login, login_steam, items, server, db, collection):
        try:
            document = {}
            login = f"{login}"
            self.dyn_server = server
            self.dyn_db = db
            self.dyn_collection = collection
            client = pymongo.MongoClient(self.dyn_server)
            self.dyn_db = client[self.dyn_db]
            self.dyn_collection = self.dyn_db[self.dyn_collection]
            if login_steam:
                existing_document = self.dyn_collection.find_one({'steamid': login})
            else:
                existing_document = self.dyn_collection.find_one({"userId": login})
            if existing_document:
                for item in items:
                    document[item] = existing_document.get(item)
            else:
                if login_steam:
                    print(f"No user found with steamid: {login}")
                else:
                    print(f"No user found with userId: {login}")
                return None
            return document
        except Exception as e:
            logger.graylog_logger(level="error", handler="mongo_get_data_with_list", message=e)
            return None

    def write_data_with_list(self, steamid, items_dict, server, db, collection):
        try:
            steam_id = str(steamid)
            self.dyn_db = db
            self.dyn_collection = collection
            client = pymongo.MongoClient(server)
            self.dyn_db = client[self.dyn_db]
            self.dyn_collection = self.dyn_db[self.dyn_collection]
            existing_document = self.dyn_collection.find_one({'steamid': steamid})

            if existing_document:
                update_query = {'$set': items_dict}
                self.dyn_collection.update_one({'steamid': steamid}, update_query)
                return {"status": "success", "message": "Data updated"}
            else:
                print(f"No user found with steamid: {steam_id}")
                return None
        except Exception as e:
            print(e)
            logger.graylog_logger(level="error", handler="mongo_write_data_with_list", message=e)
            return None


mongo = Mongo()
