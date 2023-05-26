lines = int(input())

set_final = set()


for i in range(lines):

  elements = input().split()

  for things in elements:
    set_final.add(things)


for things in set_final:
  print(things)
