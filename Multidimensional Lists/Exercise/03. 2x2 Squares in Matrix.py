row, column = input().split()

matrix = [[things for things in input().split()] for i in range(int(row))]

counter = 0

for i in range(int(row)):

    if i == int(row) - 1:
        break

    for j in range(int(column)):

        if j == int(column) - 1:
            break

        if matrix[i][j] == matrix[i][j + 1] and matrix[i][j] == matrix[i + 1][j] and matrix[i][j] == matrix[i + 1][j + 1]:
            counter += 1

print(counter)
