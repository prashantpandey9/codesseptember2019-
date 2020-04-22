a=list(input())
b=list(input())
if 'z' in a:
    print('NO')
else:
    l=ord(a[0])
    r=ord(b[0])
    if (r-l)>0:
        print("YES")
    else:
        print("NO")
