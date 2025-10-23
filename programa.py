import funcoes as fn

lista_navio_tamanho_quant = [['porta-aviões', 4, 1], ['navio-tanque', 3, 2], ['contratorpedeiro', 2, 3], ['submarino', 1, 4]]
frota = {
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
            eh_valido = fn.posicao_valida(frota, entrada_linha, entrada_coluna, entrada_orientacao, x[1])
            while not eh_valido:
                print('Esta posição não está válida!')
                print(f'Insira as informações referentes ao navio {x[0]} que possui tamanho {x[1]}')
                entrada_linha = int(input('Linha: '))
                entrada_coluna = int(input('Coluna: '))
                entrada_orientacao = 1
                eh_valido = fn.posicao_valida(frota, entrada_linha, entrada_coluna, entrada_orientacao, x[1])
            casas_ocupadas = fn.define_posicoes(entrada_linha, entrada_coluna, entrada_orientacao, x[1])
            frota = fn.preenche_frota(frota, x[0], entrada_linha, entrada_coluna, entrada_orientacao, x[1])
        else:    
            entrada_linha = int(input('Linha: '))
            entrada_coluna = int(input('Coluna: '))
            entrada_orientacao = fn.transforma_orientacao(int(input('Orientação: ')))
            eh_valido = fn.posicao_valida(frota, entrada_linha, entrada_coluna, entrada_orientacao, x[1])
            while not eh_valido:
                print('Esta posição não está válida!')
                print(f'Insira as informações referentes ao navio {x[0]} que possui tamanho {x[1]}')
                entrada_linha = int(input('Linha: '))
                entrada_coluna = int(input('Qual a coluna? '))
                entrada_orientacao = fn.transforma_orientacao(int(input('Orientação: ')))
                eh_valido = fn.posicao_valida(frota, entrada_linha, entrada_coluna, entrada_orientacao, x[1])
            casas_ocupadas = fn.define_posicoes(entrada_linha, entrada_coluna, entrada_orientacao, x[1])
            frota = fn.preenche_frota(frota, x[0], entrada_linha, entrada_coluna, entrada_orientacao, x[1])

print(frota)