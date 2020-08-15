def rotLeft(a, d):
    d=d%len(a)
    r=a[:len(a)-d]
    t=a[len(a)-d:len(a)]
    print(r,t)
    return r+t

nd = input().split()
n = int(nd[0])
d = int(nd[1])
a = list(map(int, input().rstrip().split()))
result = rotLeft(a, d)
print(result)
