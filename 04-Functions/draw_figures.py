'''3. The following program draws a square with a specified side length using the turtle module.'''

import turtle

    # Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

    # Create the turtle
pen = turtle.Turtle()
pen.speed(5)

    # Hide the turtle and finish
pen.hideturtle()
window.mainloop()

'''Save the program in the file draw_figures.py. Then, run the program. 
    Next, change the program so that the square is drawn using the draw_square(length) function with the only parameter being the length of the square's side. 
    Place the defined function in a separate module figures.py. Finally, run the program again.

    ###
    # Draw a square
    #
    def draw_square(length)
        ...
        ...'''