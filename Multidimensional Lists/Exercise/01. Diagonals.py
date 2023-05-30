rows=  int(input())

matrix = [[things for things in map(int, input().split(", "))] for i in range(rows)]

primary = 0
list_primary = []
for  i in range(rows):


    primary += matrix[i][i]
    list_primary.append(matrix[i][i])


secondary = 0
list_secondary = []
counter = 0

for i in range(rows - 1, -1, -1):

    secondary += matrix[counter][i]
    list_secondary.append(matrix[counter][i])

    counter += 1

print(f"Primary diagonal: {', '.join(list(map(str, list_primary)))}. Sum: {primary}")
print(f"Secondary diagonal: {', '.join(list(map(str, list_secondary)))}. Sum: {secondary}")
