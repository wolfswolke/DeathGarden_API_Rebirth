from flask_definitions import *


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

def add_challenge_to_user(user_id, challenge_id, challenge_type="progression"):
    user_challenge_data = mongo.get_data_with_list(login=user_id, login_steam=False, items={"challengeProgression"})[
        "challengeProgression"]
    data = {
        "challengeId": challenge_id,
        "completed": False,
        "value": 0,
        "claimed": False
    }
    if challenge_type == "time":
        data["lifetime"] = {
            "creationTime": "",
            "expirationTime": ""
        }
    user_challenge_data.append(data)
    mongo.write_data_with_list(login=user_id, login_steam=False, data={"challengeProgression": user_challenge_data})
    return data


def update_challenge_time(user_id, challenge_id, challenge_type):
    user_challenge_data = mongo.get_data_with_list(login=user_id, login_steam=False, items={"challengeProgression"})[
        "challengeProgression"]
    for challenge in user_challenge_data:
        if challenge["challengeId"] == challenge_id:
            if challenge_type == "daily":
                challenge["lifetime"]["creationTime"] = get_lifetime("daily")[0]
                challenge["lifetime"]["expirationTime"] = get_lifetime("daily")[1]
                break
            elif challenge_type == "weekly":
                challenge["lifetime"]["creationTime"] = get_lifetime("weekly")[0]
                challenge["lifetime"]["expirationTime"] = get_lifetime("weekly")[1]
                break
            else:
                logger.graylog_logger(level="Error", handler="update_challenge_time", message="Invalid challenge type")
                return None

    mongo.write_data_with_list(login=user_id, login_steam=False, data={"challengeProgression": user_challenge_data})
    return user_challenge_data


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


