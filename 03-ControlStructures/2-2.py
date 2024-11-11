'''2. Clothing sizes are often labeled with letter symbols. Write a program that prompts the user to enter a clothing size 
and then prints a verbal description of the clothing size, as below.

    * S: Small size
    * M: Medium size
    * L: Large size
    * XL: Extra large size
    * Incorrect symbol (if entered symbol dirrerent than S, M, L, XL)

    Then check the correctness of the program for each of the size symbols.'''


    ###
    # A program for checking clothing sizes
    # S: Small size, M: Medium size, L: Large size
    # XL: Extra large size or Incorrect symbol (if entered symbol
    # dirrerent than S, M, L, XL)
    #
size = input('Enter size symbol: ')

if size == 'S':
    print('S: Small size')
elif size == 'M':
    print('M: Medium size')
elif size == 'L':
    print('L: Large size')
else:
    print('XL: Extra large size')