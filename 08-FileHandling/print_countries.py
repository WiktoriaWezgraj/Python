###
# Reads from file, line by line
#
with open('countries.txt', 'r') as file:
    for index, line in enumerate(file, start = 1):
        print(f"{index}. {line.strip()}")