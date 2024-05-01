import json

json_file_path = 'catalog.json'
new_json_file_path = 'new_catalog.json'

def remove_duplicates(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    result_data = data["Result"]
    unique_display_names = set()
    cleaned_data = []

    for item in result_data:
        display_name = item[0]["DisplayName"]
        if display_name not in unique_display_names:
            unique_display_names.add(display_name)
            cleaned_data.append(item)

    cleaned_json = {"Result": cleaned_data}

    with open(new_json_file_path, 'w') as outfile:
        json.dump(cleaned_json, outfile, indent=4)

    print("Duplicates removed and new JSON file created.")

remove_duplicates(json_file_path)
