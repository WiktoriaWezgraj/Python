'''Convenient processing of CSV documents is possible using the CSV module. 
Find on the Internet how to use this module. Then write a program that, 
based on the it_company.csv file, prints the first name, last name and email 
(in the given order, without Job Title) of people employed in the position of 'Graphic Designer'. 
Sample result:

GRAPHIC DESIGNERS
=================
Chris Martin,chris.martin@example.com
Jane Taylor,jane.taylor@example.com
...
...'''
import csv

with open('it_company.csv') as file:
    csvreader= csv.DictReader(file)

    for row in csvreader:
        # Check if the Job Title matches the desired position
        if row['Job Title'] == 'Graphic Designer':
            # Extract First Name, Last Name, and Email
            first_name = row['First Name']
            last_name = row['Last Name']
            email = row['Email']
            
            # Print the required details
            print(f"{first_name} {last_name},{email}")
