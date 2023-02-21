import re

# Define the regular expression to match the data fields in the file
# regex = re.compile(r'^\d+\t(.+)\t(.+)\t(.+)$')

regex = re.compile(r'.*("imei":"[^"]*"),("chassis_number":"[^"]*").*')


# Open the file using the file path and read its contents
with open('file.txt', 'r') as file:
    contents = file.readlines()

# Extract the data fields using the regular expression
data = []
for line in contents:
    match = regex.match(line)
    if match:
        field1, field2 = match.groups()
        data.append((field1, field2))

# Filter out any unwanted data fields
filtered_data = []
for row in data:
    if row[1] != 'Unwanted':
        filtered_data.append(row)

# Save the filtered data to a new file
with open('full_file.txt', 'w') as file:
    for row in filtered_data:
        file.write('\t'.join(row) + '\n')
