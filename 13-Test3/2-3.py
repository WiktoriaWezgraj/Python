'''Flight numbers along with the number of passengers are stored in a dictionary d. 
Define a function f(d) that returns the number of flights in which the number of passengers is greater than the average number of passengers on all flights. Example: 

f({"LO231":150,"BA787":120,"NZ15":30}) à 2 
f({"LO231":150,"BA787":20,"NZ15":30}) à 1 '''

def f(d):
    count = 0
    avg = sum(d.values()) / len(d)
    for passengers in d.values():
        if passengers > avg:
            count += 1
    return count, d.values()
    
print(f({"LO231":150,"BA787":120,"NZ15":30}) )