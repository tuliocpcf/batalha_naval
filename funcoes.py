def define_posicoes(linha, coluna, orientacao, tamanho):
    casas_ocupadas = []
    for i in range(tamanho):
        if orientacao == 'vertical':
            casas_ocupadas.append([linha + i, coluna]) 
        else:
            casas_ocupadas.append([linha, coluna + i])
    return casas_ocupadas

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    if nome_navio in frota:
        frota[nome_navio] += [define_posicoes(linha, coluna, orientacao, tamanho)]
    else:
        frota[nome_navio] = [define_posicoes(linha, coluna, orientacao, tamanho)]
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro