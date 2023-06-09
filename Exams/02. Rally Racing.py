size = int(input())
racingNumber = input()

row = 0
column = 0
kilometers = 0
route = [[things for things in input().split()] for i in range(size)]

## first row then column
two_tunnels = {}

for i in range(len(route)):
  final = route[i]

  if "T" in final:

    for things in final:
      if "T" == things:
          two_tunnels[i] = final.index("T")

while True:

  commands = input()

  if commands == "End":
    print(f"Racing car {racingNumber} DNF.")
    break

  

  route[row][column] = "."

  if commands == "left":
    column -= 1
  elif commands == "right":
    column += 1
  elif commands == "up":
    row -= 1
  elif commands == "down":
    row += 1


  if route[row][column] == "T":
    route[row][column] = "."
    for key,value in two_tunnels.items():
      if row == key and value == column:
        del two_tunnels[key]
        break

    for key,value in two_tunnels.items():
      row = key
      column = value

    route[row][column] = "C"

    kilometers += 30
    continue
    
  
  if route[row][column] == "F":
    kilometers += 10
    route[row][column] ="C"
    print(f"Racing car {racingNumber} finished the stage!")
    break  
  


  kilometers += 10
  route[row][column] = "C"

print(f"Distance covered {kilometers} km.")
for things in route:
  print("".join(things))
