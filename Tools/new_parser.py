import os
import json

base_template = {
    "Result": []
}
def normalize_data(json_data, prev_guid, next_guid, is_weapon):
    normalized_data_list = []
    for item_data in json_data:
        normalized_data = {
            "Id": item_data.get("Properties", {}).get("Guid"),
            "DisplayName": item_data.get("Properties", {}).get("DisplayName", {}).get("Key"),
            "Purchasable": True,
            "Consumable": False,
            "IsWeapon": is_weapon,
            "InitialQuantity": 1,
            "DefaultCost": item_data.get("Properties", {}).get("DefaultCost"),
            "MetaData": {
                "GameplayTags": [],
                "MinPlayerLevel": 1,
                "MinCharacterLevel": 1,
                "Origin": "None",
                "PrerequisiteItem": prev_guid,
                "FollowingItem": next_guid,
            },
            "Faction": "",
            "GameplayTagContainer": {},
            "Gender": item_data.get("Properties", {}).get("Gender")
        }
        normalized_data["MetaData"]["GameplayTags"] = []
        for tag in item_data.get("Properties", {}).get("TagContainer", []):
            normalized_data["MetaData"]["GameplayTags"].append({"TagName": tag})
        if item_data.get("Properties", {}).get("TagContainer"):
            try:
                normalized_data["GameplayTagContainer"] = {"GameplayTags": [{"TagName": item_data.get("Properties", {}).get("TagContainer")[0]}],"ParentTags": [{"TagName": item_data.get("Properties", {}).get("TagContainer")[1]}]}
            except IndexError:
                normalized_data["GameplayTagContainer"] = {"ParentTags": [{"TagName": item_data.get("Properties", {}).get("TagContainer")[0]}]}
                # normalized_data.pop("GameplayTagContainer")
        tag_query = item_data.get("Properties", {}).get("TagQuery", {})
        char_tag = item_data.get("Properties", {}).get("GameplayTags", {})

        if not item_data.get("IsWeapon"):
            normalized_data["IsWeapon"] = False

        if normalized_data["MetaData"]["FollowingItem"] == "":
            normalized_data["MetaData"].pop("FollowingItem")
        if normalized_data["MetaData"]["PrerequisiteItem"] == "":
            normalized_data["MetaData"].pop("PrerequisiteItem")
        if not normalized_data["DefaultCost"]:
            normalized_data.pop("DefaultCost")
        else:
            for item in normalized_data["DefaultCost"]:
                # {'CurrencyId': 'EGMCurrency::CurrencyB', 'Price': 310}
                item["CurrencyId"] = item["CurrencyId"].replace("EGMCurrency::", "")

        faction = has_class_runner(tag_query)

        if not normalized_data["Gender"]:
            normalized_data.pop("Gender")

        if faction:
            normalized_data["Faction"] = faction
        else:
            char_tag = has_class_runner(char_tag)
            if char_tag:
                normalized_data["Faction"] = char_tag
            else:
                normalized_data.pop("Faction")
        if not normalized_data["Id"] or not normalized_data["DisplayName"]:
            normalized_data = None
        if normalized_data:
            normalized_data_list.append(normalized_data)
    return normalized_data_list


def has_class_runner(tag_query):
    if "TagQuery" in tag_query:
        tag_dictionary = tag_query["TagQuery"].get("TagDictionary", [])
        for tag in tag_dictionary:
            if "TagName" in tag and tag["TagName"] == "Class.Runner":
                return "Runner"
            elif "TagQuery" in tag and tag["TagName"] == "Class.Hunter":
                if has_class_runner(tag["TagQuery"]):
                    return "Hunter"
            else:
                return None
    else:
        for item in tag_query:
            if item == "Class.Runner":
                return "Runner"
            elif item == "Class.Hunter":
                return "Hunter"
    return False


def get_guid(json_data):
    try:
        return json_data.get("Properties", {}).get("Guid")
    except AttributeError:
        for item in json_data:
            if item.get("Properties", {}).get("Guid"):
                return item.get("Properties", {}).get("Guid")
            else:
                return ""
        #data = json_data[2]
        # return data.get("Properties", {}).get("Guid")


