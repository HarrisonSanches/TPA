"""
Exercicio resolvido: uva10038 – Contested ScoreBOard
Autores: Leonardo Laia Arpini, Harrison Sanches, Matheus Garcias

"""
import sys
from functools import cmp_to_key
class Jogador:

    def __init__(self, a, b, tempo, questoes_certas, questoes_incorretas):
        self.jogador = a
        self.qcertas = b
        self.tempo = tempo
        self.questoes_certas = questoes_certas
        self.questoes_incorretas = questoes_incorretas

    def __str__(self):
        return "{} {} {}".format(self.jogador, self.qcertas, self.tempo)

def jogador_in(lst, jogador):
    for i in range (len(lst)):
        if lst[i].jogador == jogador:
            return True, i
    return False, -1

def ordena_zerados(lst):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if (lst[i].jogador > lst[j].jogador):
                tmp = lst[i]
                lst[i] = lst[j]
                lst[j] = tmp

def order(lst):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if(lst[i].qcertas < lst[j].qcertas):
                tmp = lst[i]
                lst[i] = lst[j]
                lst[j] = tmp
            elif(lst[i].qcertas == lst[j].qcertas):
                if(lst[i].tempo > lst[j].tempo):
                    tmp = lst[i]
                    lst[i] = lst[j]
                    lst[j] = tmp

# def compara(jogador1, jogador2):
#     if jogador1.qcertas > jogador2.qcertas :
#         return True
#     elif (jogador1.qcertas == jogador2.qcertas) and (jogador1.tempo < jogador2.tempo):
#         return True
#     elif  (jogador1.qcertas == jogador2.qcertas) and (jogador1.tempo == jogador2.tempo) and (jogador1.jogador < jogador2.jogador):
#       return True
#
#     else:
#         return False

def compara2(jogador1):
    criterio1 = -jogador1.qcertas
    criterio2 = jogador1.tempo
    criterio3 = jogador1.jogador
    return criterio1, criterio2, criterio3

def main (args):
    quantidade = int(sys.stdin.readline())
    sys.stdin.readline()
    for i in range(quantidade):
        linha = sys.stdin.readline().rstrip()
        lista = []
        jogadores_zerados = []
        while linha != "":
            linha = [x.rstrip() for x in linha.split(" ")]
            if linha[-1] == "I":
                is_in, index = jogador_in(lista, int(linha[0]))
                #not (linha[1] in lista[index].questoes_certas)
                if is_in:
                    #if lista[index].qcertas == 0:
                    if int(linha[1]) not in lista[index].questoes_certas:
                        #lista[index].tempo += 20
                        lista[index].questoes_incorretas.append(int(linha[1]))
                else:
                    lista_certas = []
                    lista_erradas = [int(linha[1])]
                    jogador = Jogador(int(linha[0]), 0, 0, lista_certas, lista_erradas)
                    lista.append(jogador)

            elif linha[-1] == "C":
                is_in, index = jogador_in(lista, int(linha[0]))
                if is_in:
                    if int(linha[1]) not in lista[index].questoes_certas:
                        lista[index].tempo += int(linha[2])
                        lista[index].qcertas += 1
                        lista[index].questoes_certas.append(int(linha[1]))
                if not is_in:
                    lista_certas = []
                    lista_erradas = []
                    lista_certas.append(int(linha[1]))
                    jogador = Jogador(int(linha[0]), 1, int(linha[2]), lista_certas, lista_erradas)
                    lista.append(jogador)

            elif linha[-1] == "R" or linha[-1] == "U" or linha[-1] == "E":
                is_in, index = jogador_in(lista, int(linha[0]))
                if not is_in:
                    lista_certas = []
                    jogador = Jogador(int(linha[0]), 0, 0,lista_certas, [])
                    lista.append(jogador)
            linha = sys.stdin.readline().rstrip()
        for item in lista:
            for quest in item.questoes_incorretas:
                if quest in item.questoes_certas:
                    item.tempo += 20

        lista_naozerada = []
        lista_zerada = []
        for item in lista:
            if item.qcertas != 0 or item.tempo != 0:
                lista_naozerada.append(item)
            else:
                lista_zerada.append((item))
        a = []
        b = []
        a = sorted(lista_naozerada,key=compara2)
        b = sorted(lista_zerada, key=compara2)

        for item in a:
            print(item)
        for item in b:
            print(item)

        if i != quantidade-1:
            print()


    return 0

if __name__ == '__main__':

    import sys
    sys.exit(main(sys.argv))

