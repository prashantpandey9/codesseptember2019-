f=[6,2,5,5,4,5,6,3,7,6]
for d in range(int(input())):
    s=int(input())
    p=list(map(int,input().split()))
    l=[8]*10
    for j in p:
        l[j]=f[j]
    print(l.index(min(l)))
        
        
