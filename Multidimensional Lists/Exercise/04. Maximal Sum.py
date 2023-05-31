rows, colums = map(int, input().split())


matrix  = [[things for things in map(int, input().split())] for i in range(rows)]

biggest = 0
list_biggest= []

for i in range(rows):

    if i == rows - 2 or i == rows - 1:
        break

    for j in range(colums):


        if j == colums - 2 or j == colums - 1:
            break


        sum1 = matrix[i][j]  + matrix[i][j + 1] + matrix[i][j + 2] + matrix[i + 1][j] + matrix[i + 1][j + 1] + matrix[i + 1][j + 2] + matrix[i + 2][j] + matrix[i+ 2][j + 1] + matrix[i+ 2][j + 2]

        if sum1 >= biggest:
            list_biggest.clear()
            biggest = sum1
            list_biggest.append(matrix[i][j])
            list_biggest.append(matrix[i][j + 1])
            list_biggest.append(matrix[i][j + 2])
            list_biggest.append(matrix[i + 1][j])
            list_biggest.append(matrix[i + 1][j  + 1])
            list_biggest.append(matrix[i + 1][j + 2])
            list_biggest.append(matrix[i + 2][j])
            list_biggest.append(matrix[i+ 2][j + 1])
            list_biggest.append(matrix[i + 2][j+ 2])

print(f"Sum = {biggest}")

if list_biggest:
    for i in range(0, len(list_biggest), 3):

        print(list_biggest[i], list_biggest[i + 1], list_biggest[i + 2])
