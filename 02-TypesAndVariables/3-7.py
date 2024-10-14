'''7. In the year 2022, the world population was approximately 8 billion. The Northern Hemisphere has 7.2 billion people. Write a program that calculates and prints:

    1. The number of people and percentage of the total population living in the Northern Hemisphere
    1. The number of people and percentage of the total population living in the Southern Hemisphere'''

    ###
    # A program that calculates and prints:
    # - the number of people and percentage of the total
    #   population living in the Northern Hemisphere
    # - the number of people and percentage of the total
    #   population living in the Southern Hemisphere
    #
total = 8000000000
north = 7200000000
south = total - north
print("World population: ", total)
print("Northern Hemisphere: ", north, "Southern Hemisphere: ", south)
print("Northern Hemisphere in %: ", north/total*100)
print("Southern Hemisphere in %: ", south/total*100)