line = int(input())

commands = input().split(", ")


field = [[things for things in list(input())] for i in range(line)]

rows = 0
columns = 0
hazelnut = 0
bool1 = True
all_havelnut =0

for i in range(len(field)):
  row = field[i]

  if "s" in row:
    rows  = i
    columns = row.index('s')
    break


## doesn't work yet
flattened = [things for things1 in field for things in things1]
flattened  = " ".join(flattened)
import re
regex = r'h'
findall = re.findall(regex, flattened)
all_havelnut = len(findall)


for i in range(len(commands)):

  final = commands[i]
  
  if final == "left":

      if columns - 1  < 0:
        print("The squirrel is out of the field.")
        print(f"Hazelnuts collected: {hazelnut}")
        bool1 = False
        field[rows][columns] = "*"
        break
      else:
        field[rows][columns] = "*"
        columns -= 1
        
  
  if final == "right":

      if columns + 1  >= len(field[rows]):
        print("The squirrel is out of the field.")
        print(f"Hazelnuts collected: {hazelnut}")
        bool1 = False
        field[rows][columns] = "*"
        break
      else:
        field[rows][columns] = "*"
        columns += 1
        
  if final == "up":

    if rows - 1 < 0:
        print("The squirrel is out of the field.")
        print(f"Hazelnuts collected: {hazelnut}")
        bool1 = False
        field[rows][columns] = "*"
        break
    else:
      field[rows][columns] = "*"
      rows -= 1

  
  if final == "down":
      
    if rows + 1  >= len(field):
        print("The squirrel is out of the field.")
        print(f"Hazelnuts collected: {hazelnut}")
        bool1 = False
        field[rows][columns] = "*"
        break
    else:
      field[rows][columns] = "*"
      rows += 1


  if field[rows][columns] == "h":
    hazelnut += 1
    field[rows][columns] = "*"

  elif field[rows][columns] == "t":
    print("Unfortunately, the squirrel stepped on a trap...")
    print(f"Hazelnuts collected: {hazelnut}")
    bool1 = False
    break

if bool1:

  if hazelnut == all_havelnut:
    print("Good job! You have collected all hazelnuts!")
  else:
    print("There are more hazelnuts to collect.")

  print(f"Hazelnuts collected: {hazelnut}")