def get_next_and_prev_guid(file_path, file_name):
    print(f"Entered get_next_and_prev_guid with file_path: {file_path} and file_name: {file_name}")
    if "_001.json" in file_name:
        with open(file_path.replace("_001.json", "_002.json"), 'r') as json_file:
            next_json_data = json.load(json_file)
            next_guid = get_guid(next_json_data)
        return "", next_guid
    elif "_Item.json" in file_name:
        with open(file_path.replace("_Item.json", "_002.json"), 'r') as json_file:
            next_json_data = json.load(json_file)
            next_guid = get_guid(next_json_data)
        return "", next_guid

    elif "_010.json" in file_name:
        with open(file_path.replace("_010.json", "_009.json"), 'r') as json_file:
            prev_json_data = json.load(json_file)
            prev_guid = get_guid(prev_json_data)
            next_guid = ""
        return prev_guid, next_guid
    elif "_009.json" in file_name:
        with open(file_path.replace("_009.json", "_008.json"), 'r') as json_file:
            prev_json_data = json.load(json_file)
            prev_guid = get_guid(prev_json_data)
        with open(file_path.replace("_009.json", "_010.json"), 'r') as json_file:
            next_json_data = json.load(json_file)
            next_guid = get_guid(next_json_data)
        return prev_guid, next_guid
    else:
        try:
            current_num = file_name[-6:]
            current_num = int(current_num[0])
        except ValueError:
            return "", ""
        with open(file_path.replace(f"_00{current_num}.json", f"_00{current_num+1}.json"), 'r') as json_file:
            next_json_data = json.load(json_file)
            next_guid = get_guid(next_json_data)
        try:
            print("File found")
            with open(file_path.replace(f"_00{current_num}.json", f"_00{current_num-1}.json"), 'r') as json_file:
                prev_json_data = json.load(json_file)
                prev_guid = get_guid(prev_json_data)
        except FileNotFoundError:
            print("File not found")
            with open(file_path.replace(f"_00{current_num}.json", f"_Item.json"), 'r') as json_file:
                prev_json_data = json.load(json_file)
                prev_guid = get_guid(prev_json_data)

        return prev_guid, next_guid


def process_folder(folder_path):
    print("Processing folder: " + folder_path)
    catalog_data = []

    for root, _, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.json'):
                print("Processing file: " + file_name)
                file_path = os.path.join(root, file_name)
                with open(file_path, 'r') as json_file:
                    json_data = json.load(json_file)
                    print(f"Current PATH: {file_path}")
                    if file_path.startswith("./Items\Runners\Character\Items_Released\Perks") or file_path.startswith("./Items\Hunters\Character\Items_Released\Perks") or file_path.startswith("./Items\Hunters\Character\Items_Released\Powers"):
                        try:
                            prev_guid, next_guid = get_next_and_prev_guid(file_path, file_name)
                        except FileNotFoundError:
                            continue
                    else:
                        prev_guid = ""
                        next_guid = ""
                    if file_path.startswith("./Items\Runners\Character\Items_Released\Weapons") or file_path.startswith("./Items\Hunters\Character\Items_Released\Weapons"):
                        is_weapon = True
                    else:
                        is_weapon = False

                    normalized_data = normalize_data(json_data, prev_guid, next_guid, is_weapon)
                    if normalized_data:
                        catalog_data.append(normalized_data)
                    else:
                        print(f"Skipping file: {file_name}")

    return catalog_data

main_folder = './Items'
runner_folder = os.path.join(main_folder, 'Runners')
hunter_folder = os.path.join(main_folder, 'Hunters')

runner_catalog_data = process_folder(runner_folder)
hunter_catalog_data = process_folder(hunter_folder)

catalog_data = runner_catalog_data + hunter_catalog_data

catalog_file_path = 'catalog.json'
with open(catalog_file_path, 'w') as catalog_file:
    base_template["Result"] = catalog_data
    json.dump(base_template, catalog_file, indent=4)

print("Catalog JSON file created successfully.")
