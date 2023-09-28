import json
import pyperclip

def copy_to_clipboard(data):
    pyperclip.copy(data)
    print("Copied")

def create_json(raw_data):
    lines = raw_data.split('\n')
    data = []
    current_item = []

    for line in lines:
        parts = line.split(':')
        if len(parts) == 2:
            current_item.append(parts[0].strip())
            current_item.append(parts[1].strip())
            data.append(current_item)
            current_item = []
        elif len(parts) == 1 and current_item:
            # If there's no colon and there's an existing item, continue adding items
            current_item[-1] += " " + parts[0].strip()

    json_data = {
        "data": data
    }

    json_string = json.dumps(json_data, indent=2)  # Convert to JSON format with double quotes
    copy_to_clipboard(json_string)

# Example usage:
raw_data = """
Minimum Age : 18 Years
Maximum Age : 40 Years
"""

create_json(raw_data)
