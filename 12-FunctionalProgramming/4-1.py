'''The following people are employed in one of the company's departments:

SMITH Lucy
JONES Janet
LEE Jerry
JACKSON Peter
JOHNSON Rick
LEWIS Terry
CLARKE Robin
Save the list of employees in a string array. Then, write a program that displays people whose surnames start with the letter 'J'. Use anonymous and filter() functions. Sample result:

JONES Janet
JACKSON Peter
JOHNSON Rick
employees = ["SMITH Lucy","JONES Janet","LEE Jerry",
               "JACKSON Peter","JOHNSON Rick",
               "LEWIS Terry","CLARKE Robin"]
emp_J = list(filter(lambda e:...=="J", employees))
# print a list …'''

employees = ["SMITH Lucy","JONES Janet","LEE Jerry",
               "JACKSON Peter","JOHNSON Rick",
               "LEWIS Terry","CLARKE Robin"]
emp_J = list(filter(lambda e: e.split()[0].startswith('J'), employees))
print(emp_J)