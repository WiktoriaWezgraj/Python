'''(p9.py) The file data.csv contains a list of employees of the company ABC-Data. Define a function f(value) that returns 
the number of employees whose salary is greater than or equal to the given value. Example: 

f(9200)
f(11640)'''

import csv
def f(value):
    with open('data.csv') as file:
        csvreader = csv.DictReader(file)

        total = 0
        for row in csvreader:
            salary = row['salary']
            if int(salary) >= value:
                total += 1
    return total

print(f(9200))