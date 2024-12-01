import queue

"""
A stack is a linear data structure that follows
the Last In, First Out (LIFO) principle.
This means the last element added to the stack
is the first one to be removed. Think of a stack
as a pile of plates — the last plate you place
on the top is the first one you'll take off.
"""

# creates a stack
cards = queue.LifoQueue()

# adds elements to the top of the stack 
cards.put(2)   
cards.put(3) 
cards.put(7) 
cards.put(4) 
cards.put(1)
cards.put(9)
cards.put(8)

## prints number of elements of the stack
print('Number of stack elements:', cards.qsize())

if cards.qsize() >= 2:
    last= cards.get()
    second_last = cards.get()
    two_sum = last + second_last
    print(two_sum)
# removes and prints elements from the top of the stack
sum = 0
while not cards.empty():
    card = cards.get()
    sum += card
print(sum)
"""
Note the order of the printed elements.
The last added element is printed first.
"""
'''Put 2 on the stack
Put 3 on the stack
Put 7 on the stack
Put 4 on the stack
Put 1 on the stack
Put 9 on the stack
Put 8 on the stack
Sum the last two numbers of the stack and print result
Calculate the sum of the remaining stack elements and print the result. Use a 'while' loop.'''