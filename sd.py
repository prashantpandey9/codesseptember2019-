t=int(input())
while t>0:
    t-=1
    d=int(input())
    j=input()
    s=j.count("1")
    print(s)
    for n in range(d-1):
        m=input()
        print(m)
        for n in range(10):
            if (m[n]=="1" and j[n]=='1'):
                s-=1
            elif(m[n]=='1'):
                s+=1
    print(s)
