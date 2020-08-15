for b in range(int(input())):
    k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    q=int(input())
    odd=0
    even=0
    for n in a:
        s=bin(n^q)[2:]
        d=s.count('1')
        if d%2==0:
            even+=1
        else:
            odd+=1
    print(even,odd)
