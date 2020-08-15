c1=int(input())
st=""
while c1>0:
    if c1%2==0:
        st='0'+st
    else:
        st='1'+st
    c1=c1//2
print(st)
