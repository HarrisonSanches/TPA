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



        linha = input().split()

    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))