'''9. Monthly expenses and their corresponding expense categories are included in the arrays below. 
Write a program that calculates which expense category was the most expensive.

   categories = ["Food", "Transport", "Rent","Entertainment"]
   expenses = [500, 150, 1000, 200]'''

categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

max = 0
counter = 0
for i in expenses:
    if i > max:
        max = i
        counter += 1

print(categories[counter])