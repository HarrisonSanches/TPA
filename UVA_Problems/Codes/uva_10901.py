"""
Exercicio resolvido: uva10038 – Ferry Loading III
Autores: Leonardo Laia Arpini, Harrison Sanches, Matheus Garcias

"""
import sys
inputn = sys.stdin.readline
C = int(inputn())
for i in range(C):
    n, t, m = (int(x) for x in inputn().split())
    left = []
    right = []
    for j in range(m):
        line = inputn().split()
        if line[1] == 'left':
            left.append((int(line[0]), j))
        else:
            right.append((int(line[0]), j))
    nowtime = 0
    flag = False
    results = [0]*10000
    while True:
        if not len(left) and not len(right):
            break
        tn = 0
        if not flag:
            while tn < n and len(left) and left[0][0] <= nowtime:
                tn += 1
                results[left[0][1]] = nowtime+t
                left.pop(0)
            if tn:
                nowtime += t
                flag = not flag
                continue
            if not len(right) or (len(left) and left[0][0] <= right[0][0]):
                nowtime = left[0][0]
                while tn < n and len(left) and left[0][0] <= nowtime:
                    tn += 1
                    results[left[0][1]] = nowtime+t
                    left.pop(0)
                nowtime += t
            else:
                if len(right) or not len(left) and left[0][0] > right[0][0]:
                    nowtime = max(right[0][0], nowtime)+t
                else:
                    nowtime += t
        else:
            while tn < n and len(right) and right[0][0] <= nowtime:
                tn += 1
                results[right[0][1]] = nowtime+t
                right.pop(0)
            if tn:
                nowtime += t
                flag = not flag
                continue
            if not len(left) or (len(right) and left[0][0] >= right[0][0]):
                nowtime = right[0][0]
                while tn < n and len(right) and right[0][0] <= nowtime:
                    tn += 1
                    results[right[0][1]] = nowtime+t
                    right.pop(0)
                nowtime += t
            else:
                if len(left) or not len(right) and left[0][0] < right[0][0]:
                    nowtime = max(left[0][0], nowtime)+t
                else:
                    nowtime += t
        flag = not flag
    for k in range(m):
        print(results[k])
    if i < C-1:
        print()
