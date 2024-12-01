'''Write a program that prints the tuple (10,20,30,40,50) in reverse order. Sample result:

Tuple: 10,20,30,40,50
Reverse order: 50,40,30,20,10'''

tup = (10,20,30,40,50)

#1
tup = tup[::-1] ## wazne
print(tup)

#2
tup2 = ()
for i in reversed(tup):
    tup2 += (i, )

print(tup2)
