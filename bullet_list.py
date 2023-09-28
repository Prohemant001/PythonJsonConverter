import json
import pyperclip


def convert_text_to_json(text):
    # Split the input text by lines
    lines = text.split('\n')

    # Remove empty lines and strip leading/trailing whitespaces
    lines = [line.strip() for line in lines if line.strip()]

    # Create a JSON object with a "data" key containing the cleaned lines
    json_data = {
        "data": lines
    }

    # Convert to JSON format with double quotes and indentation
    json_string = json.dumps(json_data, indent=2)

    # Copy the JSON to the clipboard
    pyperclip.copy(json_string)

    print("Copied")


# Example usage:
input_text = """Last Qualifying Exam Mark Sheet
Cast Certificate
Income Certificate
Bank Passbook
Fee Receipt Number
Enrollment Number
Aadhar Card Number
Latest Passport Size Scan Photo"""

convert_text_to_json(input_text)
