rows = int(input())

matrix = [[things for things in input().split()] for i in range(rows)]

bags = 0
index_rows = 0
index_columns = 0

for i in range(len(matrix)):

  things = matrix[i]

  if "A" in things:
    index_rows = i
    index_columns = things.index("A")
    break


while True:

  commands = input()

  if commands == "up":
      matrix[index_rows][index_columns] = "*"

    
      if index_rows - 1 < 0:
        break
      else:

        index_rows -= 1

        if matrix[index_rows][index_columns] == "R":
          matrix[index_rows][index_columns] = "*"
          break


        if matrix[index_rows][index_columns].isdigit():
          bags += int(matrix[index_rows][index_columns])


  
  if commands == "down":
    matrix[index_rows][index_columns] = "*"

    if index_rows + 1 >= rows:
      break
    else:

      index_rows += 1

      if matrix[index_rows][index_columns] == "R":
        matrix[index_rows][index_columns] = "*"
        break

      if matrix[index_rows][index_columns].isdigit():
        bags += int(matrix[index_rows][index_columns])


  if commands == "left":
    matrix[index_rows][index_columns] = "*"

    if index_columns - 1 < 0:
      break
    else:

      index_columns -= 1

      if matrix[index_rows][index_columns] == "R":
        matrix[index_rows][index_columns] = "*"
        break

      if matrix[index_rows][index_columns].isdigit():
        bags += int(matrix[index_rows][index_columns])


  if commands == "right":
    matrix[index_rows][index_columns] = "*"

    if index_columns + 1 >= len(matrix[index_rows]):
      break
    else:
      index_columns += 1

      if matrix[index_rows][index_columns] == "R":
        matrix[index_rows][index_columns] = "*"
        break

      if matrix[index_rows][index_columns].isdigit():
        bags += int(matrix[index_rows][index_columns])

    
  if bags >= 10:
    matrix[index_rows][index_columns] = "*"
    break


if bags >= 10:
  print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for things in matrix:

    print(f"{' '.join(things)}")
