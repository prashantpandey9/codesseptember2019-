f=list(map(int,input().split()))
q=list(set(f))
print(q)
w=q[::-1]
for j in range(len(w)-1):
    while True:
        w.pop(w[j])
        w.pop(w[j-1])
