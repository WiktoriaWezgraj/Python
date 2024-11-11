'''5. The parking meter calculates the parking fee based on the number of hours the car was parked according to the following rules:

    * 1-2 hours: 5 PLN
    * 3-6 hours: 15 PLN
    * Over 6 hours: 20 PLN

    Write a program that asks for the number of hours of parking, then calculates and prints the correct fee.'''

hours = int(input('How many hours?'))
if hours in range(1,3):
    print("5 PLN payment")
elif hours in range(3,7):
    print("15 PLN payment")
elif hours > 6:
    print("20 PLN payment")
else:
    print("Incorrect input")