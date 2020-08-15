for n in range(int(input())):
    o=[0]*11  
    for j in range(int(input())):
        p,s=list(map(int,input().split()))
        if p<=8 and o[p-1]<s:
            o[p-1]=s
    print(sum(o))
