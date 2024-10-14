'''5. A transport company needs a program to calculate the cost of transporting goods.
The program calculates the cost of transporting goods based on the given distance in km, fuel price per 1 liter, and fuel consumption in liters per 100 km. Write such program.'''

    ###
    # The program calculates the cost of transporting goods
    # based on the given distance in km, fuel price per 1 liter,
    # and fuel consumption in liters per 100 km.
    #
distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input('Enter fuel consumption per 100 km:'))
fuel_consumption / 100 # per 1 km
total_fuel_consumption = distance / fuel_consumption
total_cost = fuel_consumption * fuel_price
print(total_cost)
print(total_fuel_consumption)