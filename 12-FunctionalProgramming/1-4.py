'''Write a program that converts speed in meters per second to speed in kilometers per hour. Define and use an anonymous function ms_to_kmh(ms). Sample result:

10 m/s = 36 km/h
35 m/s = 126 km/h'''

result = lambda ms: ms *3.6
end = result(10)
end = result(35)
print(end)

