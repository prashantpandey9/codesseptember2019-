def minimumBribes(Q):
    moves = 0 
    Q = [P-1 for P in Q]
    print(Q)
    for i,P in enumerate(Q):

        if P - i > 2:
            print("Too chaotic")
            return
        for j in range(max(P-1,0),i):
            print(j,P-1,Q[j])
            if Q[j] > P:
                moves += 1
    print(moves)


for j in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    minimumBribes(arr)


##minimumBribes(arr)
