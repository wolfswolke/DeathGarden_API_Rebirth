import datetime


class ItemCost:
    currency_id: str  # Can be "CurrencyA", "CurrencyB" or  "CurrencyC"
    price: int

    def __init__(self, currency_id, price):
        self.currency_id = currency_id
        self.price = price


class GameplayTag:
    tag_name: str

    def __init__(self, tag_name):
        self.tag_name = tag_name


class GameplayTagContainer:
    gameplay_tags: list[GameplayTag]
    parent_tags: list[GameplayTag]


class MetaData:
    gameplay_tags: list[GameplayTag]
    bundle_items: list[str]
    reward_bundle_items: list[str]
    required_challenges_to_complete: list[str]
    bundle_part_of: str
    prerequisite_item: str
    following_item: str
    bundle_discount_percent: int
    min_player_level: int
    min_character_level: int
    origin: str


class TerminalStyle:
    RED = "\033[31m"
    GREEN = "\033[32m"
    BLUE = "\033[34m"
    RESET = "\033[0m"
