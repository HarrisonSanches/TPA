"""
Exercicio resolvido: uva_00939 - Jolly Jumpers
Autores: Leonardo Laia Arpini, Harrison Sanches, Mathues Garcias
"""
def main(args):
    while True:
        try:
            line = input()
            while line:
                lista = line.split()
                if int(lista[0]) == 0:
                    print("Not Jolly")
                elif int(lista[0]) == 1:
                    print("Jolly")
                elif int(lista[0]) == 2:
                    print("Jolly")
                else:
                    lst = []
                    anterior = abs(int(lista[2]) - int(lista[1]))
                    lst.append((anterior))
                    j = 3
                    while j < len(lista):
                        atual = abs(int(lista[j]) - int(lista[j - 1]))
                        lst.append(atual)
                        j +=1
                    lst.sort()
                    k = 0
                    while k < len(lst):
                        if lst[k] != k + 1:
                            print("Not jolly")
                            break
                        k += 1
                    if k == len(lst):
                        print("Jolly")

                line = input()
        except EOFError:
            return



    return 0

if __name__ == '__main__':

    import sys
    sys.exit(main(sys.argv))
