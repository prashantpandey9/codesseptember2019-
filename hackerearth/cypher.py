def cipher(s, k):
    res = ""
    for i in s:
        if i.isupper():
            res += chr(65+(ord(i)+k-65) % 26)
        elif i.islower():
            res += chr(97+(ord(i)+k-97) % 26)
        elif i.isnumeric():
            res += str((int(i) + k) % 10)
        else:
            res += i
    return res
s=input()
k=int(input())
print(cipher(s,k))
