def quadrados_impares():
    quadrados = []
    quadrado = 0
    i = 1
    while quadrado < 99000:
        if i % 2 != 0:
            quadrado = i*i
            quadrados.append(quadrado)
        i += 2
    return quadrados

def pesquisa_binaria_recursiva(lista, esquerda, direita, item):
    if direita < esquerda:
        return -1
    meio = (esquerda + direita) // 2
    if lista[meio] == item:
        return meio
    elif lista[meio] > item:
        return pesquisa_binaria_recursiva(lista, esquerda, meio - 1, item)
    else: # lista[meio] < item
        return pesquisa_binaria_recursiva(lista, meio + 1, direita, item)




def main(args):

    quadrados = quadrados_impares()
    linha = input().split()
    while linha[0] != '0' and linha[1] != 0:
        tam = int(linha[0])
        elem = int(linha[1])
        if tam % 2 == 0:
            print("-1")
        elif elem == 1:
            print("Line =",2,",","column = ",2,".")
        elif elem == tam*tam:
            pos = pesquisa_binaria_recursiva(quadrados,0,len(quadrados)-1,elem)
            centro = tam - pos
            print("posição do centro", centro)
            print("Line =", centro + pos, ",", "column =", centro + pos,".")
        else:
            max = tam*tam
            pos = pesquisa_binaria_recursiva(quadrados, 0, len(quadrados)-1, max)
            centro = tam-pos
            i = 0
            while quadrados[i] < elem:
                i += 1

            faixa1 = []
            for j in range(1,tam,1):
                faixa1.append(max -j)

            posicao = -1
            for i in range(len(faixa1)):
                if faixa1[i] == elem:
                    posicao = i
                    break

            if posicao != -1:
                print("Line =", centro + pos, ",", "column =", centro + pos - (posicao+1),".")

            faixa2 = []
            ultimo_elem = faixa1[-1]
            for k in range(1,tam,1):
                faixa2.append(ultimo_elem-k)

            posicao = -1
            for i in range(len(faixa2)):
                if faixa2[i] == elem:
                    posicao = i
                    break

            if posicao != -1:
                print("Line =", centro + pos - (posicao+1), ",", "column =",  centro + pos - (tam-1), ".")


            faixa3 = []
            ultimo_elem = faixa2[-1]
            for l in range(1,tam,1):
                faixa3.append(ultimo_elem - l)

            posicao = -1
            for i in range(len(faixa3)):
                if faixa3[i] == elem:
                    posicao = i
                    break

            if posicao != -1:
                print("Line =", centro + pos - (tam-1), ",", "column =",  centro + pos - (posicao+1), ".")

            faixa4 = []

            ultimo_elem = faixa3[-1]
            for l in range(1, tam-1, 1):
                faixa4.append(ultimo_elem - l)

            posicao = -1
            for i in range(len(faixa4)):
                if faixa4[i] == elem:
                    posicao = i
                    break

            if posicao != -1:
                print("Line =", centro + pos - (posicao + 1), ",", "column =", centro + pos, ".")






        linha = input().split()

    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))