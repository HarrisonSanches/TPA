import math
def main(args):
    while True:
        try:
            line = input()
            lista = []
            while line:
                lista.append(int(line))
                lista.sort()
                if len(lista) == 1:
                    print(lista[0])
                elif len(lista)%2 != 0:
                    mid = int(len(lista)/2)
                    print(lista[mid])
                else:
                    a = lista[int(len(lista) / 2)-1]
                    b = lista[int(len(lista) / 2)]
                    c = ((int(a+b)/2))
                    print(math.floor(c))

                line = input()


        except EOFError:
            return



    return 0

if __name__ == '__main__':

    import sys
    sys.exit(main(sys.argv))