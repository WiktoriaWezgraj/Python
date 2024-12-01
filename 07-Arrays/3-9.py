'''Define a function compare(array1, array2) that returns True if both arrays are the same or False otherwise. 
Two arrays are the same if they have the same number of elements and values of elements in cells of arrays with the same index are equal. 
Then create a program and try to compare the following arrays:

1. ["water","book","sky"]   ["water","book","sky"]
1. [True,False]   [True,False,True]
1. [5,3,1]   [5,3,1]
1. [3,2,1]   [3,2]'''

def compare(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True      
        

print(compare(["water","book","sky"], ["water","book","sky"]))
print(compare([True,False],  [True,False,True]))
print(compare([3,2,1], [3,2]))