peek = lambda x: x[len(x)-1]
pop = lambda x: x.pop(len(x)-1)
push = lambda x, y: x.append(y)
N = int(input())
while(N):
    B = [int(x) for x in input().split()]
    while(B[0]):
        S = []
        B.reverse()
        i = 1
        while(i <= N):
            push(S, i)
            i += 1
            while(len(S) and peek(S) == peek(B)):
                pop(S)
                pop(B)
                if(not len(B)):
                    break
        print("Yes") if not len(S) else print("No")
        B = [int(x) for x in input().split()]
    print()
    N = int(input())