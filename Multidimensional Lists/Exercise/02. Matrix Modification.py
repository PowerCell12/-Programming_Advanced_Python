rows = int(input())

matrix  = [[things for things in map(int, input().split())] for i in range(rows)]

while True:

  commands = input().split()

  if commands[0] == "END":
    break

  if commands[0] == "Add":

    if int(commands[1]) < 0 or int(commands[1]) > rows - 1:
      print("Invalid coordinates")
      continue

    if int(commands[2]) < 0 or int(commands[2]) > len(matrix[int(commands[1])])  - 1:
      print("Invalid coordinates")
      continue


    matrix[int(commands[1])][int(commands[2])] += int(commands[3])

  if commands[0] == "Subtract":

    if int(commands[1]) < 0 or int(commands[1]) > rows - 1:
      print("Invalid coordinates")
      continue
    
    if int(commands[2]) < 0 or int(commands[2]) > len(matrix[int(commands[1])])  - 1:
      print("Invalid coordinates")
      continue
    
    matrix[int(commands[1])][int(commands[2])] -= int(commands[3])

for things in matrix:

    print(f"{' '.join(list(map(str, things)))}")
