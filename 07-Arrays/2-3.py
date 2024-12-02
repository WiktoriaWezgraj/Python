'''The data below represents monthly expenses divided into categories and weeks. Write a program that calculates and prints:

total expenses for each category
total expenses for each week
total expenses for a month'''
# Weekly expenses for different categories
# [Food, Transport, Utilities]

monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

sum_f= 0
for row in monthly_expenses:
    sum_f += row[0]

sum_t= 0
for row in monthly_expenses:
    sum_t += row[1]

sum_u= 0
for row in monthly_expenses:
    sum_u += row[-1]

sum1=0
for i in monthly_expenses[0]:
    sum1 += i

sum2=0
for i in monthly_expenses[1]:
    sum2 += i

sum3=0
for i in monthly_expenses[2]:
    sum3 += i

sum4=0
for i in monthly_expenses[3]:
    sum4 += i

total = 0
for row in monthly_expenses:
    for i in row:
        total += i
# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', sum_f)
print('Transport:',sum_t)
print('Utilities:',sum_u)
print('Week 1:',sum1)
print('Week 2:',sum2)
print('Week 3:',sum3)
print('Week 4:',sum4)
print('---------------')
print('TOTAL:',total)