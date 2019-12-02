"""
Exercicio resolvido: uva11926 - Multitasking
Autores: Leonardo Laia Arpini, Harrison Sanches, Mathues Garcias

Código está apresentando TLE no UVa, porém foram feitos testes com todos os inputs do uDebug referente ao exercício e
todos deram correto. Junto deste arquivo .py se encontra um arquivo input.txt que contém o input do brianfry713
disponível no uDebug e um arquivo expOutput.txt com o output correspondente.
"""

import sys
from collections import deque


def confere(n, m):
    start, end, interval = deque(), deque(), deque()   # inicia os deque responsaveis por armazenar as informações das atividades
    valid = True                                    # inicia valid como true pois se ocorrer conflito não é mais válido

    for i in range(n):                                  # lê as primeiras n linhas que correspondem a atividades em loop
        x, y = sys.stdin.readline().split()
        start.append(int(x))         # ao mesmo tempo que converte em inteiro adiciona o que foi lido no final do deque
        end.append(int(y))

    if n > 1:                 # caso o n seja maior que 1 ocorre a verificação de conflito entre as atividades sem loop
        for i in range(n - 1):
            if valid:
                for p in range(1, n, 1):
                    if (start[p] or end[p]) in range(start[i], end[i]):
                        if (start[p] == start[i]) and (end[p] == end[i]) and (i == p):  # verifica se não é o valor sendo comparado com ele mesmo
                            valid = True
                        elif (start[p] == start[i]) and (end[p] == end[i]) and (i != p):  # verifica se não é o valor sendo comparado com ele mesmo
                            valid = False
                            break
                        elif (start[p] == end[i]) or (end[p] == start[i]):  # verifica se não ocorre somente o toque dos inicios e finais das atividades que não pe considerado conflito
                            break
                        else:
                            valid = False
                            break
                    elif (start[i] or end[i]) in range(start[p], end[p]):
                        if (start[p] == start[i]) and (end[p] == end[i]) and (i == p):
                            valid = True
                        elif (start[p] == start[i]) and (end[p] == end[i]) and (i != p):
                            valid = False
                            break
                        elif (start[p] == end[i]) or (end[p] == start[i]):
                            break
                        else:
                            valid = False
                            break
            else:
                break

    if m > 0:                                    # se m for maior que zero e não tenha ocorrido conflito em n, irá ocorrer a leitura das m linhas que ocorrem depois de n
        for i in range(n):
            interval.append(0)                             # como m tem outra variavel alem do start e end, é inserido 0 nas posições correspondentes aos valores de n em start e end
        for i in range(m):
            x, y, z = sys.stdin.readline().split()
            start.append(int(x))
            end.append(int(y))
            interval.append(int(z))
        if valid:
            for i in range(m + n - 1):                         # pega todas as atividades com ou sem repetição menos a ultima que já foi comparada com todos os outros
                if valid:                                      # verificação responsável por saber se o que sai do segundo for é ainda válido para evitar comparações desnecessárias
                    for p in range(n, n + m, 1):               # pega todos as atividades com repetição
                        if valid:                              # verificação responsável por saber se o que sai do while é ainda válido para evitar comparações desnecessárias
                            auxs = start[p]
                            auxe = end[p]
                            while start[p] < 1000000:
                                if (start[p] or end[p]) in range(start[i], end[i]):   # comparação para saber se o que o segundo for pega está no intervalo do que o primeiro for pega
                                    if (start[p] == start[i]) and (end[p] == end[i]) and (i == p):
                                        break
                                    elif (start[p] == end[i]) or (end[p] == start[i]):
                                        break
                                    else:
                                        valid = False
                                        break
                                elif (start[i] or end[i]) in range(start[p], end[p]): # comparação para saber se o que o primeiro for pega está no intervalo do que o segundo for pega
                                    if (start[p] == start[i]) and (end[p] == end[i]) and (i == p):
                                        break
                                    elif (start[p] == end[i]) or (end[p] == start[i]):
                                        break
                                    else:
                                        valid = False
                                        break
                                else:                                                  # caso não esteja dentro do intervalos das atividade anteriores é então somado o intervalo de repetição do que é pegado no segundo for
                                    buffer = start[p] + interval[p]                    # um buffer para somar o valor inicial com o intervalo
                                    del start[p]                                       # deleta o valor inicial da posição p
                                    start.insert(p, buffer)                            # insere o novo valor na posição p
                                    buffer = min((end[p] + interval[p]), 1000000)     # um buffer para somar o valor final com o intervalo e deixar o menor valor entre a soma e 1000000
                                    del end[p]                                        # deleta o valor final da posição p
                                    end.insert(p, buffer)                             # insere o novo valor na posição p
                            del start[p]                           # deleta o valor inicial alterado da posição p
                            start.insert(p, auxs)                  # insere o valor inicial original na posição p
                            del end[p]                             # deleta o valor final alterado da posição p
                            end.insert(p, auxe)                    # insere o valor final original na posição p

    if valid:                                                  # se valid ainda for true printa NO CONFLICT
        print("NO CONFLICT")
    else:                                                      # se for false printa CONFLICT
        print("CONFLICT")


def main():
    while True:
        try:
            n, m = sys.stdin.readline().split()            # faz a leitura da primeira linha e separa nas duas variaveis
            n = int(n)                                     # transforma as variaveis que estavam em string em inteiros
            m = int(m)
            if n != 0 or m != 0:                       # verifica a condição de parada das entrada que é n e m igual a 0
                confere(n, m)                       # chama a função responsável por verificar a ocorrencia de conflitos
            else:
                break
        except EOFError:
            break


if __name__ == '__main__':
    main()
