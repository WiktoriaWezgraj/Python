'''The res array contains test results, i.e. the number of points between 0 and 100. Create a function f(fnc,res) that filters the test results according 
to the criteria contained in the fnc function. The f function returns the difference between the highest and lowest test result. Example: 

res = [95,90,20,50,70]  
fnc1 = lambda x: x>50 
f(fnc1,res) à 25 
fnc2 = lambda x: x>30 and x<90 
f(fnc2,res) à 20 '''

def f(fnc, res):
    filtered_res = list(filter(fnc, res))
    
    # Calculate the difference between the highest and lowest test result
    return max(filtered_res) - min(filtered_res)

res = [95,90,20,50,70]  
fnc1 = lambda x: x>50 
fnc2 = lambda x: x>30 and x<90 
print(f(fnc2,res))
print(f(fnc1,res))