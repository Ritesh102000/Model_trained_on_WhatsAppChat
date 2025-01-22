import re

# Define the allowed characters
allowed_chars = r"[^!\"',\-.0123456789?ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz\s]"

def remove_unwanted_chars(text):
    # Remove all characters not in the allowed list
    return re.sub(allowed_chars, '', text)

# Open and read the file
with open('shiro.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Process the lines
processed_lines = []
for line in lines:
    # Check if the line contains "<Media omitted>" or is a timestamp
    if "<Media omitted>" not in line and any(char.isalpha() for char in line.split(" - ")[-1]):
        # Extract the part of the line after the timestamp
        try:
            message = line.split(" - ", 1)[1]  # Split into timestamp and rest of the line
            message = remove_unwanted_chars(message)  # Remove unwanted characters
        except IndexError:
            continue
        processed_lines.append(message.strip())

# Write the processed lines to a new file
with open('input.txt', 'w', encoding='utf-8') as output_file:
    output_file.write("\n".join(processed_lines))

print("Processing complete. Check 'input.txt' for the output.")

