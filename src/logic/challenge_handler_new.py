import os
from flask_definitions import *
import random

from util.challenge_data import *
from logic.webhook_handler import webhook_handler


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
    if challenge_type == "Weekly" or challenge_type == "Daily":
        current_challenge_data["lifetime"]["creationTime"] = get_lifetime(challenge_type)[0]
        current_challenge_data["lifetime"]["expirationTime"] = get_lifetime(challenge_type)[1]
    else:
        logger.graylog_logger(level="Error", handler="update_challenge_time", message="Invalid challenge type")
        return None

    return current_challenge_data


def get_reward(blueprint):
    # todo add all static challenges here (SRC challenge_handler.py)
    data = {'/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner': {'weight': 100, 'amount': 200,
                                                                                   'id': 'CurrencyB',
                                                                                   'type': 'currency',
                                                                                   'claimed': False},
            '/Game/Challenges/Challenge_Down_Hunter.Challenge_Down_Hunter': {'weight': 100, 'amount': 132,
                                                                             'id': 'CurrencyB', 'type': 'currency',
                                                                             'claimed': False},
            '/Game/Challenges/Challenge_DroneCharger_Hunter.Challenge_DroneCharger_Hunter': {'weight': 100,
                                                                                             'amount': 268,
                                                                                             'id': 'CurrencyA',
                                                                                             'type': 'currency',
                                                                                             'claimed': False},
            '/Game/Challenges/Challenge_JustPlay.Challenge_JustPlay': {'weight': 100, 'amount': 52, 'id': 'CurrencyA',
                                                                       'type': 'currency', 'claimed': False},
            '/Game/Challenges/Daily/Challenge_Domination_Hunter.Challenge_Domination_Hunter': {'weight': 100,
                                                                                               'amount': 275,
                                                                                               'id': 'CurrencyB',
                                                                                               'type': 'currency',
                                                                                               'claimed': False},
            '/Game/Challenges/Daily/Challenge_Domination_Runner.Challenge_Domination_Runner': {'weight': 100,
                                                                                               'amount': 85,
                                                                                               'id': 'CurrencyA',
                                                                                               'type': 'currency',
                                                                                               'claimed': False},
            '/Game/Challenges/Events/Challenge_Darkness_Hunter.Challenge_Darkness_Hunter': {'weight': 100,
                                                                                            'amount': 257,
                                                                                            'id': 'CurrencyB',
                                                                                            'type': 'currency',
                                                                                            'claimed': False},
            '/Game/Challenges/Events/Challenge_Darkness_Runner.Challenge_Darkness_Runner': {'weight': 100,
                                                                                            'amount': 228,
                                                                                            'id': 'CurrencyB',
                                                                                            'type': 'currency',
                                                                                            'claimed': False},
            '/Game/Challenges/Progression/Challenge_AmmoOpportunist_Runner.Challenge_AmmoOpportunist_Runner': {
                'weight': 100, 'amount': 159, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_Autocollect_Hunter.Challenge_Autocollect_Hunter': {'weight': 100,
                                                                                                       'amount': 76,
                                                                                                       'id': 'CurrencyA',
                                                                                                       'type': 'currency',
                                                                                                       'claimed': False},
            '/Game/Challenges/Progression/Challenge_BiggerClipperAutoShotgun_Hunter.Challenge_BiggerClipperAutoShotgun_Hunter': {
                'weight': 100, 'amount': 211, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_BiggerClipperHuntingShotgun_Hunter.Challenge_BiggerClipperHuntingShotgun_Hunter': {
                'weight': 100, 'amount': 249, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_BiggerClipperLMG_Hunter.Challenge_BiggerClipperLMG_Hunter': {
                'weight': 100, 'amount': 286, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_BiggerClipper_Hunter.Challenge_BiggerClipper_Hunter': {
                'weight': 100, 'amount': 92, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_BubbleBuster_Hunter.Challenge_BubbleBuster_Hunter': {'weight': 100,
                                                                                                         'amount': 234,
                                                                                                         'id': 'CurrencyA',
                                                                                                         'type': 'currency',
                                                                                                         'claimed': False},
            '/Game/Challenges/Progression/Challenge_Cardio_Runner.Challenge_Cardio_Runner': {'weight': 100,
                                                                                             'amount': 192,
                                                                                             'id': 'CurrencyA',
                                                                                             'type': 'currency',
                                                                                             'claimed': False},
            '/Game/Challenges/Progression/Challenge_ChanceToActivateNearbyDrone_Hunter.Challenge_ChanceToActivateNearbyDrone_Hunter': {
                'weight': 100, 'amount': 241, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_ChanceToNotSpendAmmo_Runner.Challenge_ChanceToNotSpendAmmo_Runner': {
                'weight': 100, 'amount': 229, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_ClingWrap_Runner.Challenge_ClingWrap_Runner': {'weight': 100,
                                                                                                   'amount': 171,
                                                                                                   'id': 'CurrencyB',
                                                                                                   'type': 'currency',
                                                                                                   'claimed': False},
            '/Game/Challenges/Progression/Challenge_Clone_Runner.Challenge_Clone_Runner': {'weight': 100, 'amount': 111,
                                                                                           'id': 'CurrencyA',
                                                                                           'type': 'currency',
                                                                                           'claimed': False},
            '/Game/Challenges/Progression/Challenge_DamageDodger_Runner.Challenge_DamageDodger_Runner': {'weight': 100,
                                                                                                         'amount': 36,
                                                                                                         'id': 'CurrencyA',
                                                                                                         'type': 'currency',
                                                                                                         'claimed': False},
            '/Game/Challenges/Progression/Challenge_DamageResistWhenRevealed_Runner.Challenge_DamageResistWhenRevealed_Runner': {
                'weight': 100, 'amount': 249, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_DroneReactivationTime_Hunter.Challenge_DroneReactivationTime_Hunter': {
                'weight': 100, 'amount': 33, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_DroneShield_Hunter.Challenge_DroneShield_Hunter': {'weight': 100,
                                                                                                       'amount': 198,
                                                                                                       'id': 'CurrencyB',
                                                                                                       'type': 'currency',
                                                                                                       'claimed': False},
            '/Game/Challenges/Progression/Challenge_Emboldened_Runner.Challenge_Emboldened_Runner': {'weight': 100,
                                                                                                     'amount': 254,
                                                                                                     'id': 'CurrencyA',
                                                                                                     'type': 'currency',
                                                                                                     'claimed': False},
            '/Game/Challenges/Progression/Challenge_EvadeMaster_Runner.Challenge_EvadeMaster_Runner': {'weight': 100,
                                                                                                       'amount': 299,
                                                                                                       'id': 'CurrencyB',
                                                                                                       'type': 'currency',
                                                                                                       'claimed': False},
            '/Game/Challenges/Progression/Challenge_ExplosiveRangeIncreased_Hunter.Challenge_ExplosiveRangeIncreased_Hunter': {
                'weight': 100, 'amount': 140, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_ExtraToppings_Hunter.Challenge_ExtraToppings_Hunter': {
                'weight': 100, 'amount': 131, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_Fade_Hunter.Challenge_Fade_Hunter': {'weight': 100, 'amount': 283,
                                                                                         'id': 'CurrencyB',
                                                                                         'type': 'currency',
                                                                                         'claimed': False},
            '/Game/Challenges/Progression/Challenge_FasterBloodDeliver_Runner.Challenge_FasterBloodDeliver_Runner': {
                'weight': 100, 'amount': 83, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_Firmware_Runner.Challenge_Firmware_Runner': {'weight': 100,
                                                                                                 'amount': 89,
                                                                                                 'id': 'CurrencyB',
                                                                                                 'type': 'currency',
                                                                                                 'claimed': False},
            '/Game/Challenges/Progression/Challenge_FleetFeet_Runner.Challenge_FleetFeet_Runner': {'weight': 100,
                                                                                                   'amount': 84,
                                                                                                   'id': 'CurrencyA',
                                                                                                   'type': 'currency',
                                                                                                   'claimed': False},
            '/Game/Challenges/Progression/Challenge_FriendsForLife_Runner.Challenge_FriendsForLife_Runner': {
                'weight': 100, 'amount': 75, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_GreatShape_Hunter.Challenge_GreatShape_Hunter': {'weight': 100,
                                                                                                     'amount': 195,
                                                                                                     'id': 'CurrencyB',
                                                                                                     'type': 'currency',
                                                                                                     'claimed': False},
            '/Game/Challenges/Progression/Challenge_HackedCratesExplode_Hunter.Challenge_HackedCratesExplode_Hunter': {
                'weight': 100, 'amount': 193, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_Hacker_Hunter.Challenge_Hacker_Hunter': {'weight': 100,
                                                                                             'amount': 207,
                                                                                             'id': 'CurrencyB',
                                                                                             'type': 'currency',
                                                                                             'claimed': False},
            '/Game/Challenges/Progression/Challenge_HealFaster_Runner.Challenge_HealFaster_Runner': {'weight': 100,
                                                                                                     'amount': 71,
                                                                                                     'id': 'CurrencyA',
                                                                                                     'type': 'currency',
                                                                                                     'claimed': False},
            '/Game/Challenges/Progression/Challenge_Heal_Runner.Challenge_Heal_Runner': {'weight': 100, 'amount': 184,
                                                                                         'id': 'CurrencyA',
                                                                                         'type': 'currency',
                                                                                         'claimed': False},
            '/Game/Challenges/Progression/Challenge_HeatOfTheMoment_Runner.Challenge_HeatOfTheMoment_Runner': {
                'weight': 100, 'amount': 107, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_HerdMentality_Runner.Challenge_HerdMentality_Runner': {
                'weight': 100, 'amount': 141, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_HeyDownThere_Hunter.Challenge_HeyDownThere_Hunter': {'weight': 100,
                                                                                                         'amount': 44,
                                                                                                         'id': 'CurrencyB',
                                                                                                         'type': 'currency',
                                                                                                         'claimed': False},
            '/Game/Challenges/Progression/Challenge_InteractSpeedImprovement_Runner.Challenge_InteractSpeedImprovement_Runner': {
                'weight': 100, 'amount': 100, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_Invisibility_Runner.Challenge_Invisibility_Runner': {'weight': 100,
                                                                                                         'amount': 192,
                                                                                                         'id': 'CurrencyA',
                                                                                                         'type': 'currency',
                                                                                                         'claimed': False},
            '/Game/Challenges/Progression/Challenge_KeepHangingOn_Runner.Challenge_KeepHangingOn_Runner': {
                'weight': 100, 'amount': 256, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_LMGCompensator_Hunter.Challenge_LMGCompensator_Hunter': {
                'weight': 100, 'amount': 215, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_LuckyCharm_Hunter.Challenge_LuckyCharm_Hunter': {'weight': 100,
                                                                                                     'amount': 127,
                                                                                                     'id': 'CurrencyA',
                                                                                                     'type': 'currency',
                                                                                                     'claimed': False},
            '/Game/Challenges/Progression/Challenge_LuckyCharm_Runner.Challenge_LuckyCharm_Runner': {'weight': 100,
                                                                                                     'amount': 147,
                                                                                                     'id': 'CurrencyB',
                                                                                                     'type': 'currency',
                                                                                                     'claimed': False},
            '/Game/Challenges/Progression/Challenge_Mines_Hunter.Challenge_Mines_Hunter': {'weight': 100, 'amount': 277,
                                                                                           'id': 'CurrencyA',
                                                                                           'type': 'currency',
                                                                                           'claimed': False},
            '/Game/Challenges/Progression/Challenge_ObjectiveMaster_Runner.Challenge_ObjectiveMaster_Runner': {
                'weight': 100, 'amount': 246, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_OcularImplants_Runner.Challenge_OcularImplants_Runner': {
                'weight': 100, 'amount': 93, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_OrbitalStrike_Hunter.Challenge_OrbitalStrike_Hunter': {
                'weight': 100, 'amount': 187, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_OverTheEdge_Hunter.Challenge_OverTheEdge_Hunter': {'weight': 100,
                                                                                                       'amount': 51,
                                                                                                       'id': 'CurrencyB',
                                                                                                       'type': 'currency',
                                                                                                       'claimed': False},
            '/Game/Challenges/Progression/Challenge_PowerBoosterFade_Hunter.Challenge_PowerBoosterFade_Hunter': {
                'weight': 100, 'amount': 228, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_PowerBoosterMines_Hunter.Challenge_PowerBoosterMines_Hunter': {
                'weight': 100, 'amount': 241, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_PowerBoosterOrbital_Hunter.Challenge_PowerBoosterOrbital_Hunter': {
                'weight': 100, 'amount': 169, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_PowerBoosterTurret_Hunter.Challenge_PowerBoosterTurret_Hunter': {
                'weight': 100, 'amount': 224, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_PowerStomp_Hunter.Challenge_PowerStomp_Hunter': {'weight': 100,
                                                                                                     'amount': 182,
                                                                                                     'id': 'CurrencyA',
                                                                                                     'type': 'currency',
                                                                                                     'claimed': False},
            '/Game/Challenges/Progression/Challenge_Resting_Runner.Challenge_Resting_Runner': {'weight': 100,
                                                                                               'amount': 280,
                                                                                               'id': 'CurrencyA',
                                                                                               'type': 'currency',
                                                                                               'claimed': False},
            '/Game/Challenges/Progression/Challenge_RichGetRicher_Runner.Challenge_RichGetRicher_Runner': {
                'weight': 100, 'amount': 187, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_SecurityBlanket_Runner.Challenge_SecurityBlanket_Runner': {
                'weight': 100, 'amount': 212, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_SharingIsCaring_Runner.Challenge_SharingIsCaring_Runner': {
                'weight': 100, 'amount': 286, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_Shield_Runner.Challenge_Shield_Runner': {'weight': 100,
                                                                                             'amount': 236,
                                                                                             'id': 'CurrencyA',
                                                                                             'type': 'currency',
                                                                                             'claimed': False},
            '/Game/Challenges/Progression/Challenge_Shimmy_Runner.Challenge_Shimmy_Runner': {'weight': 100,
                                                                                             'amount': 100,
                                                                                             'id': 'CurrencyB',
                                                                                             'type': 'currency',
                                                                                             'claimed': False},
            '/Game/Challenges/Progression/Challenge_ShockRange_Hunter.Challenge_ShockRange_Hunter': {'weight': 100,
                                                                                                     'amount': 200,
                                                                                                     'id': 'CurrencyA',
                                                                                                     'type': 'currency',
                                                                                                     'claimed': False},
            '/Game/Challenges/Progression/Challenge_Shoot_AssaultRifle_Hunter.Challenge_Shoot_AssaultRifle_Hunter': {
                'weight': 100, 'amount': 75, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_Shoot_AutoShotgun_Hunter.Challenge_Shoot_AutoShotgun_Hunter': {
                'weight': 100, 'amount': 111, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_Shoot_AutoSniperGuardian_Hunter.Challenge_Shoot_AutoSniperGuardian_Hunter': {
                'weight': 100, 'amount': 200, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_Shoot_AutoSniper_Hunter.Challenge_Shoot_AutoSniper_Hunter': {
                'weight': 100, 'amount': 275, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_Shoot_BurstRifle_Hunter.Challenge_Shoot_BurstRifle_Hunter': {
                'weight': 100, 'amount': 116, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_Shoot_Carbine_Hunter.Challenge_Shoot_Carbine_Hunter': {
                'weight': 100, 'amount': 151, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_Shoot_DefaultShotgun_Hunter.Challenge_Shoot_DefaultShotgun_Hunter': {
                'weight': 100, 'amount': 66, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_Shoot_DefaultSniper_Hunter.Challenge_Shoot_DefaultSniper_Hunter': {
                'weight': 100, 'amount': 74, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_Shoot_GrenadeLauncher_Hunter.Challenge_Shoot_GrenadeLauncher_Hunter': {
                'weight': 100, 'amount': 114, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_Shoot_HuntingShotgin_Hunter.Challenge_Shoot_HuntingShotgin_Hunter': {
                'weight': 100, 'amount': 298, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_Shoot_LMG_Hunter.Challenge_Shoot_LMG_Hunter': {'weight': 100,
                                                                                                   'amount': 99,
                                                                                                   'id': 'CurrencyA',
                                                                                                   'type': 'currency',
                                                                                                   'claimed': False},
            '/Game/Challenges/Progression/Challenge_SizeMatters_Runner.Challenge_SizeMatters_Runner': {'weight': 100,
                                                                                                       'amount': 100,
                                                                                                       'id': 'CurrencyB',
                                                                                                       'type': 'currency',
                                                                                                       'claimed': False},
            '/Game/Challenges/Progression/Challenge_SmokeScreen_Runner.Challenge_SmokeScreen_Runner': {'weight': 100,
                                                                                                       'amount': 139,
                                                                                                       'id': 'CurrencyA',
                                                                                                       'type': 'currency',
                                                                                                       'claimed': False},
            '/Game/Challenges/Progression/Challenge_Sniper_Runner.Challenge_Sniper_Runner': {'weight': 100,
                                                                                             'amount': 30,
                                                                                             'id': 'CurrencyB',
                                                                                             'type': 'currency',
                                                                                             'claimed': False},
            '/Game/Challenges/Progression/Challenge_SoClose_Hunter.Challenge_SoClose_Hunter': {'weight': 100,
                                                                                               'amount': 222,
                                                                                               'id': 'CurrencyB',
                                                                                               'type': 'currency',
                                                                                               'claimed': False},
            '/Game/Challenges/Progression/Challenge_SpeedArrow_Runner.Challenge_SpeedArrow_Runner': {'weight': 100,
                                                                                                     'amount': 56,
                                                                                                     'id': 'CurrencyB',
                                                                                                     'type': 'currency',
                                                                                                     'claimed': False},
            '/Game/Challenges/Progression/Challenge_SpeedDemon_Hunter.Challenge_SpeedDemon_Hunter': {'weight': 100,
                                                                                                     'amount': 121,
                                                                                                     'id': 'CurrencyA',
                                                                                                     'type': 'currency',
                                                                                                     'claimed': False},
            '/Game/Challenges/Progression/Challenge_SpendAmmo_AssaultRifle_Hunter.Challenge_SpendAmmo_AssaultRifle_Hunter': {
                'weight': 100, 'amount': 185, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_SpendAmmo_AutoShotgun_Hunter.Challenge_SpendAmmo_AutoShotgun_Hunter': {
                'weight': 100, 'amount': 65, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_SpendAmmo_AutoSniperGuardian_Hunter.Challenge_SpendAmmo_AutoSniperGuardian_Hunter': {
                'weight': 100, 'amount': 40, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_SpendAmmo_AutoSniper_Hunter.Challenge_SpendAmmo_AutoSniper_Hunter': {
                'weight': 100, 'amount': 173, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_SpendAmmo_BurstRifleInquisitor_Hunter.Challenge_SpendAmmo_BurstRifleInquisitor_Hunter': {
                'weight': 100, 'amount': 230, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_SpendAmmo_BurstRifle_Hunter.Challenge_SpendAmmo_BurstRifle_Hunter': {
                'weight': 100, 'amount': 100, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_SpendAmmo_Carbine_Hunter.Challenge_SpendAmmo_Carbine_Hunter': {
                'weight': 100, 'amount': 212, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_SpendAmmo_DefaultShotgun_Hunter.Challenge_SpendAmmo_DefaultShotgun_Hunter': {
                'weight': 100, 'amount': 54, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_SpendAmmo_DefaultSniper_Hunter.Challenge_SpendAmmo_DefaultSniper_Hunter': {
                'weight': 100, 'amount': 156, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_SpendAmmo_GrenadeLauncher_Hunter.Challenge_SpendAmmo_GrenadeLauncher_Hunter': {
                'weight': 100, 'amount': 79, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_SpendAmmo_HuntingShotgun_Hunter.Challenge_SpendAmmo_HuntingShotgun_Hunter': {
                'weight': 100, 'amount': 60, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_SpendAmmo_LMG_Hunter.Challenge_SpendAmmo_LMG_Hunter': {
                'weight': 100, 'amount': 177, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_Splash_Runner.Challenge_Splash_Runner': {'weight': 100,
                                                                                             'amount': 115,
                                                                                             'id': 'CurrencyB',
                                                                                             'type': 'currency',
                                                                                             'claimed': False},
            '/Game/Challenges/Progression/Challenge_StaminaFreak_Hunter.Challenge_StaminaFreak_Hunter': {'weight': 100,
                                                                                                         'amount': 210,
                                                                                                         'id': 'CurrencyB',
                                                                                                         'type': 'currency',
                                                                                                         'claimed': False},
            '/Game/Challenges/Progression/Challenge_StaminaRegenDamaged_Runner.Challenge_StaminaRegenDamaged_Runner': {
                'weight': 100, 'amount': 94, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_StaminaRegenReveal_Runner.Challenge_StaminaRegenReveal_Runner': {
                'weight': 100, 'amount': 188, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_StayingAlive_Runner.Challenge_StayingAlive_Runner': {'weight': 100,
                                                                                                         'amount': 182,
                                                                                                         'id': 'CurrencyB',
                                                                                                         'type': 'currency',
                                                                                                         'claimed': False},
            '/Game/Challenges/Progression/Challenge_Stealer_Hunter.Challenge_Stealer_Hunter': {'weight': 100,
                                                                                               'amount': 288,
                                                                                               'id': 'CurrencyA',
                                                                                               'type': 'currency',
                                                                                               'claimed': False},
            '/Game/Challenges/Progression/Challenge_Stunning_Hunter.Challenge_Stunning_Hunter': {'weight': 100,
                                                                                                 'amount': 268,
                                                                                                 'id': 'CurrencyA',
                                                                                                 'type': 'currency',
                                                                                                 'claimed': False},
            '/Game/Challenges/Progression/Challenge_SuddenInsight_Runner.Challenge_SuddenInsight_Runner': {
                'weight': 100, 'amount': 245, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_ToilTogether_Runner.Challenge_ToilTogether_Runner': {'weight': 100,
                                                                                                         'amount': 294,
                                                                                                         'id': 'CurrencyA',
                                                                                                         'type': 'currency',
                                                                                                         'claimed': False},
            '/Game/Challenges/Progression/Challenge_TreasureHunter_Runner.Challenge_TreasureHunter_Runner': {
                'weight': 100, 'amount': 132, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/Challenge_Turrets_Hunter.Challenge_Turrets_Hunter': {'weight': 100,
                                                                                               'amount': 216,
                                                                                               'id': 'CurrencyA',
                                                                                               'type': 'currency',
                                                                                               'claimed': False},
            '/Game/Challenges/Progression/Challenge_UnderFoot_Runner.Challenge_UnderFoot_Runner': {'weight': 100,
                                                                                                   'amount': 161,
                                                                                                   'id': 'CurrencyB',
                                                                                                   'type': 'currency',
                                                                                                   'claimed': False},
            '/Game/Challenges/Progression/Challenge_ZeroCool_Runner.Challenge_ZeroCool_Runner': {'weight': 100,
                                                                                                 'amount': 285,
                                                                                                 'id': 'CurrencyB',
                                                                                                 'type': 'currency',
                                                                                                 'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_Aim_Hunter.Challenge_Aim_Hunter': {'weight': 100,
                                                                                               'amount': 282,
                                                                                               'id': 'CurrencyA',
                                                                                               'type': 'currency',
                                                                                               'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner': {
                'weight': 100, 'amount': 101, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_BloodMode_Runner.Challenge_BloodMode_Runner': {
                'weight': 100, 'amount': 273, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_Climb_Runner.Challenge_Climb_Runner': {'weight': 100,
                                                                                                   'amount': 252,
                                                                                                   'id': 'CurrencyA',
                                                                                                   'type': 'currency',
                                                                                                   'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo': {'weight': 100,
                                                                                                 'amount': 196,
                                                                                                 'id': 'CurrencyA',
                                                                                                 'type': 'currency',
                                                                                                 'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates': {
                'weight': 100, 'amount': 142, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner': {
                'weight': 100, 'amount': 261, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner': {
                'weight': 100, 'amount': 190, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_Crouch_Runner.Challenge_Crouch_Runner': {'weight': 100,
                                                                                                     'amount': 298,
                                                                                                     'id': 'CurrencyA',
                                                                                                     'type': 'currency',
                                                                                                     'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_Damage_Hunter.Challenge_Damage_Hunter': {'weight': 100,
                                                                                                     'amount': 200,
                                                                                                     'id': 'CurrencyB',
                                                                                                     'type': 'currency',
                                                                                                     'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner': {
                'weight': 100, 'amount': 293, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_DestroyConstructs_Runner.Challenge_DestroyConstructs_Runner': {
                'weight': 100, 'amount': 294, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner': {
                'weight': 100, 'amount': 116, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_Downing_Hunter.Challenge_Downing_Hunter': {'weight': 100,
                                                                                                       'amount': 190,
                                                                                                       'id': 'CurrencyA',
                                                                                                       'type': 'currency',
                                                                                                       'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_Drones_Hunter.Challenge_Drones_Hunter': {'weight': 100,
                                                                                                     'amount': 183,
                                                                                                     'id': 'CurrencyB',
                                                                                                     'type': 'currency',
                                                                                                     'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner': {'weight': 100,
                                                                                                   'amount': 111,
                                                                                                   'id': 'CurrencyB',
                                                                                                   'type': 'currency',
                                                                                                   'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_Execution_Hunter.Challenge_Execution_Hunter': {
                'weight': 100, 'amount': 57, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner': {'weight': 100,
                                                                                                 'amount': 270,
                                                                                                 'id': 'CurrencyA',
                                                                                                 'type': 'currency',
                                                                                                 'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_Fall_Runner.Challenge_Fall_Runner': {'weight': 100,
                                                                                                 'amount': 212,
                                                                                                 'id': 'CurrencyA',
                                                                                                 'type': 'currency',
                                                                                                 'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_HackCrates_Hunter.Challenge_HackCrates_Hunter': {
                'weight': 100, 'amount': 32, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_Hacking_Hunter.Challenge_Hacking_Hunter': {'weight': 100,
                                                                                                       'amount': 288,
                                                                                                       'id': 'CurrencyA',
                                                                                                       'type': 'currency',
                                                                                                       'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_Hang_Runner.Challenge_Hang_Runner': {'weight': 100,
                                                                                                 'amount': 203,
                                                                                                 'id': 'CurrencyB',
                                                                                                 'type': 'currency',
                                                                                                 'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_Heal_Runner.Challenge_Heal_Runner': {'weight': 100,
                                                                                                 'amount': 195,
                                                                                                 'id': 'CurrencyB',
                                                                                                 'type': 'currency',
                                                                                                 'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner': {
                'weight': 100, 'amount': 149, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_Jump_Runner.Challenge_Jump_Runner': {'weight': 100,
                                                                                                 'amount': 176,
                                                                                                 'id': 'CurrencyB',
                                                                                                 'type': 'currency',
                                                                                                 'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_LastMAnStanding_Hunter.Challenge_LastMAnStanding_Hunter': {
                'weight': 100, 'amount': 185, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_MarkAmmo_Runner.Challenge_MarkAmmo_Runner': {'weight': 100,
                                                                                                         'amount': 201,
                                                                                                         'id': 'CurrencyA',
                                                                                                         'type': 'currency',
                                                                                                         'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_MarkBloodPile_Runner.Challenge_MarkBloodPile_Runner': {
                'weight': 100, 'amount': 184, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_MarkCapturePoint_Runner.Challenge_MarkCapturePoint_Runner': {
                'weight': 100, 'amount': 223, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_MarkHealth_Runner.Challenge_MarkHealth_Runner': {
                'weight': 100, 'amount': 179, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_MarkNPI_Runner.Challenge_MarkNPI_Runner': {'weight': 100,
                                                                                                       'amount': 119,
                                                                                                       'id': 'CurrencyB',
                                                                                                       'type': 'currency',
                                                                                                       'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner': {'weight': 100,
                                                                                                 'amount': 237,
                                                                                                 'id': 'CurrencyB',
                                                                                                 'type': 'currency',
                                                                                                 'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_Powers_Hunter.Challenge_Powers_Hunter': {'weight': 100,
                                                                                                     'amount': 213,
                                                                                                     'id': 'CurrencyB',
                                                                                                     'type': 'currency',
                                                                                                     'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner': {
                'weight': 100, 'amount': 30, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_Reveal_Hunter.Challenge_Reveal_Hunter': {'weight': 100,
                                                                                                     'amount': 166,
                                                                                                     'id': 'CurrencyB',
                                                                                                     'type': 'currency',
                                                                                                     'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_Revive_Runner.Challenge_Revive_Runner': {'weight': 100,
                                                                                                     'amount': 174,
                                                                                                     'id': 'CurrencyA',
                                                                                                     'type': 'currency',
                                                                                                     'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_RingOut_Hunter.Challenge_RingOut_Hunter': {'weight': 100,
                                                                                                       'amount': 78,
                                                                                                       'id': 'CurrencyB',
                                                                                                       'type': 'currency',
                                                                                                       'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner': {'weight': 100,
                                                                                                         'amount': 133,
                                                                                                         'id': 'CurrencyB',
                                                                                                         'type': 'currency',
                                                                                                         'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_Stomp_Hunter.Challenge_Stomp_Hunter': {'weight': 100,
                                                                                                   'amount': 120,
                                                                                                   'id': 'CurrencyA',
                                                                                                   'type': 'currency',
                                                                                                   'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_Supercharge_Hunter.Challenge_Supercharge_Hunter': {
                'weight': 100, 'amount': 65, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner': {
                'weight': 100, 'amount': 203, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_TakeDamage_Runner.Challenge_TakeDamage_Runner': {
                'weight': 100, 'amount': 172, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner': {
                'weight': 100, 'amount': 225, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_Travel_Hunter.Challenge_Travel_Hunter': {'weight': 100,
                                                                                                     'amount': 283,
                                                                                                     'id': 'CurrencyA',
                                                                                                     'type': 'currency',
                                                                                                     'claimed': False},
            '/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner': {'weight': 100,
                                                                                                     'amount': 148,
                                                                                                     'id': 'CurrencyA',
                                                                                                     'type': 'currency',
                                                                                                     'claimed': False},
            '/Game/Challenges/Weekly/Challenge_ARB_Damage_HunterWeekly.Challenge_ARB_Damage_HunterWeekly': {
                'weight': 100, 'amount': 263, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Weekly/Challenge_AssaultRifleWins_HunterWeekly.Challenge_AssaultRifleWins_HunterWeekly': {
                'weight': 100, 'amount': 138, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Weekly/Challenge_BleedOut_HunterWeekly.Challenge_BleedOut_HunterWeekly': {'weight': 100,
                                                                                                        'amount': 259,
                                                                                                        'id': 'CurrencyB',
                                                                                                        'type': 'currency',
                                                                                                        'claimed': False},
            '/Game/Challenges/Weekly/Challenge_BleedOut_RunnerWeekly.Challenge_BleedOut_RunnerWeekly': {'weight': 100,
                                                                                                        'amount': 115,
                                                                                                        'id': 'CurrencyB',
                                                                                                        'type': 'currency',
                                                                                                        'claimed': False},
            '/Game/Challenges/Weekly/Challenge_Damage_HunterWeekly.Challenge_Damage_HunterWeekly': {'weight': 100,
                                                                                                    'amount': 267,
                                                                                                    'id': 'CurrencyA',
                                                                                                    'type': 'currency',
                                                                                                    'claimed': False},
            '/Game/Challenges/Weekly/Challenge_Double_HunterWeekly.Challenge_Double_HunterWeekly': {'weight': 100,
                                                                                                    'amount': 202,
                                                                                                    'id': 'CurrencyA',
                                                                                                    'type': 'currency',
                                                                                                    'claimed': False},
            '/Game/Challenges/Weekly/Challenge_DroneActivation_HunterWeekly.Challenge_DroneActivation_HunterWeekly': {
                'weight': 100, 'amount': 56, 'id': 'CurrencyA', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Weekly/Challenge_Efficient_HunterWeekly.Challenge_Efficient_HunterWeekly': {'weight': 100,
                                                                                                          'amount': 38,
                                                                                                          'id': 'CurrencyA',
                                                                                                          'type': 'currency',
                                                                                                          'claimed': False},
            '/Game/Challenges/Weekly/Challenge_Emotional_HunterWeekly.Challenge_Emotional_HunterWeekly': {'weight': 100,
                                                                                                          'amount': 205,
                                                                                                          'id': 'CurrencyA',
                                                                                                          'type': 'currency',
                                                                                                          'claimed': False},
            '/Game/Challenges/Weekly/Challenge_Emotional_RunnerWeekly.Challenge_Emotional_RunnerWeekly': {'weight': 100,
                                                                                                          'amount': 201,
                                                                                                          'id': 'CurrencyA',
                                                                                                          'type': 'currency',
                                                                                                          'claimed': False},
            '/Game/Challenges/Weekly/Challenge_Greed_HunterWeekly.Challenge_Greed_HunterWeekly': {'weight': 100,
                                                                                                  'amount': 70,
                                                                                                  'id': 'CurrencyA',
                                                                                                  'type': 'currency',
                                                                                                  'claimed': False},
            '/Game/Challenges/Weekly/Challenge_Greed_RunnerWeekly.Challenge_Greed_RunnerWeekly': {'weight': 100,
                                                                                                  'amount': 48,
                                                                                                  'id': 'CurrencyB',
                                                                                                  'type': 'currency',
                                                                                                  'claimed': False},
            '/Game/Challenges/Weekly/Challenge_Headshot_HunterWeekly.Challenge_Headshot_HunterWeekly': {'weight': 100,
                                                                                                        'amount': 225,
                                                                                                        'id': 'CurrencyA',
                                                                                                        'type': 'currency',
                                                                                                        'claimed': False},
            '/Game/Challenges/Weekly/Challenge_HuntingShotgunWins_HunterWeekly.Challenge_HuntingShotgunWins_HunterWeekly': {
                'weight': 100, 'amount': 118, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Weekly/Challenge_InDenial_HunterWeekly.Challenge_InDenial_HunterWeekly': {'weight': 100,
                                                                                                        'amount': 162,
                                                                                                        'id': 'CurrencyB',
                                                                                                        'type': 'currency',
                                                                                                        'claimed': False},
            '/Game/Challenges/Weekly/Challenge_LMGWins_HunterWeekly.Challenge_LMGWins_HunterWeekly': {'weight': 100,
                                                                                                      'amount': 160,
                                                                                                      'id': 'CurrencyA',
                                                                                                      'type': 'currency',
                                                                                                      'claimed': False},
            '/Game/Challenges/Weekly/Challenge_Mines_HunterWeekly.Challenge_Mines_HunterWeekly': {'weight': 100,
                                                                                                  'amount': 162,
                                                                                                  'id': 'CurrencyA',
                                                                                                  'type': 'currency',
                                                                                                  'claimed': False},
            '/Game/Challenges/Weekly/Challenge_Mines_RunnerWeekly.Challenge_Mines_RunnerWeekly': {'weight': 100,
                                                                                                  'amount': 263,
                                                                                                  'id': 'CurrencyA',
                                                                                                  'type': 'currency',
                                                                                                  'claimed': False},
            '/Game/Challenges/Weekly/Challenge_Reveals_hunterWeekly.Challenge_Reveals_hunterWeekly': {'weight': 100,
                                                                                                      'amount': 181,
                                                                                                      'id': 'CurrencyA',
                                                                                                      'type': 'currency',
                                                                                                      'claimed': False},
            '/Game/Challenges/Weekly/Challenge_RingOut_hunterWeekly.Challenge_RingOut_hunterWeekly': {'weight': 100,
                                                                                                      'amount': 269,
                                                                                                      'id': 'CurrencyB',
                                                                                                      'type': 'currency',
                                                                                                      'claimed': False},
            '/Game/Challenges/Weekly/Challenge_Shields_RunnerWeekly.Challenge_Shields_RunnerWeekly': {'weight': 100,
                                                                                                      'amount': 137,
                                                                                                      'id': 'CurrencyA',
                                                                                                      'type': 'currency',
                                                                                                      'claimed': False},
            '/Game/Challenges/Weekly/Challenge_ShotgunDowns_HunterWeekly.Challenge_ShotgunDowns_HunterWeekly': {
                'weight': 100, 'amount': 125, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Weekly/Challenge_SpeedCapture_RunnerWeekly.Challenge_SpeedCapture_RunnerWeekly': {
                'weight': 100, 'amount': 57, 'id': 'CurrencyB', 'type': 'currency', 'claimed': False},
            '/Game/Challenges/Weekly/Challenge_Speed_HunterWeekly.Challenge_Speed_HunterWeekly': {'weight': 100,
                                                                                                  'amount': 235,
                                                                                                  'id': 'CurrencyA',
                                                                                                  'type': 'currency',
                                                                                                  'claimed': False},
            '/Game/Challenges/Weekly/Challenge_Stuns_RunnerWeekly.Challenge_Stuns_RunnerWeekly': {'weight': 100,
                                                                                                  'amount': 285,
                                                                                                  'id': 'CurrencyB',
                                                                                                  'type': 'currency',
                                                                                                  'claimed': False},
            '/Game/Challenges/Weekly/Challenge_Turrets_HunterWeekly.Challenge_Turrets_HunterWeekly': {'weight': 100,
                                                                                                      'amount': 297,
                                                                                                      'id': 'CurrencyA',
                                                                                                      'type': 'currency',
                                                                                                      'claimed': False},
            '/Game/Challenges/Weekly/Challenge_Turrets_RunnerWeekly.Challenge_Turrets_RunnerWeekly': {'weight': 100,
                                                                                                      'amount': 37,
                                                                                                      'id': 'CurrencyA',
                                                                                                      'type': 'currency',
                                                                                                      'claimed': False},
            '/Game/Challenges/Weekly/Challenge_UPs_RunnerWeekly.Challenge_UPs_RunnerWeekly': {'weight': 100,
                                                                                              'amount': 102,
                                                                                              'id': 'CurrencyB',
                                                                                              'type': 'currency',
                                                                                              'claimed': False},
            '/Game/Challenges/Weekly/Challenge_Wasteful_HunterWeekly.Challenge_Wasteful_HunterWeekly': {'weight': 100,
                                                                                                        'amount': 66,
                                                                                                        'id': 'CurrencyA',
                                                                                                        'type': 'currency',
                                                                                                        'claimed': False},
            '/Game/Challenges/Weekly/Challenge_Wasteful_RunnerWeekly.Challenge_Wasteful_RunnerWeekly': {'weight': 100,
                                                                                                        'amount': 49,
                                                                                                        'id': 'CurrencyA',
                                                                                                        'type': 'currency',
                                                                                                        'claimed': False},
            '/Game/Challenges/Weekly/Challenge_WUP_HunterWeekly.Challenge_WUP_HunterWeekly': {'weight': 100,
                                                                                              'amount': 50,
                                                                                              'id': 'CurrencyA',
                                                                                              'type': 'currency',
                                                                                              'claimed': False},
            '/Game/Challenges/Weekly/Challenge_WUP_RunnerWeekly.Challenge_WUP_RunnerWeekly': {'weight': 100,
                                                                                              'amount': 179,
                                                                                              'id': 'CurrencyB',
                                                                                              'type': 'currency',
                                                                                              'claimed': False}}
    if blueprint in data:
        return data[blueprint]
    else:
        logger.graylog_logger(level="error", handler="get_reward", message=f"Blueprint {blueprint} not found")
        return {"weight": 100,
                "amount": 1,
                "id": "CurrencyA",
                "type": "currency",
                "claimed": False
                }


def update_achievement_challenges(user_id):
    steam_id = mongo.get_data_with_list(login=user_id, login_steam=False, items={"steamid"})["steamid"]
    data = webhook_handler.steam_check_achievments(steam_id)
    if data["playerstats"]["success"]:
        achieved_achievement = []
        for achievement in data["playerstats"]["achievements"]:
            if achievement["achieved"] == 1:
                challenge_id = achievement["apiname"]
                if challenge_id == "EFAB89E6465D1163D62A07B11048F2B6":
                    print(f"Completed challenge {challenge_id}, NotAQuitter")
                    achieved_achievement.append({"challengeId": challenge_id, "value": 50})
                elif challenge_id == "2CAEBB354D506D7C43B941BC1DA775A0":
                    print(f"Completed challenge {challenge_id}, Escapist")
                    achieved_achievement.append({"challengeId": challenge_id, "value": 10})
                elif challenge_id == "E51981B946BEE3D45C5C41B2FCFF310B":
                    print(f"Completed challenge {challenge_id}, SpecialDelivery")
                    achieved_achievement.append({"challengeId": challenge_id, "value": 500})
                elif challenge_id == "AAD05B9D46471DC811BBE0BA91916AB7":
                    print(f"Completed challenge {challenge_id}, DontBeADowner")
                    achieved_achievement.append({"challengeId": challenge_id, "value": 50})
                elif challenge_id == "BA2D4A5445CB70276A8F5D9E1AFCE080":
                    print(f"Completed challenge {challenge_id}, DroneZone")
                    achieved_achievement.append({"challengeId": challenge_id, "value": 100})
                else:
                    logger.graylog_logger(level="error", handler="update_achievement_challenges",
                                          message=f"Achievement Challenge {challenge_id} not found")
        if len(achieved_achievement) > 0:
            user_challenges = mongo.get_data_with_list(login=steam_id, login_steam=True, items={"challengeProgression"})["challengeProgression"]
            for achievement in achieved_achievement:
                challenge_id = achievement["challengeId"]
                value = achievement["value"]
                for challenge in user_challenges:
                    if challenge["challengeId"] == challenge_id:
                        challenge["completed"] = True
                        challenge["value"] = value
                        break
            mongo.write_data_with_list(login=steam_id, login_steam=True,
                                       items_dict={"challengeProgression": user_challenges})
    else:
        logger.graylog_logger(level="error", handler="update_achievement_challenges",
                              message=f"Failed to get achievements for steam_id {steam_id}reason {data['playerstats']['error']}")



def get_challenge_ids_from_inventory(user_id):
    Progression_HunterGroupA = mongo.get_data_with_list(login=user_id, login_steam=False,
                                                        items={"HunterGroupA"})["HunterGroupA"]
    Progression_HunterGroupB = mongo.get_data_with_list(login=user_id, login_steam=False,
                                                        items={"HunterGroupB"})["HunterGroupB"]
    Progression_HunterGroupC = mongo.get_data_with_list(login=user_id, login_steam=False,
                                                        items={"HunterGroupC"})["HunterGroupC"]
    Progression_HunterGroupD = mongo.get_data_with_list(login=user_id, login_steam=False,
                                                        items={"HunterGroupD"})["HunterGroupD"]
    Progression_RunnerGroupA = mongo.get_data_with_list(login=user_id, login_steam=False,
                                                        items={"RunnerGroupA"})["RunnerGroupA"]
    Progression_RunnerGroupB = mongo.get_data_with_list(login=user_id, login_steam=False,
                                                        items={"RunnerGroupB"})["RunnerGroupB"]
    Progression_RunnerGroupC = mongo.get_data_with_list(login=user_id, login_steam=False,
                                                        items={"RunnerGroupC"})["RunnerGroupC"]
    Progression_RunnerGroupD = mongo.get_data_with_list(login=user_id, login_steam=False,
                                                        items={"RunnerGroupD"})["RunnerGroupD"]
    Progression_RunnerGroupE = mongo.get_data_with_list(login=user_id, login_steam=False,
                                                        items={"RunnerGroupE"})["RunnerGroupE"]
    Progression_RunnerGroupF = mongo.get_data_with_list(login=user_id, login_steam=False,
                                                        items={"RunnerGroupF"})["RunnerGroupF"]

    HunterGroups = [Progression_HunterGroupA, Progression_HunterGroupB, Progression_HunterGroupC,
                    Progression_HunterGroupD]
    RunnerGroups = [Progression_RunnerGroupA, Progression_RunnerGroupB, Progression_RunnerGroupC,
                    Progression_RunnerGroupD, Progression_RunnerGroupE, Progression_RunnerGroupF]
    hardcoded_challenges = new_challenge_handler.hard_code_challenges
    steam_achievements = new_challenge_handler.steam_achievements
    user_challenges = mongo.get_data_with_list(login=user_id, login_steam=False, items={"challengeProgression"})[
        "challengeProgression"]
    for runner_group in RunnerGroups:
        if runner_group is []:
            continue
        for runner_challenge in runner_group['pickedChallenges']:
            blueprint = runner_challenge["list"][0]["challengeAsset"]
            challenge_id = runner_challenge["list"][0]["challengeId"]
            challenge_found = False
            for int_challenge in user_challenges:
                if int_challenge["challengeId"] == challenge_id:
                    challenge_found = True
                    int_challenge["blueprint"] = blueprint
            if not challenge_found:
                new_challenge_handler.add_challenge_to_user(user_id, challenge_id, challenge_type="progression", blueprint=blueprint)

    for hunter_group in HunterGroups:
        if hunter_group is []:
            continue
        for hunter_challenge in hunter_group['pickedChallenges']:
            blueprint = hunter_challenge["list"][0]["challengeAsset"]
            challenge_id = hunter_challenge["list"][0]["challengeId"]
            challenge_found = False
            for int_challenge in user_challenges:
                if int_challenge["challengeId"] == challenge_id:
                    challenge_found = True
                    int_challenge["blueprint"] = blueprint
            if not challenge_found:
                new_challenge_handler.add_challenge_to_user(user_id, challenge_id)

    for challenge in hardcoded_challenges:
        challenge_found = False
        for int_challenge in user_challenges:
            if int_challenge["challengeId"] == challenge:
                challenge_found = True
        if not challenge_found:
            new_challenge_handler.add_challenge_to_user(user_id, challenge)
    for challenge in steam_achievements:
        challenge_found = False
        for int_challenge in user_challenges:
            if int_challenge["challengeId"] == challenge:
                challenge_found = True
        if not challenge_found:
            new_challenge_handler.add_challenge_to_user(user_id, challenge)
    update_achievement_challenges(user_id)


class ChallengeHandler:
    def __init__(self):
        # imported from challenge data weekly_challenges
        self.weekly_challenges = weekly_challenges
        # imported from challenge data daily_challenges
        self.daily_challenges = daily_challenges
        self.event_challenges = []
        self.steam_achievements = ["BA2D4A5445CB70276A8F5D9E1AFCE080","AAD05B9D46471DC811BBE0BA91916AB7",
                                   "E51981B946BEE3D45C5C41B2FCFF310B","2CAEBB354D506D7C43B941BC1DA775A0",
                                   "EFAB89E6465D1163D62A07B11048F2B6"]
        self.hard_code_challenges = ['400AE859456112F4EB7516A42821AEF3', '8DAE5C0943DA33C28E82FC92B9644702',
                                     '6DFAA85548F1C349CE1E6A9F29188FCF', 'A1047B3B49BFBF12313991A8FBB3E215',
                                     '6AFBAEC144C206BDBFD4F0B2216148B6', 'AB4B4E524F00B197156256AFACE501EF',
                                     '590D3041420289011FB868A89A43F7CF', 'CF29BA964B65E429DD2B559A4D335CD3',
                                     '32749AFC47E7C872933FC9AB8E76AD61', '9CD0EEEC4D2D193E168AD78026BFC6E3',
                                     '077EEED2433E763CEE4657B929E23043', 'EAC4FDA245A1B54CB15BE8926EB62E89',
                                     '0E7912E34B0F76F06A54769371A1615A', '8F2FD32744CCF967D64953B8C27B8B4C',
                                     '0502BFE9440E8A45212F4EBF2023368B', '7A25ABAE43856F2D5233F5A39CFAF921',
                                     '8046419A474EDC58A273FDA473064FF8', 'C9E2E88A4502470E1146629BBD79A876',
                                     '05DFDE95403708570292FE847BBA8EA2', '3941A0454830CAB53F4C6B993F1BC7B8',
                                     '836A4FD246B33F91BDC4C3A2608C6289', '721E2D644D051394207BC492127586CA',
                                     'ACB79B5049C283856BEA039BEF9952A1', 'ECAEAF9A4A2A0038999D738A7C9E502F',
                                     '92B4BBED409F403E37B844879B3AEB7A', 'F56098E54E0F19E6F67FB89C42212AB8',
                                     '1D7A66E34ECAF02BC243FB880323A6B8', 'A207A3624BEA90AE22A71BA08F529866',
                                     '35E18B6B48AC6D8022E13B88A3853F81', 'A00B9E6844C5ABFF86DB4FAA5B81CBC7',
                                     '1CA09F684C2F4464AA4C158F9BAA72D1', '5FE03903416D3BBE9D2FD592B36809FC',
                                     '0A5C2455485A166F60009FA3246504C4', '6871DC8B46D62AEFDE7FDCBC7B1AF9B4',
                                     'D8DBF1924EAEA4218A2110B54339E020', '9764321E4BC15FC21F0AD782BB98802A',
                                     '03A1382643FC39C99F58C6BB3FF4DB05', '85C7B811415DA97C04FB609BE76ACDF0',
                                     'A1F03DFD49F4100C2153CEAAF8EAF151', '4583917643CA36A950C56CA0FD5EBD82',
                                     '2BBECCBD478778B7D2A1B0AED3E46150', '2A5C401C49DE3F36D0D999983B2C5D98',
                                     '15317A48494297C052E6EFBB3DA122BF', 'D80A9221429E0A5FCD91DCB002D73482',
                                     '1D23B53D43864CD2CA8F1990B011DB16', '5129E6EE4DC7B2DCDF3C96A8E80910F3',
                                     '66E774454A815AE6E2A7FEA0B502ACD7', '676FAE5145065F8BBA15679F1E969C2B',
                                     '674BB4C7477253BA116C8CBE079E27D6', '15EA674043E212F8616A059D5297CB35',
                                     'F2C4067544A6B04B10FF6CB2C404BB55', 'E9C46086458C98543BBA0790979E1DF4',
                                     'FA07B43A4338C9246A1B02A7EED39599', 'DAFFE67D41200269194C65B9BCD7F32D',
                                     'AA2DE101478F3F59FBCA7C9B67EB8280', '049CDB464DF3A69EA626BF9593DF01F8',
                                     'E4A92BE94DA6CA174AD3F282FA512BA1', '2F143F5E4568F315134B928703F5E5D8',
                                     'F2A11BEC42ED900D1C8F10B90B7D658B', '2AFA685143848895C024E1B3AF427DE1',
                                     'C327A6394A86400943197881CFF49AD8', '5B9ED08049C7E6777E231D84F4EDBC91',
                                     '229F8DD3420F6E79CBBC5D87FD40243F', 'C3CEEED74144161D420801B656C5BB8D',
                                     'FF4AA7174BA721EA6B449AA8D7D2B70C', 'E32CC16A47F9C290EC993696079BB6DC',
                                     '0EAEAA3C494F4F47A35AF885FDAD8939', '43AB4B234479F0002C8D798F583CF6F4',
                                     '0DEBB34141DD7D719EE5C199707ED8E4', '0C7FE4CB479408600F00EDB83279C7D2',
                                     '4C48C95A4ED425708F038591BC28446D', '4A63E56745F10564D6111EABB309C47C',
                                     'AA290B6544528300C0B85A9A6B3FB6F7', '21B04F8E4D93BAE9A3550190FF918AD7',
                                     '589168EA42DE8131A4611ABD189B1EEF', '50EF445E456459E224013C8E2B24A336',
                                     '45D437BD4AD85F9477DD5593AAE9130F', 'ABCDD5744A0CB60A8F40FEABD293FE18',
                                     '9D59DA354BB511D4C7EE64B60B546A1B', 'FCB391DA4DAD486C8E31EABAE21EB19A',
                                     '508182E842C9BEFA20BE5488083716CC', 'A1DFB20F48B76A509B424599E30F8A0E',
                                     'F13B9B0F4BF97BB9C7023F90EF1C0594', 'EDED745B4523ADC54CD950BD8B238F6B',
                                     '87A39D494DF78A55D012B4BCA091E043', '164FAA5D41B127B316ABAD9E7DAAD674',
                                     '9F8EE83B438410496374ADA522F55713', '997A3A384F8156F76E9405ABA503DDEE',
                                     'D686CACE4B3C6C55F5BD9A80177D12AE', 'C987A00C4AB705897336E1A84899264B',
                                     '1FD7D2EB4616FC6F475D58AA8AF7F93B', '72718B874504A50CD3FA4385FB5523FF',
                                     'FA8F508E40A808178CE740940F817554', 'FDC959494B25E5982F050DAE6D312DF2',
                                     '4D5CCA7D42CD770262551591FB8D1C62', '8D8F602F4D0BFDE7B2A884A97D88F169',
                                     '702074B04572D0ECF67FA9BF1AE5DD7E', 'ADA907B24D8DCBD28848F18B6D15FF57',
                                     '9B3DF194466FF239257F1289F7BC4A71', '6E327F42491E3FC4FF0A77A0ECFDBF09',
                                     'F40221D745C692533271C3BDD63633A1', '0FFB7F6A41EBE9C6DB89108D46762F53',
                                     'F62DA5304F26F2F0FCDFFCB7DBA45398', '7F3CF15A48BE7AE1948698A7BD718D2E',
                                     'BC7EB2484D54F89131082FBCEDB1F34C', '77B930CE49352D062CCBD0A27C8E0F0A',
                                     'DB625B8B415DE703C5DB0698D1969A8E', 'A26AB1694E2CC8669D08CD8E5F4F64BE',
                                     '6049D85045161D075666E18DE4AFC772', '6B20937348A89A1A9E6CCB9EE09FC4DA',
                                     '2675258345FC8734A6CB0E98E02DE88A', '00C0407C47E60CDB558C67B153E75DB6',
                                     '4246C6904E8F91584CE55885C633683E', '9EFF069F492B3251D37FCD9BB813523C',
                                     'E3F005244D6BE2A392382F8CA270474F', '4555B2C545C8B41867FB9299306D3108',
                                     'FB6DFDE94DAE90B29C20F7A65FD4D050', 'AC14BF3547AB708F0D50C58C5440CFEB',
                                     '72A784C644E05E2631AB88883C1A11B1', 'D33B49BB4F79DE0F6E39BD94DA15FA23',
                                     'FBA3C3F3458AAD1B6D8199AF1451FE45', '3E4613F84B59697E68DE42A3B0E5F4CB',
                                     '9953E63E44CB478CAD903D82263F72B8', '86F2BDF74F433C03F8FE62B5C5F47AF9',
                                     'CDE15380452E06616D377190D2028AB7', 'D880BF184B480D714667688CC4D9D6C0',
                                     '69371CA0409766B1F0DAAC80A900893A', 'C8C05D874477C9A9413F9F9BF6BB29E8',
                                     '49C135BD4F919597CF8D3D99F5FC3E79', 'ACE6AD4440EFB8606FAC8282301CDBF5',
                                     '6F499FE24C36B15740613AB3200B5B4B', 'CC8DAF104B0229ADA48CF4A6784CC03A',
                                     '21CBC39E4B2D8C37439881A5879570EC', '9BB2D0A04B6B168325E9A080E84EBD05',
                                     'CF6113864077974B00CD37B51736426B', '608464EC41965D826856CEA1174CD757',
                                     '59DCADA849BC53D93DD04D9D63EF6351', '1D4401744D1CCCF2CE52628E0A6929A2',
                                     '1E01EC5A44B1016ED59E0ABD6C2FAF60', '153C237F41FFA085A7114795F0DB33FC',
                                     '164B28054A2E2DAEC8BF5C820AF4B9B2', '9878CAFC405F96494869F5AE145254FC',
                                     '067F39B3487120E9110DFFA181AB78B3', '89444BC84AA08F43E29B4DA1EB983561',
                                     'AA0018EC4461BE055CF7428554EC046F', 'A6941C2F42077160B5FFF49887ABD46C',
                                     '8CD20AD04CCF051497216F84AF29A327', '15BAB1914646A660541129B61394D930',
                                     '6F9FFCE24EE28E24EEF4C69E8FF69F99', 'A75399654B2523F75B30BAA3704B5898',
                                     '0A27212D496448FD389A1DA525E284CE', '919AD6964781C5FFED35F19DF9CB5560',
                                     'E8ED480C4FAD11C001A840AA53B55B4F', 'C08D9F6B4F6414A99BDB569495AA0A9B',
                                     '35368570459015AD1FD2F9A209909515', '46B1491D436AEBB823247297F4943066',
                                     '734B85884E566BD13FD2BDA148F6055C', 'E7B6132F461D5850A8D0738D87D54C0A',
                                     '310D7A264DC6FD62F67B3BAFE2E6876B', 'B4B156CC47C8D987B9BDBEB910B12C9E',
                                     '15C925544AA67E20214C8AB09F5B33E9', '950524C144BE794AABFFED8142C119B4',
                                     'F2D57F3443BF0F1A162ED8AF80A509D7', 'AF8CBA94413BCED1445D269F99D3F747',
                                     '885A5CBE4C36F665FA3296ABDD81D610', 'FD314A694D049989202D01BC36269F44',
                                     '0A728AD54AF5EAB6CB4356A074F01C1B', '688EC1704C4EA4BCB18181ADE23E2C3D',
                                     '4F99C43949B5CAC87BCEB4877B7FAB64', '2ABDC29A4D174CDC114AEBACB898927E',
                                     '37B650F145BF27B3B670CB9D84D58111', 'B0B11BDC4AF524274D6171A8BF605CF8',
                                     '9A0964D947748E6C0338AA9684DF1055', '22B70F5B49B3973D84DD9E9E621987BC',
                                     'ECCBA78D4055676F9C17D79B9D5FA2D4', '6CAD2AAC4C56C1224448C599A0E16119',
                                     'B54522334820602C6E998D9FD7E785BA', 'EE05AA53420DF8C7E43A1EACB7C407FE',
                                     'AACEE7044F69CED52B10F0AF6C70D433', 'B2B903254EB0C6ADAD59599C40A3C5FE',
                                     '8DF21FE8442BD778190141A9C9E06BC6', '9053883B41EBC8D6A9A8CA809D02845A',
                                     'B48B9B9743994F0AA12B82BAF69AE738', 'FB53A7E442EA53EA5727E4BA3611F45C',
                                     'A45C7DF44353DDAAF58F1EB1CAF954FF', 'C3C6528F4CA1D3D4B34235968746C223',
                                     'FD1AA64E41BA2576DBF566B436C256C6', '356CFA3942F21C3B64160D9942DF1C52',
                                     'AB8313E24DFB01401DEF5E92219A8965', '0AE15B56425FB92D3301D9932FED9D74',
                                     '831999A04EEA4635762B8A8606F0D4DD', '24424E874589E3D4582EF198EE7D1E42',
                                     '269DDC2D41013F0AD817C4ACA0BA139C', '2C4E3AB94438A43C81D515815ACB4C9D',
                                     'EFAA2DFC4C3AAEE70EB32697013003D7', '786DF18B48F5D69CA1BD558B5240A2EA',
                                     'AC2C19A94926471049C06DA3C519ADE9', 'C78F353F40FF62E7298ECD94086D78D7',
                                     '0C5A99E44EDD7325ED5BC687F75374DE', 'E239202F452ED0540F4479AFF248A3D4',
                                     '6F53D959409C9C2740F6789E221BCECF', 'F34255F3443EB1429FCA809DF2DFA012',
                                     '8BFB3FCD4432176BAAFB90BF65EB6165', 'F531602641251AEE39C024B3F85845FD',
                                     '23F0E5E7497912D11C520EA86348C114', '0D884DA743B3AFAA884DD3B7CFF0364D',
                                     '99B40C044F75D1324B48DCA4FAC3D5DF', '2D233F9F4106D8660D3D5D997E68EC0F',
                                     '7673C2D347769AAB0539D1B57E0928E3', '75885A2644B01B3CCA579E8B86159713',
                                     '444383D34E12F314623320B0E23CA691', 'EBF333814F32313057BC0AA50BF880FC',
                                     '55B032B147384D04065B39A0CC5D825D', 'DC70D1B746AF456C71FB29BFB27F356E',
                                     'A00E590E4EB9F479ACE7BD852BCBA78C', 'A734774F4E6162C9A60C4B9D537D0723',
                                     'D6C518B242C0F5C6ABDB32984C0970EF', '35898FD44E80FD68376F67A560E815BC',
                                     'E1BB40D145181323071EBBAAC924E4F5', 'CA2FE47E45EE792DFA26FFA3A30FC0A3',
                                     '0E514F8A467DB3E7DEBF99ABAC2313A0', 'DE92510443074D9DB518B7A93A3A2FD9',
                                     '6AD7B28E48E611BDAD2386940B2790AA', '5E5F70254373FB5C274AD9BA59A49E32',
                                     '9A5FDE8841D953C38AA5BBB47EEFB01D', '27A4E81B472948ED80142E8E6749F979',
                                     '99A6BD974F814624352257B2DDAAC3B7', '2CE18C86481989D772300DAD6D054A0C',
                                     'D635E5CE4EEF85664D87F490CF01B01E', '44EA40CE43D410AF19A687A993EF7EBC',
                                     'B5F0CB894653B2C56CED9E92C7BB1251', 'C40789F0410D07A6DFACCBB46A28EACB',
                                     '8894F68B4549F8F096812AB6896D48AC', 'AC5CED5D4D2F28952117F0B0EA0085E3',
                                     '48769C24490AE4488D7CCD906E283EEB', '82033B9F4033D82B4392779F3A986F09',
                                     '6246612A483F1C1D0D9AD48568591FDB', '4D6510D3474A414BE76C95A42D09024C',
                                     '8AD5A0194A0528BDC957EFABCFF03CA4', 'B78308DF48036BCF914060944AAF4A19',
                                     '24CE65364362CB2A90C0E08876176937', '6D79A03B4F3E4EDA33FAD69FF55289BA',
                                     '5B9CCC03408C7B49717192831A9E4288', '5D2E6D06498C0F005E0EF78E7580AAA9',
                                     '7E173CD547DB59D507CDD492C9F2CB93', 'DFA555C7452D8461CD412DA68D4FB301',
                                     '499EBA6443A83B4FE1F4F7AFE8EFE66E', '4212C3604C9FD931278E189EB962B5F1',
                                     'B0CB575B40C95E09484440B04BA36E08', 'FF8996344C73AADD1D2C1C9E26BD23EF',
                                     '2ACEB8984337D2518F010E9337EB656B', '5879F0FC4892D53FE2195AABA05EDA2A',
                                     'EED2F02B4A55B844E1B682804C84308D', '4A40EFB44EAC4CDEB16D8B8E7D6ECA8F',
                                     '92F65520408CBF8F52028FB3D83C6D5A', 'F2182D4C49439EEFDB38EAA2F35C5D9C',
                                     '83BE1ABF46705544813B42AC257A2A2C', 'BE19828E4910DB01722D3384A491DCAD',
                                     '0901F162440C086DB4E112956F7E651D', 'C6BA901346B618AB770225B3B48D6509',
                                     '34F4FE4C4825CB2E34D1CD8ADBF43312', '4BDF4B094F7B2FC939E21CA64F95A749',
                                     'D56D259A4F85D29F4F4164B8F27F3BB1', '605347B34E33EFAB829163AF16B6C0FB',
                                     '5E661D664FB8560D3519ECA53BB97ED2', '2D426791495793A662D1DBACCFAAE3CC',
                                     '290112D94B4F60152BAE088F9E942F1F']
        self.dev_logging = os.environ['DEV']

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
        #          "completed":False
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
        if challenge_type == "Daily":
            challenges = self.daily_challenges
        elif challenge_type == "Weekly":
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
        else:
            logger.graylog_logger(level="info", handler="get_time_based_challenges",
                                  message=f"No User Challenge Data Found")

        for challenge_id in challenges:

            if challenge_id not in user_time_challenges:
                current_challenge_data = self.add_challenge_to_user(userid, challenge_id, challenge_type)
            else:
                #if self.dev_logging:
                #    logger.graylog_logger(level="info", handler="get_time_based_challenges",
                #                          message=f"Data {user_data[user_time_challenges.index(challenge_id)]})")

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
                "challengeCompletionValue": challenges[challenge_id]["ChallengeCompletionValue"],
                "faction": challenges[challenge_id]["faction"],
                "challengeBlueprint": challenges[challenge_id]["challengeBlueprint"],
                "rewards": [get_reward(challenges[challenge_id]["challengeBlueprint"])]
            })

        return return_data

    def update_challenge(self, user_id, challenge_id, value=0, completed=False):
        user_data = mongo.get_data_with_list(login=user_id, login_steam=False, items={"challengeProgression"})[
            "challengeProgression"]
        hardcoded_challenges = self.hard_code_challenges
        writen_data = []
        returning = []
        for challenge in user_data:
            if challenge["challengeId"] == challenge_id:
                if completed:
                    challenge["completed"] = True
                    # todo: get reward
                    if challenge_id not in hardcoded_challenges:
                        data = get_reward(challenge["blueprint"])
                        returning.append(data)
                    else:
                        returning.append("/Engine/")
                else:
                    challenge["value"] = value
                    returning.append("/Engine/")
            writen_data.append(challenge)
        data = {"challengeProgression": writen_data}
        mongo.write_data_with_list(login=user_id, login_steam=False, items_dict=data)
        return returning

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
        #                "claimed":False
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
        #                "claimed":False
        #             }
        #          ]
        #       }
        #    ]
        # }
        pass

    #def generate_challenge(self, challenge_id):
    #    challengeCompletionValue = random.randint(1, 100)
    #    progression.append({"challengeId": challenge_id, "value": 0, "completed": False,
    #                        "challengeCompletionValue": challengeCompletionValue,
    #                        "lifetime": {"creationTime": "2019-11-25T02:17:22.484Z",
    #                                     "expirationTime": "2020-11-25T02:17:22.484Z"}})

    def add_challenge_to_user(self, user_id, challenge_id, challenge_type="progression", blueprint=None):
        user_challenge_data = \
            mongo.get_data_with_list(login=user_id, login_steam=False, items={"challengeProgression"})[
                "challengeProgression"]

        if user_challenge_data is None:
            user_challenge_data = []

        data = {
            "challengeId": challenge_id,
            "completed": False,
            "value": 0,
            # Seems like many functions rely on challengeType to exist
            "challengeType": challenge_type,
            #Difference in challeneType and className???
            "className": challenge_type,
            "blueprint": blueprint,
        }

        if challenge_type == "Weekly" or challenge_type == "Daily":
            data["lifetime"] = {
                "creationTime": "",
                "expirationTime": ""
            }
            data = update_challenge_time(data, challenge_type)

            data["challengeId"] = challenge_id + ":" + get_lifetime(challenge_type)[0]

        user_challenge_data.append(data)
        mongo.write_data_with_list(login=user_id, login_steam=False,
                                   items_dict={"challengeProgression": user_challenge_data})
        return data

    def get_progression_batch(self, challenge_id, userid):
        #combine challenge dicts and see if ID is in them
        #Should not alter anything if challenge_id is not a recognized challenge
        if challenge_id in self.daily_challenges or challenge_id in self.weekly_challenges:
            user_data = mongo.get_data_with_list(login=userid, login_steam=False, items={"challengeProgression"})[
                "challengeProgression"]
            for challenge in user_data:
                if challenge["challengeId"] == challenge_id:
                    if challenge["value"] == 0:
                        data = {"challengeId": challenge["challengeId"],
                                "completed": False}
                    else:
                        if challenge["completed"]:
                            reward_key = "rewardsClaimed"
                            # TEST should be rewardsClaimed
                        else:
                            reward_key = "rewards"
                        reward = get_reward(challenge["blueprint"])
                        data = {
                            "challengeId": challenge["challengeId"],
                            "className": "ChallengeProgressionCounter",
                            reward_key: [
                                reward
                            ],
                            "completed": challenge["completed"],
                            "schemaVersion": 1,
                            "value": challenge["value"]
                        }
                    if challenge["challengeType"] == "Daily":
                        create_time, expiration_time = get_lifetime("Daily")
                    elif challenge["challengeType"] == "Weekly":
                        create_time, expiration_time = get_lifetime("Weekly")
                    else:
                        return data
                    if create_time > challenge["lifetime"]["expirationTime"]:
                        challenge["completed"] = False
                        challenge["completion_count"] = challenge["completion_count"] + 1
                        challenge["lifetime"]["creationTime"] = create_time
                        challenge["lifetime"]["expirationTime"] = expiration_time
                        mongo.write_data_with_list(login=userid, login_steam=False,
                                                   items_dict={"challengeProgression": user_data})
                        return data
                    else:
                        start_data = challenge["lifetime"]["creationTime"]
                        expiration_date = challenge["lifetime"]["expirationTime"]
                        data["lifetime"] = {
                            "creationTime": start_data,
                            "expirationTime": expiration_date
                        }
                    return data

                    #if not found in user db_challenge create challenge
                else:
                    challenge_type = \
                        {**self.daily_challenges, **self.weekly_challenges, **challenge_data}[challenge_id]["challengeType"]

                    if challenge_type == "Daily":
                        create_time, expiration_time = get_lifetime("Daily")
                        self.add_challenge_to_user(userid, challenge_id, challenge_type)
                        return {"challengeId": challenge_id, "completed": False, "className": "Weekly",
                                "lifetime": {
                                    "creationTime": create_time,
                                    "expirationTime": expiration_time
                                },
                                "completion_count": 0}
                    if challenge_type == "Weekly":
                        create_time, expiration_time = get_lifetime("Weekly")
                        self.add_challenge_to_user(userid, challenge_id, challenge_type)
                        return {"challengeId": challenge_id, "completed": False, "className": "Weekly",
                                "lifetime": {
                                    "creationTime": create_time,
                                    "expirationTime": expiration_time
                                },
                                "completion_count": 0}
                    self.add_challenge_to_user(userid, challenge_id, challenge_type)
                    return {"challengeId": challenge_id, "completed": False}

        else:
            user_data = mongo.get_data_with_list(login=userid, login_steam=False, items={"challengeProgression"})["challengeProgression"]
            for challenge in user_data:
                if challenge["challengeId"] == challenge_id:
                    if challenge["value"] == 0:
                        data = {"challengeId": challenge["challengeId"],
                                "completed": False}
                    else:
                        if challenge["completed"]:
                            reward_key = "rewardsClaimed"
                            # TEST should be rewardsClaimed
                        else:
                            reward_key = "rewards"
                        if challenge["challengeId"] in self.hard_code_challenges:
                            try:
                                rewards = get_reward(challenge["blueprint"])
                            except KeyError:
                                rewards = {}
                                logger.graylog_logger(level="error", handler="get_progression_batch", message=f"Challenge {challenge_id} Blueprint Error.")

                        else:
                            rewards = {}
                        data = {
                            "challengeId": challenge["challengeId"],
                            "className": "ChallengeProgressionCounter",
                            reward_key: [
                                rewards
                            ],
                            "completed": challenge["completed"],
                            "schemaVersion": 1,
                            "value": challenge["value"]
                        }
                    return data
            # disabled because the API takes a long time to print but is very fast to run
            #logger.graylog_logger(level="info", handler="get_progression_batch", message=f"Challenge {challenge_id} not found in user data")
            #A lot of challenges are sent that are not in challenge_data
            #Add them anyways
            # if challenge_id not in db_challenge:
            #    self.add_challenge_to_user(userid, challenge_id, "ChallengeProgressionCounter")
            return {"challengeId": challenge_id, "completed": False}

    # def login_update_time(self, userId):
    #    for challenge_int in self.daily_challenges:
    #        for challenge in progression:
    #            if challenge['challengeId'] == challenge_int:
    #                if challenge['lifetime']['expirationTime'] < get_lifetime("daily")[1]:
    #                    challenge['lifetime']['expirationTime'] = get_lifetime("daily")[1]
    #                    challenge['lifetime']['creationTime'] = get_lifetime("daily")[0]
    #    for challenge_int in self.weekly_challenges:
    #        for challenge in progression:
    #            if challenge['challengeId'] == challenge_int:
    #                if challenge['lifetime']['expirationTime'] < get_lifetime("weekly")[1]:
    #                    challenge['lifetime']['expirationTime'] = get_lifetime("weekly")[1]
    #                    challenge['lifetime']['creationTime'] = get_lifetime("weekly")[0]

    #def update_progression(challengeId, value):
    #    for challenge_int in progression:
    #        if challenge_int['challengeId'] == challengeId:
    #            challenge_int['value'] = value

    #def complete_challenge(challengeId):
    #    for challenge_int in progression:
    #        if challenge_int['challengeId'] == challengeId:
    #            challenge_int['completed'] = True

    #def get_challenge(challengeId):
    #    for challenge_int in progression:
    #        if challenge_int['challengeId'] == challengeId:
    #            return challenge_int
    #    return None

    #def generate_execute_response(userid, challengeId, value):
    #    update_progression(challengeId, value)
    #    challenge_int = get_challenge(challengeId)
    #    if value >= challenge_int['challengeCompletionValue']:
    #        complete_challenge(challengeId)
    #        return {"userId": userid, "challengeId": challengeId, "value": value, "completed": True}
    #    return {"userId": userid, "challengeId": challengeId, "value": value, "completed": False}


new_challenge_handler = ChallengeHandler()
