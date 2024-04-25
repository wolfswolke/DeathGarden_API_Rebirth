import math

from flask_definitions import *

# 'RunnerGroupA': {
#                 'prestige': 0,
#                 'experience': {
#                     'level': 1,
#                     'experienceToReach': 5403,
#                     'currentExperience': 0
#                 },
#             },
#             'RunnerGroupB': {
#                 'prestige': 0,
#                 'experience': {
#                     'level': 1,
#                     'experienceToReach': 5403,
#                     'currentExperience': 0
#                 },
#             },
#             'RunnerGroupC': {
#                 'prestige': 0,
#                 'experience': {
#                     'level': 1,
#                     'experienceToReach': 5403,
#                     'currentExperience': 0
#                 },
#             },
#             'RunnerGroupD': {
#                 'prestige': 0,
#                 'experience': {
#                     'level': 1,
#                     'experienceToReach': 5403,
#                     'currentExperience': 0
#                 },
#             },
#             'RunnerGroupE': {
#                 'prestige': 0,
#                 'experience': {
#                     'level': 1,
#                     'experienceToReach': 5403,
#                     'currentExperience': 0
#                 },
#             },
#             'RunnerGroupF': {
#                 'prestige': 0,
#                 'experience': {
#                     'level': 1,
#                     'experienceToReach': 5403,
#                     'currentExperience': 0
#                 },
#             },
#             'HunterGroupA': {
#                 'prestige': 0,
#                 'experience': {
#                     'level': 1,
#                     'experienceToReach': 5403,
#                     'currentExperience': 0
#                 },
#             },
#             'HunterGroupB': {
#                 'prestige': 0,
#                 'experience': {
#                     'level': 1,
#                     'experienceToReach': 5403,
#                     'currentExperience': 0
#                 },
#             },
#             'HunterGroupC': {
#                 'prestige': 0,
#                 'experience': {
#                     'level': 1,
#                     'experienceToReach': 5403,
#                     'currentExperience': 0
#                 },
#             },
#             'HunterGroupD': {
#                 'prestige': 0,
#                 'experience': {
#                     'level': 1,
#                     'experienceToReach': 5403,
#                     'currentExperience': 0
#                 },
#             },
#             'RunnerProgression':{
#                 "experience": {
#                     "level": 1,
#                     "experienceToReach": 5,
#                     "currentExperience": 3
#                 }
#             },
#             'HunterProgression': {
#                 "experience": {
#                     "level": 1,
#                     "experienceToReach": 5,
#                     "currentExperience": 3
#                 }
#             },
#             'PlayerProgression': {
#                 "experience": {
#                     "level": 1,
#                     "experienceToReach": 5,
#                     "currentExperience": 3
#                 }
#             },
#             'ProfileMetaData': {
#                 'characterCumulativeExperience': 0
#             }

def get_xp_for_new_level(level):
    xp = 5000 * 1.2 ** level - 1
    xp = math.ceil(xp)
    return xp

def update_user_xp(user_id, xp, characterGroup):
    # todo Find out what PlayerProgression, HunterProgression and RunnerProgression are
    user_data_raw = mongo.get_data_with_list(login=user_id, login_steam=False, items={characterGroup, "ProfileMetaData"})
    user_data = user_data_raw[characterGroup]
    profile_meta_data = user_data_raw['ProfileMetaData']
    current_xp = user_data['experience']['currentExperience']
    new_experience = current_xp + xp
    if new_experience >= user_data['experience']['experienceToReach']:
        overflow = new_experience - user_data['experience']['experienceToReach']
        user_data['experience']['level'] += 1
        user_data['experience']['experienceToReach'] = get_xp_for_new_level(user_data['experience']['level'])
        user_data['experience']['currentExperience'] = overflow
    else:
        user_data['experience']['currentExperience'] = new_experience
    profile_meta_data['characterCumulativeExperience'] += xp
    mongo.write_data_with_list(login=user_id, login_steam=False, items_dict={characterGroup: user_data,
                                                                             "ProfileMetaData": profile_meta_data})
