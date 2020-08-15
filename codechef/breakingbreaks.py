for n in range(int(input())):
    d=list(map(int,input().split()))
    s=0
    e=0
    for n in range(1,4):
        s+=d[n]
    #print("s",s)
    while(s!=0):
        f=s%d[0]
        s=s//d[0]
        e+=s
    print(e)
