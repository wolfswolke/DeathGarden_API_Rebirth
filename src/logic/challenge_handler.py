from flask_definitions import *

challenges = [
    {"Challenge_CollectAmmo.Challenge_CollectAmmo": "C2FBC79142A07F76235B75BDAF9338A9"},
    {"Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner": "0527312743FCA3395B2AE6B8E219B25D"},
    {"Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner": "B21D9FC3435A99E660BCE58AEBC91EFF"},
    {"Challenge_Travel_Runner.Challenge_Travel_Runner": "ED30B32345CF146902659F99073EB91F"},
    {"Challenge_Heal_Runner.Challenge_Heal_Runner": "AD517FF84996921CE6BD1DB60ED8FED0"},
    {"Challenge_Travel_Runner.Challenge_Travel_Runner": "E7516AA94C12951D23D9FCACCD47C03D"},
    {"Challenge_Ressources_Runner.Challenge_Ressources_Runner": "8834EEAA433943FA430B9599910C082B"},
    {"Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner": "EE66207E437E88EA8CE0C2A810BC308B"},
    {"Challenge_TeamActions_Runner.Challenge_TeamActions_Runner": "944265564A8270755A426093528CD3B0"},
    {"Challenge_CollectHealthCrates.Challenge_CollectHealthCrates": "42D2BFB841E3DBD4BA1179962DAB1C0F"},
    {"Challenge_Evade_Runner.Challenge_Evade_Runner": "7BEE126C4E847D02E23AEFBE023FCBF9"},
    {"Challenge_Travel_Runner.Challenge_Travel_Runner": "F547143C478411E0B622B8B0AC955B1D"},
    {"Challenge_Travel_Runner.Challenge_Travel_Runner": "192BE76846846DE5EEB711BA791813E7"},
    {"Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner": "4114117E44044A576C95F8BAF40303A2"},
    {"Challenge_Climb_Runner.Challenge_Climb_Runner": "3FBEB50C478C55F698FDD1AE7C119404"},
    {"Challenge_CollectHealthCrates.Challenge_CollectHealthCrates": "6C862CEF4B5E9B2FF77388973DDBFD42"},
    {"Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner": "5818290740CF09ECC25C7BB9CC953D46"},
    {"Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner": "4BF74EA544C2BD6A9DDDF4AC02DC88D3"},
    {"Challenge_Travel_Runner.Challenge_Travel_Runner": "45CA0FC74CBC690758F248A789BD07F1"},
    {"Challenge_CollectAmmo.Challenge_CollectAmmo": "CF9700A2422398A7D0E8F39DADF860C3"},
    {"Challenge_TeamActions_Runner.Challenge_TeamActions_Runner": "7F46BCA949243314C798DC9E8F8E2A2F"},
    {"Challenge_TakeDamage_Runner.Challenge_TakeDamage_Runner": "883FCAEF44D57B748A716F803474015E"},
    {"Challenge_TakeDamage_Runner.Challenge_TakeDamage_Runner": "E43B65104994E89822C86C87C7D5E048"},
    {"Challenge_TeamActions_Runner.Challenge_TeamActions_Runner": "1084A56940669B27AA636EBF819DFAD5"},
    {"Challenge_Mark_Runner.Challenge_Mark_Runner": "6A005E96499ACBB528B1AAAACA57A411"},
    {"Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner": "EC5E729842AA79FF8DE8C99D3FAFF6AE"},
    {"Challenge_Climb_Runner.Challenge_Climb_Runner": "6D003BF84A9A6EDD74A675A8B8E1E10D"},
    {"Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner": "EE2449BA4354BC83EF2D24A278068C7E"},
    {"Challenge_Evade_Runner.Challenge_Evade_Runner": "DEB741E84BB47D033350EC8B35C1BBCD"},
    {"Challenge_Mark_Runner.Challenge_Mark_Runner": "1D79F5294CDCB72D9AC22FBE21B1BFD1"},
    {"Challenge_TakeDamage_Runner.Challenge_TakeDamage_Runner": "6AC4110D4D3E3D4824C207A3960D31B8"},
    {"Challenge_Evade_Runner.Challenge_Evade_Runner": "EDF3FFB24B957622AB3EDBBE0935B3D9"},
    {"Challenge_Exit_Runner.Challenge_Exit_Runner": "B61C6835421F18DAE0D8FD989431B78F"},
    {"Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner": "F1F7C0FA435B6C751AFE66A084405073"},
    {"Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner": "9B5B115D4A1D7B991ADF52B5D6E727B2"},
    {"Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner": "839E102E4C297C60E277D08A2151B70A"},
    {"Challenge_Travel_Runner.Challenge_Travel_Runner": "71CF96474E83D32AA732DA9EDE79DEFB"},
    {"Challenge_Climb_Runner.Challenge_Climb_Runner": "0F25F9954001826DBB392E9B75946BAE"},
    {"Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner": "A3D51253447E6345D91A119DFB4F56BF"},
    {"Challenge_HunterClose_Runner.Challenge_HunterClose_Runner": "824297E3465193D52D28D86F55719B0"},
    {"Challenge_TeamActions_Runner.Challenge_TeamActions_Runner": "C2DC5D1D4852EAD902A10FBF7CE3C71C"},
    {"Challenge_Ressources_Runner.Challenge_Ressources_Runner": "8EE479CF4C4244230C551EB29D685CBE"},
    {"Challenge_Climb_Runner.Challenge_Climb_Runner": "07C33D364C336BD3EAE63B9E617C47EC"},
    {"Challenge_HunterClose_Runner.Challenge_HunterClose_Runner": "9C2031874115DDDA6C3B63BCBE4E5B46"},
    {"Challenge_CollectAmmo.Challenge_CollectAmmo": "88C86B25475B87E850BF698B3987FF58"},
    {"Challenge_Ressources_Runner.Challenge_Ressources_Runner": "F3D0BEE4433FD7CF79F84DACD2E51CDB"},
    {"Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner": "5CE64F2C4B2F3EE1387F0DBC9EF0BF86"},
    {"Challenge_CollectAmmo.Challenge_CollectAmmo": "B868B5D84D1C521574093093A043FD99"},
    {"Challenge_Domination_Hunter": "Challenge_Domination_Hunter"},
    {"Challenge_Deliver_Runner": "Challenge_Deliver_Runner"},
]
challenge_data = [
    {
        "challenge_id": "C2FBC79142A07F76235B75BDAF9338A9",
        "faction": "Runner",
        "challengeBlueprint": "Challenge_CollectAmmo.Challenge_CollectAmmo",
        "ChallengeCompletionValue": 10,
        "currency": "currencyA",
        "currencyAmount": 1
    }
]


