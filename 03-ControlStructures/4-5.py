'''5. Write a program that calculates values for the following fractions: 1/2, 1/3, ..., 1/10. Sample result:

    1/1 = 1.0\
    1/2 = 0.5\
    1/3 = 0.3333333333333333\
    ...\
    1/10 = 0.1'''

    ###
    # Calculates values for the following fractions: 1/2, 1/3, ..., 1/10
    #
for i in range(1,11):
    print(f'1/{i} = {1/i}')