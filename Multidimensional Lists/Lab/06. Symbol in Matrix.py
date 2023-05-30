lines   = int(input())

matrix = [[things for things in list(input())] for i in range(lines)]
symbol = input()

list_indexes  = []

for i in range(len(matrix)):

    for j in range(len(matrix[i])):

        if matrix[i][j] == symbol:
            list_indexes.append(i)
            list_indexes.append(j)


if list_indexes:
    print(f"({list_indexes[0]}, {list_indexes[1]})")
else:
    print(f"{symbol} does not occur in the matrix")
