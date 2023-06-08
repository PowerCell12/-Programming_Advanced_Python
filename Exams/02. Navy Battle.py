rows = int(input())

battlefield = [[things for things in list(input())] for i in range(rows)]

row = 0
column = 0
hits = 0
ships_disc = 0

for i in range(len(battlefield)):
  final  = battlefield[i]

  if "S" in final:
    row = i
    column  = final.index("S")



final = [things for things1 in battlefield for things in things1]
final = " ".join(final)

allShip = 3

## all of the given command will be in the battlefield
while True:
  
  if hits == 3:
    print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {column}]!")
    break
  elif ships_disc == allShip:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
    break

  command = input()



  if command == "left":

    battlefield[row][column] = "-"
    
    column -= 1

  elif command == "right":
    battlefield[row][column] = "-"

    column += 1

  elif command == "up":
    battlefield[row][column] = "-"
    row -= 1

  elif command == "down":
    battlefield[row][column] = "-"
    row += 1
  
  if battlefield[row][column] == "*":
      hits += 1
      battlefield[row][column] = "S"
  elif battlefield[row][column] == "C":
      battlefield[row][column] = "S"
      ships_disc += 1
  else:
    battlefield[row][column] = "S"

for things in battlefield:
  print(f"{''.join(things)}")
