columns, rows = map(int, input().split())


matrix  = [[things for things in input().split()] for  i in range(columns)]

bool1 = True
while True:

    commands = input().split()


    if commands[0] == 'END':
        break


    for i in range(len(commands)):
      things = commands[i]
      
      if "swap" not in commands:
         bool1  = False
         break
  

    ## if things.isalpha():
    ##    matrix[int(commands[int(i)])] = list(matrix[int(commands[int(i)])])

      if len(commands) != 5:
          bool1 = False
          break
  
      
      if things.isdigit():
          if int(things) < 0:
            bool1 = False
            break

      if i == 1 or i == 3:
            if int(commands[i]) > rows:
              bool1 = False
              break

    if i == 2 or i == 4:
          if int(commands[i]) > columns:
            bool1 =  False
            break


    if bool1:
      matrix[int(commands[1])][int(commands[2])], matrix[int(commands[3])][int(commands[4])] = matrix[int(commands[3])][int(commands[4])] , matrix[int(commands[1])][int(commands[2])]
    
      for things in matrix:
        print(" ".join(things))
    else:
      print("Invalid input!")

    bool1 = True