def get_challenge(guid):
    if guid is None:
        return None
    if guid.startswith("Challenge_Deliver_Runner") or guid.startswith("Challenge_Domination_Hunter"):
        guid = guid.split(":")[0]
    creation_time, expiration_time = get_lifetime("daily")
    for item in challenges:
        for key, value in item.items():
            if value == guid:
                # Testing if Shimmy set value 10
                if key == "Challenge_CollectAmmo.Challenge_CollectAmmo":
                    return_val = {
                        "challengeId": f"{key}:{creation_time}",
                        "completed": False,
                        "value":10
                    }
                    return return_val
                return_val = {
                    "challengeId": f"{key}:{creation_time}",
                    "completed": False
                }
                return return_val
    return None


def _setup_challenges(id, userid):
    for item in challenge_data:
        if id == item["challenge_id"]:
            challenge_id = item["challenge_id"]
            faction = item["faction"]
            challengeBlueprint = item["challengeBlueprint"]
            ChallengeCompletionValue = item["ChallengeCompletionValue"]
            base = {
                "challenge_id": challenge_id,
                "faction": faction,
                "challengeBlueprint": challengeBlueprint,
                "ChallengeCompletionValue": ChallengeCompletionValue,
                "last_completion": 0,
                "claimed": False,
                "completion_count": 0
            }
            mongo.write_data_with_list(login=userid, login_steam=False, items_dict={"challenges": base})
            return True
