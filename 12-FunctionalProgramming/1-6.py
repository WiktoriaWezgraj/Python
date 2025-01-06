'''Write a program that calculates the average speed of a vehicle. Enter from the keyboard: a distance in km, a number of travel hours and a number of travel minutes. Define and use an anonymous function avg_speed(distance,hours,minutes) to calculate the result. Sample result:

Enter distance in km: 70
Enter number of travel hours: 1
Enter number of travel minutes: 23
Average speed: 50.6 km/h '''

km = int(input('Enter distance in km:'))
hours = int(input('Enter number of travel hours:'))
minutes = int(input('Enter number of travel minutes:'))
result = lambda km, hours, minutes: km/(hours+(minutes/60))
end = result(km, hours, minutes)
print(end)