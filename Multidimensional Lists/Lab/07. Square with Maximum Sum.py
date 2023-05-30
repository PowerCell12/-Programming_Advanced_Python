rows, columns = list(map(int, input().split(", ")))

metrix = [[things for things in map(int, input().split(", "))] for i in range(rows)]



sum_final = 0 
elements = []

for i in range(rows):

    if i + 1 == rows:
        break

    for j in range(columns):

        if j + 1 == columns:
            break

        
        sum1 = metrix[i][j] + metrix[i][j + 1] + metrix[i + 1][j] + metrix[i + 1][j + 1]

        if sum1 > sum_final:
            elements.clear()
            sum_final = sum1
            elements.append(metrix[i][j])
            elements.append(metrix[i][j + 1])
            elements.append(metrix[i + 1][j])
            elements.append(metrix[i + 1][j + 1])

print(f"{elements[0]} {elements[1]}")
print(f"{elements[2]} {elements[3]}")
print(sum_final)
