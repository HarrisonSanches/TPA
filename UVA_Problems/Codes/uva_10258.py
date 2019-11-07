import sys
from functools import cmp_to_key
class Jogador:

    def __init__(self, a, b, tempo):
        self.jogador = a
        self.qcertas = b
        self.tempo = tempo

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

    for _ in range(quantidade):
        sys.stdin.readline()
        linha = sys.stdin.readline().rstrip()
        lista = []
        while linha != "":
            linha = [x.rstrip() for x in linha.split(" ")]
            if linha[-1] == "I":
                is_in, index = jogador_in(lista, int(linha[0]))
                if is_in:
                    lista[index].tempo += 20
                else:
                    jogador = Jogador(int(linha[0]), 0, 20)
                    lista.append(jogador)

            elif linha[-1] == "C":
                is_in, index = jogador_in(lista, int(linha[0]))
                if is_in:
                    lista[index].tempo += int(linha[2])
                    lista[index].qcertas += 1
                else:
                    jogador = Jogador(int(linha[0]), 1, int(linha[2]))
                    lista.append(jogador)

            else:
                is_in, index = jogador_in(lista, int(linha[0]))
                if not is_in:
                    jogador = Jogador(int(linha[0]), 0, 0)
                    lista.append(jogador)

            linha = sys.stdin.readline().rstrip()


        a = sorted(lista, key=compara2)

        for item in a:
            (print(item))
        print()


    return 0

if __name__ == '__main__':

    import sys
    sys.exit(main(sys.argv))