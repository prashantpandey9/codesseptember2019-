for n in range(int(input())):
    j=list(map(int,input().split()))
    n=j[0]
    p=j[1]
    cash=list(map(int,input().split()))
    u=[0]*n
    s=0
    for n in cash:
        if p%n==0:
            s+=1
    if s==len(cash):
        print("NO")
    else:
        a=max(cash)
        q=cash.index(a)
        d=p//a
        r=p%a
        if (d*a)<p and r>0:
            u[q]=d+1
            print("YES",' '.join(map(str,u)))
