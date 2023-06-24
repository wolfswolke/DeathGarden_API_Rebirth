import glob
import json
import os

from ItemClasses import *


class ItemResult:
    id: str
    display_name: str
    purchasable: bool = True
    consumable: bool = False
    is_weapon: bool = False
    initial_quantity: int
    default_cost: list[ItemCost]
    meta_data: MetaData
    faction: str  # Either "Runner" or "Hunter"
    gameplay_tags_container: GameplayTagContainer
    customization_gameplay_tag_by_faction: list
    gender: str

