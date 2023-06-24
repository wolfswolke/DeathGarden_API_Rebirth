import glob
import json
import os

from ItemClasses import *


class ItemResult:
    id: str
    display_name: str
    purchasable: bool = True  # always true
    consumable: bool = False  # always false
    is_weapon: bool = False # only in abilities nad hunter weapons
    initial_quantity: int
    default_cost: list[ItemCost] = []
    meta_data: MetaData = MetaData()
    faction: str  # Either "Runner" or "Hunter"
    gameplay_tags_container: GameplayTagContainer
    customization_gameplay_tag_by_faction: list
    gender: str


def create_not_found_message(key: str, object_index) -> str:
    return f'{key} not Found in object {TerminalStyle.BLUE + object_index}'

def parse_file(file_path: str):
    new_item: ItemResult = ItemResult()
    file = open(file_path)
    json_data: json = json.load(file)

    try:


    except Exception as e:
        print(f"{TerminalStyle.RED}could not parse file: {filename}\nFor reason: {e}")


for filename in glob.iglob("./ItemsToParse/**", recursive=True):
    if os.path.isfile(filename):
        print("Start parsing file: {}".format(filename))
        parse_file(filename)
