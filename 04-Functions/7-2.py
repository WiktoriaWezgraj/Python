'''2. Each month of a calendar year can be expressed by its name or by a number that indicates the position of the month in year. 
In a separate module, define a function month(n) that returns a month name based on the month number (values from 1 to 12). 
Then, write a program to print the name of the month 7. Import the module with the created function. Sample result:

    ```
    Enter month number: 9
    The name of month 9 is September'''

def month(n):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
    letters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    return f"The name of month {letters[n-1]} is {months[n-1]}"
