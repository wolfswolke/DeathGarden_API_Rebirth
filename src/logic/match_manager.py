from time import time
import uuid


class Match:
    def __init__(self, match_uuid, json_dict):
        self._match_uuid = match_uuid
        self.time_created = time()
        self.users = json_dict.get("Players")
        self.rank = json_dict.get("Rank")
        self.category = json_dict.get("Category")
        self.exclude_friends = json_dict.get("ExcludeFriends")
        self.exclude_clan_members = json_dict.get("ExcludeClanMembers")
        self.status = json_dict.get("Status")
        self.creator = json_dict.get("Creator")
        self.players_side_a = json_dict.get("SideA")
        self.players_side_b = json_dict.get("SideB")
        self.custom_data = json_dict.get("CustomData")
        self.props = json_dict.get("Props")
        self.schema = json_dict.get("Schema")


class MatchManager:
    def __init__(self):
        self._matches = {}
        self._queue_dict = {}

    def create_match(self, json_dict):
        self.cleanup()
        match_id = str(uuid.uuid4())
        match = Match(match_id, json_dict)
        self._matches[match_id] = match
        return match_id

    def find_match_id_from_user(self, user_id):
        self.cleanup()
        for match_id, match in self._matches.items():
            if user_id in match.users:
                return match
        return None

    def find_json_with_match_id(self, match_id):
        self.cleanup()
        match = self._matches.get(match_id)
        if match:
            return match
        return None

    def cleanup(self):
        match_ids = self._matches.keys()
        for match_id, match in match_ids:
            if time() - match.time_created > 60 * 1:
                del self._matches[match_id]

    def delete_match(self, match_id):
        del self._matches[match_id]

    def find_eta_and_position(self, match_id):
        self.cleanup()
        match = self._matches.get(match_id)
        if match:
            queue_list = list(self._matches.values())
            rank_x_matches = [m for m in queue_list if m.rank == match.rank]
            rank_x_matches.sort(key=lambda m: m.time_created)
            eta = rank_x_matches.index(match) * 5
            position = rank_x_matches.index(match) + 1
            return eta, position
        return None, None

    def players_searching_for_match(self, user_id, catagory, region):
        self.cleanup()
        queue = self._queue_dict
        players_a = []
        players_b = []
        for key, value in queue.items():
            if key == "B":
                players_b.append(value)
            else:
                players_a.append(value)

        if user_id in self._queue_dict.items():
            json_dict = {{'category': catagory, 'region': region, 'playersA': [players_b],
                         'playersB': [players_b],
                         'props': {
                             'MatchConfiguration': '/Game/Configuration/MatchConfig/MatchConfig_Demo.MatchConfig_Demo'},
                         'latencies': []}}
            self.create_match(json_dict)

        else:
            self._queue_dict[user_id] = user_id


match_manager = MatchManager()
