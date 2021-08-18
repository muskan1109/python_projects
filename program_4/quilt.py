# Program name: quilt.py 

import random
import sys
from ezgraphics import GraphicsWindow

QUILT_WIDTH = 300
QUILT_HEIGHT = 200 
N = 2                       # default dimensions of quilt if no 
                            # selection made by the user

OUTLINE_COLOUR = "black"    # patch outline
FILL_COLOUR = "orange"      # patch colour


def draw_HH(canvas, x, y, width, height):
    """
    Draw pattern HH on the canvas at x, y, with width, height.

    Parameters
    ----------
    canvas : canvas object
        ezgraphics canvas on which we draw the design
    x : int
        x coordinate of top-left of rectangle
    y : int
        y coordinate of top-left of rectangle    
    width : int
        patch width
    height : int
        patch height
        
    """
    
    # set colour of outline to black
    canvas.setOutline(OUTLINE_COLOUR)
    # draw rectangle 
    canvas.drawRectangle(x, y, width, height)
    # set fill colour to orange 
    canvas.setFill(FILL_COLOUR)
    # draw triangle 
    canvas.drawPoly(x, y, x, (y + height), (x + width), y)
    # set fill colour to white
    canvas.setFill("white")


def draw_TH(canvas, x, y, width, height):
    """
    Draw pattern TH on the canvas at x, y, with width, height.

    Parameters
    ----------
    canvas : canvas object
        ezgraphics canvas on which we draw the design
    x : int
        x coordinate of top-left of rectangle
    y : int
        y coordinate of top-left of rectangle    
    width : int
        patch width
    height : int
        patch height
        
    """

    # set colour of outline to black
    canvas.setOutline(OUTLINE_COLOUR)
    # draw rectangle 
    canvas.drawRectangle(x, y, width, height)
    # set fill colour to orange 
    canvas.setFill(FILL_COLOUR)
    # draw triangle 
    canvas.drawPoly(x, y, x, (y + height), (x + width), (y + height))
    # set fill colour to white
    canvas.setFill("white")


def draw_HT(canvas, x, y, width, height):
    """
    Draw pattern TH on the canvas at x, y, with width, height.

    Parameters
    ----------
    canvas : canvas object
        ezgraphics canvas on which we draw the design
    x : int
        x coordinate of top-left of rectangle
    y : int
        y coordinate of top-left of rectangle    
    width : int
        patch width
    height : int
        patch height
        
    """

    # set colour of outline to black
    canvas.setOutline(OUTLINE_COLOUR)
    # draw rectangle 
    canvas.drawRectangle(x, y, width, height)
    # set fill colour to orange 
    canvas.setFill(FILL_COLOUR)
    # draw triangle 
    canvas.drawPoly((x + width), y, x, (y + height), (x + width), (y + height))
    # set fill colour to white
    canvas.setFill("white")


def draw_TT(canvas, x, y, width, height):
    """
    Draw pattern TT on the canvas at x, y, with width, height.

    Parameters
    ----------
    canvas : canvas object
        ezgraphics canvas on which we draw the design
    x : int
        x coordinate of top-left of rectangle
    y : int
        y coordinate of top-left of rectangle    
    width : int
        patch width
    height : int
        patch height
        
    """

    # set colour of outline to black
    canvas.setOutline(OUTLINE_COLOUR)
    # draw rectangle 
    canvas.drawRectangle(x, y, width, height)
    # set fill colour to orange 
    canvas.setFill(FILL_COLOUR)
    # draw triangle 
    canvas.drawPoly(x, y, (x + width), (y + height), (x + width), y)
    # set fill colour to white
    canvas.setFill("white")


