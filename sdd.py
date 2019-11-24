"""
e=int(input())
d=""
while True:
    try:
        a=int(input())
        d=d+str(a)+" "
    except ValueError:
        break
print(d)
"""
i=int(input())
if i%5==0:
    print(i/5)
else:
    print(i//5+1)
