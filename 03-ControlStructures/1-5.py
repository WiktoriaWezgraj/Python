'''5. A test is passed when the number of correctly completed tasks is at
    least 50%. Write a program that checks whether the test is passed. Then use the program to check if you passed the test for the following number of properly performed tasks:

    20, 11, 10, 9, 0 '''

    ###
    # Checking whether the test is passed
    # Test is passed when the number of correctly completed
    # tasks is at least 50%
    #
total_tasks = 20
tasks_ok = int(input('Enter tasks completed: '))
test_passed = False
    
if tasks_ok >= total_tasks/2 :
    test_passed = True
    
if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')
