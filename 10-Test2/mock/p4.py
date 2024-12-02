'''(p4.py) The dictionary contains the names of subjects and the grades obtained. Define a function f(subjects) that, 
for the given subjects and their grades, returns the name of the subject for which the average grade is the highest. Example: 

f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}) -> "comp" '''


def f(subjects):
    average = 0
    for subject, grades in subjects.items():
        total = 0
        for grade in grades:
            total += grade
        
        average_4subj = total/len(grades)
        if average_4subj > average:
            average = average_4subj
            subj = subject

    return subj


print(f({"math":[5,5,5],"geo":[5,4,4,4],"comp":[5,4]}))
