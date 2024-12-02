'''Write a program that calculates, prints, and saves to a text file integers from 1 to 100 and their second and third powers. Sample result:

1,1,1
2,4,8
3,9,27
...
...'''

with open("thirdpower.txt", "w") as f:
    for i in range(1,101):
        f.write(f'{i},{i**2},{i**3}')
        f.write('\n')