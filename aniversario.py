import random


def aniversario(num_alunos):
    dias = list()
    for i in range(num_alunos):
        dia = random.randint(1, 365)
        dias.append(dia)
    # Se todos os aniversários forem em dias diferentes, retornaremos TRUE
    # Se algum aniversário for repetido (no mesmo dia), a lista de distintos é menor, portanto, retornaremos FALSE
    return len(dias) == len(set(dias))


def main(num_alunos, num_vezes):
    results = list()
    # Lembrando que no python posso somar True é UM e False é ZERO
    for i in range(num_vezes):
        results.append(aniversario(num_alunos))
    print(f'A probabilidade de termos pelo menos um aniversário repetido em uma turma de {num_alunos} alunos '
          f'é de {(1 - (sum(results)/num_vezes)) * 100:.5f}%, com simulação de {num_vezes} vezes.')


if __name__ == '__main__':
    n_vezes = 10000
    n_alunos = 41
    main(n_alunos, n_vezes)
