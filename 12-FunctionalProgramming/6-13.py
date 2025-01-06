'''At one of the Olympic Games, the medal classification is as follows:

{"country":"Denmark","gold":2,"silver":4,"bronze":6}
{"country":"Finland","gold":5,"silver":0,"bronze":4}
{"country":"USA","gold":12,"silver":5,"bronze":11}
{"country":"Peru","gold":0,"silver":1,"bronze":7}
Write a program that creates a bar chart showing the total number of medals won by each country. Add a title for the chart and descriptions for the x and y axes.

Tip: Use the map() function to create arrays of data for your chart.'''

import matplotlib.pyplot as plt

# Data
medal_data = [
    {"country": "Denmark", "gold": 2, "silver": 4, "bronze": 6},
    {"country": "Finland", "gold": 5, "silver": 0, "bronze": 4},
    {"country": "USA", "gold": 12, "silver": 5, "bronze": 11},
    {"country": "Peru", "gold": 0, "silver": 1, "bronze": 7},
]

# Extract x and y data using map()
countries = list(map(lambda x: x["country"], medal_data))
total_medals = list(map(lambda x: x["gold"] + x["silver"] + x["bronze"], medal_data))

# Create the bar chart
plt.bar(countries, total_medals, color='gold')

# Add title and axis labels
plt.title("Total Number of Medals by Country", fontsize=16)
plt.xlabel("Country", fontsize=12)
plt.ylabel("Total Medals", fontsize=12)

# Show the chart
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
