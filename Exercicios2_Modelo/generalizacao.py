from Exercicios2_Modelo import simulation


if __name__ == '__main__':
    passos = 10
    todas_as_medias = 0
    for i in range(passos):
        sim = simulation.Simulacao()
        todas_as_medias += sim.run_model()
    print(f'A média da experiencia de simular {passos} número de vezes é: {todas_as_medias/passos}')
        # Guardar o valor da média
