

def example_pass():
    pass


def check_empty(l):
    if len(l) == 0:
        print('Empty list')
    else:
        print('List not empty')


def copy_list(l):
    l2 = list()
    for i in l:
        l2.append(i)
    return l2


if __name__ == '__main__':
    l1 = ['hello', 0, 23, 23, 23, 23, 'Osmar']
    check_empty(l1)
    l2 = copy_list(l1)
    l3 = []
    print(l2)
    print(copy_list(l3))
    example_pass()