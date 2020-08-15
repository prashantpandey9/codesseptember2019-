test=int(input())
for i in range(test):
    lines=int(input())
    lines-=1
    counter=1
    while(lines!=-1):
        print(counter*"*",2*lines*"#",counter*"*",sep="")
        lines-=1
        counter+=1
    print("\n")
