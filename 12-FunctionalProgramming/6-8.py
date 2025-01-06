'''The educational course finished with a test checking the participants' knowledge. Here are the results obtained by the students:

[37,51,44,23,78,92,39,84,83,51]
Write a program that calculates and displays student scores that are equal to or greater than the following minimum number of points to pass the course:

70
40
30
Use the filter() function and the following higher order function:

def min_pts(limit):
   return lambda pts: pts>=limit
Sample result:

Min 70 pts: [78, 92, 84, 83]
Min 40 pts: [51, 44, 78, 92, 84, 83, 51]
Min 30 pts: [37, 51, 44, 78, 92, 39, 84, 83, 51]'''

results = [37,51,44,23,78,92,39,84,83,51]
def min_pts(limit):
   return lambda pts: pts>=limit

final_7 = list(filter(min_pts(70), results))
final_4 = list(filter(min_pts(40), results))
final_3 = list(filter(min_pts(30), results))
print(final_7)
