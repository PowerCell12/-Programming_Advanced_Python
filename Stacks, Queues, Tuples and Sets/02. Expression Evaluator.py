## training
from collections import deque

int_op = input().split()
list_final  = []
deque1 = deque(int_op)


for i in range(len(deque1)):
  ## There might be negative numbers in the string
  
  final = deque1.popleft()

  if final.isdigit() or final.lstrip('-').isdigit():
    list_final.append(int(final))

  elif final == "+": 
    final1 = sum(list_final)
    list_final.clear()
    list_final.append(final1)

  elif final == "*":
    final1 = 0
    
    for i in range(1, len(list_final)):
      if i == 1:
        final1 = list_final[0] * list_final[1]
      else: 
        final1 *= list_final[i]


    list_final.clear()
    list_final.append(final1)

  elif final == "-":
    final1 = 0
    
    for i in range(1, len(list_final)):
      if i == 1:
        final1 = list_final[0] - list_final[1]
      else:
        final1 -= list_final[i]

    list_final.clear()
    list_final.append(final1)

  elif final == "/":
    ## There will be no case of division by zero

    final1 = 0

    for i in range(1, len(list_final)):
      if i == 1:
        final1 = list_final[0] / list_final[1]
      else:
        final1 = final1 / list_final[i]

    list_final.clear()
    list_final.append(int(final1))

print(list_final[0])
