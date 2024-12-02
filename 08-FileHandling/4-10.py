'''The clothing.csv contains a list of clothing in stock. 
Write a program that prints those products whose price is less than 60 and whose stock is less than 40.'''

import csv
with open('clothing.csv') as f:
    csvreader = csv.DictReader(f)

    for row in csvreader:
        if float(row["Price"]) < 60 and float(row["Stock_Quantity"]) >40:
            print(row["Product_ID"])
            print(row["Product_Name"])