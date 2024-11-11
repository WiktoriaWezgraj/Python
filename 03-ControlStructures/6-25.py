'''25. The payment card is secured with a four-digit PIN code (0805). 
Write a program that checks if the PIN code entered in the payment terminal is correct. 
The user has up to three possibilities for entering a PIN code. In case of three unsuccessful attempts, the card is blocked. Sample result:

    Enter the PIN code: 2398\
    Incorrect\...\
    Enter the PIN code: 0912\
    Incorrect\...\
    Enter the PIN code: 7860\
    Incorrect\...\
    Sorry, your payment card has been blocked.'''

number_of_tries = 0
while number_of_tries <= 3:
    PIN = input('Enter the PIN code: ')
    if PIN == '0805':
        print('Correct!')
        break
    else:
        print('Incorrect!')
        number_of_tries += 1

    if number_of_tries >= 3:
        print('Sorry, your payment card has been blocked.')