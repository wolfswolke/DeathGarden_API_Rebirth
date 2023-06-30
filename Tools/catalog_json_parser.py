import json
import os
import sys
output = []


def create_structure(id, display_name, currency, price, tag):
    gameplay_tag = tag[1]
    parent_tag = tag[0]
    return_val = {
         "Id":id,
         "DisplayName":display_name,
         "Purchasable":True,
         "Consumable":False,
         "IsWeapon":False,
         "InitialQuantity":1,
         "DefaultCost":[
            {
               "CurrencyId":currency,
               "Price":price
            }
         ],
         "MetaData":{
            "GameplayTags":[
               {
                  "TagName":gameplay_tag
               }
            ],
            "MinPlayerLevel":1,
            "MinCharacterLevel":1,
            "Origin":"None"
         },
         "Faction":"Runner",
         "GameplayTagContainer":{
            "GameplayTags":[
               {
                  "TagName": parent_tag
               }
            ],
            "ParentTags":[
               {
                  "TagName":gameplay_tag
               }
            ]
         }
      }
    global output
    output.append(return_val)


def create_structure_Vambraces(guid, display_name, currency_id, price, tag, faction):

    gameplay_tag = tag[1]
    parent_tag = tag[0]
    return_val = {
         "Id":guid,
         "DisplayName":display_name,
         "Purchasable":True,
         "Consumable":False,
         "IsWeapon":False,
         "InitialQuantity":1,
         "DefaultCost":[
            {
               "CurrencyId":currency_id,
               "Price":price
            }
         ],
         "MetaData":{
            "GameplayTags":[
               {
                  "TagName":parent_tag
               }
            ],
            "MinPlayerLevel":1,
            "MinCharacterLevel":1,
            "Origin":"None"
         },
         "Faction":"Runner",
         "GameplayTagContainer":{
            "GameplayTags":[
               {
                  "TagName": parent_tag
               }
            ],
            "ParentTags":[
               {
                  "TagName":gameplay_tag
               }
            ]
         },
          "CustomizationGameplayTagByFaction": [
              "Runner",
              {
                  "TagName": faction
              }
          ],
          "Gender": "Male"
      }
    global output
    output.append(return_val)


def get_json(data):
    try:
        for item in data:
            try:
                guid = item["Properties"]["Guid"]
                tag_container = item["Properties"]["TagContainer"]
                try:
                    currency_id = item["Properties"]["DefaultCost"][0]["CurrencyId"]
                    price = item["Properties"]["DefaultCost"][0]["Price"]
                except KeyError:
                    currency_id = "CurrencyA"
                    price = 10
                display_name = item["Properties"]["DisplayName"]["Key"]
                create_structure(guid, display_name, currency_id, price, tag_container)
            except KeyError as e:
                if e == "Properties":
                    guid = item["Guid"]
                    tag_container = item["TagContainer"]
                    try:
                        currency_id = item["DefaultCost"][0]["CurrencyId"]
                        price = item["DefaultCost"][0]["Price"]
                    except KeyError:
                        currency_id = "CurrencyA"
                        price = 10
                    display_name = item["DisplayName"]["Key"]
                    faction = item["TagQuery"]["TagDictionary"]["TagName"]
                    create_structure_Vambraces(guid, display_name, currency_id, price, tag_container, faction)
            except Exception as e:
                print("Error Type: {}".format(type(e)), file=sys.stderr)
                print("Error: {}".format(e), file=sys.stderr)
                return None

    except Exception as e:
        print("Error Type: {}".format(type(e)), file=sys.stderr)
        print("Error: {}".format(e), file=sys.stderr)
        return None


if __name__ == "__main__":
    for items in os.listdir("./ItemsToParse"):
        with open("./ItemsToParse/" + items, "r") as file:
            print("Start parsing file: {}".format(items), file=sys.stdout)
            data = json.load(file)
            get_json(data)
    print(output)

