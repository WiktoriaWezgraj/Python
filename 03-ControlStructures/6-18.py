'''18. Yes-no question are often used in surveys to gauge people\'s attitudes with regard to specific ideas or beliefs. 
Write a program that prints a survey consisting of three questions. Save the answers to logical type variables. Then view the survey result. Sample result:

    SURVEY
    Are you interested in computer science? (y/n): y\
    Do you like playing computer games? (y/n): n\
    Do you have an Instagram account? (y/n): y

    SURVEY RESULTS
    Interested in computer science: Yes\
    Playing computer games: No\
    Has an Instagram account: Yes'''

print('SURVEY')
comp_science = input('Are you interested in computer science? (y/n):')
games = input('Do you like playing computer games? (y/n)')
instagram = input('Do you have an Instagram account? (y/n):')

print('\nSURVEY RESULTS')
print('Interested in computer science:', end  = ' ')
if comp_science == 'y':
    print('Yes')
if comp_science == 'n':
    print('No')

print('Playing computer games:', end  = ' ')
if games == 'y':
    print('Yes')
if games == 'n':
    print('No')

print('Has an Instagram account:', end  = ' ')
if instagram == 'y':
    print('Yes')
if instagram == 'n':
    print('No')