##n=int(input())
##s=list(map(str,input()))
##t=list(map(str,input()))
##if n>=1 and n<=10**3 and len(s)==len(t):
##    count=0
##    match=0
##    l=n
##    for i in range(n-1):
##        print(s[i:n-1],t[0:n-1-i])
##        if s[i:n-1]==t[0:n-1-i]:
##            break
##
##    print(i)  
n = int(input())
s = input()
t = input()
for i in range(0,n):
    k = s[i:]
    print(k)
    if k in t:
        print(n-len(k))
        break
