"""
Exercicio resolvido: uva_12247 - JOllo
Autores: Leonardo Laia Arpini, Harrison Sanches, Matheus Garcias

"""
def condicao(carta1, carta2, carta3, carta4, carta5):
    if carta1 > carta4:
        if carta2 > carta5:
            return -1
        if carta2 < carta5:
            return carta3 + 1
    else:
        if carta2 > carta5:
            return carta3 + 1
        else:
            return 1


def main(args):
    linha = input()
    while linha != '0 0 0 0 0':
        linha = linha.split()
        cartas = []
        carta1, carta2, carta3, carta4, carta5 = int(linha[0]), int(linha[1]), int(linha[2]), int(linha[3]), int(linha[4])
        condicoes = []
        cartas.append(carta1)
        cartas.append(carta2)
        cartas.append(carta3)
        cartas.append(carta4)
        cartas.append(carta5)

        condicoes.append(condicao(carta1, carta2, carta3, carta4, carta5))
        condicoes.append(condicao(carta1, carta3, carta2, carta4, carta5))
        condicoes.append(condicao(carta2, carta1, carta3, carta4, carta5))
        condicoes.append(condicao(carta2, carta3, carta1, carta4, carta5))
        condicoes.append(condicao(carta3, carta1, carta2, carta4, carta5))
        condicoes.append(condicao(carta3, carta2, carta1, carta4, carta5))

        condicoes.sort()

        impossivel = -1
        if impossivel in condicoes:
            print(-1)
        else:
            menor_carta = max(condicoes)
            while menor_carta in cartas:
                menor_carta += 1
            if menor_carta <= 52:
                print(menor_carta)
            else:
                print("-1")

        linha = input()

    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
