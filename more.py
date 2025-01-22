import re

# Open and read the file
with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Process each line
processed_lines = []
for line in lines:
    # Replace the first occurrence of 'Catoysigma' and 'Ritesh'
    line = re.sub(r'\bCatoysigma\b', 'User:', line, count=1)
    line = re.sub(r'\bRitesh\b', 'Output:', line, count=1)
    processed_lines.append(line)

# Write the updated lines to a new file
with open('input.txt', 'w', encoding='utf-8') as output_file:
    output_file.writelines(processed_lines)

print("Replacements complete. Check 'updated_shiro.txt' for the updated content.")
