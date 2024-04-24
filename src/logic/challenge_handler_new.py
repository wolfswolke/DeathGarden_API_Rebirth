from flask_definitions import *
from src.util.challenge_data import *

# Base pickedChallenges Item
# {
# "itemId":"7F33795840136A9EBC0186A529E4A82A",
# "list":[
# {
# "challengeId":"DFB83AF243A8D25193F814BC94240037",
# "challengeCompletionValue":60,
# "challengeAsset":"/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
# }
# ]
# },


def update_challenge_time(current_challenge_data, challenge_type):
    if challenge_type == "daily":
        current_challenge_data["lifetime"]["creationTime"] = get_lifetime("daily")[0]
        current_challenge_data["lifetime"]["expirationTime"] = get_lifetime("daily")[1]
    elif challenge_type == "weekly":
        current_challenge_data["lifetime"]["creationTime"] = get_lifetime("weekly")[0]
        current_challenge_data["lifetime"]["expirationTime"] = get_lifetime("weekly")[1]
    else:
        logger.graylog_logger(level="Error", handler="update_challenge_time", message="Invalid challenge type")
        return None

    return current_challenge_data


def get_reward(blueprint):
    # todo add all static challenges here (SRC challenge_handler.py)
    data = {
        "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner": {
            "weight": 100,
            "amount": 30,
            "id": "CurrencyA",
            "type": "currency",
            "claimed": False
        },

    }
    if blueprint in data:
        return data[blueprint]
    else:
        return None



def get_challenge_ids_from_inventory(user_id):
    Progression_HunterGroupA = mongo.get_data_with_list(login=user_id, login_steam=False,
                                                        items={"HunterGroupA"})
    Progression_HunterGroupB = mongo.get_data_with_list(login=user_id, login_steam=False,
                                                        items={"HunterGroupB"})
    Progression_HunterGroupC = mongo.get_data_with_list(login=user_id, login_steam=False,
                                                        items={"HunterGroupC"})
    Progression_HunterGroupD = mongo.get_data_with_list(login=user_id, login_steam=False,
                                                        items={"HunterGroupD"})
    Progression_RunnerGroupA = mongo.get_data_with_list(login=user_id, login_steam=False,
                                                        items={"RunnerGroupA"})
    Progression_RunnerGroupB = mongo.get_data_with_list(login=user_id, login_steam=False,
                                                        items={"RunnerGroupB"})
    Progression_RunnerGroupC = mongo.get_data_with_list(login=user_id, login_steam=False,
                                                        items={"RunnerGroupC"})
    Progression_RunnerGroupD = mongo.get_data_with_list(login=user_id, login_steam=False,
                                                        items={"RunnerGroupD"})
    Progression_RunnerGroupE = mongo.get_data_with_list(login=user_id, login_steam=False,
                                                        items={"RunnerGroupE"})
    Progression_RunnerGroupF = mongo.get_data_with_list(login=user_id, login_steam=False,
                                                        items={"RunnerGroupF"})

    user_data = mongo.get_data_with_list(login=user_id, login_steam=False,
                                         items={"challengeProgression"})["challengeProgression"]

    HunterGroups = [Progression_HunterGroupA, Progression_HunterGroupB, Progression_HunterGroupC,
                    Progression_HunterGroupD]
    RunnerGroups = [Progression_RunnerGroupA, Progression_RunnerGroupB, Progression_RunnerGroupC,
                    Progression_RunnerGroupD, Progression_RunnerGroupE, Progression_RunnerGroupF]
    runner_challenges = []
    hunter_challenges = []
    for runner_group in RunnerGroups:
        for runner_challenge in runner_group['data']['pickedChallenges']:
            challenge_in_user = False
            for user_challenge in user_data:
                if runner_challenge["list"][0]["challengeId"] == user_challenge["challengeId"]:
                    challenge_in_user = True
                    break
            if not challenge_in_user:
                new_challenge_handler.generate_challenge(runner_challenge["list"][0]["challengeId"])

    for hunter_group in HunterGroups:
        for hunter_challenge in hunter_group['data']['pickedChallenges']:
            challenge_in_user = False
            for user_challenge in user_data:
                if hunter_challenge["list"][0]["challengeId"] == user_challenge["challengeId"]:
                    challenge_in_user = True
                    break
            if not challenge_in_user:
                new_challenge_handler.generate_challenge(hunter_challenge["list"][0]["challengeId"])

    return runner_challenges, hunter_challenges


