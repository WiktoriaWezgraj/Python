'''5. To improve readability, telephone numbers are often presented with a dash or space separating some digits. 
Write a program that prints a 9-digit telephone number entered from the keyboard as three groups of 3 digits each, separated by a dash character. Sample result:

    ```
    Enter phone number: 543097329
    Phone number: 543-097-329
    ```

    Complete the following program code.'''

    ###
    # a program that prints a 9-digit telephone number
    # entered from the keyboard as three groups of 3 digits each,
    # separated by a dash character.
    #
phone = input('Enter phone number: ')
print(phone[0:3] + "-" + phone[3:6] + "-" + phone[6:9])