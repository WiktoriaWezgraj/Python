'''The data below contains a price list of items from a clothing store along with their prices. 
Due to a seasonal sale, the store is reducing the price of each item by 10%. Write a program that:

prints a list of products and their prices before the discount
prints the total value of the products before the discount
modifies the price list according to the discount (round prices to two decimal places)
prints a list of products and their prices after the 10% discount
prints the total value of the products after the discount'''

price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
for key, values in price_list.items():
    print(f"{key}:{values}")

sum = 0
for i in price_list.values():
    sum += i
print(f"Sum:{sum:.2f}")

for values in price_list:
    after_disc = price_list[values] * 0.9
    price_list[values] = round(after_disc, 2)

for key, values in price_list.items():
    print(f"{key}:{values}")

sum = 0
for i in price_list.values():
    sum += i
print(f"Sum:{sum:.2f}")