class ChallengeHandler:
    def __init__(self):
        self.weekly_challenges = [
            "Challenge_ARB_Damage_HunterWeekly",
            "Challenge_AssaultRifleWins_HunterWeekly",
            "Challenge_BleedOut_HunterWeekly",
            "Challenge_BleedOut_RunnerWeekly",
            "Challenge_Damage_HunterWeekly",
            "Challenge_Double_HunterWeekly",
            "Challenge_DroneActivation_HunterWeekly",
            "Challenge_Efficient_HunterWeekly",
            "Challenge_Emotional_HunterWeekly",
            "Challenge_Emotional_RunnerWeekly",
            "Challenge_Greed_HunterWeekly",
            "Challenge_Greed_RunnerWeekly",
            "Challenge_Headshot_HunterWeekly",
            "Challenge_HuntingShotgunWins_HunterWeekly",
            "Challenge_InDenial_HunterWeekly",
            "Challenge_LMGWins_HunterWeekly",
            "Challenge_Mines_HunterWeekly",
            "Challenge_Mines_RunnerWeekly",
            "Challenge_Reveals_hunterWeekly",
            "Challenge_RingOut_hunterWeekly",
            "Challenge_Shields_RunnerWeekly",
            "Challenge_ShotgunDowns_HunterWeekly",
            "Challenge_Speed_HunterWeekly",
            "Challenge_SpeedCapture_RunnerWeekly",
            "Challenge_Stuns_RunnerWeekly",
            "Challenge_Turrets_HunterWeekly",
            "Challenge_Turrets_RunnerWeekly",
            "Challenge_UPs_RunnerWeekly",
            "Challenge_Wasteful_HunterWeekly",
            "Challenge_Wasteful_RunnerWeekly",
            "Challenge_WUP_HunterWeekly",
            "Challenge_WUP_RunnerWeekly"
        ]
        self.daily_challenges = [
            "Daily_Domination_Hunter",
            "Daily_Domination_Runner",
        ]
        self.event_challenges = []

    def get_challenge_by_id(self, challenge_id, user_id):
        user_data = mongo.get_data_with_list(login=user_id, login_steam=False, items={"challengeProgression"})[
            "challengeProgression"]
        if challenge_id in self.hard_code_challenges:
            challenge = self.hard_code_challenges[challenge_id]
            rt_user_challenge = None
            for user_challenge in user_data:
                if user_challenge["challengeId"] == challenge_id:
                    rt_user_challenge = user_challenge
                    break
            return challenge, rt_user_challenge
        if challenge_id in self.daily_challenges:
            print("Daily Challenge")
        if challenge_id in self.weekly_challenges:
            print("Weekly Challenge")

        user_challenge_data = \
            mongo.get_data_with_list(login=user_id, login_steam=False, items={"challengeProgression"})[
                "challengeProgression"]
        rt_challenge = None
        rt_user_challenge = None
        for challenge in user_data:
            if challenge["list"][0]["challengeId"] == challenge_id:
                rt_challenge = challenge
                break
        if rt_challenge is None:
            return None, None
        for user_challenge in user_challenge_data:
            if user_challenge["challengeId"] == challenge_id:
                rt_user_challenge = user_challenge
                break
        if rt_user_challenge is None:
            # create user challenge
            rt_user_challenge = self.add_challenge_to_user(user_id, challenge_id)
        return rt_challenge, rt_user_challenge

    def build_progression_batch(self, user_id, challenge_id):
        # Not started
        #       {
        #          "challengeId":"Challenge_RingOut_hunterWeekly:2019-11-21T23:22:11.927Z",
        #          "completed":false
        #       },
        # Completed
        #       {
        #          "challengeId":"Challenge_SurviveAChase_Runner:2019-11-21T23:22:11.927Z",
        #          "className":"ChallengeProgressionCounter",
        #          "rewardsClaimed":[
        #             {
        #                "type":"currency",
        #                "amount":1000,
        #                "id":"CurrencyC"
        #             }
        #          ],
        #          "completed":true,
        #          "schemaVersion":1,
        #          "value":10
        #       }
        challenge, user_challenge = self.get_challenge_by_id(challenge_id, user_id)
        if user_challenge["completed"]:
            rewards = get_reward(challenge["list"][0]["challengeAsset"])
            return {
                "challengeId": challenge_id,
                "className": "ChallengeProgressionCounter",
                "rewardsClaimed": rewards,
                "completed": True,
                "schemaVersion": 1,
                "value": user_challenge["value"]
            }
        elif user_challenge["value"] != 0:
            rewards = get_reward(challenge["list"][0]["challengeAsset"])
            return {
                "challengeId": challenge_id,
                "className": "ChallengeProgressionCounter",
                "completed": False,
                "schemaVersion": 1,
                "value": user_challenge["value"],
                "rewards": [
                    {
                        "weight": 100,
                        "amount": rewards["amount"],
                        "id": rewards["id"],
                        "type": rewards["type"],
                        "claimed": user_challenge["claimed"],
                    }
                ]
            }
        else:
            return {
                "challengeId": challenge_id,
                "completed": False
            }

    def get_time_based_challenges(self, userid, challenge_type):
        if challenge_type == "daily":
            challenges = self.daily_challenges
        elif challenge_type == "weekly":
            challenges = self.weekly_challenges
        else:
            return None

        return_data = []
        user_data = mongo.get_data_with_list(login=userid, login_steam=False,
                                             items={"challengeProgression"})["challengeProgression"]
        user_time_challenges = []
        if user_data is not None:
            for challenge in user_data:
                user_time_challenges.append(challenge["challengeId"].split(":")[0])

        for challenge_id in challenges:

            if challenge_id not in user_time_challenges:
                current_challenge_data = self.add_challenge_to_user(userid, challenge_id, challenge_type)
            else:
                current_challenge_data = user_data[user_time_challenges.index(challenge_id)]
                lifetime = get_lifetime(challenge_type)[0]
                if lifetime > current_challenge_data["lifetime"]["expirationTime"]:
                    current_challenge_data = update_challenge_time(current_challenge_data, challenge_type)
                    user_data = mongo.get_data_with_list(login=userid, login_steam=False,
                                                         items={"challengeProgression"})["challengeProgression"]
                    user_data[user_time_challenges.index(challenge_id)] = current_challenge_data
            return_data.append({
                "lifetime": current_challenge_data["lifetime"],
                "challengeType": challenge_type,
                "challengeId": current_challenge_data["challengeId"],
                "challengeCompletionValue": challenge_data[challenge_id]["ChallengeCompletionValue"],
                "faction": challenge_data[challenge_id]["faction"],
                "challengeBlueprint": challenge_data[challenge_id]["challengeBlueprint"],
                "rewards": [get_reward(challenge_data[challenge_id]["challengeBlueprint"])]
            })
        else:
            logger.graylog_logger(level="info", handler="get_time_based_challenges", message=f"No User Challenge Data Found ({challenge_type})")

        return return_data

    def update_challenge(self, user_id, challenge_id, value=0, completed=False):
        user_data = mongo.get_data_with_list(login=user_id, login_steam=False, items={"challengeProgression"})[
            "challengeProgression"]
        writen_data = []
        returning = []
        for challenge in user_data:
            if challenge["challengeId"] == challenge_id:
                if completed:
                    challenge["completed"] = True
                    data = get_reward(challenge["challengeBlueprint"])
                    returning.append(data)
                else:
                    challenge["value"] = value
            writen_data.append(challenge)
        mongo.write_data_with_list(login=user_id, login_steam=False, items={"challengeProgression"}, items_dict=writen_data)

    def build_challenges(self):
        # getChallenges.php.json
        # Get all challenges
        # Get all user challenges
        # Compare
        # Return
        # {
        #    "challenges":[
        #       {
        #          "lifetime":{
        #             "creationTime":"2019-11-25T02:17:22.484Z",
        #             "expirationTime":"2019-11-25T17:59:59.000Z"
        #          },
        #          "challengeType":"Daily",
        #          "challengeId":"Challenge_Deliver_Runner:2019-11-25T02:17:22.484Z",
        #          "challengeCompletionValue":50,
        #          "faction":"Runner",
        #          "challengeBlueprint":"\/Game\/Challenges\/Challenge_Deliver_Runner.Challenge_Deliver_Runner",
        #          "rewards":[
        #             {
        #                "weight":100,
        #                "amount":30,
        #                "id":"CurrencyA",
        #                "type":"currency",
        #                "claimed":false
        #             }
        #          ]
        #       },
        #       {
        #          "lifetime":{
        #             "creationTime":"2019-11-25T02:17:22.484Z",
        #             "expirationTime":"2019-11-25T17:59:59.000Z"
        #          },
        #          "challengeType":"Daily",
        #          "challengeId":"Challenge_Domination_Hunter:2019-11-25T02:17:22.484Z",
        #          "challengeCompletionValue":1,
        #          "faction":"Hunter",
        #          "challengeBlueprint":"\/Game\/Challenges\/Daily\/Challenge_Domination_Hunter.Challenge_Domination_Hunter",
        #          "rewards":[
        #             {
        #                "weight":100,
        #                "amount":30,
        #                "id":"CurrencyA",
        #                "type":"currency",
        #                "claimed":false
        #             }
        #          ]
        #       }
        #    ]
        # }
        pass

    def generate_challenge(self, challenge_id):
        challengeCompletionValue = random.randint(1, 100)
        progression.append({"challengeId": challenge_id, "value": 0, "completed": False,
                            "challengeCompletionValue": challengeCompletionValue,
                            "lifetime": {"creationTime": "2019-11-25T02:17:22.484Z",
                                         "expirationTime": "2020-11-25T02:17:22.484Z"}})


    def add_challenge_to_user(self, user_id, challenge_id, challenge_type="progression"):
        user_challenge_data = \
        mongo.get_data_with_list(login=user_id, login_steam=False, items={"challengeProgression"})[
            "challengeProgression"]

        if user_challenge_data is None:
            user_challenge_data = []

        data = {
            "challengeId": challenge_id,
            "completed": False,
        }

        if challenge_type.upper() == "WEEKLY" or challenge_type.upper() == "DAILY":
            data["lifetime"] = {
                "creationTime": "",
                "expirationTime": ""
            }
            data = update_challenge_time(data, challenge_type)
            data["challengeId"] = challenge_id + ":" + get_lifetime(challenge_type)[0]


        user_challenge_data.append(data)
        mongo.write_data_with_list(login=user_id, login_steam=False, items_dict={"challengeProgression": user_challenge_data})
        return data

    def get_progression_batch(self, challenge_id, userid):
        #challenge_data is now a dict
        #will loop through keys
        for item in challenge_data:
            if challenge_id == item:
                db_challenge = mongo.get_data_with_list(login=userid, login_steam=False, items={"challenges"})[
                    "challenges"]
                for challenge in db_challenge:
                    if challenge["challenge_id"] == challenge_id:
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
                    challenge_type = challenge_data[item]["challengeType"]
                except KeyError:
                    logger.graylog_logger(level="error", handler="get_progression_batch",
                                          message=f"Challenge KEY ERROR {challenge_id}")
                    challenge_type = "NONE"

                if challenge_type == "Daily":
                    create_time, expiration_time = get_lifetime("daily")
                    self.add_challenge_to_user(userid, challenge_id, challenge_type)
                    return {"challengeId": challenge_id, "completed": False, "className": "Weekly",
                            "lifetime": {
                                "creationTime": create_time,
                                "expirationTime": expiration_time
                            },
                            "completion_count": 0}
                if challenge_type == "Weekly":
                    create_time, expiration_time = get_lifetime("weekly")
                    self.add_challenge_to_user(userid, challenge_id, challenge_type)
                    return {"challengeId": challenge_id, "completed": False, "className": "Weekly",
                            "lifetime": {
                                "creationTime": create_time,
                                "expirationTime": expiration_time
                            },
                            "completion_count": 0}
                self.add_challenge_to_user(userid, challenge_id, challenge_type)
                return {"challengeId": challenge_id, "completed": False}
        logger.graylog_logger(level="debug", handler="get_progression_batch", message=f"Challenge not found {challenge_id}")
        return {"challengeId": challenge_id,
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

    def login_update_time(self, userId):
        # todo get user inv and use as progression
        for challenge_int in self.daily_challenges:
            for challenge in progression:
                if challenge['challengeId'] == challenge_int:
                    if challenge['lifetime']['expirationTime'] < get_lifetime("daily")[1]:
                        challenge['lifetime']['expirationTime'] = get_lifetime("daily")[1]
                        challenge['lifetime']['creationTime'] = get_lifetime("daily")[0]
        for challenge_int in self.weekly_challenges:
            for challenge in progression:
                if challenge['challengeId'] == challenge_int:
                    if challenge['lifetime']['expirationTime'] < get_lifetime("weekly")[1]:
                        challenge['lifetime']['expirationTime'] = get_lifetime("weekly")[1]
                        challenge['lifetime']['creationTime'] = get_lifetime("weekly")[0]

    def update_progression(challengeId, value):
        for challenge_int in progression:
            if challenge_int['challengeId'] == challengeId:
                challenge_int['value'] = value

    def complete_challenge(challengeId):
        for challenge_int in progression:
            if challenge_int['challengeId'] == challengeId:
                challenge_int['completed'] = True

    def get_challenge(challengeId):
        for challenge_int in progression:
            if challenge_int['challengeId'] == challengeId:
                return challenge_int
        return None

    def generate_execute_response(userid, challengeId, value):
        update_progression(challengeId, value)
        challenge_int = get_challenge(challengeId)
        if value >= challenge_int['challengeCompletionValue']:
            complete_challenge(challengeId)
            return {"userId": userid, "challengeId": challengeId, "value": value, "completed": True}
        return {"userId": userid, "challengeId": challengeId, "value": value, "completed": False}


new_challenge_handler = ChallengeHandler()
