from flask_definitions import *
from src.util.challenge_data import *
# Database keys GLOBAL:
# challenge_id = XXX str
# value = 0 int
# completed = True/False bool

# Database keys WEEKLY/DAILY:
# completion_count = 0 int
# start_time = ISO
# expiration_time = ISO

# Cross matching keys:
# challenge_id = XXX str
# challengeBlueprint = XXX str
# faction = XXX str
# ChallengeCompletionValue = 0 int
# type = XXX str (currency)
# amount = 0 int
# challengeType = XXX str (daily/weekly/progression)



def looper(challenge, userid):
    data = get_progression_batch(challenge, userid)
    for base_challenge in challenge_data:
        if base_challenge["challenge_id"] == challenge:
            data["challengeBlueprint"] = base_challenge["challengeBlueprint"]
            data["faction"] = base_challenge["faction"]
            data["ChallengeCompletionValue"] = base_challenge["ChallengeCompletionValue"]
    try:
        data.pop("className")
        data["rewards"][0]["weight"] = 100
    except KeyError:
        pass
    if not "rewards" in data.keys():
        if not "rewardsClaimed" in data.keys():
            data["rewards"] = [
                {
                    "weight": 100,
                    "amount": 30,
                    "id": "CurrencyA",
                    "type": "currency",
                    "claimed": False
                }
            ]
    data["schemaVersion"] = 1
    return data


def get_time_based_challenges(challenge_type, userid):
    return_cal = []
    if challenge_type == "daily":
        for challenge in daily_challenges:
            data = looper(challenge, userid)
            data["challengeType"] = "Daily"
            return_cal.append(data)

    elif challenge_type == "weekly":
        for challenge in weekly_challenges:
            data = looper(challenge, userid)
            data["challengeType"] = "Weekly"
            return_cal.append(data)
    else:
        logger.graylog_logger(level="error", handler="get_time_based_challenges", message=f"Challenge type not found {challenge_type}")
        return []
    return return_cal


def get_progression_batch(guid, userid):
    for item in challenge_data:
        if guid == item["challenge_id"]:
            db_challenge = mongo.get_data_with_list(login=userid, login_steam=False, items={"challenges"})["challenges"]
            for challenge in db_challenge:
                if challenge["challenge_id"] == guid:
                    if challenge["value"] == 0:
                        data = {"challengeId": challenge["challenge_id"],
                                "completed": False}
                    else:
                        if challenge["completed"]:
                            reward_key = "rewards"
                            # TEST should be rewardsClaimed
                        else:
                            reward_key = "rewards"
                        data = {
                            "challengeId": challenge["challenge_id"],
                            "className": "ChallengeProgressionCounter",
                            reward_key: [
                                {
                                    "weight": 100,
                                    "type": "currency",
                                    "amount": 30,
                                    "id": "CurrencyA"
                                }
                            ],
                            "completed": challenge["completed"],
                            "schemaVersion": 1,
                            "value": challenge["value"]
                        }
                    if item["challengeType"] == "Daily":
                        create_time, expiration_time = get_lifetime("daily")
                    elif item["challengeType"] == "Weekly":
                        create_time, expiration_time = get_lifetime("weekly")
                    else:
                        return data
                    if create_time > challenge["lifetime"]["expirationTime"]:
                        challenge["completed"] = False
                        challenge["completion_count"] = challenge["completion_count"] + 1
                        challenge["lifetime"]["creationTime"] = create_time
                        challenge["lifetime"]["expirationTime"] = expiration_time
                        mongo.write_data_with_list(login=userid, login_steam=False,
                                                   items_dict={"challenges": db_challenge})
                        return data
                    else:
                        start_data = challenge["lifetime"]["creationTime"]
                        expiration_date = challenge["lifetime"]["expirationTime"]
                        data["lifetime"] = {
                            "creationTime": start_data,
                            "expirationTime": expiration_date
                        }
                    return data
            else:
                try:
                    challenge_type = item["challengeType"]
                except KeyError:
                    logger.graylog_logger(level="error", handler="get_progression_batch", message=f"Challenge KEY ERROR {guid}")
                    challenge_type = "NONE"

                if challenge_type == "Daily":
                    create_time, expiration_time = get_lifetime("daily")
                    _setup_challenges(guid, userid, challenge_type)
                    return {"challengeId": guid, "completed": False, "className": "Weekly",
                            "lifetime": {
                                "creationTime": create_time,
                                "expirationTime": expiration_time
                            },
                            "completion_count": 0}
                if challenge_type == "Weekly":
                    create_time, expiration_time = get_lifetime("weekly")
                    _setup_challenges(guid, userid, challenge_type)
                    return {"challengeId": guid, "completed": False, "className": "Weekly",
                            "lifetime": {
                                "creationTime": create_time,
                                "expirationTime": expiration_time
                            },
                            "completion_count": 0}
                _setup_challenges(guid, userid, challenge_type)
                return {"challengeId": guid, "completed": False}
    logger.graylog_logger(level="debug", handler="get_progression_batch", message=f"Challenge not found {guid}")
    return {"challengeId": guid,
            "completed": False,
            "className": "ChallengeProgressionCounter",
                            "rewardsClaimed": [
                                {
                                    "weight": 100,
                                    "type": "currency",
                                    "amount": 999,
                                    "id": "CurrencyA"
                                }
                            ],
                            "schemaVersion": 1,
                            "value": 0}


