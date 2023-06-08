rows, columns = list(map(int, input().split()))

playground = [[things for things in input().split()]for i in range(rows)]

row_pos = 0
column_pos = 0

for i in range(len(playground)):
  final = playground[i]


  if "B" in final:
    row_pos = i
    column_pos = final.index('B')

touched_players = 0
moves = 0

while True:
  direction = input()

  if direction == "Finish":
    break


  if direction == "left":
    if column_pos - 1 < 0:
      continue

    if playground[row_pos][column_pos - 1] == "O":
      continue

    column_pos -= 1
    moves += 1


  if direction == "right":
    if column_pos + 1 >= len(playground[row_pos]):
        continue

    if playground[row_pos][column_pos + 1] == "O":
      continue

    column_pos += 1
    moves += 1


  if direction == "up":
    
    if row_pos  - 1 < 0:
      continue

    if playground[row_pos - 1][column_pos] == "O":
      continue

    row_pos -= 1
    moves += 1  


  if direction == "down":
    if row_pos + 1 >= len(playground):
      continue

    if playground[row_pos + 1][column_pos] == "O":
      continue

    row_pos += 1
    moves += 1


  if playground[row_pos][column_pos] == "P":
    touched_players += 1    
    playground[row_pos][column_pos] = "-"


    if touched_players == 3:
      break

print(f"Game over!")
print(f"Touched opponents: {touched_players} Moves made: {moves}")
