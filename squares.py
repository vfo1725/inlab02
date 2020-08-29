"""
Student Name: Victor Oliveira
Project: In-Lab 2
08/29/20

This program will use recursion to draw a pattern of squares that get smaller and smaller depending
on the input number of 'depths' they put. The colors of each depth will also alternate.
"""

import turtle



def draw_square_rec(size, depth):
    """

    :param size: indicates how big the initial square the user wants
    :param depth:
    :return:
    """
    if depth == 0:
        pass
    else:
        turtle.pencolor(COLORS[depth % 2])
        for i in range(2):
            turtle.forward(size)
            turtle.left(90)
        draw_square_rec(size/3, depth-1)
        turtle.pencolor(COLORS[depth % 2])
        for i in range(2):
            turtle.forward(size)
            turtle.left(90)
        draw_square_rec(size/3, depth-1)


def main():
    depth = int(input("Enter the depth levels: "))
    size = int(input("Enter the size of your squares: "))
    draw_square_rec(size, depth)

    print('Close the graphic window when done.')
    turtle.mainloop()

if __name__ == '__main__':
    main()