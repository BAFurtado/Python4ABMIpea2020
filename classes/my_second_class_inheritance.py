# Exemplo de herança -- inheritance


from classes.my_first_class import Animal


class Dog(Animal):

    def sound(self):
        return 'bark, bark, bark'


class Cat(Animal):

    def sound(self):
        return 'miaouw, miaouw, miaouw'


class Funcionarios():
    # TODO incluir horas trabalhadas, salário, controle férias
    pass


class Gerente(Funcionarios):
    # TODO incluir distribuição bonus
    pass


if __name__ == '__main__':
    a = Dog('Augusto')
    print(a.age)
    print(a.name)
    print(a)
    print(a.sound())
    b = Cat('James')
    print(b.sound())
