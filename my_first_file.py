"""
    Exemplos de persistência

"""


def first():
    with open('nome_do_arquivo.txt', 'w') as handler:
        # as handler --- como manuseador (ou algo assim)
        # handler é um OBJETO python que me permite o acesso/manuseio aquele arquivo que está aberto
        handler.write('Mensagem a ser gravada... Este é meu primeiro arquivo persistente em Python!\n')
        handler.write('Sumiu...\n')
        handler.write('Outra mensagem para conferir que veio na linha de baixo\n')
        handler.write('Como viram, o arquivo anterior sumiu')


def second():
    file = 'persistence/meu_segundo_arquivo.txt'
    # Lembrando que 'a' é append... então ele adiciona novas linha, não apaga o texto anterior
    with open(file, 'a') as f:
        f.write('This is my second saved output\n')
        f.write('em inglês, para ficar em sintonia com a língua do python')


# Let's try with some numbers:
def numbers():
    l = list()
    for i in range(10):
        # O quadrado do numero de 0 a 9
        l.append(i ** i)
        print(i)
        print(i ** i)

    with open('persistence/numeros.csv', 'a') as f:
        # Se eu coloco ';' como separador e salvo em CSV, o EXCEL abre direto...
        for each in l:
            f.write('{};'.format(str(each)))


# What have we done?
def reading(file='persistence/texto_para_ser_lido.txt'):
    # parametro opcional, vai dentro do parenteses, com um igual, se o usuário não enviar um parametro novo,
    # o padrão é utilizado, se ele envie, é sobrescrito e utiliza o que foi enviado.
    with open(file, 'r') as handler:
        # troquei o segundo parametro por 'r', para fazer a leitura, 'read'
        lida = handler.read()
    print(lida)
    return lida


def recover_list(li):
    li = li.split('\n')
    # eu poderia uma lista com várias linhas e aí, cada elemento da lista ia ser uma linha...
    recovered = list()
    for each in li[0].split(';'):
        if len(each) > 0:
            recovered.append(int(each))

    print(recovered)
    return recovered


def sum_list(recovered):
    print('A soma da lista recuperada é {:,.0f}'.format(sum(recovered)))
    return sum(recovered)


def salvar_soma(valor):
    with open('soma_lista.txt', 'w') as handler:
        # as handler --- como manuseador (ou algo assim)
        # handler é um OBJETO python que me permite o acesso/manuseio aquele arquivo que está aberto
        handler.write(f'{valor}')



if __name__ == '__main__':
    # first()
    # second()
    # numbers()
    r = reading('persistence/numeros.csv')
    ll = recover_list(r)
    soma = sum_list(ll)
    salvar_soma(soma)
