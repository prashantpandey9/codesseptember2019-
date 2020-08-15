s=input()
a=s[0]
d=a
for j in range(1,len(s)):
    if a==s[j]:
        d+=s[j]
        break
    else:
        d+=s[j]
        a=s[j-1]
print(len(d))
