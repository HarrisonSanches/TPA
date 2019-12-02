"""
Exercicio resolvido: uva11340 - Newsapers
Autores: Leonardo Laia Arpini, Harrison Sanches, Matheus Garcias

"""
def main(args):
    try:
        tests = int(input())
        for i in range(tests):
            caracteres = int(input())
            i = 0
            dic_caracteres = {}
            while i < caracteres:
                linha = input()
                dic_caracteres[linha.split()[0]] = int(linha.split()[1])
                i += 1

            quantidade_linhas = int(input())
            valor_final = 0
            for i in range(quantidade_linhas):
                linha_texto = input()
                for item in linha_texto:
                    if item in dic_caracteres:
                        valor_final += dic_caracteres[item]

            valor_final = valor_final/100
            print("%.2f$" %valor_final)



    except EOFError:
        return

    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
