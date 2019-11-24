"""
from itertools import permutations 
  
def allPermutations(str):
    f=[]
    permList = permutations(str)
    for perm in list(permList):
        f.append(''.join(perm))
    print(f)
for j in range(int(input())):
    f=int(input())
    j=input()
    allPermutations(j)
"""
"""
def rotate(j):
    k=j
    l=[]
    l.append(int(j,2))
    while True:
        if (j[1:]+j[0:1])!=k:
            l.append(int(j[1:]+j[0:1],2))
            j=j[1:]+j[0:1]
        else:
            break
    o=0
    for d in l:
        if d%2==0:
            o+=1
    print(o)
for s in range(int(input())):
    r=int(input())
    bb=input()
    rotate(bb)
"""
"""
def rotate(j):
    k=j
    l=[]
    l.append(j)
    while True:
        if (j[1:]+j[0:1])!=k:
            l.append(j[1:]+j[0:1])
            j=j[1:]+j[0:1]
        else:
            break
    o=0
    kk=[]
    for d in l:
        
        decimal = 0
        for digit in d:
            decimal = decimal*2 + int(digit)
        kk.append(decimal)
    for s in kk:
        if s%2==0:
            o+=1
    print(o)
for s in range(int(input())):
    r=int(input())
    bb=input()
    rotate(bb)
"""
for j in range(int(input())):
    f=int(input())
    o=input()
    s=0
    for m in o:
        if m=="0":
            s+=1
    print(s)
