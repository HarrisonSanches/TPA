"""
Exercicio resolvido: uva11988 - BrokenKeyboard
Autores: Leonardo Laia Arpini, Harrison Sanches, Mathues Garcias

"""

from sys import stdin, stdout


def matching(dict_F, output, len_frags):
    matches = 0
    for i in range(1, len(output)):
        esq = output[:i]
        dir = output[i:]
        if esq not in dict_F and dir not in dict_F:
            continue
        if esq in dict_F and dir in dictF:
            if dict_F[esq] != dict_F[dir]:
                return False
            matches += (2 * dict_F[esq] if esq != dir else dict_F[esq])
    if matches == len_frags:
        return True
    else:
        return False


def achasolucao(dictF, frags):
    arqSize = (2 * tam) // len(frags)
    i = 0
    conf = set()
    for j in range(1, len(frags)):
        if len(frags[i]) + len(frags[j]) == arqSize:
            if frags[j] not in conf:
                output = frags[i] + frags[j]
                if matching(dictF, output, len(frags)):
                    stdout.write(output + "\n")
                    break
                output = frags[j] + frags[i]
                if matching(dictF, output, len(frags)):
                    stdout.write(output + "\n")
                    break
                conf.add(frags[j])


line = int(input())
for l in range(line):

    if l == 0:
        stdin.readline()

    frags = []
    dictF = {}
    cases = input().strip()
    tam = 0

    while cases != "":
        frags.append(cases)
        tam += len(cases)

        if cases in dictF:
            dictF[cases] += 1
        else:
            dictF[cases] = 1

        cases = stdin.readline().strip()

    if len(frags) == 2:
        stdout.write("".join(frags[0] + frags[1]) + "\n")

    else:
        achasolucao(dictF, frags)

    if l < line - 1:
        stdout.write("\n")
