rows = int(input())


matrix = [[things for things in map(int, input().split())] for i in range(rows)]
counter = 0

total = 0 
for i in range(len(matrix)):


    total += matrix[i][counter]

    counter += 1

print(total)
