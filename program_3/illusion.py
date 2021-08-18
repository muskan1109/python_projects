# Program name: illusion.py

import sys
from ezgraphics import GraphicsWindow

WIDTH = 500
BOARD_DIMENSION = 10
# '//' is to make sure SQUARE_DIMENSION is an integer 
SQUARE_DIMENSION = WIDTH // BOARD_DIMENSION 
MORTAR_WIDTH = 2
MORTAR_COLOR = "grey"
 
 
def draw_row(canvas, x, y, square_dimension, row_length, fill_square=True):
    '''
    Draw a row of squares 

    Parameters 
    ----------
    canvas : GraphicsCanvas
        A reference to the GraphicsCanvas contained in the window
    x : int
        x coordinate of the top-left corner of the first square in the row
    y : int
        y coordinate of the top-left corner of the squares in the current row
    square_dimension : int
        Side length in pixels of a square
    row_length : int
        number of squares in one row
    fill_square : boolean
        used to indicate whether the square should be black or white
    '''
    
    for x_coord in range(x, square_dimension*row_length, square_dimension):
        # when fill_square is True, the square is black (else it is white)
        canvas.setFill("black") if fill_square == True \
                                else canvas.setFill("white")
        # draw a reactangle (with all sides = square_dimension)
        canvas.drawRect(x_coord, y, square_dimension, square_dimension)
        # toggle fill_square to alternate between black and white
        fill_square = not fill_square


def draw_cafe_wall(canvas, x, y, square_dimension, board_dimension):
    """
    Draw cafe wall illusion.


    Parameters
    ----------
    canvas : GraphicsCanvas
        A reference to the GraphicsCanvas contained in the window
    x : int
        x coordinate of the top-left corner of the row
    y : int
        y coordinate of the top-left corner   the row
    square_dimension : int
        side length in pixels of a square
    board_dimension : int
        number of squares in one side of the board

    """
    
    # color of outline
    canvas.setOutline(MORTAR_COLOR)
    # width of outline
    canvas.setLineWidth(MORTAR_WIDTH)
    # x_vals holds the values of the x coordinates with which the row can start
    x_vals = [x + (square_dimension // 2), x]

    # for loop to make board_dimension rows
    for i in range(0, board_dimension, 1):
        # if i % 2 = 0, x is passed else x + square_dimension // 2 is passed
        draw_row(canvas, x_vals[i % 2], y, square_dimension, board_dimension)
        y += square_dimension # increment y by square_dimension
    

def draw_chequerboard(canvas, x, y, square_dimension, board_dimension,
                      chequers=False):
    """
    Draw the board.


    Parameters
    ----------
    canvas : GraphicsCanvas
        A reference to the GraphicsCanvas contained in the window
    x : int
        x coordinate of the top-left corner of the row
    y : int
        y coordinate of the top-left corner of the row
    square_dimension : int
        side length in pixels of a square
    board_dimension : int
        number of squares in a side of the board
    chequers : boolean
        Used to indicate whether the squares in every row should be
        alternately black and white

    """

    # used to indicate if first square in the row is black or white 
    fill_square = False 

    # for loop to make board_dimension rows
    for i in range(0, board_dimension, 1):  
        draw_row(canvas, x, y, square_dimension, board_dimension, fill_square)
        y += square_dimension # y is incremented by square_dimension
        # if chequers=True, fill_square is toggled each time after drawing a row
        if chequers == True:
            fill_square = not fill_square


def usage_message():
    """
    Return usage message for this program.


    Returns
    -------
    str
        Usage message

    """

    return 'illusion.py: incorrect usage\n' \
        + 'Use:\n' \
        + '\tpython3 illusion.py' \


def help_message():
    """
    Return help message for this program.


    Returns
    -------
    str
        Help message

    """

    return 'Use:\n\n' \
        + 'Columns pattern:' \
        + '\tpython3 illusion.py -columns \n' \
        + 'Chequers pattern:' \
        + '\tpython3 illusion.py -chequers \n' \
        + 'Cafe illusion pattern:' \
        + '\tpython3 illusion.py -cafe \n'


def check_args(args):
    """
    Check the arguments passed to the program.


    Parameters
    ----------
    args : list
        List of strings in argv containing the options passed to this program

    Returns
    -------
    boolean
        False if option is invalid, True if option is valid

    """

    # Process the command line input
    valid_option = False
    if len(args) == 1:
        valid_option = args[0] == "-chequers" or args[0] == "-cafe"\
            or args[0] == "-columns"
    elif len(args) == 0:
        valid_option = True

    return valid_option


def main():
    args = sys.argv[1:]

    okay = check_args(args)

    option = "-columns"

    if okay:
        # Create a graphics window (WIDTH x WIDTH pixels):
        win = GraphicsWindow(WIDTH, WIDTH)

        # Access the canvas contained in the graphics window:
        canvas = win.canvas()

        if len(args) == 1:
            option = args[0]

        if len(args) == 0:
            print(help_message())
            exit(1)

        if option == "-columns":
            draw_chequerboard(canvas, 0, 0, SQUARE_DIMENSION, BOARD_DIMENSION)
        elif option == "-chequers":
            draw_chequerboard(canvas, 0, 0, SQUARE_DIMENSION, BOARD_DIMENSION,
                              chequers=True)
        else:   # args[0] == "-cafe":
            draw_cafe_wall(canvas, 0, 0, SQUARE_DIMENSION, BOARD_DIMENSION)

        # Wait for the user to close the window
        win.wait()
    else:
        print(usage_message())
        exit(1)


if __name__ == "__main__":
    main()
