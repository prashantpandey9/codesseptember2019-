s = input()
s_open = []
w=0
for i in s:
  if i=='(':
    s_open.append(i)
    print(s_open)
  else:
    if len(s_open) == 0:
      print(w)
      print(s_open)
    else:
      if s_open[-1] == '(' and i == ')':
        s_open.pop()
        w+=1
      else:
        print(w)
        break
    
##else:
##  if len(s_open) == 0:
##    print(w)
##  else:
##      print(w)
