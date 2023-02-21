import re

# Define the regular expression to match the data fields in the file
regex = re.compile(r'.*("imei":"[^"]*"),("chassis_number":"[^"]*").*')

# Open the file using the file path and read its contents
with open('file.txt', 'r') as file:
    contents = file.readlines()

# Extract the data fields using the regular expression
data = []
for line in contents:
    match = regex.match(line)
    if match:
        imei, chassis_number = match.groups()
        data.append((imei, chassis_number))

# Filter out any unwanted data fields
filtered_data = []
for row in data:
    if row[1] != 'Unwanted':
        filtered_data.append(row)

# Remove duplicates in the new file
unique_data = set(filtered_data)

# Save the filtered and unique data to a new file
with open('No_Duplicates_file.txt', 'w') as file:
    for row in unique_data:
        file.write('\t'.join(row) + '\n')
