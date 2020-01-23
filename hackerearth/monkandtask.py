for n in range(int(input())):
    m=int(input())
    k=list(map(int,input().split()))
    dk=[]
    for n in k:
        dk.append([bin(n).count('1'),n])
    dk=sorted(dk)
    for d in dk:
        print(d[1],end=' ')
