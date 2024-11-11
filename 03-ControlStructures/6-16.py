'''16. Write a program that allows you to convert time in 24-hour format to 12-hour format. The time in 24-hour format (hh:mm) is read from the keyboard. Sample result:

    Enter time (24-hour format): 16:32\
    Time in 12-hour format: 4:32pm'''

time = input('Enter time: ')
hours = int(time[:2])
minutes = time[3:]
time_12 = f"{hours-12}:{minutes}"
print(time_12)