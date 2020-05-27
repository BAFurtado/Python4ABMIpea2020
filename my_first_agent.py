"""
Adapted from Think Python 2, by Allen Downey. Chapter 4
"""

import turtle


def polygon_generalizado(my_agent, n, comprimento_lado):
    """ Receives a turtle and moves it in a square
        Specifically, not using for (yet)
    """
    my_agent.speed(2)
    angle = 360 / n
    for lado in range(n):
        my_agent.fd(comprimento_lado)
        my_agent.lt(angle)
    print('terminado')


if __name__ == '__main__':
    william = turtle.Turtle()
    sirley = turtle.Turtle()
    alan = turtle.Turtle()
    alan.fd(200)
    alan.color('red')
    sirley.fd(50)
    sirley.color('green')
    num_lados = 8
    comprimento = 50
    polygon_generalizado(william, num_lados, comprimento)
    polygon_generalizado(sirley, num_lados, comprimento)
    polygon_generalizado(alan, num_lados, comprimento)

    # for i in range(4):
    #     dif_square(tuga, 25 * i, 20 * i * i)
    turtle.mainloop()

