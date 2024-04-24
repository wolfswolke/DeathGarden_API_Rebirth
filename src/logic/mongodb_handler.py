import pymongo
import uuid
from logic.logging_handler import logger


class Mongo:
    def __init__(self):
        self.dyn_server = ""
        self.dyn_db = ""
        self.dyn_collection = ""
        self.default_user_schema = {
            'eula': False,
            'currency_blood_cells': 1000,
            'currency_iron': 1000,
            'currency_ink_cells': 1000,
            'inventory': [],
            'is_banned': False,
            'ban_reason': "NoReasonGiven",
            'ban_start': 2177449139,
            'ban_expire': 253392484149,
            'special_unlocks': [],
            'challengeProgression': [],
            'unread_msg_ids': [],
            'unlocked_special_item_ids': [],
            'last_played_faction': 'Runner',
            'tutorial_completed': False,
            'last_runner': 'Runner.Smoke',
            'last_hunter': 'Hunter.Inquisitor',
            'hasPlayedDeathGarden1': False,
            'RunnerGroupA': {
                'prestige': 0,
                'experience': {
                    'level': 1,
                    'experienceToReach': 5403,
                    'currentExperience': 0
                },
                'Equipment': [],
                'EquippedPerks': [],
                'EquippedPowers': [],
                'EquippedWeapons': [],
                'EquippedBonuses': [],
                'pickedChallenges': [],
                'equippedConsumables': [],
                'characterId': {"tagName":"Runner.Sawbones"}
            },
            'RunnerGroupB': {
                'prestige': 0,
                'experience': {
                    'level': 1,
                    'experienceToReach': 5403,
                    'currentExperience': 0
                },
                'Equipment': [],
                'EquippedPerks': [],
                'EquippedPowers': [],
                'EquippedWeapons': [],
                'EquippedBonuses': [],
                'pickedChallenges': [],
                'equippedConsumables': [],
                'characterId': {"tagName":"Runner.Ink"}
            },
            'RunnerGroupC': {
                'prestige': 0,
                'experience': {
                    'level': 1,
                    'experienceToReach': 5403,
                    'currentExperience': 0
                },
                'Equipment': [],
                'EquippedPerks': [],
                'EquippedPowers': [],
                'EquippedWeapons': [],
                'EquippedBonuses': [],
                'pickedChallenges': [],
                'equippedConsumables': [],
                'characterId': {"tagName":"Runner.Ghost"}
            },
            'RunnerGroupD': {
                'prestige': 0,
                'experience': {
                    'level': 1,
                    'experienceToReach': 5403,
                    'currentExperience': 0
                },
                'Equipment': [],
                'EquippedPerks': [],
                'EquippedPowers': [],
                'EquippedWeapons': [],
                'EquippedBonuses': [],
                'pickedChallenges': [],
                'equippedConsumables': [],
                'characterId': {"tagName":"Runner.Switch"}
            },
            'RunnerGroupE': {
                'prestige': 0,
                'experience': {
                    'level': 1,
                    'experienceToReach': 5403,
                    'currentExperience': 0
                },
                'Equipment': [],
                'EquippedPerks': [],
                'EquippedPowers': [],
                'EquippedWeapons': [],
                'EquippedBonuses': [],
                'pickedChallenges': [],
                'equippedConsumables': [],
                'characterId': {"tagName":"Runner.Smoke"}
            },
            'RunnerGroupF': {
                'prestige': 0,
                'experience': {
                    'level': 1,
                    'experienceToReach': 5403,
                    'currentExperience': 0
                },
                'Equipment': [],
                'EquippedPerks': [],
                'EquippedPowers': [],
                'EquippedWeapons': [],
                'EquippedBonuses': [],
                'pickedChallenges': [],
                'equippedConsumables': [],
                'characterId': {"tagName":"Runner.Dash"}
            },
            'HunterGroupA': {
                'prestige': 0,
                'experience': {
                    'level': 1,
                    'experienceToReach': 5403,
                    'currentExperience': 0
                },
                'Equipment': [],
                'EquippedPerks': [],
                'EquippedPowers': [],
                'EquippedWeapons': [],
                'EquippedBonuses': [],
                'pickedChallenges': [],
                'equippedConsumables': [],
                'characterId': {"tagName":"Hunter.Stalker"}
            },
            'HunterGroupB': {
                'prestige': 0,
                'experience': {
                    'level': 1,
                    'experienceToReach': 5403,
                    'currentExperience': 0
                },
                'Equipment': [],
                'EquippedPerks': [],
                'EquippedPowers': [],
                'EquippedWeapons': [],
                'EquippedBonuses': [],
                'pickedChallenges': [],
                'equippedConsumables': [],
                'characterId': {"tagName":"Hunter.Inquisitor"}
            },
            'HunterGroupC': {
                'prestige': 0,
                'experience': {
                    'level': 1,
                    'experienceToReach': 5403,
                    'currentExperience': 0
                },
                'Equipment': [],
                'EquippedPerks': [],
                'EquippedPowers': [],
                'EquippedWeapons': [],
                'EquippedBonuses': [],
                'pickedChallenges': [],
                'equippedConsumables': [],
                'characterId': {"tagName":"Hunter.Poacher"}
            },
            'HunterGroupD': {
                'prestige': 0,
                'experience': {
                    'level': 1,
                    'experienceToReach': 5403,
                    'currentExperience': 0
                },
                'Equipment': [],
                'EquippedPerks': [],
                'EquippedPowers': [],
                'EquippedWeapons': [],
                'EquippedBonuses': [],
                'pickedChallenges': [],
                'equippedConsumables': [],
                'characterId': {"tagName":"Hunter.Mass"}
            },
            'RunnerProgression':{
                "experience": {
                    "level": 1,
                    "experienceToReach": 5,
                    "currentExperience": 3
                }
            },
            'HunterProgression': {
                "experience": {
                    "level": 1,
                    "experienceToReach": 5,
                    "currentExperience": 3
                }
            },
            'PlayerProgression': {
                "experience": {
                    "level": 1,
                    "experienceToReach": 5,
                    "currentExperience": 3
                }
            },
            'ProfileMetaData': {
                'characterCumulativeExperience': 0
            }
        }

    def setup(self, server, db, collection):
        self.dyn_server = server
        self.dyn_db = db
        self.dyn_collection = collection

    def user_db_handler(self, steamid):
        try:
            client = pymongo.MongoClient(self.dyn_server)
            dyn_client_db = client[self.dyn_db]
            dyn_collection = dyn_client_db[self.dyn_collection]

            existing_document = dyn_collection.find_one({'steamid': steamid})

            if existing_document:
                userId = existing_document['userId']
                token = existing_document['token']

                for key, default_value in self.default_user_schema.items():
                    if key not in existing_document:
                        existing_document[key] = default_value
                        logger.graylog_logger(level="info", handler="mongodb", message=f"New key added to database: {key} for user {steamid}")

                    if type(default_value) == dict:
                        for k, val in default_value.items():
                            if k not in existing_document[key]:
                                existing_document[key][k] = val
                                logger.graylog_logger(level="info", handler="mongodb", message=f"New key added to database: {k} for user {steamid}")

                dyn_collection.replace_one({'steamid': steamid}, existing_document)

                client.close()
                return userId, token
            else:
                userId = str(uuid.uuid4())
                token = str(uuid.uuid4())

                new_document = {
                    'steamid': steamid,
                    'userId': userId,
                    'token': token,
                }

                for key, default_value in self.default_user_schema.items():
                    new_document[key] = default_value

                dyn_collection.insert_one(new_document)
                logger.graylog_logger(level="info", handler="mongodb", message=f"New user added to database: {steamid}")
                client.close()
                return userId, token
        except Exception as e:
            logger.graylog_logger(level="error", handler="mongodb_user_db_handler", message=e)
            return None, None

    def eula(self, userId, get_eula):
        try:
            client = pymongo.MongoClient(self.dyn_server)
            dyn_client_db = client[self.dyn_db]
            dyn_collection = dyn_client_db[self.dyn_collection]
            existing_document = dyn_collection.find_one({'userId': userId})
            if existing_document:
                if get_eula:
                    eula = existing_document['eula']
                    client.close()
                    return eula
                else:
                    dyn_collection.update_one({'userId': userId}, {'$set': {'eula': True}})
                    client.close()
                    return True
            else:
                client.close()
                return False
        except Exception as e:
            logger.graylog_logger(level="error", handler="mongodb_eula", message=e)
            return None, None

    def get_debug(self, steamid):
        try:
            client = pymongo.MongoClient(self.dyn_server)
            dyn_client_db = client[self.dyn_db]
            dyn_collection = dyn_client_db[self.dyn_collection]
            existing_document = dyn_collection.find_one({'steamid': steamid})
            if existing_document:
                client.close()
                return existing_document
            else:
                client.close()
                return None
        except Exception as e:
            logger.graylog_logger(level="error", handler="mongodb_get_debug", message=e)
            return {"status": "error", "message": "Error in mongodb_handler"}

    def get_data_with_list(self, login, login_steam, items):
        try:
            document = {}
            login = f"{login}"
            client = pymongo.MongoClient(self.dyn_server)
            dyn_client_db = client[self.dyn_db]
            dyn_collection = dyn_client_db[self.dyn_collection]
            if login_steam:
                existing_document = dyn_collection.find_one({'steamid': login})
            else:
                existing_document = dyn_collection.find_one({"userId": login})
            if existing_document:
                for item in items:
                    document[item] = existing_document.get(item)
            else:
                if login_steam:
                    print(f"No user found with steamid: {login}")
                else:
                    print(f"No user found with userId: {login}")
                client.close()
                return None
            client.close()
            return document
        except Exception as e:
            logger.graylog_logger(level="error", handler="mongo_get_data_with_list", message=e)
            return None

    def write_data_with_list(self, login, login_steam, items_dict):
        try:
            client = pymongo.MongoClient(self.dyn_server)
            dyn_client_db = client[self.dyn_db]
            dyn_collection = dyn_client_db[self.dyn_collection]
            if login_steam:
                steam_id = str(login)
                existing_document = dyn_collection.find_one({'steamid': steam_id})
            else:
                user_id = str(login)
                existing_document = dyn_collection.find_one({"userId": user_id})
            if existing_document:
                update_query = {'$set': items_dict}
                if login_steam:
                    dyn_collection.update_one({'steamid': steam_id}, update_query)
                else:
                    dyn_collection.update_one({'userId': user_id}, update_query)
                client.close()
                return {"status": "success", "message": "Data updated"}
            else:
                print(f"No user found with steamid: {steam_id}")
                client.close()
                return None
        except Exception as e:
            print(e)
            logger.graylog_logger(level="error", handler="mongo_write_data_with_list", message=e)
            return None


    def add_to_array(self, login, login_steam, array_name, data):
        try:
            client = pymongo.MongoClient(self.dyn_server)
            dyn_client_db = client[self.dyn_db]
            dyn_collection = dyn_client_db[self.dyn_collection]
            if login_steam:
                steam_id = str(login)
                existing_document = dyn_collection.find_one({'steamid': steam_id})
            else:
                user_id = str(login)
                existing_document = dyn_collection.find_one({"userId": user_id})
            if existing_document:
                update_query = {'$push': {array_name: data}}
                if login_steam:
                    dyn_collection.update_one({'steamid': steam_id}, update_query)
                else:
                    dyn_collection.update_one({'userId': user_id}, update_query)
                client.close()
                return {"status": "success", "message": "Data updated"}
            else:
                print(f"No user found with steamid: {steam_id}")
                client.close()
                return None
        except Exception as e:
            print(e)
            logger.graylog_logger(level="error", handler="mongo_add_to_array", message=e)
            return None

    def update_array(self, login, login_steam, array_name, data, index):
        try:
            client = pymongo.MongoClient(self.dyn_server)
            dyn_client_db = client[self.dyn_db]
            dyn_collection = dyn_client_db[self.dyn_collection]
            if login_steam:
                steam_id = str(login)
                existing_document = dyn_collection.find_one({'steamid': steam_id})
            else:
                user_id = str(login)
                existing_document = dyn_collection.find_one({"userId": user_id})
            if existing_document:
                update_query = {'$set': {f"{array_name}.{index}": data}}
                if login_steam:
                    dyn_collection.update_one({'steamid': steam_id}, update_query)
                else:
                    dyn_collection.update_one({'userId': user_id}, update_query)
                client.close()
                return {"status": "success", "message": "Data updated"}
            else:
                print(f"No user found with steamid: {steam_id}")
                client.close()
                return None
        except Exception as e:
            print(e)
            logger.graylog_logger(level="error", handler="mongo_update_array", message=e)
            return None


mongo = Mongo()
