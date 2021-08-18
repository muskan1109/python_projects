# Program name: tangential_circles.py

import turtle

START_RADIUS = 10
RADIUS_INCREMENT = 5

def tangential_circles(total_circles):
    '''Draw tangential circles.'''
    # iterate through all radius values and draw circle for each radius
    # use range function in for loop to iterate through each radius
    # start - START_RADIUS
    # stop - START_RADIUS + RADIUS_INCREMENT * total_circles
    # step - RADIUS_INCREMENT
    for radius in range(START_RADIUS, \
                        START_RADIUS + RADIUS_INCREMENT * total_circles, \
                        RADIUS_INCREMENT):
        turtle.circle(radius) # drawing circle

def move_to(position):
    '''Move turtle to position. Pick the pen up before moving and put the pen
        back down afterwards.
    '''
    # pen is lifted (to ensure no drawing when changing position)
    turtle.penup() 
    # change position 
    turtle.goto(position) 
    # pen is put down to draw
    turtle.pendown() 

def main():
    # turtle speed set to 10
    turtle.speed(10) 
    # movement set to (-50,0)
    move_to((-50, 0)) 
    # no. of circles set to 10
    tangential_circles(10)

    # movement set to (50,0)
    move_to((50, 0)) 
    # rotate 90 degree clockwise (to draw in same orientation as in PDF)
    turtle.right(90) 
    # no. of circles set to 10
    tangential_circles(10) 

    turtle.exitonclick()

if __name__ == "__main__":
    main()
