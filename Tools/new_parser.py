import json
import os

output = []
path = os.path.join(os.getcwd(), "Items")


class CATALOG:

    def __init__(self):
        self.IsWeapon = False
        self.id = ""
        self.display_name = ""
        self.default_cost = []
        self.gameplay_tag = ""
        self.gameplay_tag_character = ""
        self.parent_tag = ""
        self.PrerequisiteItem = ""
        self.FollowingItem = ""
        self.faction = ""
        self.faction_tag = ""
        self.gender = ""
        self.template ={
         "Id": self.id,
         "DisplayName": self.display_name,
         "Purchasable":True,
         "Consumable":False,
         "IsWeapon":self.IsWeapon,
         "InitialQuantity":1,
         "DefaultCost":self.default_cost,
         "EventCostList": [
                    {
                      "Name": self.display_name,
                      "StartDate": "2020-05-13T00:00:00",
                        "EndDate": "2027-05-19T23:59:59",
                      "Cost": self.default_cost
                    }
                  ],
         "MetaData":{
            "GameplayTags":[
               {
                  "TagName": self.gameplay_tag_character
               }
            ],
            "MinPlayerLevel":1,
            "MinCharacterLevel":1,
            "Origin":"None",
           "PrerequisiteItem": self.PrerequisiteItem,
           "FollowingItem": self.FollowingItem
         },
         "Faction":self.faction,
         "GameplayTagContainer":{
            "GameplayTags":[
               {
                  "TagName": self.gameplay_tag
               }
            ],
            "ParentTags":[
               {
                  "TagName":self.parent_tag
               }
            ]
      },
                "CustomizationGameplayTagByFaction": {
            "Runner": {
        "TagName": self.faction_tag
      }
          },
          "Gender": self.gender
   }

    def create_structure(self):
        self.template["IsWeapon"] = False
        self.template["id"] = ""
        self.template["display_name"] = ""
        self.template["default_cost"] = []
        self.template["gameplay_tag"] = ""
        self.template["gameplay_tag_character"] = ""
        self.template["parent_tag"] = ""
        self.template["PrerequisiteItem"] = ""
        self.template["FollowingItem"] = ""
        self.template["faction"] = ""
        self.template["faction_tag"] = ""
        self.template["gender"] = ""

    def parse_json_data(self, json_data):
        for item in json_data:
            catalog_item = CATALOG()

            catalog_item.id = item.get("id", "")
            catalog_item.display_name = item.get("display_name", "")
            catalog_item.default_cost = item.get("default_cost", [])
            catalog_item.gameplay_tag = item.get("gameplay_tag", "")
            catalog_item.gameplay_tag_character = item.get("gameplay_tag_character", "")
            catalog_item.parent_tag = item.get("parent_tag", "")
            catalog_item.PrerequisiteItem = item.get("PrerequisiteItem", "")
            catalog_item.FollowingItem = item.get("FollowingItem", "")
            catalog_item.faction = item.get("faction", "")
            catalog_item.faction_tag = item.get("faction_tag", "")

            catalog_item.create_structure()

            output.append(catalog_item)

    def parse_json_file(self, file_path):
        with open(file_path, 'r') as json_file:
            json_data = json.load(json_file)
        return json_data

    def parse_json_files_in_directory(self, directory_path):
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith('.json'):
                    file_path = os.path.join(root, file)
                    json_data = self.parse_json_file(file_path)
                    self.parse_json_data(json_data)


catalog = CATALOG()

catalog.parse_json_files_in_directory(path)
print(json.dumps(output, indent=4))
