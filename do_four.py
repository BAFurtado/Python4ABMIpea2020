"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""


def do_twice(funcao, argumento):

    """Runs a function twice.

    func: function object
    arg: argument passed to the function
    """
    funcao(argumento)
    funcao(argumento)


def print_twice(argumento):
    """Prints the argument twice.

    arg: anything printable
    """
    print(argumento)
    print(argumento)


def do_four(func, arg):
    """Runs a function four times.

    func: function object
    arg: argument passed to the function
    """
    do_twice(func, arg)
    do_twice(func, arg)


if __name__ == '__main__':
    # do_twice(print, 'Diego Castro Patrimonio')
    # do_twice(print, 'paralelepipedo')
    # print('')
    #
    do_four(print, 'spam')
    # print_twice('Boa noite, pessoal!')
