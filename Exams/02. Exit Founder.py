TomAndJerry = input().split(", ")
first = ""
second = ""

if TomAndJerry[0] == "Tom":
  first = "Tom"
  second = "Jerry"
else:
  first  = "Jerry"
  second = "Tom"


matrix = [[things for things in input().split()] for i in range(6)]
counter = 0
hit_wall1 = False
hit_wall2 = False

while True:

  command = input().split(", ")
  
  if counter % 2 == 0:

    pos1_row = int(command[0][1])
    pos1_column = int(command[1][0])
  
    if hit_wall1:
      hit_wall1 = False
      counter += 1
      continue
  
    if matrix[pos1_row][pos1_column] == "E":
      print(f"{first} found the Exit and wins the game!")
      break
    elif matrix[pos1_row][pos1_column] == "T":
      print(f"{first} is out of the game! The winner is {second}.")
      break
    elif matrix[pos1_row][pos1_column] == "W":
      print(f"{first} hits a wall and needs to rest.")
      hit_wall1 = True
      
  else:

    pos2_row  = int(command[0][1])
    pos2_column = int(command[1][0])

    if hit_wall2:
      hit_wall2 = False
      counter += 1
      continue
    
    if matrix[pos2_row][pos2_column] == "E":
      print(f"{second} found the Exit and wins the game!")
      break
    elif matrix[pos2_row][pos2_column] =="T":
      print(f"{second} is out of the game! The winner is {first}.")
      break
    elif matrix[pos2_row][pos2_column] == "W":
      print(f"{second} hits a wall and needs to rest.")
      hit_wall2  = True
  
  counter += 1
