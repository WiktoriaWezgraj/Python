'''Write a program that displays the first five lines from the it_company.csv file and then prints 'Press Enter key...' in the next line 
and waits for the Enter key to be pressed. The program repeats printing the next five lines from the file, 
waiting for the Enter key to be pressed each time.'''

import csv

with open('it_company.csv', 'r') as f:
    reader = csv.reader(f)

    rows = []
    for row in reader:
        rows.append(row)
    total_rows = len(rows) 
    
    start = 0
    chunk_size = 5

    while start < total_rows:
        end = start + chunk_size
        chunk = rows[start:end] 
        
        for row in chunk:
            print(row)
        if start < total_rows:
            input("Press Enter to continue...") 
        
        start = end

    