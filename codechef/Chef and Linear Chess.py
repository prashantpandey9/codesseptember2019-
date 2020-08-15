# cook your dish here
for h in range(int(input())):
    n,k=map(int,input().split())
    pi=list(map(int,input().split()))
    
    ma=float("inf")
    for j in pi:

        if k%j==0:
            if ma>k//j:
                ma=j
    if ma==float("inf"):
        ma=-1
    print(ma)
        

##import sys
##for j in range(int(sys.stdin.readline())):
##    h,p=map(int,sys.stdin.readline().split())
##    chef=0
##    while True:
##        h-=p
##        p=p//2
##        if h<=0:
##            print(1)
##            break
##        elif p<=0:
##            print(0)
##            break
##        else:
##            pass
##
