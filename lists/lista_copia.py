

def copia_lista(lst):
    """ Essa função recebe uma lista e retorna uma copia dessa lista.
    """
    l2 = []
    for cada in lst:
        l2.append(cada)
    return l2


if __name__ == '__main__':
    l1 = [2, 3, 4, 1, 1, 1, 0, 'segredo', 7]
    l2 = copia_lista(l1)
    print(l1)
    print(l2)
