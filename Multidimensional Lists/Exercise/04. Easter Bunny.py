rows = int(input())

matrix = [[things for things in input().split()] for i in range(rows)]

## if error check if the bunny position is wrong 

index_row = 0
index_column = 0

for i in range(len(matrix)):

    things = matrix[i]

    if "B" in things:
        index_row = i
        index_column  = things.index("B")

left = 0
right  = 0
up = 0 
down = 0 

## in the dict first is row then column
dict_left = {}
dict_right = {}
dict_down = {}
dict_up = {}

old_row = index_row
old_column = index_column


## left
while index_column - 1 >= 0:
    index_column -= 1

    if matrix[index_row][index_column] == "X":
        break

    left += int(matrix[index_row][index_column])
    dict_left[index_column] = index_row

## they change every time 
index_row = old_row
index_column = old_column

## right
while index_column + 1 < len(matrix[index_row]):
    index_column += 1

    if matrix[index_row][index_column] == "X":
        break

    right += int(matrix[index_row][index_column])
    dict_right[index_column] = index_row


index_row = old_row
index_column = old_column

## up
while index_row - 1 >= 0:

    index_row -= 1

    if matrix[index_row][index_column] == "X":
        break

    up += int(matrix[index_row][index_column])
    dict_up[index_row] = index_column

index_row = old_row
index_column = old_column

## down
while index_row + 1 < rows:
    index_row  += 1

    if matrix[index_row][index_column] == "X":
        break

    down += int(matrix[index_row][index_column])
    dict_down[index_row] = index_column

list1 = [left, right, up, down]
final = max(list1)


if final != 0:
    if up == final:
        print("up")
        for key,value in dict_up.items():
            print(f"[{key}, {value}]")
        print(up)

    elif down == final:
        print("down")
        for key, value in dict_down.items():
            print(f"[{key}, {value}]")
        print(down)

    elif left == final:
        print("left")
        for key, value in dict_left.items():
            print(f"[{value}, {key}]")
        print(left)

    elif right == final:
        print("right")
        for key, value in dict_right.items():
            print(f"[{value}, {key}]")
        print(right)
