from collections import deque

water = int(input())

people = deque()


while True:

  names = input()

  if names == "Start":
    break


  people.append(names)


while True: 
  commands = input().split(" ")


  if commands[0] == "End":
    break



  if len(commands) > 1:
    water += int(commands[1])
  else:
    if water - int(commands[0]) >= 0:
      print(f"{people[0]} got water")
      water -= int(commands[0])
      people.popleft()
    else:
      print(f"{people[0]} must wait")
      people.popleft()

print(f"{water} liters left")
