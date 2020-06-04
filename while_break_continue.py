""" Miscellaneous of while break continue tests """


def got_it(number):
    while number > 0:
        # Quando usar o while -- deixe sempre subjacente alguma maneira do while ser interrompido
        print('Got it!')
        # Contagem regressiva valor = valor - 1
        number -= 1
    # alguma coisa

def para_sempre():
    while True:
        # Não tente em casa!
        print('não vou parar nunca')


def while_true():
    while True:
        ipt = input('Do you wanna stop?')
        if ipt == 'YES!':
            break


def divisivel_por_valor(n, valor):
    for i in range(n):
        # Contagem regressiva
        n -= 1
        if n % valor == 0:
            print(n)
        else:
            # o continue, interrompe o código, ou seja, a proxima linha não é executada,
            # e continua o próximo item do loop
            continue
            # por isso que essa linha, após o continue nunca vai rodar...
            # o próximo item do loop "for" é que roda...
            print('This is an never going to print')


def outro_continue_ou_break(test):
    """ Este exemplo recebe uma palavra teste. Se o teste for 'breaK', o programa, de fato, interrompe a execução
        após print('break')
        Se a palavra teste for 'continu', o programa, de fato, continua o loop e termina a passagem pela palavra python
        """
    for letter in 'PytHon':     # First Example
        if letter == 'H':
            if test == "break":
                # o break sai do loop/conditional. ele interrompe o loop
                print('break')
                break
            if test == "continue":
                # o continue é o contrário, ele interrompe a linha, MAS continua o loop...
                print('continue')
                continue
        print('Current Letter :', letter)


if __name__ == '__main__':
    # got_it(5)
    # while_true()
    divisivel_por_valor(200, 133)
    # outro_continue_ou_break("break")
    # outro_continue_ou_break("continue")
