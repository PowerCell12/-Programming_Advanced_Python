howManyPresents = int(input())
size = int(input())

matrix  = [[things for things in input().split()] for i in range(size)]

index_row = 0
index_column = 0

for i in range(len(matrix)):

    things = matrix[i]


    if "S" in things:
        index_row  = i
        index_column = things.index("S")
        break

## X naughty kid
## V nice kid
## C cookies
## -  empty
presents_Given = 0

matrix1  = [things for things1 in matrix for things in things1]
matrix1  = " ".join(matrix1)

import re
pattern  = r"V"
final = re.findall(pattern, matrix1)


while True:

    commands = input()

    if commands == "Christmas morning":
        break

    matrix[index_row][index_column] = "-"
    if commands == "up":

        if index_row  - 1 >= 0:
            index_row -= 1

    elif commands == "down":

        if index_row + 1 < size:
            index_row += 1
        
    elif commands == "left":

        if index_column - 1 >= 0:
            index_column -= 1


    elif commands == "right":

        if index_column + 1 < len(matrix[index_row]):
            index_column += 1

    if matrix[index_row][index_column] == "X":
        matrix[index_row][index_column] = "S"

    if matrix[index_row][index_column] == "V":
        howManyPresents -= 1
        presents_Given += 1

        matrix[index_row][index_column] = "S"

        if howManyPresents <= 0:
            break

    if matrix[index_row][index_column] == "C":
        matrix[index_row][index_column] = "S"
        ## left
        if index_column - 1 >= 0:

            if matrix[index_row][index_column - 1] == "X":
                howManyPresents -= 1
                matrix[index_row][index_column  - 1] = "-"

            if  matrix[index_row][index_column - 1] == "V":
                howManyPresents -= 1
                presents_Given += 1
                matrix[index_row][index_column - 1] = "-"

        if howManyPresents <= 0:
            break

        ## right
        if index_column + 1 < len(matrix[index_row]):

            if matrix[index_row][index_column + 1] == "X":
                howManyPresents -= 1
                matrix[index_row][index_column + 1] = "-"

            if  matrix[index_row][index_column + 1] == "V":
                howManyPresents -= 1
                presents_Given += 1
                matrix[index_row][index_column + 1] = "-"

        if howManyPresents <= 0:
            break

        ## up
        if index_row - 1 >= 0:
        
            if matrix[index_row - 1][index_column] == "X":
                howManyPresents -= 1
                matrix[index_row - 1][index_column] = "-"

            if  matrix[index_row - 1][index_column] == "V":
                howManyPresents -= 1
                presents_Given += 1
                matrix[index_row - 1][index_column] = "-"

        if howManyPresents <= 0:
            break

        ## down
        if index_row + 1 < size:

            if matrix[index_row + 1][index_column] == "X":
                howManyPresents -= 1
                matrix[index_row + 1][index_column] = "-"

            if  matrix[index_row + 1][index_column] == "V":
                howManyPresents -= 1
                presents_Given += 1
                matrix[index_row + 1][index_column] = "-"

        if howManyPresents <= 0:
            break

if howManyPresents >= 0 and len(final)  - presents_Given != 0:
    print("Santa ran out of presents!")

for things in matrix:

    print(f"{' '.join(things)}")

if len(final)  - presents_Given == 0:
    print(f"Good job, Santa! {presents_Given} happy nice kid/s.")
else:
    print(f"No presents for {len(final) - presents_Given} nice kid/s.")
