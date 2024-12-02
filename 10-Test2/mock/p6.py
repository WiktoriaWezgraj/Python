'''(p6.py) Define a function f(years, course, average_grade) that, for the j file, 
returns the number of students who are at least the given number of years and have 
a grade average of at least average_grade in the given course name. Example: 

f(21, "statistics", 4)'''

import json
def f(years, course, average_grade):
    with open('data.json') as file:
        content = json.load(file)

    total_students = 0

    for student in content:
        grades = content['courses'][course]

    if content['age'] >= years and course in content['courses'] and sum(grades)/len(grades) >= average_grade:
        total_students += 1
    
    return total_students
    
print(f(21, "statistics", 4))