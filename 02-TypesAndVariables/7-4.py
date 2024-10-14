'''4. A tree may be cut down if its diameter is at least 50 cm. Write a program that, based on the circumference of the tree entered from the keyboard, 
calculates and prints the value True if the tree can be cut down, or print the value False otherwise. Sample result:

    Enter tree circumference in cm: 120 
    Tree can be cut down: False

    Then, check if the program works correctly. There are several trees in the garden with the given circumferences in cm. Which trees can be cut down?

    Tree 1: 160 
    Tree 2: 90
    Tree 3: 230
    Tree 4: 120'''

C = float(input("Enter tree circumference in cm: "))
print("Tree can be cut down: ", C/3.14 >= 50 )