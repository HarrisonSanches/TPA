"""
Exercicio resolvido: uva11988 - BrokenKeyboard
Autores: Leonardo Laia Arpini, Harrison Sanches, Mathues Garcias

"""

genestype = ["non-existent", "recessive", "dominant"]
people = []


class Person:

    def __init__(self, name):
        self.name = name
        self.gene = "Anything"
        self.parents = []

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    def __gt__(self, other):
        return self.name > other.name


def comparagene(p):
    domgene = 0
    recegene = 0
    for i in range(len(p.parents)):
        for j in range(len(people)):
            if p.parents[i] == people[j].name:
                if people[j].gene == "Anything":
                    arrumagene(people[j])
                    if people[j].gene == genestype[2]:
                        domgene += 1
                    elif people[j].gene == genestype[1]:
                        recegene += 1
                elif people[j].gene == genestype[2]:
                    domgene += 1
                elif people[j].gene == genestype[1]:
                    recegene += 1
    return domgene, recegene


def arrumagene(p):
    domgene, recegene = comparagene(p)
    if domgene == 2 or (domgene == 1 and recegene == 1):
        p.gene = genestype[2]
    elif recegene == 2 or (domgene == 1 and recegene == 0):
        p.gene = genestype[1]
    else:
        p.gene = genestype[0]


def main():
    while True:
        try:
            line = int(input())
            if 1 <= line <= 3100:
                for i in range(line):
                    count = 0
                    n, m = input().split()
                    if m not in genestype:
                        for p in people:
                            if m == p.name:
                                p.parents.append(n)
                                break
                            else:
                                count += 1
                        if count == len(people):
                            p = Person(m)
                            p.parents.append(n)
                            people.append(p)
                    else:
                        p = Person(n)
                        p.gene = m
                        p.parents.append("None")
                        people.append(p)
                for p in people:
                    if p.gene == "Anything":
                        arrumagene(p)
                sorted_people = sorted(people)
                for x in sorted_people:
                    print(x.name, x.gene)
            else:
                break
        except EOFError:
            break


if __name__ == '__main__':
    main()
