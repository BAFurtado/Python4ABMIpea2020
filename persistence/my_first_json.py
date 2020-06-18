import json

db = {'data': '2020-06-24', 'hora': '18:30', 'objeto': 'lista_exercicio_1_completa'}


def save_json(ob, file='my_obj.json'):
    with open(file, 'w') as f:
        json.dump(ob, f)
    print('Saved! You can check my_obj.json')


def load_json():
    with open("my_obj.json", "r") as f:
        ll = json.load(f)
    print('A soma da lista lida é {:,.0f}'.format(sum(ll)))
    return ll


def load_generico(file='obj.json'):
    with open(file, 'r') as handler:
        obj = json.load(handler)
    return obj


if __name__ == '__main__':
    # f = 'persistence/numeros.csv'
    # r = reading(f)
    # l = recover_list(r)
    #
    # save_json(l)
    # save_json(db, 'meu_dict_json.json')
    lst1 = load_json()
    meu_dict = load_generico('meu_dict_json.json')
