"""
def tr(a):
    z=0
    while a:
        a=a/5
        k=int(a)
        z+=k
    return(z)
#ae=int(input())
#print(tr(ae))
t=int(input())
for j in range(t):
    z1=int(input())
    w=5**(z1-1)
    i=z1*5
    for j in range(w,i):
        print(j)

"""
"""
import math
j=int(input())
for d in range(1,j+1):
    print(d,"= ",math.factorial(d))

"""
for i in range(int(input())):
    n = int(input())
    count = 0
    k = 0
    while count < n:
        k += 1
        count +=1
        c = k
        while c > 0:
            if c%5 == 0:
                count += 1
                c=c/5
            else: break
        print(k,count,c)
    if count == n:
        print(5)
        print(" ".join([str(5*k + j) for j in range(5)]))
    else:
        print(0)
 
