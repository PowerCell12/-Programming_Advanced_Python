rows  = int(input())

matrix = [[things for things in map(int, input().split(", "))] for i in range(rows)]


flattened = [things1 for things in matrix for things1 in things]

print(flattened)
