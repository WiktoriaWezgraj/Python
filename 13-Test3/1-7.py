'''Create a function f(arr2D) that returns true when the sum of the values in at least two columns is the same. Otherwise, the function returns false. Example: 

arr = [[3,4,2],[2,2,2,0],[5,0,0,5],[4,7,0,2],[0,2,0,0]] 
f([[3,4,2],[5,1,6]]) à True 
f([[3,4,2],[5,1,7]]) à False 
f([[3,4],[5,1],[4,7]]) à True 
f([[3,4],[5,9],[4,7]]) à False '''

def f(arr2D):
    cols = [sum(col) for col in zip(*arr2D)]

    if len(cols) != len(set(cols)):
        return True
    return False

print(f([[3,4,2],[5,1,6]]))
print(f([[3,4,2],[5,1,7]]))
