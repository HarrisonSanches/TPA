def cria_matriz():
    matriz = []
    for i in range(3):
        vet = []
        linha = input()
        vet.append(int(linha[0]))
        vet.append(int(linha[1]))
        vet.append(int(linha[2]))
        matriz.append(vet)

    return matriz

def eh_nula(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > 0:
                return False
    return True

def cria_matriz_zerada():
    linha_com_zeros = [0] *3
    matriz_nova = [linha_com_zeros] * 3
    return matriz_nova

def transforma_matriz(matriz):
    matriz_nova = []
    linha = []
    linha.append((matriz[0][1] + matriz[1][0]) % 2)
    linha.append((matriz[0][0] + matriz[0][2] + matriz[1][1]) % 2)
    linha.append((matriz[0][1] + matriz[1][2]) % 2)
    matriz_nova.append(linha)

    linha = []
    linha.append((matriz[0][0] + matriz[2][0] + matriz[1][1]) % 2)
    linha.append((matriz[0][1] + matriz[1][0] + matriz[1][2] + matriz[2][1]) % 2)
    linha.append((matriz[0][2] + matriz[1][1] + matriz[2][2]) % 2)
    matriz_nova.append(linha)

    linha = []
    linha.append((matriz[1][0] + matriz[2][1]) % 2)
    linha.append((matriz[2][0] + matriz[1][1] + matriz[2][2]) % 2)
    linha.append((matriz[2][1] + matriz[1][2]) % 2)
    matriz_nova.append(linha)

    return matriz_nova


def main(args):
    try:
        quantidade = int(input())
        input()
        i = 0
        while i < quantidade:
            matriz= cria_matriz()
            if eh_nula(matriz):
                print("-1")
            else:
                contador = 0
                while not eh_nula(matriz):
                    matriz = transforma_matriz(matriz)
                    contador += 1
                print(contador - 1)


            input()
            i += 1


    except EOFError:
        return

    return 0

if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))