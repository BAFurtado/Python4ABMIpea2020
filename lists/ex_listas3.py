""" Exercícios de listas
    Verifique se a palavra é maior que um dado número e a imprima
    """


def big_words(l, num):
    # Função que acha palavras acima de 'num'
    l2 = list()
    for each in l:
        if len(each) > num:
            l2.append(each)

    print('Your big words are/is: \n{}'.format('\n'.join(l2)))


if __name__ == '__main__':
    # coddimwomple é uma gíria inglesa que significa
    # to travel purposefully toward an as-yet-unknown destination
    l1 = ['mom', 'longingly', 'coddiwomple', 'fish', 'boat', 'inconspicous']
    n = 8
    big_words(l1, n)
