'''The following data contains information about the number of products available in a computer store. Write a program that prints:

-a list of products and the quantity
-the total number of products in the store'''
store = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}
for key, values in store.items():
    print(f"{key} : {values}")

sum = 0
for i in store.values():
    sum += i
print("Sum of itmes", sum)