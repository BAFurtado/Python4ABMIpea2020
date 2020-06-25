""" Manipulating class objects in relation to one another
"""

# TODO: Planejar as classes necessárias

# 1. Criar classes
# 2. Criar instâncias das classes (lista)

# 3. Chamar as instâncias das listas e promover interação
# 4. Classes devem prever interação
# 5. Dinãmica geral: início, interação, output resultados.


class Morador:
    def __init__(self, name):
        self.name = name
        self.renda = 0

    def adiciona_renda(self, quantia):
        self.renda += quantia

    def transfere_renda(self):
        self.renda = 0


class Domicilios:
    def __init__(self):
        self.endereco = None
        self.moradores = list()
        self.poupanca = 0

    def adiciona_morador(self, morador):
        self.moradores.append(morador)

    def poupanca_da_familia(self):
        for m in self.moradores:
            self.poupanca += m.renda
            m.transfere_renda()


if __name__ == '__main__':
    dom1 = Domicilios()
    m1 = Morador('Sirley')
    dom1.adiciona_morador(m1)
    m1.adiciona_renda(10000)
    print(m1.renda)
    print(dom1.poupanca)
    dom1.poupanca_da_familia()
    print(m1.renda)
    print(dom1.poupanca)
    m2 = Morador('Pandas')
    dom1.adiciona_morador(m2)
    m2.adiciona_renda(600)
    dom1.poupanca_da_familia()
    print(dom1.poupanca)

