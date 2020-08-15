for n in range(int(input())):
    f=int(input())
    d=input()
    s=[0]*26
    
    for j in d:
        g=(ord(j)-97)%26
        s[g]+=1
    print(s)
    for h in range(26):
        if s[h]>1:
            s[h]=s[h]//2
        else:
            s[h]=0
    print(sum(s))
