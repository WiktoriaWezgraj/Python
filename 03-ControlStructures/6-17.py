'''17. Let x and y denote the coordinates of a point on the plane. Write a program that determines in which quadrant of the coordinate system the point 
P(x, y) is located or on which axis it is located, or that it is located in the position (0,0) of the coordinate system. Sample result:

x = 5
y = 2
Point P(5,2) is in the first quadrant of the coordinate system'''

x = int(input('x ='))
y = int(input('y = '))
if x> 0 and y>0:
    quadrant = 'first'
elif x> 0 and y<0:
    quadrant = 'fourth'
elif x< 0 and y> 0:
    quadrant = 'second'
elif x<0 and y<0:
    quadrant = 'third'
else:
    print('Incorrect input')

print(f"Point P({x},{y}) is in the {quadrant} quadrant of the coordinate system")
