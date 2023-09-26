import os
import json

# Define your base template here
base_template = {
    "Result": []
}

# Function to normalize JSON data based on your template
def normalize_data(json_data, prev_guid, next_guid):
    normalized_data = {
        "Id": json_data.get("GUID"),
        "DisplayName": json_data.get("DisplayName"),
        "Purchasable": True,
        "Consumable": False,
        "IsWeapon": json_data.get("IsWeapon"),
        "InitialQuantity": json_data.get("InitialQuantity"),
        "DefaultCost": json_data.get("DefaultCost"),
        "MetaData": {
            "GameplayTags": json_data.get("MetaData", {}).get("GameplayTags"),
            "MinPlayerLevel": json_data.get("MetaData", {}).get("MinPlayerLevel"),
            "MinCharacterLevel": json_data.get("MetaData", {}).get("MinCharacterLevel"),
            "Origin": json_data.get("MetaData", {}).get("Origin"),
            "PrerequisiteItem": prev_guid,
            "FollowingItem": next_guid,
        },
        "Faction": json_data.get("Faction"),
        "GameplayTagContainer": json_data.get("GameplayTagContainer")
    }
    return normalized_data

# Function to process and normalize JSON files in a given directory
def process_folder(folder_path):
    catalog_data = []

    for root, _, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.json'):
                file_path = os.path.join(root, file_name)
                with open(file_path, 'r') as json_file:
                    json_data = json.load(json_file)
                    # Check if it's an item with levels
                    if "_002.json" in file_name:
                        prev_guid = file_name.replace("_002.json", "_001.json")
                        next_guid = file_name.replace("_002.json", "_003.json")
                    else:
                        prev_guid = ""
                        next_guid = ""
                    normalized_data = normalize_data(json_data, prev_guid, next_guid)
                    catalog_data.append(normalized_data)

    return catalog_data

# Traverse the main directory for Runner and Hunter folders
main_folder = './Items'
runner_folder = os.path.join(main_folder, 'Runner')
hunter_folder = os.path.join(main_folder, 'Hunter')

# Process and normalize JSON files in Runner and Hunter folders
runner_catalog_data = process_folder(runner_folder)
hunter_catalog_data = process_folder(hunter_folder)

# Combine Runner and Hunter catalog data into one catalog
catalog_data = runner_catalog_data + hunter_catalog_data

# Save the catalog data to catalog.json
catalog_file_path = 'catalog.json'
with open(catalog_file_path, 'w') as catalog_file:
    json.dump(base_template, catalog_file, indent=4)

print("Catalog JSON file created successfully.")
