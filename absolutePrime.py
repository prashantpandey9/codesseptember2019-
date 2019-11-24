def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True
for i in range(int(input())):
    r=int(input())
    for n in range(r,1,-1):
        
        if isPrime(n):
            n=str(n)
            n=list(n)
            d=0
            for ni in n:
                ni=int(ni)
                d+=ni
            if isPrime(d):
                o=''
                for m in n:
                    o+=m
                print(o)
                break
            
            
