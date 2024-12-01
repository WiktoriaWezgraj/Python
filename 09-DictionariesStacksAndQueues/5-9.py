'''A traffic camera records passing vehicles. The camera saves their registration numbers in the file vehicle.txt. 
Write a program that calculates and prints how many registered cars come from each province of Poland. 
The list of provinces and the corresponding first letters of the vehicle registration numbers are contained in the file province.csv.

Hint: use the dictionary containing the letters corresponding to the provinces and the numbers of vehicles
whose first letters of the registration number match the letters of the province.'''

import csv

with open('vehicle.txt', encoding='latin-1') as f2:
    vehicles = f2.read().strip().splitlines()

vehicle_dict = {}
with open('province.csv', mode='r', encoding='latin-1') as f:
    for row in f:
        province_id = row[0]
        province_name = row.strip().split(',')[1]  
        vehicle_dict[province_id] = province_name

province_vehicle_count = {province: 0 for province in vehicle_dict.values()}


for vehicle in vehicles:
    first_letter = vehicle[0] 
    if first_letter in vehicle_dict: 
        province_name = vehicle_dict[first_letter]
        province_vehicle_count[province_name] += 1

for province, count in province_vehicle_count.items():
    print(f"{province}: {count} vehicles")