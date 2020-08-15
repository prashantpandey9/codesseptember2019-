t = int(input())
for i in range(t):
    inp = input()
    
    list1 = list(inp)
    letters = list(set(list1))
    letters.sort()
##    print(letters)
    counts = []
    for l in letters :
        counts.append(list1.count(l))
##    print(counts)
    j = len(counts) 
    for _ in range(j) :
        print(letters[counts.index(min(counts))] * min(counts),end = '')
        del letters[counts.index(min(counts))]
        counts.remove(min(counts))
    print()
