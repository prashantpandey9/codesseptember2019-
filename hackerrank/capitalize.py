def solve(s):
    f=s.split()
    d=''
    for j in range(len(f)):
        d+=f[j].capitalize()
        d+=' '
    print(d)
solve(input())
