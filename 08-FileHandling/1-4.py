'''4. The file it_company.csv contains a list of employees. Write a program that displays only employees with the position "Software Engineer". 
Number the items on the printed list.

   > Hint: You can check if a string is contained within another string using the 'in' operator.'''

   ###
   # Prints employees employed in a specified position.
   #

   # Employee List
file_name = 'it_company.csv'

   # Position
job_title = 'Software Engineer'

arr = []
with open(file_name) as f:
   for line in f:
      if job_title in line:
         line_split= line.strip().split(',')
         person = f"{line_split[0]} {line_split[1]}"
         arr.append(person)
   for index, person in enumerate(arr, start=1):
      print(f'{index}. {person}')
         