'''A program contains two functions:

hotel_list(hotels) that returns a list of hotel names, separated by a comma sign
avg_price(hotels) that returns the average room price for a given list of hotels, rounded to an integer value
Write a program that calculates and displays the average price for a room in hotels in Krakow and Sopot and indicates in which cities hotels are cheaper. Sample result:

Hotels in Krakow: …,…,…,…
Average hotel price in Krakow: …
Hotels in Sopot: …,…,…,…
Average hotel price in Sopot: …
Cheaper hotels in: …'''

hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]

for index, hotel in enumerate(hotels_in_Krakow):
    if index+1 != len(hotels_in_Krakow):
        print(hotel['name'], end=", ")
    else:
        print(hotel['name'])

sum = 0 
for hotel in hotels_in_Krakow:
    sum += hotel['price'] 
average = sum/len(hotels_in_Krakow)
print(average)

for index, hotel in enumerate(hotels_in_Sopot):
    if index+1 != len(hotels_in_Sopot):
        print(hotel['name'], end=", ")
    else:
        print(hotel['name'])

sum = 0 
for hotel in hotels_in_Sopot:
    sum += hotel['price'] 
average2 = sum/len(hotels_in_Sopot)
print(average2)

if average > average2:
    print('Cheaper hotels in Krakow')
elif average == average2:
    print('No difference')
else:
    print('Cheaper hotels in Sopot')