def jarvis():
    seq = [int(i) for i in input()]
    seq = sorted(seq)
    ran=[]
    for i in range(seq[0],seq[-1]+1,1):
        ran.append(i)

    if seq == ran:
        print("YES")
    else:
        print("NO")
def main():
    for i in range(int(input())):
        jarvis()
main()
