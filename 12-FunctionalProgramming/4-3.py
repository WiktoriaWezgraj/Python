'''The final grades obtained by students in the "Economic Geography" course are included in the array:

[3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]
Write a program that calculates the arithmetic mean of the grades, excluding negative grades (2.0). Use the filter() along with an anonymous function. Sample result:

Arithmetic mean for grades <> 2.0 is 3.85'''

values = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]
val = list(filter(lambda grade: grade>2, values))
mean = sum(val)/len(val)
print(mean)