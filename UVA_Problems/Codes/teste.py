
teste = input()
while teste != '0 0':
    teste = teste.split()
    n, m = int(teste[0]), int(teste[1])
    jack = []
    for i in range(n):
        linha = input()
        jack.append(linha)
    count = 0
    for j in range(m):
        linha = input()
        if linha in jack:
            count+=1
    teste = input()
    print(count)
