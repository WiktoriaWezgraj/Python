'''1. Create a dictionary describing your mobile phone. Use 6 key-value pairs of data. 
Then, using `for` loop, display the contents of the dictionary. To read a key and value, use the `items()` method. Sample result:
'''
mobile = {
   "OS":"Android",
    "RAM":16,
    "Storage": 64,
    "Color": "Blue",
    "Camera": "16px",
    "Brand": "Samsung"
   }
for key,value in mobile.items():
      print(f"{key} : {value}")