'''4. Write a program that saves data of employees employed in the position of 'Software Engineer' to the file 'software_engineer.txt'. 
Data is available in the file 'it_company.csv'.

   > Hint: Read employee data line by line. For each line, check if it contains the name of the indicated position. If so, write this line to the output file.'''

   ###
   # Saves to a file a list of employees working at a specified position.
   #

   # file names
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

   # Position
job_title = 'Software Engineer'

   # write selected employees to a file
with open(employees_file, 'r') as f:   
    with open(position_file, 'w') as f2:
        for line in f:
            if job_title in line:
               f2.write(line)
    