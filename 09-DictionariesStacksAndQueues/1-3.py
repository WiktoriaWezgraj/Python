'''3. Create a dictionary as in the example below. Do you know what type of value was used in each of the six key-value pairs?'''

person = {
      "name": "Marek",
      "surname": "Banach",
      "age": 25,
      "hobby": ["swimming","excursions"],
      "married": True,
      "phone":{"landline":"123444321","mobile":"777888999"}
   }


'''Then, create a program that:

   1. Displays name
   1. Displays hobby
   1. Displays the entire contents of the dictionary
   1. Changes surname to 'Nowak'
   1. Changes person's marriage status
   1. Adds gender: 'male'
   1. Adds a new hobby: 'bicycle'
   1. Adds work phone to existing phones: '313131444'
   1. Displays the entire contents of the dictionary (iterate over dictionary items)'''

print(person["name"])
print(person["hobby"])
person["surname"] = "Nowak"
person["married"] = True
person["gender"] = "male"
person["hobby"].append("bicycle")
person["phone"]["workphone"] = '313131444'
for key, values in person.items():
    print(f"{key} : {values}")