"""
Exercicio resolvido: uva11988 - BrokenKeyboard
Autores: Leonardo Laia Arpini, Harrison Sanches, Mathues Garcias

"""


from collections import deque
import functools
@functools.lru_cache(maxsize = 1000000)

def rearruma(line):
    pos = 0
    buffer = []
    output = deque()
    for c in line:
        if c == '[':
            pos = 0 # a posição a ser inserida é o zero
        elif c == ']':
            pos = len(output) + 1 # a posição a ser inserida é o final da lista
        else:
            output.insert(pos,c)
            pos += 1

    return("".join(output))


def main():
    while True:
        try:
            line = input()
            print(rearruma(line))
        except EOFError:
            break



if __name__ == '__main__':
    main()