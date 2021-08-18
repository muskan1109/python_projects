# Program name: concentric_circles.py

import turtle

START_RADIUS = 10
RADIUS_INCREMENT = 10

def concentric_circles(total_circles):
    '''Draw concentric circles'''
    # iterate through all radius values and draw circle for each radius
    # use range function in for loop to iterate through each radius
    # start - START_RADIUS
    # stop - START_RADIUS + RADIUS_INCREMENT * total_circles
    # step - RADIUS_INCREMENT
    for radius in range(START_RADIUS, \
                        START_RADIUS + RADIUS_INCREMENT * total_circles, \
                        RADIUS_INCREMENT):
        # move to position with new current radius
        move_to((radius, 0)) 
        # draw circle
        turtle.circle(radius)

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
    # turn turtle 90 degrees anti-clockwise (to match arrowhead in PDF)
    turtle.left(90) 
    turtle.speed(10) 
    concentric_circles(10)
    
    turtle.exitonclick()

if __name__ == "__main__":
    main()
