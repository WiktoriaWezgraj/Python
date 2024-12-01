'''The following program identifies students who are absent. 
Complete and run the program.'''

all_students = {"Alice", "John", "Sara", "Bob"}
attended_students = {"Alice", "Bob"}

absent_students = all_students - attended_students  # Difference
print(absent_students)