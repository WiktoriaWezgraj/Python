'''The medical thermometer measures the patient's temperature in the range from 34.0 to 42.0 degrees Celsius, with an accuracy of 0.1 degrees. 
Write a program in which define a class that describes the states and behaviors of the thermometer. 
The thermometer should enable temperature measurement (do it by generating a random number from the 34.0 to 42.0 range) and display the measured value. 
If the temperature is at least 37 degrees Celsius, the thermometer should additionally display the 'Fever' message, e.g.

Temperature: 37.2C (fever)
When the temperature is at least 41.0, the thermometer should additionally print the message 'CRITICAL TEMPERATURE!!'. 
Place the class definition and the main program in separate files. Then use the program and:

Create a thermometer
Turn thermometer on
Measure temperature
Display temperature
Turn thermometer off'''
import random 

class Therm:
    def __init__(self, is_on=False):
        self.is_on = is_on
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def measure(self):
        self.temperature= round(random.uniform(34.0, 42.0), 1)
        
        if self.temperature > 37 :
            print(f"Temperature: {self.temperature} (fever)")
        elif 37 > self.temperature > 41:
            print(f"Temperature: {self.temperature} CRITICAL TEMPERATURE!!")
        else:
            print(f"Temperature: {self.temperature}")

therm = Therm()
therm.turn_on()
therm.measure()

