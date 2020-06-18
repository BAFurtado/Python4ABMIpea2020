import pickle


def save_pickle(ob):
    with open('my_first_serialized_python_obj', 'wb') as f:
        pickle.dump(ob, f)
    print('Saved!!!')


def load_pickle():
    with open('my_first_serialized_python_obj', 'rb') as f:
        # agora na leitura, utilizo 'rb' read bytes
        # na escrita, use 'wb', write bytes
        ll = pickle.load(f)
    print('A soma da lista lida é {}'.format(sum(ll)))
    print('Lida!')
    return ll


if __name__ == '__main__':
    # f = 'persistence/numeros.csv'
    # r = reading(f)
    # l = recover_list(r)
    # save_pickle(l)
    load_pickle()
