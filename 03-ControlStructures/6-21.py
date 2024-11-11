'''21. Write a program that prints numbers from 1 to 30. If the number is divisible by 3 then the program prints the word \'THREE\'. 
Next, if the number is divisible by 5 then the program prints the word \'FIVE\'. Finally, if the number is divisible by both 3 and 5 then the program prints the word \'BINGO\'. 
Sample result:

    1 2 THREE 4 FIVE THREE 7 \...'''

for i in range(1,31):
    if i % 15 == 0:
        i = 'BINGO'
    elif i % 3 == 0:
        i = 'THREE'
    elif i % 5 == 0:
        i = 'FIVE'
    print(i)
