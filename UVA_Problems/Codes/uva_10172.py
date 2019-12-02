"""
Exercicio resolvido: uva_00939 - The Lonesome Cargo Distributor
Autores: Leonardo Laia Arpini, Harrison Sanches, Mathues Garcias
"""

from sys import stdin, stdout
input = stdin.readline
SET = int(input())
for _ in range(SET):
    N, S, Q = [int(x) for x in input().split()]
    platform = []
    s = 0
    for _ in range(N):
        tmp = [int(x) for x in input().split()]
        s += tmp[0]
        platform.append([i-1 for i in tmp[1:]])
    carros = []
    pos = 0
    time = 0
    while True:
        while len(carros):
            if carros[-1] == pos:
                carros.pop()
                s -= 1
            elif len(platform[pos]) < Q:
                platform[pos].append(carros.pop())
            else:
                break
            time += 1
        while len(platform[pos]) and len(carros) < S:
            carros.append(platform[pos].pop(0))
            time += 1
        pos += 1
        if pos == N:
            pos = 0
        if s == 0:
            print(time)
            break
        time += 2