def draw_quilt(canvas, x, y, width, height, n):
    """ 
    Draw a quilt of dimensions width, height with n patches in each row and col.

    Parameters
    ----------
    canvas : canvas object
        ezgraphics canvas on which we draw the design
    x : int 
        x coordinate of top-left of rectangle
    y : int
        y coordinate of top-left of rectangle    
    width : int
        patch width
    height : int
        patch height
    n : int
        number of patches in one dimension    
    """
    truchet = generate_truchet(n, n) # call generate_truchet() function 
    index = 0 # index will go through the truchet string
    for y_coord in range(y, y + (height // n) * n, height // n): # each row
        for x_coord in range(x, x + (width // n) * n, width // n): # each column
            if truchet[index:index + 2] == "HH":
                draw_HH(canvas, x_coord, y_coord, width // n, height // n)
            elif truchet[index:index + 2] == "HT":
                draw_HT(canvas, x_coord, y_coord, width // n, height // n)        
            elif truchet[index:index + 2] == "TH":
                draw_TH(canvas, x_coord, y_coord, width // n, height // n)        
            elif truchet[index:index + 2] == "TT":
                draw_TT(canvas, x_coord, y_coord, width // n, height // n)
            index += 2; # increment index by 2 to go to the next pattern

def generate_truchet(width, depth):
    """ 
    Return a string of characters. Each pair of characters in the string 
    represents a Truchet tile.

    The symbol for a truchet tile must be one of the options: HH, HT, TH, TT. 
    The number of symbols in the string will be equal to the number of 
    patches in the quilt. The number of patches = width x depth.

    Parameters
    ----------
    width : int
        Width of the quilt in number of patches.
    depth : int
        Depth of the quilt in number of patches.

    Returns
    -------
    str
        truchet values
    """
    # output_truchet holds the truchet string 
    output_truchet = ""

    # patches holds all patches
    patches = ["HH", "HT", "TH", "TT"]

    for i in range(0, width * depth, 1):
        # generate random patch each time and append to string 
        output_truchet += random.choice(patches)
    
    return output_truchet


def help_message():
    """
    Return help message for this program.


    Returns
    -------
    str
        Help message

    """
    return 'Use:\n\n' \
        + 'HH patch:' \
        + '\t\t\t\t\t\t\t\tpython3 quilt.py -HH\n' \
        + 'HT patch:' \
        + '\t\t\t\t\t\t\t\tpython3 quilt.py -HT\n' \
        + 'TH patch:' \
        + '\t\t\t\t\t\t\t\tpython3 quilt.py -TH\n' \
        + 'TT patch:' \
        + '\t\t\t\t\t\t\t\tpython3 quilt.py -TT\n' \
        + 'Quilt patch:' \
        + '\t\t\t\t\t\t\t\tpython3 quilt.py -quilt\n' \
        + 'Quilt with n x n patches:' \
        + '\t\t\t\t\t\tpython3 quilt.py -quilt [n]\n' \
        + 'Quilt with n x n patches with w pixels in width and h pixels in height:' \
        + '\tpython3 quilt.py -quilt [n] [w] [h]\n' \
        + '\n*n, w, h are integers'


def usage_message():
    """
    Return usage message for this program.


    Returns
    -------
    str
        Usage message

    """
    return 'quilt.py: incorrect usage\n' \
        + 'Use:\n' \
        + '\tpython3 quilt.py' \


def main():

    # DO NOT EDIT THIS CODE
    # main() is lengthy because we are handling all the test cases.
    n = N                   # default value for number of patches
    width = QUILT_WIDTH     # default value for quilt width in pixels
    height = QUILT_HEIGHT   # default value for quilt height in pixels

    args = sys.argv[1:]
    if len(args) < 1 or len(args) > 4:
        #print('usage: (one of -TT -TH, -HT, -HH, -quilt) [n] [width] [height]')
        return print(help_message())    

    # Parse [n]/[width]/[height] from command line, giving a helpful
    # error message if it fails.

    try:
        if len(args) > 1:
            n = int(args[1])
            print("n is: ", n)

        if len(args) > 2:
            width = int(args[2])
            height = int(args[3])
    except Exception:
        print("Error parsing int n/width/height from command line:" + ' '.join(args))
        return

    if args[0] == '-HH':
        win = GraphicsWindow(width * 2, height * 2)
        canvas = win.canvas()
        draw_HH(canvas, 0, 0, width, height)
        draw_HH(canvas, width, height, width, height)
    elif args[0] == '-HT':
        win = GraphicsWindow(width * 2, height * 2)
        canvas = win.canvas()
        draw_HT(canvas, 0, 0, width, height)
        draw_HT(canvas, width, height, width, height)
    elif args[0] == '-TH':
        win = GraphicsWindow(width * 2, height * 2)
        canvas = win.canvas()
        draw_TH(canvas, 0, 0, width, height)
        draw_TH(canvas, width, height, width, height)
    elif args[0] == '-TT':
        win = GraphicsWindow(width * 2, height * 2)
        canvas = win.canvas()
        draw_TT(canvas, 0, 0, width, height)
        draw_TT(canvas, width, height, width, height)
    else:
        print(usage_message())
        exit(1)
    """
    else: # args[0] is assumed to be -quilt
        win = GraphicsWindow(width, height)
        canvas = win.canvas()
        draw_quilt(canvas, 0, 0, width, height, n)
    """
    win.wait()

if __name__ == "__main__":
    main()