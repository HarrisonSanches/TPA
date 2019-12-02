"""
Exercicio resolvido: uva11988 - BrokenKeyboard
Autores: Leonardo Laia Arpini, Harrison Sanches, Mathues Garcias

"""

import sys


def coordinates(sz, p):
    x = int(sz // 2)
    y = int(sz // 2)

    col = 1
    linha = 1

    dir = True
    valor = -1

    p -= 1
    while p > 0:
        if dir:
            comp = col
        else:
            comp = linha

        quantia = min(p, comp)
        p -= quantia

        if dir:
            y += (quantia * valor)
            col += 1
        else:
            x += (quantia * valor)
            linha += 1
            valor *= -1
        dir = not dir

    print("Line = ", (sz - y), ", column = ", (x + 1), ".\n")


while True:
    sz, p = sys.stdin.readline().split()
    sz = int(sz)
    p = int(p)
    if sz != 0 or p != 0:
        coordinates(sz, p)
    else:
        break

