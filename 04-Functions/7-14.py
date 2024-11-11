'''14. A device in a door registers people entering and leaving a room.
The + sign means a person entering a room and the - sign a person leaving a room. 
Define the function f(detector) that returns True if at least 3 people were in the room at the same time, or False otherwise. Sample result:

    f("+-+++-+---") returns True
    f("+-+-+-+-") returns False
    f("+-++-+--") returns False
    f("+-++-++-+---") returns True'''

def f(detector):
    enter_count = 0
    leave_count = 0
    for sign in detector:
        if sign == '+':
            enter_count +=1
        elif sign == '-':
            leave_count += 1
        if enter_count-leave_count<3:
            continue
        else:
            return True
    return False
    
