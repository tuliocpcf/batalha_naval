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

def posiciona_frota (frota):
    tabuleiro = []
    for x in range(10):
        linha = []
        for y in range(10):
            linha.append(0)
        tabuleiro.append(linha)

    for nome_navio in frota:
        for navio in frota[nome_navio]: 
            for posicao in navio:        
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro[linha][coluna] = 1  
    
    return tabuleiro

def afundados(relatorio, tabuleiro):
    n_afundados = 0
    for navio, posicoes in relatorio.items():
        for posicao in posicoes:
            afundou = True
            for coordenada in posicao:
                if tabuleiro[coordenada[0]][coordenada[1]] != 'X':
                    afundou = False
            if afundou == True:
                n_afundados += 1
    return n_afundados