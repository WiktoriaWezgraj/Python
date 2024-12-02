'''(p2.py) An array contains at least 3 integers. All numbers in the array are equal except one. Define a function f(arr) that returns a number in the arr array that is different from the other numbers. Example: 

f([7,7,7,7,7,5,7,7]) à 5 '''

def f(arr):
    dict = {}
    
    for num in arr:
        if num in dict:
            dict[num] +=1
        else:
            dict[num] = 1

    for num, count in dict.items():
        unique_val = 0
        if count ==1:
            unique_val = num
    return unique_val
    

        


print(f([7,7,7,7,7,7,7,5]))

