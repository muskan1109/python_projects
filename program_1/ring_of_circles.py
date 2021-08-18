# Program name: ring_of_circles.py

import turtle 

OUTER_CIRCLE_COLOR = "slate grey"
INSIDE_CIRCLE_RADIUS = 20
INSIDE_CIRCLE_COLOR = "orange"

def setup():
    '''Set turtle characteristics.'''
    turtle.speed(10)
    turtle.pu()     # pen up
    turtle.ht()     # hide turtle
    turtle.seth(0)  # set heading to 0 (east)

def draw_circle(circle_color, radius):
    '''Draw a circle with a radius 'radius' and color 'circle_color'''
    # setting pen color to circle_color
    # setting fill color to circle_color
    turtle.pen(pencolor=circle_color, fillcolor=circle_color) 
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_inside_circle():
    '''Draw the inner circle.'''
    draw_circle(INSIDE_CIRCLE_COLOR, INSIDE_CIRCLE_RADIUS)

# pattern_radius -
# distance from centre of the inner circle to centre of the outer circle
def draw_ring_of_circles(num_circles, outer_circle_radius, pattern_radius):
    '''Draw the outer ring of circles.'''
    # angle = angle of the turtle head, angle first set to 0 degrees (east)
    angle = 0

    while angle < 360:
        turtle.setheading(angle) # set heading
        turtle.forward(pattern_radius) # forward pattern_radius
        # get tutrle pos and add outer circle radius to x pos and move
        turtle.goto((turtle.pos()[0] + outer_circle_radius, turtle.pos()[1]))
        turtle.seth(90) # set heading north
        draw_circle(OUTER_CIRCLE_COLOR, outer_circle_radius)
        turtle.goto((0,0)) # return to (0,0)
        angle = angle + (360 / num_circles) # increment by 360 / n degrees 

def main():
    setup() # set up the turtle
    # moving turtle to center circle at (0,0)  
    turtle.goto((0, -1*INSIDE_CIRCLE_RADIUS))
    turtle.seth(0) # face east
    draw_inside_circle()
    turtle.goto((0,0))
    turtle.seth(0)
    # pattern_radius set to 130
    draw_ring_of_circles(6, 40, 100)  
    turtle.goto((0,0))
    turtle.exitonclick()

if __name__ == "__main__":
    main()
