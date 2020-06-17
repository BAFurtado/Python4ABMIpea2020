

def nested_sum(lst):
    acumuladora = 0
    for i in lst:
        acumuladora += sum(i)
    return acumuladora


def nested_sum_varying_size(lst):
    # Essa função explicita o uso do par: TRY: tentativa, 4 espaços e EXCEPT tipo de erro, tenta outra coisa.
    # Além disso, essa função usa a função RECURSIVA.
    total = 0
    for i in lst:
        try:
            # Try integer
            total += i
        except TypeError:
            try:
                # Try a list
                total += sum(i)
            except TypeError:
                # If there is another list on the list, use RECURSÃO
                total += nested_sum_varying_size(i)
    return total


if __name__ == '__main__':
    #
    # t = [[1, 2], [3, 5, 6, [6], 6, 6, 6], [4, 5, 6, 8, 9]]
    # print(nested_sum(t))

    x = [1, 2, 3, [4, 5], 6, 7, 8, 9, 10, 11, [12, [13, 14, [15, [16]]]]]
    print(nested_sum_varying_size(x))
