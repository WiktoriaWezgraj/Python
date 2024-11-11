'''7. The employee's basic salary is PLN 5000. The employee may receive a bonus of several percent of the basic salary. 
Write a program that calculates the employee's salary, taking into account the possibility of receiving a bonus. Then calculate the employee's total salary for the following cases:

    * The employee does not receive a bonus
    * The employee receives a bonus of 30%'''

    ###
    # Program that calculates the employee's salary,
    # taking into account the possibility of receiving a bonus.
    #
basic_salary = 5000
total_salary = 0
is_bonus = False # does the employee receive a bonus
bonus = 0.15 # 15%
    
if is_bonus == True:
    total_salary = basic_salary + basic_salary*bonus
else:
    basic_salary
    
print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')