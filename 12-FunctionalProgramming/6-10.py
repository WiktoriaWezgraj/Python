'''Measuring stations recorded the following temperatures in degrees Celsius:

{"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
Write a program that creates a bar chart showing temperatures recorded in cities. Add a title for the chart and descriptions for the x and y axes.

Tip: use the map() function to create two arrays of data for the chart.'''

import matplotlib.pyplot as plt

# Data
cities = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}

# Extract x and y data using map()
x_data = list(cities.keys())
y_data = list(cities.values())

# Create the bar chart
plt.bar(x_data, y_data, color='pink', edgecolor='black')

# Add title and axis labels
plt.title("Temperatures Recorded in Cities", fontsize=16)
plt.ylabel("Temperature (°C)", fontsize=12)

# Show the chart
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


