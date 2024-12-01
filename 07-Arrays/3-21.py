'''Write a program that checks whether the first array is a subset of the second one (whether all elements of the first array appear in the second array).'''

def subset(arr1, arr2):
    for i in arr1:
        if i in arr2:
            continue
        else:
            return False
    return True

print(subset([1,2,4],[2,3,4,5]))    
