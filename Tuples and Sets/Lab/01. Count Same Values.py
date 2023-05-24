numbers = input().split(" ")

tuple = tuple(numbers)
list1 = []

for i in range(len(tuple)):
  current = tuple[i]


  if current not in list1  :
      print(f"{float(current):.1f} - {tuple.count(current)} times")

  list1.append(current)
