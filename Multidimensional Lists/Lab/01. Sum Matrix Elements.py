rows, columns = list(map(int, input().split(', ')))
matrix = []
sum1 = 0

for i in range(rows):

  matrix.append([])
  things_in = list(map(int, input().split(', ')))

  sum1 += sum(things_in)
  
  for j in range(columns):
    matrix[i].append(things_in[j])

print(sum1)
print(matrix)
