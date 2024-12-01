'''Write a program that draws the graph of the function f(x)=x2-3. Sample result:

import matplotlib.pyplot as plt

x = []
y = []

# create x values
for n in range(-100,101):
   x = x + [n]

# create y values
for n in x:
   y = ...

# print chart
...
...
'''

import matplotlib.pyplot as plt

x = []
y = []

# create x values
for n in range(-100,101):
   x = x + [n]

# create y values
for n in x:
   y = y + [n**3 + 2]

# print chart
plt.plot(x,y)
plt.show()