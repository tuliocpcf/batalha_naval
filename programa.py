import funcoes as fn

lista_navio_tamanho_quant = [['porta-aviões', 4, 1], ['navio-tanque', 3, 2], ['contratorpedeiro', 2, 3], ['submarino', 1, 4]]
frota_jogador = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
} 

for x in lista_navio_tamanho_quant:
    for i in range(x[2]): #repete o loop pela quantidade de vezes descrita na 'lista_navio_tamanho_quant'    
        print(f'Insira as informações referentes ao navio {x[0]} que possui tamanho {x[1]}')
        if x[1] == 1:    
            entrada_linha = int(input('Linha: '))
            entrada_coluna = int(input('Coluna: '))
            entrada_orientacao = 1
            eh_valido = fn.posicao_valida(frota_jogador, entrada_linha, entrada_coluna, entrada_orientacao, x[1])
            while not eh_valido:
                print('Esta posição não está válida!')
                print(f'Insira as informações referentes ao navio {x[0]} que possui tamanho {x[1]}')
                entrada_linha = int(input('Linha: '))
                entrada_coluna = int(input('Coluna: '))
                entrada_orientacao = 1
                eh_valido = fn.posicao_valida(frota_jogador, entrada_linha, entrada_coluna, entrada_orientacao, x[1])
            casas_ocupadas = fn.define_posicoes(entrada_linha, entrada_coluna, entrada_orientacao, x[1])
            frota_jogador = fn.preenche_frota(frota_jogador, x[0], entrada_linha, entrada_coluna, entrada_orientacao, x[1])
        else:    
            entrada_linha = int(input('Linha: '))
            entrada_coluna = int(input('Coluna: '))
            entrada_orientacao = fn.transforma_orientacao(int(input('Orientação: ')))
            eh_valido = fn.posicao_valida(frota_jogador, entrada_linha, entrada_coluna, entrada_orientacao, x[1])
            while not eh_valido:
                print('Esta posição não está válida!')
                print(f'Insira as informações referentes ao navio {x[0]} que possui tamanho {x[1]}')
                entrada_linha = int(input('Linha: '))
                entrada_coluna = int(input('Qual a coluna? '))
                entrada_orientacao = fn.transforma_orientacao(int(input('Orientação: [1] Vertical [2] Horizontal ')))
                eh_valido = fn.posicao_valida(frota_jogador, entrada_linha, entrada_coluna, entrada_orientacao, x[1])
            casas_ocupadas = fn.define_posicoes(entrada_linha, entrada_coluna, entrada_orientacao, x[1])
            frota_jogador = fn.preenche_frota(frota_jogador, x[0], entrada_linha, entrada_coluna, entrada_orientacao, x[1])

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_jogador = fn.posiciona_frota(frota_jogador)
tabuleiro_oponente = fn.posiciona_frota(frota_oponente)

jogando = True
lista_de_ataques_jogador = []

while jogando:
    print(fn.monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
    linha_ataque = int(input('Jogador, qual linha deseja atacar? '))
    while linha_ataque not in [0,1,2,3,4,5,6,7,8,9]:
        print('Linha inválida!')
        linha_ataque = int(input('Jogador, qual linha deseja atacar? '))

    coluna_ataque = int(input('Jogador, qual coluna deseja atacar? '))
    while coluna_ataque not in [0,1,2,3,4,5,6,7,8,9]:
        print('Coluna inválida!')
        coluna_ataque = int(input('Jogador, qual coluna deseja atacar? '))

    while [linha_ataque, coluna_ataque] in lista_de_ataques_jogador:
        print(f'A posição linha {linha_ataque} e coluna {coluna_ataque} já foi informada anteriormente!')

        linha_ataque = int(input('Jogador, qual linha deseja atacar? '))
        while linha_ataque not in [0,1,2,3,4,5,6,7,8,9]:
            print('Linha inválida!')
            linha_ataque = int(input('Jogador, qual linha deseja atacar? '))

        coluna_ataque = int(input('Jogador, qual coluna deseja atacar? '))
        while coluna_ataque not in [0,1,2,3,4,5,6,7,8,9]:
            print('Coluna inválida!')
            coluna_ataque = int(input('Jogador, qual coluna deseja atacar? '))

    lista_de_ataques_jogador.append([linha_ataque, coluna_ataque])
    tabuleiro_oponente = fn.faz_jogada(tabuleiro_oponente, linha_ataque, coluna_ataque)

    if fn.afundados(frota_oponente, tabuleiro_oponente) == 10:
        jogando = False

print('Parabéns! Você derrubou todos os navios do seu oponente!')
