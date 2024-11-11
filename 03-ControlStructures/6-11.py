'''11. In one of the online stores, a 25% discount is charged for each product purchased over two. 
Write a program that calculates the amount to be paid. Read the number of purchased products and the product price from the keyboard. Sample result:

    Number of products purchased: 5\
    Product price: 40\
    Amount to pay: 170.00'''

products_purch = int(input('Number of products purchased: '))
product_price = float(input('Product price: '))
if products_purch > 2:
    pay = product_price *2 + (product_price-(product_price*0.25))*(products_purch-2)
else:
    pay = product_price

print(pay)