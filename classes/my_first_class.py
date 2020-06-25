""" Exemplo de classe Animal """


class Animal:
    # Constructor. Todas as variáveis que o objeto vai ter são construídos
    def __init__(self, name, diet='herbivora'):
        # Variáveis padrão do meu objeto
        self.name = name
        self.diet = diet
        self.legs = None
        self.age = 0

    def name(self):
        print(self.name)

    def set_diet(self, type):
        self.diet = type

    def change_legs(self, number):
        self.legs = number

    def get_old(self):
        self.age += 1

    def __repr__(self):
        return 'My name is {}'.format(self.name)


if __name__ == '__main__':
    a = Animal('Aveia')
    # print(a)
    b = Animal('Mel')
    # b.get_old()
    # print(b.age)
    # b.get_old()
    # print(a.age)
    # print(b.name)
    # print('{} is {} years old'.format(b.name, b.age))
