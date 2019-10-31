def main(args):
    teste = input()
    while teste.split() [0]!= '0' and teste.split()[1] != '0':
        teste = teste.split()
        quantidade = int(teste[0]) + int(teste[1])
        cds = []
        i = 0
        while i < quantidade:
            linha = input()
            cds.append(linha)
            i += 1

        print(quantidade - len(set(cds)))
        teste = input()



    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))