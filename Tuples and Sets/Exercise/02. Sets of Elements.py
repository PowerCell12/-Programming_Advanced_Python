line1, line2 = list(map(int, input().split(" ")))

set_1 = set()
set_2 = set()

for i in range(line1):
  things_1 = input()

  set_1.add(things_1)

for j in range(line2):
  things_2 = input()

  set_2.add(things_2)


final = set_1 & set_2


for things in final:
  print(things)
