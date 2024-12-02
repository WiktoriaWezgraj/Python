'''(p7.py) A valid username consists of 4 to 12 characters: lowercase letters, numbers and the underscore character. Define a function f(array) that, for a given array of usernames, returns the number of valid usernames in the array. Example: 

f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]) à 2 '''

import re

def f(array):
    sum = 0

    pattern = '^[a-z\d_]{4,12}$'
    for i in array:
        matched = re.match(pattern, i)
        if matched:
            sum += 1

    return sum

print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))
