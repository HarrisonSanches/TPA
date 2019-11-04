import sys
def main(args):
    teste = sys.stdin.readline().split()

    while teste[0] != '0' and teste[1] != '0':
        quantidade = int(teste[0]) + int(teste[1])

        cds = set()
        i = 0
        while i < quantidade:
            cds.add(sys.stdin.readline())
            i += 1

        print(quantidade - len(set(cds)))
        teste = sys.stdin.readline().split()



    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))