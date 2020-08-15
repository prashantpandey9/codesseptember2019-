##'A' => 'T',
##'T' => 'A',
##'C' => 'G',
##'G' => 'C
for n in range(int(input())):
    i=['A','T','C','G']
    p=['T','A','G','C']
    f=int(input())
    r=input()
    s=''
    for j in r:
        if j in i:
            s+=p[i.index(j)]
    if len(s)==len(r):
        print(s)
    else:
        print('Error RNA nucleobases found!')
