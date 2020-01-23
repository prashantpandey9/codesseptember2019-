def add(A,B):
    t=0
    while B>0:
        U = A^B
        V = A&B
        A = U
        B = V*2
        t+=1
    return t
    bin(A)[:2]
    bin(B)[:2]
for n in  range(int(input())):
    A=input()
    B=input()
    A=int(A,2)
    B=int(B,2)
    print(add(A,B))
    
