"""
Student Name: Victor Oliveira
Project: In-Lab 2
08/29/20

This program will use recursion to draw a pattern of squares that get smaller and smaller depending
on the input number of 'depths' they put. The colors of each depth will also alternate.
"""

import turtle

# Global constant COLORS so that, if need be, the colors need to change
COLORS = ('orange', 'blue')


def draw_square_rec(size, depth):
    """

    :param size: indicates how big the initial square the user wants
    :param depth: int that represents the total number of levels that the user wants
    :return: None.
    """

    # base case to stop once the final depth is reached
    if depth == 0:
        pass
    else:
        # pen color will change depending on the level (will either be 1 or 0)
        turtle.pencolor(COLORS[depth % 2])

        # For loop to draw the squares depending on the size from user
        for i in range(2):
            turtle.forward(size)
            turtle.left(90)
        # Recursive calls that passes in size / 3 and decrements depth by 1
        draw_square_rec(size / 3, depth - 1)

        # same calls as above to draw other side of squares
        turtle.pencolor(COLORS[depth % 2])
        for i in range(2):
            turtle.forward(size)
            turtle.left(90)
        draw_square_rec(size / 3, depth - 1)


def main():
    # prompt for user to inter in depth level
    depth = int(input("Enter the depth levels: "))

    # prompt for user to enter in size
    size = int(input("Enter the size of your squares: "))

    # calls draw square function based on user inputed values
    draw_square_rec(size, depth)

    print('Close the graphic window when done.')
    turtle.mainloop()


if __name__ == '__main__':
    main()
