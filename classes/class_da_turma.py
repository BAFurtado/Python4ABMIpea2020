""" Exemplo de uma class construída coletivamente
"""


class Aluno:
    def __init__(self, name):
        self.name = name
        self.disciplinas = list()
        self.email = ''


class Turma:
    def __init__(self, name='Python4ABMIpea'):
        self.name = name
        self.students = list()

    def add_student(self, name):
        self.students.append(name)

    def remove_student(self, name):
        self.students.remove(name)

    def count_std(self):
        return len(self.students)

    def list_std(self):
        for each in self.students:
            print(each)

    def __repr__(self):
        return '{} tem {} alunos'.format(self.name, self.count_std())


if __name__ == '__main__':
    t1 = Turma()
    print(type(t1))
    print(t1)
    t1.add_student('Sirley')
    t1.add_student('Paulo Sávio')
    t1.add_student('Paulo Martins')
    t1.add_student('Godoy')
    t1.add_student('William')
    t1.add_student('Alan')
    t1.add_student('Diego')
    t1.add_student('Bruno')
    t1.add_student('Douglas')
    t1.add_student('Kadidja')
    t1.add_student('Marcio')
    print(t1)
    t1.list_std()
    t1.add_student('Bernardo')
    t1.remove_student('Bernardo')
    t2 = Turma('Econometria')
    for aluno in t1.students:
        t2.add_student(aluno)
    t2.remove_student('Sirley')
    t2.remove_student('William')
    t2.remove_student('Alan')
    print(t2)
    t2.list_std()

    b = Aluno('Bernardo')
    t3 = Turma('100daysofwebPython')
    t3.add_student(b)

