##for j in range(int(input())):
##    
##    c,cure=map(int,input().split())
##    country=list(map(int,input().split()))
##    s=0
##    country=sorted(country)
##    for j in country:
##        while True:
##            if cure>=j:
##                s+=1
##                break
##            else:
##                cure*=2
##            print("cure",cure)
##    print(s)

for n in range(int(input())):
    sss=list(map(int,input().split()))
    r=sss[1]
    l=list(map(int,input().split()))
    i=sss[0]    
    r=r%i
##    print("r",r)
    s=l[r:i]+l[0:r]
    for n in s:
        print(n,end=" ")
    print()
