import json

def has_null_value(data):
    if isinstance(data, list):
        return any(has_null_value(item) for item in data)
    elif isinstance(data, dict):
        return any(has_null_value(value) for value in data.values())
    else:
        return data is None

def remove_items_with_null(data):
    return [item for item in data if not has_null_value(item)]

# File path
file_path = 'src/json/catalog/te-23ebf96c-27498-ue4-7172a3f5/catalog.json'

# Read JSON data from file
with open(file_path, 'r') as file:
    json_data = json.load(file)

# Remove items with null values
updated_json_data = remove_items_with_null(json_data)

# Save updated JSON data back to the file
with open(file_path, 'w') as file:
    json.dump(updated_json_data, file, indent=4)

# Print the updated JSON data
print(json.dumps(updated_json_data, indent=4))
