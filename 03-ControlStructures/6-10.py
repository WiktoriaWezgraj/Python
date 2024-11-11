'''10. A computer program analyses the price of a product in an online store. If the product price decreases by at least 10%, the program prints a purchase recommendation:

    Buy the product!!\
    Product price reduced by 17%

    Create such program. The current and previous price of the product are included in variables. Sample result:

    Current product price: 140.00\
    Previous product price: 200.00\
    Buy the product!!\
    Product price reduced by 30%'''

current_price = float(input("Current product price: "))
previous_price = float(input("Previous product price: "))
reduction = 100 - (current_price/previous_price *100)
if reduction > 10:
    print("Buy the product!!")
    print(f"Product price reduced by {reduction} %")