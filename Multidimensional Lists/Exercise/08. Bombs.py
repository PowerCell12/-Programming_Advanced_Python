rows = int(input())

matrix = [[things for things in map(int, input().split())] for i in range(rows)]
bombs = input().split()

for i in range(len(bombs)):

    bomb =  list(map(int, bombs[i].split(",")))


    if matrix[bomb[0]][bomb[1]] <= 0:
      continue
    else:
## for everyone check if they are different from zero, and below. They exist in the matrix.

      if 0 <= bomb[1] - 1:
        if matrix[bomb[0]][bomb[1] - 1] > 0:
          matrix[bomb[0]][bomb[1] - 1] -= matrix[bomb[0]][bomb[1]]


      if bomb[1] + 1 < len(matrix[bomb[0]]):
        if matrix[bomb[0]][bomb[1] + 1] > 0:
          matrix[bomb[0]][bomb[1] + 1] -= matrix[bomb[0]][bomb[1]]


      if bomb[0] - 1 >= 0: ## upper in the matrix, but techniqly lower
        if matrix[bomb[0] - 1][bomb[1]] > 0:
          matrix[bomb[0] - 1][bomb[1]] -= matrix[bomb[0]][bomb[1]] 

      if bomb[0] - 1 >= 0  and 0 <= bomb[1] - 1:
        if matrix[bomb[0] - 1][bomb[1] - 1] > 0:
          matrix[bomb[0] - 1][bomb[1] - 1] -= matrix[bomb[0]][bomb[1]]

      if bomb[0] - 1 >= 0:
        if bomb[1] + 1 < len(matrix[bomb[0] - 1]):
          if matrix[bomb[0] - 1][bomb[1] + 1] > 0:
            matrix[bomb[0] - 1][bomb[1] + 1] -= matrix[bomb[0]][bomb[1]]

        ## less then rows

      if bomb[0] + 1 < rows:
        if matrix[bomb[0] + 1][bomb[1]] > 0:
           matrix[bomb[0] + 1][bomb[1]] -= matrix[bomb[0]][bomb[1]]

      if bomb[0] + 1 < rows and 0 <= bomb[1] - 1:
        if matrix[bomb[0] + 1][bomb[1] - 1] > 0:
          matrix[bomb[0] + 1][bomb[1] - 1] -= matrix[bomb[0]][bomb[1]]

      if bomb[0] + 1 < rows: 
        if  bomb[1] + 1 < len(matrix[bomb[0] + 1]):
            if matrix[bomb[0] + 1][bomb[1] + 1] > 0:    
              matrix[bomb[0] + 1][bomb[1] + 1] -= matrix[bomb[0]][bomb[1]]
      
      
      matrix[bomb[0]][bomb[1]] = 0


alive = [things1 for things in matrix for things1 in things if things1 > 0]


print(f"Alive cells: {len(alive)}")
print(f"Sum: {sum(alive)}")


for things in matrix:

    print(f"{' '.join(list(map(str,things)))}")
