'''3. The car has three driving modes: Auto (A), Manual (M) and Eco (E). In each of these three modes, the average fuel consumption in 
liters per 100 km is 7, 9 and 6 respectively. Write a program that calculates total fuel consumption for a given distance in km and a given driving mode. 
Then, calculate the total fuel consumption for the following data:

    * distance 200 km, driving mode M (the result should be 18 liters) 
    * distance 400 km, driving mode A (the result should be 28 liters) 
    * distance 350 km, driving mode E (the result should be 21 liters) '''

    ###
    # The car has three driving modes: Auto (A), Manual (M) and Eco (E).
    # In each of these three modes, the average fuel consumption in liters
    # per 100 km is 7, 9 and 6 respectively. Write a program that calculates
    # total fuel consumption for a given distance in km and a given
    # driving mode.
    #
driving_mode = input('Enter driving mode (A/M/E):')
distance = float(input('Enter distance in km: '))

if driving_mode == 'A':
    fuel_consumption = 7*distance/100 # liters per 100km
elif driving_mode == 'M':
    fuel_consumption = 9*distance/100
else:
    fuel_consumption = 6*distance/100

print(fuel_consumption)