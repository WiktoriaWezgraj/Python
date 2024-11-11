'''5. The atm.py program simulates a simple ATM where the user can deposit, withdraw, or check the balance. 
Analyze the program code and then run the program. Next, add two more functions to the program:

    * Check PIN
    * Change PIN

    The PIN should consist of exactly 4 digits. To check if a string contains only digits, you can use the isdigit() method. 
    This method returns True if all characters in the string are digits and False otherwise'''
###
# ATM (cash machine) simulator
#
balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("5. Check PIN")
    print("6. Change PIN")

    choice = input("Choose an option (1-6): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    elif choice == '5':
        print(f"Your PIN is {pin}")
    elif choice == '6':
        numbers = input("Change your pin:")
        if numbers.isdigit() == True:
            pin = numbers
            print(f"PIN changed: {pin}")
        else:
            print(f"PIN must contain only of digits. Pin didn't change: {pin}")
    else:
        print("Invalid option. Please try again.")
