import math 

def primeFactors(n):
    q=0
    while n % 2 == 0: 
##        print(2)
        q+=1
        n = n / 2 
    for i in range(3,int(math.sqrt(n))+1,2): 
           
        while n % i== 0: 
##            print(i)
            q+=1
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
##        print(n)
        q+=1
    print(q)
    
primeFactors(int(input()))
