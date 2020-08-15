"""
a=int(input())
r=input()
f=r.count('.')
s=''
if f!=0:
    for j in r:
        if j=='.':
            s+='B'
        else:
            s+=j
    print("YES")
    print(s)
else:
    print("NO")
"""
N=int(input())
st=input()[:N]
if 'HH' in st:
    print('NO')
elif '.' in st or len(st)==1:
    print('YES')
    print(st.replace('.','B'))
else:
    print('NO')
