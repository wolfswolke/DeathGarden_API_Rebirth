from datetime import datetime


class Presence:
    def __init__(self):
        self.user_id = None
        self.userType = None
        self.gameState = None
        self.last_updated = None


class RichPresenceHandler:

    def __init__(self):
        self.presence = {}

    def update_presence(self, user_id, user_type, game_state):
        if user_id not in self.presence:
            self.presence[user_id] = Presence()
        self.presence[user_id].user_id = user_id
        self.presence[user_id].userType = user_type
        self.presence[user_id].gameState = game_state
        self.presence[user_id].last_updated = datetime.now()

    def cleanup_presence(self):
        for user_id in list(self.presence.keys()):
            # if user has not checked in the last 2 min remove
            if (datetime.now() - self.presence[user_id].last_updated).seconds > 120:
                del self.presence[user_id]

    def get_presence_length(self):
        self.cleanup_presence()
        return len(self.presence)

    def get_presence(self):
        self.cleanup_presence()
        return self.presence

    def get_arena_presence(self):
        self.cleanup_presence()
        return len({k: v for k, v in self.presence.items() if v.gameState == "Arena"})

    def get_locker_room_presence(self):
        self.cleanup_presence()
        return len({k: v for k, v in self.presence.items() if v.gameState == "LockerRoom"})


rich_presence_handler = RichPresenceHandler()
