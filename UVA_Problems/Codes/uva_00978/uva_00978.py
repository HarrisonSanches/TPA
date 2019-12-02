"""
Exercicio resolvido: uva_00978 - Lemming batle! 
Autores: Leonardo Laia Arpini, Harrison Sanches, Mathues Garcias
"""

from sys import stdin
from bisect import insort

inputn = stdin.readline
testcases = int(inputn())
for h in range(testcases):
    tmp = (int(x) for x in inputn().split())
    B, SG, SB = tmp
    GreenSet = []
    BlueSet = []

    for i in range(SG):
        GreenSet.append(int(inputn()))
    for i in range(SB):
        BlueSet.append(int(inputn()))

    while(not (not len(GreenSet) or not len(BlueSet))):
        fights = min(B, min(len(GreenSet), len(BlueSet)))
        greenRemain = []
        blueRemain = []
        for i in range(fights):
            
            mg = max(GreenSet)
            mb = max(BlueSet)

            GreenSet.remove(mg)
            BlueSet.remove(mb)

            if mg > mb:
                greenRemain.append(mg-mb)
            elif mb > mg:
                blueRemain.append(mb-mg)

        for lemming in greenRemain:
            GreenSet.append(lemming)
        for lemming in blueRemain:
            BlueSet.append(lemming)

    if not len(GreenSet) and len(BlueSet):
        print("blue wins")
        BlueSet.sort(reverse=True)
        for lemming in BlueSet:
            print(lemming)
    elif len(GreenSet) and not len(BlueSet):
        print("green wins")
        GreenSet.sort(reverse=True)
        for lemming in GreenSet:
            print(lemming)
    else:
        print("green and blue dies")
    if h != testcases-1:
        print()
