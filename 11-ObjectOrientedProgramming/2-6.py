'''Identify at least 3 states and 3 behaviors for your smartphone. Then, for the listed states and behaviors, create a class with attributes and methods. 
Try to use verbs in method names as they describe activities. Finally, create a smartphone object, call its methods and display object’s properties.'''

class Phone():
    def __init__(self, storage, color, RAM):
        self.color = color
        self.storage = storage
        self.RAM = RAM
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def call_mom(self):
        self.is_calling = True

    def end_call(self):
        self.is_calling = False

    def display_info(self):
        print(f"Storage: {self.storage}")
        print(f"Color: {self.color}")
        print(f"RAM: {self.RAM}")
        print(f"Is turned on? {self.is_on}")
        print(f"Call? {self.is_calling}")

phone = Phone(64, 'red', 16)
phone.turn_on()
phone.call_mom()
phone.end_call()
phone.call_mom()
phone.display_info()



