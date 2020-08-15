for j in range(int(input())):
    n,r=map(int,input().split())
    s=list(map(int,input().split()))
    
    flag=0
    su=0
    for i in range(len(s)):
        if flag!=s[i] and flag<s[i]:
            flag=s[i]
            su+=1
    print(su*r)
