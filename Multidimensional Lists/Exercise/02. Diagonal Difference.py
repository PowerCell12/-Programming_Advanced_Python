size = int(input())

matrix = [[things for things in map(int, input().split())] for i in range(size)]

primary, secondary = [], []

for i in range(size):
    
    primary.append(matrix[i][i])

counter = 0
for i in range(size - 1, -1, -1):

    secondary.append(matrix[counter][i])

    counter += 1


print(f"{abs(sum(primary) - sum(secondary))}")
