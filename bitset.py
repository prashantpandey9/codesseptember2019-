for j in range(int(input())):
    k=[0]*32
    for n in range(int(input())):
        d=int(input())
        v=bin(d)[2:]
        s=v[::-1]
        
        for j in range(len(s)):
            if s[j]=='1':
                k[j]+=1
    print(k.index(max(k)))

