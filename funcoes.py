def define_posicoes(linha, coluna, orientacao, tamanho):
    casas_ocupadas = []
    for i in range(tamanho):
        if orientacao == 'vertical':
            casas_ocupadas.append([linha + i, coluna]) 
        else:
            casas_ocupadas.append([linha, coluna + i])
    return casas_ocupadas
