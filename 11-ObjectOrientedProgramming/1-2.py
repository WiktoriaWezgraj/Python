'''The Square class represents objects describing a geometric figure (square). 
Complete the class by adding a method to calculate the perimeter of a square. 
Then write a program that creates two squares with sides of 4 and 6, respectively. 
Calculate the areas and perimeters of these squares. Print the results.'''

class Square:
   def __init__(self, a):
      self.a = a
   def area(self):
      return self.a * self.a
   def perimeter(self):
      return self.a*4

square1 = Square(4)
square2 = Square(6)

print(f'Area of square with side 4 is {square1.area()} , Perimeter is {square1.perimeter()}')
print(f'Area of square with side 6 is {square2.area()} , Perimeter is {square2.perimeter()}')