def cria_matriz(matriz):
    for i in range(3):
        vet = []
        linha = input()
        vet.append(int(linha[0]))
        vet.append(int(linha[1]))
        vet.append(int(linha[2]))
        matriz.append(vet)

    return matriz
def eh_nula(matriz):
    cont = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 0:
                cont += 1

    if cont == len(matriz)*3:
        return 1
    else:
        return -1

def cria_matriz_zerada(matriz):
    linha_com_zeros = [0] *3
    matriz = [linha_com_zeros] * 3
    return matriz


def transforma_matriz(matriz_nova,matriz):
    matriz_nova[0][1] =
    matriz_nova[0][2] =
    matriz_nova[0][3] =
    matriz_nova[1][0] =
    matriz_nova[1][1] =
    matriz_nova[1][2] =
    matriz_nova[2][0] =
    matriz_nova[2][1] =
    matriz_nova[2][2] =


def main(args):
    try:
        quantidade = int(input())
        input()
        i = 0
        while i < quantidade:
            matriz = []
            matriz = cria_matriz(matriz)
            nova_matriz = cria_matriz_zerada(nova_matriz)
            nao_nula = True


            while nao_nula:
            #     recursão até encontrar uma matriz nula, depois é soó mandar quantas recursões fez - q

            input()
            i += 1



    except EOFError:
        return

    return 0

if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))