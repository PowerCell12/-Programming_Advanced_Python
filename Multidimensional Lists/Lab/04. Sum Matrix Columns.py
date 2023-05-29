rows, columns  = map(int, input().split(", "))



matrix  = [[things for things in map(int, input().split())] for i in range(rows)]


for i in range(columns):

    sum1  = 0
    for j in range(rows):
        matrix1 = matrix[j][i]
        sum1 += matrix1

    print(sum1)
