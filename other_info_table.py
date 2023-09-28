import pyperclip

def convert_to_list_and_copy(input_text):
    # Split the input text into lines
    lines = input_text.strip().split('\n')
    
    # Initialize an empty list to store the converted data
    data = []

    for line in lines:
        # Check if the line is not empty
        if line.strip():
            # Enclose each item in double quotation marks and add to the list
            data.append(f'"{line.strip()}"')

    # Combine the data list into a string with square brackets
    result = '[' + ',\n'.join(data) + ']'

    # Copy the result to the clipboard
    pyperclip.copy(result)

    # Print a "copied" message
    print("Copied")

# Example usage:
input_text = """Gram Panchayat Adhikari

849

117

139

356

07

1468"""

convert_to_list_and_copy(input_text)