class ChallengeHandler:
    def __init__(self):
        self.hard_code_challenges = {
            "400AE859456112F4EB7516A42821AEF3": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Autocollect_Hunter.Challenge_Autocollect_Hunter',
                'ChallengeCompletionValue': 25},
            "8DAE5C0943DA33C28E82FC92B9644702": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Autocollect_Hunter.Challenge_Autocollect_Hunter',
                'ChallengeCompletionValue': 63},
            "6DFAA85548F1C349CE1E6A9F29188FCF": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Autocollect_Hunter.Challenge_Autocollect_Hunter',
                'ChallengeCompletionValue': 250},
            "A1047B3B49BFBF12313991A8FBB3E215": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_GreatShape_Hunter.Challenge_GreatShape_Hunter',
                'ChallengeCompletionValue': 50},
            "6AFBAEC144C206BDBFD4F0B2216148B6": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_GreatShape_Hunter.Challenge_GreatShape_Hunter',
                'ChallengeCompletionValue': 125},
            "AB4B4E524F00B197156256AFACE501EF": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_GreatShape_Hunter.Challenge_GreatShape_Hunter',
                'ChallengeCompletionValue': 500},
            "590D3041420289011FB868A89A43F7CF": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Hacker_Hunter.Challenge_Hacker_Hunter',
                'ChallengeCompletionValue': 15},
            "CF29BA964B65E429DD2B559A4D335CD3": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Hacker_Hunter.Challenge_Hacker_Hunter',
                'ChallengeCompletionValue': 38},
            "32749AFC47E7C872933FC9AB8E76AD61": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Hacker_Hunter.Challenge_Hacker_Hunter',
                'ChallengeCompletionValue': 150},
            "9CD0EEEC4D2D193E168AD78026BFC6E3": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_PowerBoosterTurret_Hunter.Challenge_PowerBoosterTurret_Hunter',
                'ChallengeCompletionValue': 10},
            "077EEED2433E763CEE4657B929E23043": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_PowerBoosterTurret_Hunter.Challenge_PowerBoosterTurret_Hunter',
                'ChallengeCompletionValue': 25},
            "EAC4FDA245A1B54CB15BE8926EB62E89": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_PowerBoosterTurret_Hunter.Challenge_PowerBoosterTurret_Hunter',
                'ChallengeCompletionValue': 100},
            "0E7912E34B0F76F06A54769371A1615A": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SoClose_Hunter.Challenge_SoClose_Hunter',
                'ChallengeCompletionValue': 1},
            "8F2FD32744CCF967D64953B8C27B8B4C": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SoClose_Hunter.Challenge_SoClose_Hunter',
                'ChallengeCompletionValue': 3},
            "0502BFE9440E8A45212F4EBF2023368B": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SoClose_Hunter.Challenge_SoClose_Hunter',
                'ChallengeCompletionValue': 10},
            "7A25ABAE43856F2D5233F5A39CFAF921": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SpeedDemon_Hunter.Challenge_SpeedDemon_Hunter',
                'ChallengeCompletionValue': 100},
            "8046419A474EDC58A273FDA473064FF8": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SpeedDemon_Hunter.Challenge_SpeedDemon_Hunter',
                'ChallengeCompletionValue': 250},
            "C9E2E88A4502470E1146629BBD79A876": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SpeedDemon_Hunter.Challenge_SpeedDemon_Hunter',
                'ChallengeCompletionValue': 1000},
            "05DFDE95403708570292FE847BBA8EA2": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_HeyDownThere_Hunter.Challenge_HeyDownThere_Hunter',
                'ChallengeCompletionValue': 3},
            "3941A0454830CAB53F4C6B993F1BC7B8": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_HeyDownThere_Hunter.Challenge_HeyDownThere_Hunter',
                'ChallengeCompletionValue': 8},
            "836A4FD246B33F91BDC4C3A2608C6289": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_HeyDownThere_Hunter.Challenge_HeyDownThere_Hunter',
                'ChallengeCompletionValue': 30},
            "721E2D644D051394207BC492127586CA": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_LuckyCharm_Hunter.Challenge_LuckyCharm_Hunter',
                'ChallengeCompletionValue': 3},
            "ACB79B5049C283856BEA039BEF9952A1": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_LuckyCharm_Hunter.Challenge_LuckyCharm_Hunter',
                'ChallengeCompletionValue': 8},
            "ECAEAF9A4A2A0038999D738A7C9E502F": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_LuckyCharm_Hunter.Challenge_LuckyCharm_Hunter',
                'ChallengeCompletionValue': 30},
            "92B4BBED409F403E37B844879B3AEB7A": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_PowerBoosterFade_Hunter.Challenge_PowerBoosterFade_Hunter',
                'ChallengeCompletionValue': 5},
            "F56098E54E0F19E6F67FB89C42212AB8": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_PowerBoosterFade_Hunter.Challenge_PowerBoosterFade_Hunter',
                'ChallengeCompletionValue': 13},
            "1D7A66E34ECAF02BC243FB880323A6B8": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_PowerBoosterFade_Hunter.Challenge_PowerBoosterFade_Hunter',
                'ChallengeCompletionValue': 50},
            "A207A3624BEA90AE22A71BA08F529866": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_PowerStomp_Hunter.Challenge_PowerStomp_Hunter',
                'ChallengeCompletionValue': 2},
            "35E18B6B48AC6D8022E13B88A3853F81": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_PowerStomp_Hunter.Challenge_PowerStomp_Hunter',
                'ChallengeCompletionValue': 5},
            "A00B9E6844C5ABFF86DB4FAA5B81CBC7": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_PowerStomp_Hunter.Challenge_PowerStomp_Hunter',
                'ChallengeCompletionValue': 20},
            "1CA09F684C2F4464AA4C158F9BAA72D1": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Stealer_Hunter.Challenge_Stealer_Hunter',
                'ChallengeCompletionValue': 3},
            "5FE03903416D3BBE9D2FD592B36809FC": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Stealer_Hunter.Challenge_Stealer_Hunter',
                'ChallengeCompletionValue': 8},
            "0A5C2455485A166F60009FA3246504C4": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Stealer_Hunter.Challenge_Stealer_Hunter',
                'ChallengeCompletionValue': 30},
            "6871DC8B46D62AEFDE7FDCBC7B1AF9B4": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Stunning_Hunter.Challenge_Stunning_Hunter',
                'ChallengeCompletionValue': 5},
            "D8DBF1924EAEA4218A2110B54339E020": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Stunning_Hunter.Challenge_Stunning_Hunter',
                'ChallengeCompletionValue': 13},
            "9764321E4BC15FC21F0AD782BB98802A": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Stunning_Hunter.Challenge_Stunning_Hunter',
                'ChallengeCompletionValue': 50},
            "03A1382643FC39C99F58C6BB3FF4DB05": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_LMGCompensator_Hunter.Challenge_LMGCompensator_Hunter',
                'ChallengeCompletionValue': 3},
            "85C7B811415DA97C04FB609BE76ACDF0": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_LMGCompensator_Hunter.Challenge_LMGCompensator_Hunter',
                'ChallengeCompletionValue': 8},
            "A1F03DFD49F4100C2153CEAAF8EAF151": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_LMGCompensator_Hunter.Challenge_LMGCompensator_Hunter',
                'ChallengeCompletionValue': 30},
            "4583917643CA36A950C56CA0FD5EBD82": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_BiggerClipperLMG_Hunter.Challenge_BiggerClipperLMG_Hunter',
                'ChallengeCompletionValue': 350},
            "2BBECCBD478778B7D2A1B0AED3E46150": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_BiggerClipperAutoShotgun_Hunter.Challenge_BiggerClipperAutoShotgun_Hunter',
                'ChallengeCompletionValue': 100},
            "2A5C401C49DE3F36D0D999983B2C5D98": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_BiggerClipperHuntingShotgun_Hunter.Challenge_BiggerClipperHuntingShotgun_Hunter',
                'ChallengeCompletionValue': 125},
            "15317A48494297C052E6EFBB3DA122BF": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_ExtraToppings_Hunter.Challenge_ExtraToppings_Hunter',
                'ChallengeCompletionValue': 15},
            "D80A9221429E0A5FCD91DCB002D73482": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_ExtraToppings_Hunter.Challenge_ExtraToppings_Hunter',
                'ChallengeCompletionValue': 38},
            "1D23B53D43864CD2CA8F1990B011DB16": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_ExtraToppings_Hunter.Challenge_ExtraToppings_Hunter',
                'ChallengeCompletionValue': 150},
            "5129E6EE4DC7B2DCDF3C96A8E80910F3": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_OverTheEdge_Hunter.Challenge_OverTheEdge_Hunter',
                'ChallengeCompletionValue': 50},
            "66E774454A815AE6E2A7FEA0B502ACD7": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_OverTheEdge_Hunter.Challenge_OverTheEdge_Hunter',
                'ChallengeCompletionValue': 125},
            "676FAE5145065F8BBA15679F1E969C2B": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_OverTheEdge_Hunter.Challenge_OverTheEdge_Hunter',
                'ChallengeCompletionValue': 500},
            "674BB4C7477253BA116C8CBE079E27D6": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_PowerBoosterMines_Hunter.Challenge_PowerBoosterMines_Hunter',
                'ChallengeCompletionValue': 20},
            "15EA674043E212F8616A059D5297CB35": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_PowerBoosterMines_Hunter.Challenge_PowerBoosterMines_Hunter',
                'ChallengeCompletionValue': 50},
            "F2C4067544A6B04B10FF6CB2C404BB55": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_PowerBoosterMines_Hunter.Challenge_PowerBoosterMines_Hunter',
                'ChallengeCompletionValue': 200},
            "E9C46086458C98543BBA0790979E1DF4": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_StaminaFreak_Hunter.Challenge_StaminaFreak_Hunter',
                'ChallengeCompletionValue': 50},
            "FA07B43A4338C9246A1B02A7EED39599": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_StaminaFreak_Hunter.Challenge_StaminaFreak_Hunter',
                'ChallengeCompletionValue': 125},
            "DAFFE67D41200269194C65B9BCD7F32D": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_StaminaFreak_Hunter.Challenge_StaminaFreak_Hunter',
                'ChallengeCompletionValue': 500},
            "AA2DE101478F3F59FBCA7C9B67EB8280": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_ChanceToActivateNearbyDrone_Hunter.Challenge_ChanceToActivateNearbyDrone_Hunter',
                'ChallengeCompletionValue': 5},
            "049CDB464DF3A69EA626BF9593DF01F8": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_ChanceToActivateNearbyDrone_Hunter.Challenge_ChanceToActivateNearbyDrone_Hunter',
                'ChallengeCompletionValue': 13},
            "E4A92BE94DA6CA174AD3F282FA512BA1": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_ChanceToActivateNearbyDrone_Hunter.Challenge_ChanceToActivateNearbyDrone_Hunter',
                'ChallengeCompletionValue': 50},
            "2F143F5E4568F315134B928703F5E5D8": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_DroneReactivationTime_Hunter.Challenge_DroneReactivationTime_Hunter',
                'ChallengeCompletionValue': 30},
            "F2A11BEC42ED900D1C8F10B90B7D658B": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_DroneReactivationTime_Hunter.Challenge_DroneReactivationTime_Hunter',
                'ChallengeCompletionValue': 75},
            "2AFA685143848895C024E1B3AF427DE1": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_DroneReactivationTime_Hunter.Challenge_DroneReactivationTime_Hunter',
                'ChallengeCompletionValue': 300},
            "C327A6394A86400943197881CFF49AD8": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_DroneShield_Hunter.Challenge_DroneShield_Hunter',
                'ChallengeCompletionValue': 15},
            "5B9ED08049C7E6777E231D84F4EDBC91": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_DroneShield_Hunter.Challenge_DroneShield_Hunter',
                'ChallengeCompletionValue': 38},
            "229F8DD3420F6E79CBBC5D87FD40243F": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_DroneShield_Hunter.Challenge_DroneShield_Hunter',
                'ChallengeCompletionValue': 150},
            "C3CEEED74144161D420801B656C5BB8D": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_ExplosiveRangeIncreased_Hunter.Challenge_ExplosiveRangeIncreased_Hunter',
                'ChallengeCompletionValue': 3},
            "FF4AA7174BA721EA6B449AA8D7D2B70C": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_ExplosiveRangeIncreased_Hunter.Challenge_ExplosiveRangeIncreased_Hunter',
                'ChallengeCompletionValue': 8},
            "E32CC16A47F9C290EC993696079BB6DC": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_ExplosiveRangeIncreased_Hunter.Challenge_ExplosiveRangeIncreased_Hunter',
                'ChallengeCompletionValue': 30},
            "0EAEAA3C494F4F47A35AF885FDAD8939": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_HackedCratesExplode_Hunter.Challenge_HackedCratesExplode_Hunter',
                'ChallengeCompletionValue': 120},
            "43AB4B234479F0002C8D798F583CF6F4": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_HackedCratesExplode_Hunter.Challenge_HackedCratesExplode_Hunter',
                'ChallengeCompletionValue': 300},
            "0DEBB34141DD7D719EE5C199707ED8E4": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_HackedCratesExplode_Hunter.Challenge_HackedCratesExplode_Hunter',
                'ChallengeCompletionValue': 1200},
            "0C7FE4CB479408600F00EDB83279C7D2": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_PowerBoosterOrbital_Hunter.Challenge_PowerBoosterOrbital_Hunter',
                'ChallengeCompletionValue': 10},
            "4C48C95A4ED425708F038591BC28446D": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_PowerBoosterOrbital_Hunter.Challenge_PowerBoosterOrbital_Hunter',
                'ChallengeCompletionValue': 25},
            "4A63E56745F10564D6111EABB309C47C": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_PowerBoosterOrbital_Hunter.Challenge_PowerBoosterOrbital_Hunter',
                'ChallengeCompletionValue': 100},
            "AA290B6544528300C0B85A9A6B3FB6F7": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Fade_Hunter.Challenge_Fade_Hunter',
                'ChallengeCompletionValue': 30},
            "21B04F8E4D93BAE9A3550190FF918AD7": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Fade_Hunter.Challenge_Fade_Hunter',
                'ChallengeCompletionValue': 75},
            "589168EA42DE8131A4611ABD189B1EEF": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Fade_Hunter.Challenge_Fade_Hunter',
                'ChallengeCompletionValue': 300},
            "50EF445E456459E224013C8E2B24A336": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Mines_Hunter.Challenge_Mines_Hunter',
                'ChallengeCompletionValue': 3},
            "45D437BD4AD85F9477DD5593AAE9130F": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Mines_Hunter.Challenge_Mines_Hunter',
                'ChallengeCompletionValue': 8},
            "ABCDD5744A0CB60A8F40FEABD293FE18": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Mines_Hunter.Challenge_Mines_Hunter',
                'ChallengeCompletionValue': 30},
            "9D59DA354BB511D4C7EE64B60B546A1B": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_OrbitalStrike_Hunter.Challenge_OrbitalStrike_Hunter',
                'ChallengeCompletionValue': 15},
            "FCB391DA4DAD486C8E31EABAE21EB19A": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_OrbitalStrike_Hunter.Challenge_OrbitalStrike_Hunter',
                'ChallengeCompletionValue': 80},
            "508182E842C9BEFA20BE5488083716CC": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_OrbitalStrike_Hunter.Challenge_OrbitalStrike_Hunter',
                'ChallengeCompletionValue': 150},
            "A1DFB20F48B76A509B424599E30F8A0E": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Turrets_Hunter.Challenge_Turrets_Hunter',
                'ChallengeCompletionValue': 150},
            "F13B9B0F4BF97BB9C7023F90EF1C0594": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Turrets_Hunter.Challenge_Turrets_Hunter',
                'ChallengeCompletionValue': 375},
            "EDED745B4523ADC54CD950BD8B238F6B": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Turrets_Hunter.Challenge_Turrets_Hunter',
                'ChallengeCompletionValue': 1500},
            "87A39D494DF78A55D012B4BCA091E043": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SpendAmmo_AssaultRifle_Hunter.Challenge_SpendAmmo_AssaultRifle_Hunter',
                'ChallengeCompletionValue': 210},
            "164FAA5D41B127B316ABAD9E7DAAD674": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Shoot_AssaultRifle_Hunter.Challenge_Shoot_AssaultRifle_Hunter',
                'ChallengeCompletionValue': 200},
            "9F8EE83B438410496374ADA522F55713": {
                'challengeBlueprint': '/Game/Challenges/Progression/General/Challenge_Damage_Hunter.Challenge_Damage_Hunter',
                'ChallengeCompletionValue': 12000},
            "997A3A384F8156F76E9405ABA503DDEE": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SpendAmmo_AutoShotgun_Hunter.Challenge_SpendAmmo_AutoShotgun_Hunter',
                'ChallengeCompletionValue': 50},
            "D686CACE4B3C6C55F5BD9A80177D12AE": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Shoot_AutoShotgun_Hunter.Challenge_Shoot_AutoShotgun_Hunter',
                'ChallengeCompletionValue': 130},
            "C987A00C4AB705897336E1A84899264B": {
                'challengeBlueprint': '/Game/Challenges/Progression/General/Challenge_Damage_Hunter.Challenge_Damage_Hunter',
                'ChallengeCompletionValue': 12000},
            "1FD7D2EB4616FC6F475D58AA8AF7F93B": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SpendAmmo_AutoShotgun_Hunter.Challenge_SpendAmmo_AutoShotgun_Hunter',
                'ChallengeCompletionValue': 50},
            "72718B874504A50CD3FA4385FB5523FF": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Shoot_AutoShotgun_Hunter.Challenge_Shoot_AutoShotgun_Hunter',
                'ChallengeCompletionValue': 130},
            "FA8F508E40A808178CE740940F817554": {
                'challengeBlueprint': '/Game/Challenges/Progression/General/Challenge_Damage_Hunter.Challenge_Damage_Hunter',
                'ChallengeCompletionValue': 12000},
            "FDC959494B25E5982F050DAE6D312DF2": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SpendAmmo_AutoSniper_Hunter.Challenge_SpendAmmo_AutoSniper_Hunter',
                'ChallengeCompletionValue': 60},
            "4D5CCA7D42CD770262551591FB8D1C62": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Shoot_AutoSniper_Hunter.Challenge_Shoot_AutoSniper_Hunter',
                'ChallengeCompletionValue': 80},
            "8D8F602F4D0BFDE7B2A884A97D88F169": {
                'challengeBlueprint': '/Game/Challenges/Progression/General/Challenge_Damage_Hunter.Challenge_Damage_Hunter',
                'ChallengeCompletionValue': 12000},
            "702074B04572D0ECF67FA9BF1AE5DD7E": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SpendAmmo_AutoSniperGuardian_Hunter.Challenge_SpendAmmo_AutoSniperGuardian_Hunter',
                'ChallengeCompletionValue': 60},
            "ADA907B24D8DCBD28848F18B6D15FF57": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Shoot_AutoSniper_Hunter.Challenge_Shoot_AutoSniper_Hunter',
                'ChallengeCompletionValue': 80},
            "9B3DF194466FF239257F1289F7BC4A71": {
                'challengeBlueprint': '/Game/Challenges/Progression/General/Challenge_Damage_Hunter.Challenge_Damage_Hunter',
                'ChallengeCompletionValue': 12000},
            "6E327F42491E3FC4FF0A77A0ECFDBF09": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SpendAmmo_BurstRifle_Hunter.Challenge_SpendAmmo_BurstRifle_Hunter',
                'ChallengeCompletionValue': 180},
            "F40221D745C692533271C3BDD63633A1": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Shoot_BurstRifle_Hunter.Challenge_Shoot_BurstRifle_Hunter',
                'ChallengeCompletionValue': 160},
            "0FFB7F6A41EBE9C6DB89108D46762F53": {
                'challengeBlueprint': '/Game/Challenges/Progression/General/Challenge_Damage_Hunter.Challenge_Damage_Hunter',
                'ChallengeCompletionValue': 12000},
            "F62DA5304F26F2F0FCDFFCB7DBA45398": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SpendAmmo_BurstRifleInquisitor_Hunter.Challenge_SpendAmmo_BurstRifleInquisitor_Hunter',
                'ChallengeCompletionValue': 180},
            "7F3CF15A48BE7AE1948698A7BD718D2E": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Shoot_BurstRifle_Hunter.Challenge_Shoot_BurstRifle_Hunter',
                'ChallengeCompletionValue': 160},
            "BC7EB2484D54F89131082FBCEDB1F34C": {
                'challengeBlueprint': '/Game/Challenges/Progression/General/Challenge_Damage_Hunter.Challenge_Damage_Hunter',
                'ChallengeCompletionValue': 12000},
            "77B930CE49352D062CCBD0A27C8E0F0A": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SpendAmmo_DefaultShotgun_Hunter.Challenge_SpendAmmo_DefaultShotgun_Hunter',
                'ChallengeCompletionValue': 60},
            "DB625B8B415DE703C5DB0698D1969A8E": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Shoot_DefaultShotgun_Hunter.Challenge_Shoot_DefaultShotgun_Hunter',
                'ChallengeCompletionValue': 120},
            "A26AB1694E2CC8669D08CD8E5F4F64BE": {
                'challengeBlueprint': '/Game/Challenges/Progression/General/Challenge_Damage_Hunter.Challenge_Damage_Hunter',
                'ChallengeCompletionValue': 12000},
            "6049D85045161D075666E18DE4AFC772": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SpendAmmo_DefaultSniper_Hunter.Challenge_SpendAmmo_DefaultSniper_Hunter',
                'ChallengeCompletionValue': 30},
            "6B20937348A89A1A9E6CCB9EE09FC4DA": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Shoot_DefaultSniper_Hunter.Challenge_Shoot_DefaultSniper_Hunter',
                'ChallengeCompletionValue': 40},
            "2675258345FC8734A6CB0E98E02DE88A": {
                'challengeBlueprint': '/Game/Challenges/Progression/General/Challenge_Damage_Hunter.Challenge_Damage_Hunter',
                'ChallengeCompletionValue': 12000},
            "00C0407C47E60CDB558C67B153E75DB6": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SpendAmmo_GrenadeLauncher_Hunter.Challenge_SpendAmmo_GrenadeLauncher_Hunter',
                'ChallengeCompletionValue': 60},
            "4246C6904E8F91584CE55885C633683E": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Shoot_GrenadeLauncher_Hunter.Challenge_Shoot_GrenadeLauncher_Hunter',
                'ChallengeCompletionValue': 80},
            "9EFF069F492B3251D37FCD9BB813523C": {
                'challengeBlueprint': '/Game/Challenges/Progression/General/Challenge_Damage_Hunter.Challenge_Damage_Hunter',
                'ChallengeCompletionValue': 15000},
            "E3F005244D6BE2A392382F8CA270474F": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SpendAmmo_LMG_Hunter.Challenge_SpendAmmo_LMG_Hunter',
                'ChallengeCompletionValue': 300},
            "4555B2C545C8B41867FB9299306D3108": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Shoot_LMG_Hunter.Challenge_Shoot_LMG_Hunter',
                'ChallengeCompletionValue': 300},
            "FB6DFDE94DAE90B29C20F7A65FD4D050": {
                'challengeBlueprint': '/Game/Challenges/Progression/General/Challenge_Damage_Hunter.Challenge_Damage_Hunter',
                'ChallengeCompletionValue': 12000},
            "AC14BF3547AB708F0D50C58C5440CFEB": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SpendAmmo_HuntingShotgun_Hunter.Challenge_SpendAmmo_HuntingShotgun_Hunter',
                'ChallengeCompletionValue': 50},
            "72A784C644E05E2631AB88883C1A11B1": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Shoot_HuntingShotgin_Hunter.Challenge_Shoot_HuntingShotgin_Hunter',
                'ChallengeCompletionValue': 110},
            "D33B49BB4F79DE0F6E39BD94DA15FA23": {
                'challengeBlueprint': '/Game/Challenges/Progression/General/Challenge_Damage_Hunter.Challenge_Damage_Hunter',
                'ChallengeCompletionValue': 12000},
            "FBA3C3F3458AAD1B6D8199AF1451FE45": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SpendAmmo_Carbine_Hunter.Challenge_SpendAmmo_Carbine_Hunter',
                'ChallengeCompletionValue': 60},
            "3E4613F84B59697E68DE42A3B0E5F4CB": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Shoot_Carbine_Hunter.Challenge_Shoot_Carbine_Hunter',
                'ChallengeCompletionValue': 80},
            "9953E63E44CB478CAD903D82263F72B8": {
                'challengeBlueprint': '/Game/Challenges/Progression/General/Challenge_Damage_Hunter.Challenge_Damage_Hunter',
                'ChallengeCompletionValue': 12000},
            "86F2BDF74F433C03F8FE62B5C5F47AF9": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_EvadeMaster_Runner.Challenge_EvadeMaster_Runner',
                'ChallengeCompletionValue': 50},
            "CDE15380452E06616D377190D2028AB7": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_EvadeMaster_Runner.Challenge_EvadeMaster_Runner',
                'ChallengeCompletionValue': 125},
            "D880BF184B480D714667688CC4D9D6C0": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_EvadeMaster_Runner.Challenge_EvadeMaster_Runner',
                'ChallengeCompletionValue': 500},
            "69371CA0409766B1F0DAAC80A900893A": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_HerdMentality_Runner.Challenge_HerdMentality_Runner',
                'ChallengeCompletionValue': 45},
            "C8C05D874477C9A9413F9F9BF6BB29E8": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_HerdMentality_Runner.Challenge_HerdMentality_Runner',
                'ChallengeCompletionValue': 113},
            "49C135BD4F919597CF8D3D99F5FC3E79": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_HerdMentality_Runner.Challenge_HerdMentality_Runner',
                'ChallengeCompletionValue': 450},
            "ACE6AD4440EFB8606FAC8282301CDBF5": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SizeMatters_Runner.Challenge_SizeMatters_Runner',
                'ChallengeCompletionValue': 5},
            "6F499FE24C36B15740613AB3200B5B4B": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SizeMatters_Runner.Challenge_SizeMatters_Runner',
                'ChallengeCompletionValue': 13},
            "CC8DAF104B0229ADA48CF4A6784CC03A": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SizeMatters_Runner.Challenge_SizeMatters_Runner',
                'ChallengeCompletionValue': 50},
            "21CBC39E4B2D8C37439881A5879570EC": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SuddenInsight_Runner.Challenge_SuddenInsight_Runner',
                'ChallengeCompletionValue': 15},
            "9BB2D0A04B6B168325E9A080E84EBD05": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SuddenInsight_Runner.Challenge_SuddenInsight_Runner',
                'ChallengeCompletionValue': 38},
            "CF6113864077974B00CD37B51736426B": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SuddenInsight_Runner.Challenge_SuddenInsight_Runner',
                'ChallengeCompletionValue': 150},
            "608464EC41965D826856CEA1174CD757": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_ToilTogether_Runner.Challenge_ToilTogether_Runner',
                'ChallengeCompletionValue': 10},
            "59DCADA849BC53D93DD04D9D63EF6351": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_ToilTogether_Runner.Challenge_ToilTogether_Runner',
                'ChallengeCompletionValue': 25},
            "1D4401744D1CCCF2CE52628E0A6929A2": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_ToilTogether_Runner.Challenge_ToilTogether_Runner',
                'ChallengeCompletionValue': 100},
            "1E01EC5A44B1016ED59E0ABD6C2FAF60": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_TreasureHunter_Runner.Challenge_TreasureHunter_Runner',
                'ChallengeCompletionValue': 30},
            "153C237F41FFA085A7114795F0DB33FC": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_TreasureHunter_Runner.Challenge_TreasureHunter_Runner',
                'ChallengeCompletionValue': 75},
            "164B28054A2E2DAEC8BF5C820AF4B9B2": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_TreasureHunter_Runner.Challenge_TreasureHunter_Runner',
                'ChallengeCompletionValue': 300},
            "9878CAFC405F96494869F5AE145254FC": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_ChanceToNotSpendAmmo_Runner.Challenge_ChanceToNotSpendAmmo_Runner',
                'ChallengeCompletionValue': 10},
            "067F39B3487120E9110DFFA181AB78B3": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_ChanceToNotSpendAmmo_Runner.Challenge_ChanceToNotSpendAmmo_Runner',
                'ChallengeCompletionValue': 25},
            "89444BC84AA08F43E29B4DA1EB983561": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_ChanceToNotSpendAmmo_Runner.Challenge_ChanceToNotSpendAmmo_Runner',
                'ChallengeCompletionValue': 100},
            "AA0018EC4461BE055CF7428554EC046F": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_DamageResistWhenRevealed_Runner.Challenge_DamageResistWhenRevealed_Runner',
                'ChallengeCompletionValue': 100},
            "A6941C2F42077160B5FFF49887ABD46C": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_DamageResistWhenRevealed_Runner.Challenge_DamageResistWhenRevealed_Runner',
                'ChallengeCompletionValue': 250},
            "8CD20AD04CCF051497216F84AF29A327": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_DamageResistWhenRevealed_Runner.Challenge_DamageResistWhenRevealed_Runner',
                'ChallengeCompletionValue': 1000},
            "15BAB1914646A660541129B61394D930": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_FasterBloodDeliver_Runner.Challenge_FasterBloodDeliver_Runner',
                'ChallengeCompletionValue': 20},
            "6F9FFCE24EE28E24EEF4C69E8FF69F99": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_FasterBloodDeliver_Runner.Challenge_FasterBloodDeliver_Runner',
                'ChallengeCompletionValue': 50},
            "A75399654B2523F75B30BAA3704B5898": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_FasterBloodDeliver_Runner.Challenge_FasterBloodDeliver_Runner',
                'ChallengeCompletionValue': 200},
            "0A27212D496448FD389A1DA525E284CE": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_InteractSpeedImprovement_Runner.Challenge_InteractSpeedImprovement_Runner',
                'ChallengeCompletionValue': 50},
            "919AD6964781C5FFED35F19DF9CB5560": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_InteractSpeedImprovement_Runner.Challenge_InteractSpeedImprovement_Runner',
                'ChallengeCompletionValue': 125},
            "E8ED480C4FAD11C001A840AA53B55B4F": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_InteractSpeedImprovement_Runner.Challenge_InteractSpeedImprovement_Runner',
                'ChallengeCompletionValue': 500},
            "C08D9F6B4F6414A99BDB569495AA0A9B": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_StaminaRegenDamaged_Runner.Challenge_StaminaRegenDamaged_Runner',
                'ChallengeCompletionValue': 3},
            "35368570459015AD1FD2F9A209909515": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_StaminaRegenDamaged_Runner.Challenge_StaminaRegenDamaged_Runner',
                'ChallengeCompletionValue': 8},
            "46B1491D436AEBB823247297F4943066": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_StaminaRegenDamaged_Runner.Challenge_StaminaRegenDamaged_Runner',
                'ChallengeCompletionValue': 30},
            "734B85884E566BD13FD2BDA148F6055C": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_StaminaRegenReveal_Runner.Challenge_StaminaRegenReveal_Runner',
                'ChallengeCompletionValue': 5},
            "E7B6132F461D5850A8D0738D87D54C0A": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_StaminaRegenReveal_Runner.Challenge_StaminaRegenReveal_Runner',
                'ChallengeCompletionValue': 13},
            "310D7A264DC6FD62F67B3BAFE2E6876B": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_StaminaRegenReveal_Runner.Challenge_StaminaRegenReveal_Runner',
                'ChallengeCompletionValue': 50},
            "B4B156CC47C8D987B9BDBEB910B12C9E": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_AmmoOpportunist_Runner.Challenge_AmmoOpportunist_Runner',
                'ChallengeCompletionValue': 60},
            "15C925544AA67E20214C8AB09F5B33E9": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_AmmoOpportunist_Runner.Challenge_AmmoOpportunist_Runner',
                'ChallengeCompletionValue': 150},
            "950524C144BE794AABFFED8142C119B4": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_AmmoOpportunist_Runner.Challenge_AmmoOpportunist_Runner',
                'ChallengeCompletionValue': 600},
            "F2D57F3443BF0F1A162ED8AF80A509D7": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Emboldened_Runner.Challenge_Emboldened_Runner',
                'ChallengeCompletionValue': 5},
            "AF8CBA94413BCED1445D269F99D3F747": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Emboldened_Runner.Challenge_Emboldened_Runner',
                'ChallengeCompletionValue': 13},
            "885A5CBE4C36F665FA3296ABDD81D610": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Emboldened_Runner.Challenge_Emboldened_Runner',
                'ChallengeCompletionValue': 50},
            "FD314A694D049989202D01BC36269F44": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_FleetFeet_Runner.Challenge_FleetFeet_Runner',
                'ChallengeCompletionValue': 150},
            "0A728AD54AF5EAB6CB4356A074F01C1B": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_FleetFeet_Runner.Challenge_FleetFeet_Runner',
                'ChallengeCompletionValue': 375},
            "688EC1704C4EA4BCB18181ADE23E2C3D": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_FleetFeet_Runner.Challenge_FleetFeet_Runner',
                'ChallengeCompletionValue': 1500},
            "4F99C43949B5CAC87BCEB4877B7FAB64": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_HeatOfTheMoment_Runner.Challenge_HeatOfTheMoment_Runner',
                'ChallengeCompletionValue': 60},
            "2ABDC29A4D174CDC114AEBACB898927E": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_HeatOfTheMoment_Runner.Challenge_HeatOfTheMoment_Runner',
                'ChallengeCompletionValue': 150},
            "37B650F145BF27B3B670CB9D84D58111": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_HeatOfTheMoment_Runner.Challenge_HeatOfTheMoment_Runner',
                'ChallengeCompletionValue': 600},
            "B0B11BDC4AF524274D6171A8BF605CF8": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SharingIsCaring_Runner.Challenge_SharingIsCaring_Runner',
                'ChallengeCompletionValue': 5},
            "9A0964D947748E6C0338AA9684DF1055": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SharingIsCaring_Runner.Challenge_SharingIsCaring_Runner',
                'ChallengeCompletionValue': 13},
            "22B70F5B49B3973D84DD9E9E621987BC": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SharingIsCaring_Runner.Challenge_SharingIsCaring_Runner',
                'ChallengeCompletionValue': 50},
            "ECCBA78D4055676F9C17D79B9D5FA2D4": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Shimmy_Runner.Challenge_Shimmy_Runner',
                'ChallengeCompletionValue': 250},
            "6CAD2AAC4C56C1224448C599A0E16119": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Shimmy_Runner.Challenge_Shimmy_Runner',
                'ChallengeCompletionValue': 625},
            "B54522334820602C6E998D9FD7E785BA": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Shimmy_Runner.Challenge_Shimmy_Runner',
                'ChallengeCompletionValue': 2500},
            "EE05AA53420DF8C7E43A1EACB7C407FE": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_ClingWrap_Runner.Challenge_ClingWrap_Runner',
                'ChallengeCompletionValue': 10},
            "AACEE7044F69CED52B10F0AF6C70D433": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_ClingWrap_Runner.Challenge_ClingWrap_Runner',
                'ChallengeCompletionValue': 25},
            "B2B903254EB0C6ADAD59599C40A3C5FE": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_ClingWrap_Runner.Challenge_ClingWrap_Runner',
                'ChallengeCompletionValue': 100},
            "8DF21FE8442BD778190141A9C9E06BC6": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_DamageDodger_Runner.Challenge_DamageDodger_Runner',
                'ChallengeCompletionValue': 20},
            "9053883B41EBC8D6A9A8CA809D02845A": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_DamageDodger_Runner.Challenge_DamageDodger_Runner',
                'ChallengeCompletionValue': 50},
            "B48B9B9743994F0AA12B82BAF69AE738": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_DamageDodger_Runner.Challenge_DamageDodger_Runner',
                'ChallengeCompletionValue': 200},
            "FB53A7E442EA53EA5727E4BA3611F45C": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_KeepHangingOn_Runner.Challenge_KeepHangingOn_Runner',
                'ChallengeCompletionValue': 20},
            "A45C7DF44353DDAAF58F1EB1CAF954FF": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_KeepHangingOn_Runner.Challenge_KeepHangingOn_Runner',
                'ChallengeCompletionValue': 50},
            "C3C6528F4CA1D3D4B34235968746C223": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_KeepHangingOn_Runner.Challenge_KeepHangingOn_Runner',
                'ChallengeCompletionValue': 200},
            "FD1AA64E41BA2576DBF566B436C256C6": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_ObjectiveMaster_Runner.Challenge_ObjectiveMaster_Runner',
                'ChallengeCompletionValue': 25},
            "356CFA3942F21C3B64160D9942DF1C52": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_ObjectiveMaster_Runner.Challenge_ObjectiveMaster_Runner',
                'ChallengeCompletionValue': 63},
            "AB8313E24DFB01401DEF5E92219A8965": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_ObjectiveMaster_Runner.Challenge_ObjectiveMaster_Runner',
                'ChallengeCompletionValue': 250},
            "0AE15B56425FB92D3301D9932FED9D74": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Resting_Runner.Challenge_Resting_Runner',
                'ChallengeCompletionValue': 90},
            "831999A04EEA4635762B8A8606F0D4DD": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Resting_Runner.Challenge_Resting_Runner',
                'ChallengeCompletionValue': 225},
            "24424E874589E3D4582EF198EE7D1E42": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Resting_Runner.Challenge_Resting_Runner',
                'ChallengeCompletionValue': 900},
            "269DDC2D41013F0AD817C4ACA0BA139C": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_StayingAlive_Runner.Challenge_StayingAlive_Runner',
                'ChallengeCompletionValue': 1},
            "2C4E3AB94438A43C81D515815ACB4C9D": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_StayingAlive_Runner.Challenge_StayingAlive_Runner',
                'ChallengeCompletionValue': 3},
            "EFAA2DFC4C3AAEE70EB32697013003D7": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_StayingAlive_Runner.Challenge_StayingAlive_Runner',
                'ChallengeCompletionValue': 10},
            "786DF18B48F5D69CA1BD558B5240A2EA": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Firmware_Runner.Challenge_Firmware_Runner',
                'ChallengeCompletionValue': 1},
            "AC2C19A94926471049C06DA3C519ADE9": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Firmware_Runner.Challenge_Firmware_Runner',
                'ChallengeCompletionValue': 3},
            "C78F353F40FF62E7298ECD94086D78D7": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Firmware_Runner.Challenge_Firmware_Runner',
                'ChallengeCompletionValue': 10},
            "0C5A99E44EDD7325ED5BC687F75374DE": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_LuckyCharm_Runner.Challenge_LuckyCharm_Runner',
                'ChallengeCompletionValue': 4},
            "E239202F452ED0540F4479AFF248A3D4": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_LuckyCharm_Runner.Challenge_LuckyCharm_Runner',
                'ChallengeCompletionValue': 10},
            "6F53D959409C9C2740F6789E221BCECF": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_LuckyCharm_Runner.Challenge_LuckyCharm_Runner',
                'ChallengeCompletionValue': 40},
            "F34255F3443EB1429FCA809DF2DFA012": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_OcularImplants_Runner.Challenge_OcularImplants_Runner',
                'ChallengeCompletionValue': 15},
            "8BFB3FCD4432176BAAFB90BF65EB6165": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_OcularImplants_Runner.Challenge_OcularImplants_Runner',
                'ChallengeCompletionValue': 38},
            "F531602641251AEE39C024B3F85845FD": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_OcularImplants_Runner.Challenge_OcularImplants_Runner',
                'ChallengeCompletionValue': 150},
            "23F0E5E7497912D11C520EA86348C114": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_RichGetRicher_Runner.Challenge_RichGetRicher_Runner',
                'ChallengeCompletionValue': 40},
            "0D884DA743B3AFAA884DD3B7CFF0364D": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_RichGetRicher_Runner.Challenge_RichGetRicher_Runner',
                'ChallengeCompletionValue': 100},
            "99B40C044F75D1324B48DCA4FAC3D5DF": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_RichGetRicher_Runner.Challenge_RichGetRicher_Runner',
                'ChallengeCompletionValue': 400},
            "2D233F9F4106D8660D3D5D997E68EC0F": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Sniper_Runner.Challenge_Sniper_Runner',
                'ChallengeCompletionValue': 15},
            "7673C2D347769AAB0539D1B57E0928E3": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Sniper_Runner.Challenge_Sniper_Runner',
                'ChallengeCompletionValue': 38},
            "75885A2644B01B3CCA579E8B86159713": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Sniper_Runner.Challenge_Sniper_Runner',
                'ChallengeCompletionValue': 150},
            "444383D34E12F314623320B0E23CA691": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_ZeroCool_Runner.Challenge_ZeroCool_Runner',
                'ChallengeCompletionValue': 1},
            "EBF333814F32313057BC0AA50BF880FC": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_ZeroCool_Runner.Challenge_ZeroCool_Runner',
                'ChallengeCompletionValue': 3},
            "55B032B147384D04065B39A0CC5D825D": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_ZeroCool_Runner.Challenge_ZeroCool_Runner',
                'ChallengeCompletionValue': 10},
            "DC70D1B746AF456C71FB29BFB27F356E": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Cardio_Runner.Challenge_Cardio_Runner',
                'ChallengeCompletionValue': 15},
            "A00E590E4EB9F479ACE7BD852BCBA78C": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Cardio_Runner.Challenge_Cardio_Runner',
                'ChallengeCompletionValue': 38},
            "A734774F4E6162C9A60C4B9D537D0723": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Cardio_Runner.Challenge_Cardio_Runner',
                'ChallengeCompletionValue': 150},
            "D6C518B242C0F5C6ABDB32984C0970EF": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_FriendsForLife_Runner.Challenge_FriendsForLife_Runner',
                'ChallengeCompletionValue': 10},
            "35898FD44E80FD68376F67A560E815BC": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_FriendsForLife_Runner.Challenge_FriendsForLife_Runner',
                'ChallengeCompletionValue': 25},
            "E1BB40D145181323071EBBAAC924E4F5": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_FriendsForLife_Runner.Challenge_FriendsForLife_Runner',
                'ChallengeCompletionValue': 100},
            "CA2FE47E45EE792DFA26FFA3A30FC0A3": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_HealFaster_Runner.Challenge_HealFaster_Runner',
                'ChallengeCompletionValue': 60},
            "0E514F8A467DB3E7DEBF99ABAC2313A0": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_HealFaster_Runner.Challenge_HealFaster_Runner',
                'ChallengeCompletionValue': 150},
            "DE92510443074D9DB518B7A93A3A2FD9": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_HealFaster_Runner.Challenge_HealFaster_Runner',
                'ChallengeCompletionValue': 600},
            "6AD7B28E48E611BDAD2386940B2790AA": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SecurityBlanket_Runner.Challenge_SecurityBlanket_Runner',
                'ChallengeCompletionValue': 40},
            "5E5F70254373FB5C274AD9BA59A49E32": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SecurityBlanket_Runner.Challenge_SecurityBlanket_Runner',
                'ChallengeCompletionValue': 100},
            "9A5FDE8841D953C38AA5BBB47EEFB01D": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SecurityBlanket_Runner.Challenge_SecurityBlanket_Runner',
                'ChallengeCompletionValue': 400},
            "27A4E81B472948ED80142E8E6749F979": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Splash_Runner.Challenge_Splash_Runner',
                'ChallengeCompletionValue': 3},
            "99A6BD974F814624352257B2DDAAC3B7": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Splash_Runner.Challenge_Splash_Runner',
                'ChallengeCompletionValue': 8},
            "2CE18C86481989D772300DAD6D054A0C": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Splash_Runner.Challenge_Splash_Runner',
                'ChallengeCompletionValue': 30},
            "D635E5CE4EEF85664D87F490CF01B01E": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_UnderFoot_Runner.Challenge_UnderFoot_Runner',
                'ChallengeCompletionValue': 15},
            "44EA40CE43D410AF19A687A993EF7EBC": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_UnderFoot_Runner.Challenge_UnderFoot_Runner',
                'ChallengeCompletionValue': 38},
            "B5F0CB894653B2C56CED9E92C7BB1251": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_UnderFoot_Runner.Challenge_UnderFoot_Runner',
                'ChallengeCompletionValue': 150},
            "C40789F0410D07A6DFACCBB46A28EACB": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Invisibility_Runner.Challenge_Invisibility_Runner',
                'ChallengeCompletionValue': 10},
            "8894F68B4549F8F096812AB6896D48AC": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Invisibility_Runner.Challenge_Invisibility_Runner',
                'ChallengeCompletionValue': 25},
            "AC5CED5D4D2F28952117F0B0EA0085E3": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Invisibility_Runner.Challenge_Invisibility_Runner',
                'ChallengeCompletionValue': 100},
            "48769C24490AE4488D7CCD906E283EEB": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SpeedArrow_Runner.Challenge_SpeedArrow_Runner',
                'ChallengeCompletionValue': 300},
            "82033B9F4033D82B4392779F3A986F09": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SpeedArrow_Runner.Challenge_SpeedArrow_Runner',
                'ChallengeCompletionValue': 750},
            "6246612A483F1C1D0D9AD48568591FDB": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SpeedArrow_Runner.Challenge_SpeedArrow_Runner',
                'ChallengeCompletionValue': 3000},
            "4D6510D3474A414BE76C95A42D09024C": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Heal_Runner.Challenge_Heal_Runner',
                'ChallengeCompletionValue': 60},
            "8AD5A0194A0528BDC957EFABCFF03CA4": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Heal_Runner.Challenge_Heal_Runner',
                'ChallengeCompletionValue': 600},
            "B78308DF48036BCF914060944AAF4A19": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Heal_Runner.Challenge_Heal_Runner',
                'ChallengeCompletionValue': 600},
            "24CE65364362CB2A90C0E08876176937": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SmokeScreen_Runner.Challenge_SmokeScreen_Runner',
                'ChallengeCompletionValue': 10},
            "6D79A03B4F3E4EDA33FAD69FF55289BA": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SmokeScreen_Runner.Challenge_SmokeScreen_Runner',
                'ChallengeCompletionValue': 25},
            "5B9CCC03408C7B49717192831A9E4288": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SmokeScreen_Runner.Challenge_SmokeScreen_Runner',
                'ChallengeCompletionValue': 100},
            "5D2E6D06498C0F005E0EF78E7580AAA9": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Clone_Runner.Challenge_Clone_Runner',
                'ChallengeCompletionValue': 10},
            "7E173CD547DB59D507CDD492C9F2CB93": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Clone_Runner.Challenge_Clone_Runner',
                'ChallengeCompletionValue': 25},
            "DFA555C7452D8461CD412DA68D4FB301": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Clone_Runner.Challenge_Clone_Runner',
                'ChallengeCompletionValue': 100},
            "499EBA6443A83B4FE1F4F7AFE8EFE66E": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Invisibility_Runner.Challenge_Invisibility_Runner',
                'ChallengeCompletionValue': 10},
            "4212C3604C9FD931278E189EB962B5F1": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Invisibility_Runner.Challenge_Invisibility_Runner',
                'ChallengeCompletionValue': 25},
            "B0CB575B40C95E09484440B04BA36E08": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Invisibility_Runner.Challenge_Invisibility_Runner',
                'ChallengeCompletionValue': 100},
            "FF8996344C73AADD1D2C1C9E26BD23EF": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Invisibility_Runner.Challenge_Invisibility_Runner',
                'ChallengeCompletionValue': 10},
            "2ACEB8984337D2518F010E9337EB656B": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Invisibility_Runner.Challenge_Invisibility_Runner',
                'ChallengeCompletionValue': 25},
            "5879F0FC4892D53FE2195AABA05EDA2A": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Invisibility_Runner.Challenge_Invisibility_Runner',
                'ChallengeCompletionValue': 100},
            "EED2F02B4A55B844E1B682804C84308D": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Shield_Runner.Challenge_Shield_Runner',
                'ChallengeCompletionValue': 10},
            "4A40EFB44EAC4CDEB16D8B8E7D6ECA8F": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Shield_Runner.Challenge_Shield_Runner',
                'ChallengeCompletionValue': 25},
            "92F65520408CBF8F52028FB3D83C6D5A": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Shield_Runner.Challenge_Shield_Runner',
                'ChallengeCompletionValue': 100},
            "F2182D4C49439EEFDB38EAA2F35C5D9C": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Heal_Runner.Challenge_Heal_Runner',
                'ChallengeCompletionValue': 60},
            "83BE1ABF46705544813B42AC257A2A2C": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Heal_Runner.Challenge_Heal_Runner',
                'ChallengeCompletionValue': 600},
            "BE19828E4910DB01722D3384A491DCAD": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Heal_Runner.Challenge_Heal_Runner',
                'ChallengeCompletionValue': 600},
            "0901F162440C086DB4E112956F7E651D": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Shield_Runner.Challenge_Shield_Runner',
                'ChallengeCompletionValue': 10},
            "C6BA901346B618AB770225B3B48D6509": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Shield_Runner.Challenge_Shield_Runner',
                'ChallengeCompletionValue': 25},
            "34F4FE4C4825CB2E34D1CD8ADBF43312": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Shield_Runner.Challenge_Shield_Runner',
                'ChallengeCompletionValue': 100},
            "4BDF4B094F7B2FC939E21CA64F95A749": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Clone_Runner.Challenge_Clone_Runner',
                'ChallengeCompletionValue': 10},
            "D56D259A4F85D29F4F4164B8F27F3BB1": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Clone_Runner.Challenge_Clone_Runner',
                'ChallengeCompletionValue': 25},
            "605347B34E33EFAB829163AF16B6C0FB": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_Clone_Runner.Challenge_Clone_Runner',
                'ChallengeCompletionValue': 100},
            "5E661D664FB8560D3519ECA53BB97ED2": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SmokeScreen_Runner.Challenge_SmokeScreen_Runner',
                'ChallengeCompletionValue': 10},
            "2D426791495793A662D1DBACCFAAE3CC": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SmokeScreen_Runner.Challenge_SmokeScreen_Runner',
                'ChallengeCompletionValue': 25},
            "290112D94B4F60152BAE088F9E942F1F": {
                'challengeBlueprint': '/Game/Challenges/Progression/Challenge_SmokeScreen_Runner.Challenge_SmokeScreen_Runner',
                'ChallengeCompletionValue': 100}
        }
        self.daily_challenges = []
        self.weekly_challenges = []
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
            rt_user_challenge = add_challenge_to_user(user_id, challenge_id)
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

        for challenge in challenges:
            if challenge["challengeId"] not in user_data:
                add_challenge_to_user(userid, challenge["challengeId"], "time")
                update_challenge_time(userid, challenge["challengeId"], challenge_type)
                user_data = mongo.get_data_with_list(login=userid, login_steam=False,
                                                     items={"challengeProgression"})["challengeProgression"]
            else:
                lifetime = get_lifetime(challenge_type)[0]
                if lifetime > user_data[challenge["challengeId"]]["lifetime"]["expirationTime"]:
                    update_challenge_time(userid, challenge["challengeId"], challenge_type)
                    user_data = mongo.get_data_with_list(login=userid, login_steam=False,
                                                         items={"challengeProgression"})["challengeProgression"]
            challenge_data = user_data[challenge["challengeId"]]
            return_data.append({
                "lifetime": challenge_data["lifetime"],
                "challengeType": challenge_type,
                "challengeId": challenge_data["challengeId"],
                "challengeCompletionValue": challenge["ChallengeCompletionValue"],
                "faction": challenge["faction"],
                "challengeBlueprint": challenge["challengeBlueprint"],
                "rewards": [get_reward(challenge["challengeBlueprint"])]
            })
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
        mongo.write_data_with_list(login=user_id, login_steam=False, items={"challengeProgression"}, data=writen_data)





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


new_challenge_handler = ChallengeHandler()
