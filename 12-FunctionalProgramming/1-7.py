'''Define an anonymous function is_even(number) that checks whether a number is even. Then test it by writing a program.'''

is_even = lambda num: num%2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # A list of numbers to test
for num in numbers:
    print(f"{num} is {'even' if is_even(num) else 'odd'}")