

def remove_duplicates(l):
    l2 = list()
    for i in l:
        if i in l2:
            # o comando continue interrompe o for e continua no proximo elemento
            continue
            # faça alguma coisa, se o continue ocorre, o programa nunca chega nessa linha
        else:
            l2.append(i)
    return l2


if __name__ == '__main__':
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 3]
    result = remove_duplicates(l1)
    if len(result) < len(l1):
        print("We found duplicates!")
    else:
        print("No duplicates found!")