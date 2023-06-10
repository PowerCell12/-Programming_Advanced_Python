matrix = [[things for things in input().split()] for i in range(6)]
commands = input().split(", ")

row = 0
column = 0
for i in range(len(matrix)):

    things = matrix[i]

    if "E" in things:
        row = i
        column = things.index("E")
        break

dict_materials = {"Water": 0, "Metal": 0, "Concrete": 0}


for i in range(len(commands)):

    command = commands[i]


    if command == "left": ## yes

        if column - 1 < 0:
            column = len(matrix[row]) - 1

        else:
            column -= 1

    if command == "right": ##  yes

        if column + 1 >= len(matrix[row]):
            column = 0

        else:
            column +=1

    if command  == "up":  ##yes

        if row - 1  < 0:
            row  = len(matrix) - 1

        else:
            row -= 1
        
    if command == "down":

        if row + 1 >= len(matrix):
            row = 0
        
        else:
            row += 1

    if matrix[row][column] == "W":
        print(f"Water deposit found at ({row}, {column})")
        dict_materials["Water"] += 1

    if matrix[row][column] == "M":
        print(f"Metal deposit found at ({row}, {column})")
        dict_materials["Metal"] += 1

    if matrix[row][column] == "C":
        print(f"Concrete deposit found at ({row}, {column})")
        dict_materials["Concrete"] += 1

    if matrix[row][column] == "R":
        print(f"Rover got broken at ({row}, {column})")
        break

if dict_materials["Metal"] > 0 and dict_materials["Concrete"] > 0 and dict_materials["Water"] > 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
