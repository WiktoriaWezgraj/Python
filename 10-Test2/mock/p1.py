'''(p1.py) The playing cards have the following values: Ace (A), King (K), Queen (Q), Jack (J) and 10 (T) have a value of 10 each. The other cards have the value indicated by the card number. Define a function f(player1,player2) that returns true if the first player has cards of the same or higher value, and false otherwise. Example: 

f("AJ972","AQT72") à False 
f("9532","K8") à True '''

def f(player1, player2):

    cards = {'A':10,
        'K':10,
        'Q':10,
        'J':10,
        'T':10}
    
    sum_player1 = 0
    for char in player1:
        if char in cards:
            char = cards[char]
            sum_player1 += int(char)
        else:
            sum_player1 += int(char)

    sum_player2 = 0
    for char in player2:
        if char in cards:
            char = cards[char]
            sum_player2 += int(char)
        else:
            sum_player2 += int(char)
    print(sum_player1, sum_player2)
    if sum_player1 >= sum_player2:
        return True
    return False

print(f('9532', 'K8'))