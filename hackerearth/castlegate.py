"""
import itertools
for n in range(int(input())):
    q=int(input())
    k=list(range(1,q+1))
    i=0
    for result in itertools.combinations(k, 2):
        if result[0]^result[1]<=q:
            i+=1
    print(i)
"""
for n in range(int(input())):
    f=int(input())
    i=0
    for h in range(1,f+1):
        for g in range(h+1,f+1):
            if h^g<=f:
                i+=1
    print(i)
                
               
