rows = int(input())


matrix = [[things for things in map(int, input().split(", "))  if things % 2 == 0] for i in range(rows)]

print(matrix)
