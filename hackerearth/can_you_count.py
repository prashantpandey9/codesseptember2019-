def canYouCount (s):
    # write your code here
    r=0
    q=0
    l=['a','e','i','o','u']
    t=[]
    for j in s:
        if j=="_":
            r+=1
        if j in l:
            t.append(j)
    q=set(t)
    print(t)
    print(q)
    f=1
    if r>0:
        for j in range(1,len(q)+1):
            f*=j
        return f
    else:
        return f
T = int(input())
for _ in range(T):
    s = input()
    out_ = canYouCount(s)
    print (out_)