def update_progression_batch(guid, userid, value=0, complete=False):
    user_challenges = mongo.get_data_with_list(login=userid, login_steam=False, items={"challenges"})["challenges"]
    for challenge in user_challenges:
        if challenge["challenge_id"] == guid:
            for base_challenge in challenge_data:
                if base_challenge["challenge_id"] == guid:
                    if complete:
                        challenge["completed"] = True
                        challenge["value"] = base_challenge["ChallengeCompletionValue"]
                        if base_challenge["challengeType"] == "Daily":
                            challenge["completion_count"] = challenge["completion_count"] + 1
                        elif base_challenge["challengeType"] == "Weekly":
                            challenge["completion_count"] = challenge["completion_count"] + 1
                    else:
                        if base_challenge["ChallengeCompletionValue"] <= value:
                            challenge["completed"] = True
                            challenge["value"] = base_challenge["ChallengeCompletionValue"]
                            if base_challenge["challengeType"] == "Daily":
                                challenge["completion_count"] = challenge["completion_count"] + 1
                            elif base_challenge["challengeType"] == "Weekly":
                                challenge["completion_count"] = challenge["completion_count"] + 1

                        challenge["value"] = value
                    mongo.write_data_with_list(login=userid, login_steam=False, items_dict={"challenges": user_challenges})
                    return True
    return False


def _setup_challenges(guid, userid, challenge_type):
    user_challenges = mongo.get_data_with_list(login=userid, login_steam=False, items={"challenges"})["challenges"]
    if challenge_type == "ChallengeProgressionCounter":
        user_challenges.append({"challenge_id": guid, "value": 0, "completed": False})
    elif challenge_type == "Weekly":
        create_time, expiration_time = get_lifetime("weekly")
        user_challenges.append(
            {"challenge_id": guid, "value": 0, "completed": False, "completion_count": 0, "lifetime": {
                                "creationTime": create_time,
                                "expirationTime": expiration_time
                            },})
    else:
        create_time, expiration_time = get_lifetime("daily")
        user_challenges.append(
            {"challenge_id": guid, "value": 0, "completed": False, "completion_count": 0, "lifetime": {
                                "creationTime": create_time,
                                "expirationTime": expiration_time
                            },})
    mongo.write_data_with_list(login=userid, login_steam=False, items_dict={"challenges": user_challenges})
