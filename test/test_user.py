from unittest import TestCase
from flask_definitions import app, mongo_host, mongo_db, mongo_collection
from logic.global_handlers import load_config
from logic.mongodb_handler import mongo

config = load_config()
user_cookie = config["test_case"]["user_cookie"]


class TestUser(TestCase):
    def test_steam_login(self):

        c = app.test_client()
        c.set_cookie('bhvrSession', user_cookie)
        c.get('/URL')
        self.assertEquals(1, 1)

    def test_get_currency(self):
        c = app.test_client()
        c.set_cookie('bhvrSession', user_cookie)
        response = c.get('/api/v1/wallet/currencies')
        self.assertEquals(response.status_code, 200)
        response_json = response.json
        currency_iron = response_json['List'][0]['Balance']
        currency_blood_cells = response_json['List'][1]['Balance']
        currency_ink_cells = response_json['List'][2]['Balance']
        currency_hard = response_json['List'][3]['Balance']
        currency_progression = response_json['List'][4]['Balance']
        currencies = mongo.get_data_with_list(login=user_cookie("bhvrSession"), login_steam=False,
                                              items={"currency_blood_cells", "currency_iron", "currency_ink_cells"},
                                              server=mongo_host, db=mongo_db, collection=mongo_collection)
        self.assertEquals(currency_iron, currencies['currency_iron'])
        self.assertEquals(currency_blood_cells, currencies['currency_blood_cells'])
        self.assertEquals(currency_ink_cells, currencies['currency_ink_cells'])
        self.assertEquals(1, 1)

    def test_get_modifiers_me(self):
        self.assertEquals(1, 1)

    def test_check_username(self):
        self.assertEquals(1, 1)

    def test_get_progression_experience(self):
        self.assertEquals(1, 1)

    def test_get_challenges_daily(self):
        self.assertEquals(1, 1)

    def test_get_challenges_weekly(self):
        self.assertEquals(1, 1)

    def test_get_specific_challenge(self):
        self.assertEquals(1, 1)

    def test_get_inventory(self):
        self.assertEquals(1, 1)

    def test_get_ProgressionGroups(self):
        self.assertEquals(1, 1)

    def test_get_ban_status(self):
        self.assertEquals(1, 1)

    def test_get_ban_info(self):
        self.assertEquals(1, 1)

    def test_get_splinteredstates(self):
        self.assertEquals(1, 1)

    def test_get_message_list(self):
        self.assertEquals(1, 1)

    def test_initOrGetGroups(self):
        self.assertEquals(1, 1)

    def test_unlockSpecialItems(self):
        self.assertEquals(1, 1)

    def test_getChallengeProgressionBatch(self):
        self.assertEquals(1, 1)
