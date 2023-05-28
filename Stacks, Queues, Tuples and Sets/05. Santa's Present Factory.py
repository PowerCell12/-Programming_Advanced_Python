materials = list(map(int, input().split()))
magic_level = list(map(int, input().split()))
from collections import deque
magic_level = deque(magic_level)
dict_toys = {}
bool1 = False

while materials and magic_level:
  
  material = materials.pop()
  magic = magic_level.popleft()

  if material == 0 and magic == 0:
    continue

  if material == 0 and magic != 0:
    magic_level.appendleft(magic)
    continue

  if magic == 0 and material != 0:
    materials.append(material)
    continue
  
  total = material * magic

  if total == 150:
    if "Doll" not in dict_toys:
      dict_toys["Doll"] = 0
    dict_toys["Doll"] += 1
  elif total == 250:
    if "Wooden train" not in dict_toys:
      dict_toys["Wooden train"] = 0
    dict_toys["Wooden train"] += 1
  elif total == 300:
    if "Teddy bear" not in dict_toys:
      dict_toys["Teddy bear"] = 0
    dict_toys["Teddy bear"] += 1
  elif total  == 400:
    if "Bicycle" not in dict_toys:
      dict_toys["Bicycle"] = 0
    dict_toys["Bicycle"] += 1
  else:

      if total < 0:
        the_sum = material + magic
        materials.append(the_sum)

      if total > 0:
        material += 15
        materials.append(material)

if "Doll" in dict_toys.keys() and "Wooden train" in dict_toys.keys():
  bool1 = True

if "Teddy bear" in dict_toys.keys() and "Bicycle" in dict_toys.keys():
  bool1 = True


if bool1:
  print("The presents are crafted! Merry Christmas!")
else:
  print("No presents this Christmas!")

## can be wrong
if materials:
  materials.reverse()
  print(f"Materials left: {', '.join(list(map(str, materials)))}")

if magic_level:
  print(f"Magic left: {', '.join(list(map(str, magic_level)))}")

## can be wrong
sorted_dict =   sorted(dict_toys.items())

for key in sorted_dict:
  print(f"{key[0]}: {key[1]}")
