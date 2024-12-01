'''The program contains two dictionaries with personal data:'''

basic_data = {
   "name":"Barbara",
   "age":21
}

advanced_data = {
    "name":"Barbara",
   "status":"student",
   "married":False,
   "interest":["reading","swimming"]
}

#   Write a program that creates a dictionary
#  called person containing data from the two other dictionaries (five key-value pairs). Print the contents of the ‘person’ dictionary.

person = {}
for key, value in basic_data.items():
    person[key] = value
for key2, value2 in advanced_data.items():
    person[key2] = value2

print(person)