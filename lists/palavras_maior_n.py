

def palavras_maior(n, words):
    """ Essa função recebe um valor para comparar o tamanho de cada palavra e uma lista de palavras.
        Retorna todas as palavras da lista que são maiores que o valor estipulado.
        """
    results = list()
    for word in words:
        if len(word) > n:
            results.append(word)
    return results


if __name__ == '__main__':
    palavras = ['Brasil', 'COVID', 'o', 'Aulas', 'Mestrado do Ipea', 'Python',
                'Na próxima aula já tem lista de exercícios']
    m = 8
    grandes = palavras_maior(m, palavras)
