'''15. A washing machine allows you to wash a jacket, which takes 40 minutes, wash underwear, which takes 70 minutes, 
and wash shoes, which takes 20 minutes. In addition, it is possible to program an additional rinse (15 minutes) and an additional spin (9 minutes). 
The washing machine settings are saved in variables. Write a program that calculates and prints the total washing time. Sample result:

    washing_product = \"shoes\"\
    rinse = True\
    spin = False\
    Total washing time: 35 minutes'''

    ###
    # Calculates and prints the total washing time.
    #
    # A washing machine allows you to wash a jacket, which takes
    # 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
    # which takes 20 minutes. In addition, it is possible to program
    # an additional rinse (15 minutes) and an additional spin (9 minutes).
    #

total_washing_time = 0
rinse = True
spin = False
washing_product = input('Select washing program: (j)acket, (u)nderwear, (s)hoes:')
extra_rinse = input('Extra rinse? (y/n)')
extra_spin = input('Extra spin? (y/n)')

if washing_product == "j":
    washing_time = 40
elif washing_product == "u":
    washing_time = 70
elif washing_product == "s":
    washing_time = 20
else:
    washing_time = 0

if rinse:
    washing_time += 15
if spin:
    washing_time += 9

if extra_rinse == 'y':
    washing_time += 15
if extra_spin == 'y':
    washing_time += 9

print(washing_time)