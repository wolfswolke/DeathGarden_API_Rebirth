import os
import json


# GLOBALS
error_items = []

def find_guid_in_json_files(directory):
    guid_list = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as json_file:
                    try:
                        json_data = json.load(json_file)
                    except json.decoder.JSONDecodeError:
                        print(f"Error decoding JSON file: {file_path}")
                        continue
                    except UnicodeDecodeError:
                        print(f"Error decoding JSON file UnicodeError: {file_path}")
                        continue
                    find_and_append_guid(json_data, guid_list, file_path)

    return guid_list


def find_and_append_guid(data, guid_list, file_path):
    if data is None:
        return  # Exit the function if data is None
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "GUID":
                guid_list.append(f"GUID: {value}, File: {file_path}")
            elif isinstance(value, (dict, list)):
                find_and_append_guid(value, guid_list, file_path)
    elif isinstance(data, list):
        for item in data:
            find_and_append_guid(item, guid_list, file_path)
    if isinstance(data, dict):
        properties = data.get("Properties")
        if properties is not None and isinstance(properties, dict) and "Guid" in properties:
            guid_list.append(f"GUID: {properties['Guid']}, File: {file_path}")
        else:
            error_items.append(file_path)


def save_output_to_file(filename, output):
    with open(filename, 'w') as file:
        for line in output:
            file.write(line + "\n")


if __name__ == "__main__":
    directory = "./TheExit/"
    guid_list = find_guid_in_json_files(directory)
    output = []
    output.append("--------------------------------------------------")
    output.append("Error items:")
    for entry in error_items:
        output.append(entry)
    output.append("--------------------------------------------------")
    output.append("Found Items:")
    for entry in guid_list:
        output.append(entry)
    output.append("--------------------------------------------------")

    # Specify the filename where you want to save the output
    output_filename = "output.txt"

    # Save the output to the file
    save_output_to_file(output_filename, output)
