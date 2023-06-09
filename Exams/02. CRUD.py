matrix = [[things for things in input().split()] for i in range(6)]

position = input()

## pos1 = row, pos2  = column
pos1 = int(position[1])
pos2 = int(position[4])


while True:
  commands = input().split(", ")

  if commands[0] == "Stop":
    break

  if commands[0] == "Create":
    if commands[1] == "up":
        if matrix[pos1 - 1][pos2] == ".":
          matrix[pos1 - 1][pos2] = commands[2]
          
        pos1 -= 1

    if commands[1] == "down":
      if matrix[pos1 + 1][pos2] == ".":
        matrix[pos1 + 1][pos2] = commands[2]
        
      pos1 += 1

    if commands[1] == "left":
      if matrix[pos1][pos2 - 1] == ".":
         matrix[pos1][pos2 - 1] = commands[2]

      pos2 -= 1

    if commands[1] == "right":
      if matrix[pos1 ][pos2 + 1] == ".":
        matrix[pos1][pos2 + 1] = commands[2]

      pos2 += 1


  if commands[0] == "Update":
    if commands[1] == "up":
        if matrix[pos1 - 1][pos2] != ".":
          matrix[pos1 - 1][pos2] = commands[2]
          
        pos1 -= 1

    if commands[1] == "down":
      if matrix[pos1 + 1][pos2] != ".":
        matrix[pos1 + 1][pos2] = commands[2]
        
      pos1 += 1

    if commands[1] == "left":
      if matrix[pos1][pos2 - 1] != ".":
         matrix[pos1][pos2 - 1] = commands[2]

      pos2 -= 1

    if commands[1] == "right":
      if matrix[pos1 ][pos2 + 1] != ".":
        matrix[pos1][pos2 + 1] = commands[2]

      pos2 += 1


  if commands[0] == "Delete":
    if commands[1] == "up":
          if matrix[pos1 - 1][pos2] != ".":
            matrix[pos1 - 1][pos2] = "."
          
          pos1 -= 1

    if commands[1] == "down":
      if matrix[pos1 + 1][pos2] != ".":
        matrix[pos1 + 1][pos2] = "."
        
      pos1 += 1

    if commands[1] == "left":
      if matrix[pos1][pos2 - 1] != ".":
         matrix[pos1][pos2 - 1] = "."

      pos2 -= 1

    if commands[1] == "right":
      if matrix[pos1 ][pos2 + 1] != ".":
        matrix[pos1][pos2 + 1] = "."

      pos2 += 1

  
  if commands[0] == "Read":
    if commands[1] == "up":
        if matrix[pos1 - 1][pos2] != ".":
          print(matrix[pos1 - 1][pos2])
        
        pos1 -= 1

    if commands[1] == "down":
      if matrix[pos1 + 1][pos2] != ".":
        print(matrix[pos1 + 1][pos2])
      
      pos1 += 1

    if commands[1] == "left":
      if matrix[pos1][pos2 - 1] != ".":
        print(matrix[pos1][pos2 - 1])
        
      pos2 -= 1

    if commands[1] == "right":
      if matrix[pos1][pos2 + 1] != ".":
        print(matrix[pos1][pos2 + 1])
      
      pos2 += 1


for things in matrix:
  print(f"{' '.join(things)}")
