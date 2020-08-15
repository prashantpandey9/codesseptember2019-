from itertools import chain, combinations
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
a=int(input())
s=set(map(int,input().split()))
ss=0
for n in list(powerset(s)):
    if sum(n)%2==0 and len(n)!=0:
        ss+=1
print(ss)
