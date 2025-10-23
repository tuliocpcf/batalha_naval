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

def afundados(frota, tabuleiro):
    n_afundados = 0
    for navio, posicoes in frota.items():
        for posicao in posicoes:
            afundou = True
            for coordenada in posicao:
                if tabuleiro[coordenada[0]][coordenada[1]] != 'X':
                    afundou = False
            if afundou == True:
                n_afundados += 1
    return n_afundados

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    entrada = define_posicoes(linha, coluna, orientacao, tamanho)

    for coordenada in entrada:
        if coordenada[0] < 10 and coordenada[1] < 10:
            eh_valido = True
            for navio, posicoes in frota.items():
                for posicao in posicoes:
                    if coordenada in posicao:
                        eh_valido = False
                        break
                if not eh_valido:
                    break
            if not eh_valido:
                break
        else:    
            eh_valido = False
            break
    return eh_valido

def transforma_orientacao(orientacao):
    if orientacao == 1:
        return 'vertical'
    else:
        return 'horizontal'