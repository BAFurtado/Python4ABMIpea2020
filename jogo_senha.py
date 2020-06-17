import random


def main(tamanho=3):
    # 1. Comecei com uma string vazia
    segredo = ''
    # 2. Adicionei um número aleatório entre 0 e 9, transformado em string, 4x.
    for i in range(tamanho):
        segredo += str(random.randint(0, 9))
    em_jogo = True
    tentativas = 0
    while em_jogo:
        erros, acertos = 0, 0
        tentativas += 1
        chute = input(f'Entre um valor numérico com {tamanho} dígitos: ')
        for i in range(len(segredo)):
            if segredo[i] == chute[i]:
                acertos += 1
            else:
                erros += 1
        if acertos == len(segredo):
            print('Parabéns, você é um grande adivinho!!!')
            print(f'Você acertou em {tentativas} tentativas')
            print(f'Voce chutou {chute} e o segredo era {segredo}')
            em_jogo = False
        else:
            print(f'Você acertou {acertos} dígitos e errou {erros}')
        if chute == 'socorro':
            break


if __name__ == '__main__':
    main()
