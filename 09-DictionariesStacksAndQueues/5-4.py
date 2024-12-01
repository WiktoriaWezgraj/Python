'''A dictionary contains course names along with the number of hours. 
Write a program that calculates and prints the total number of hours. Sample results:

The total number of hours in the winter semester is …'''

winter_semester = {
   "math":60,
   "programming":30,
   "history":15
}

sum = 0
for i in winter_semester.values():
    sum += i

print(sum)
## ciag fibonacciego powtorzyc