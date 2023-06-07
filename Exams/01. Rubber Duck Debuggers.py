from collections import deque

integers1 = deque([int(things) for things in input().split()])
integers2 = [int(things) for things in input().split()]


dict_ducks = {"Darth Vader Ducky":0, "Thor Ducky":0, "Big Blue Rubber Ducky":0, "Small Yellow Rubber Ducky":0}


while len(integers1) or len(integers2):

  TimeValue = integers1.popleft()
  TaskValue = integers2.pop()

  final = TimeValue * TaskValue 
  
  if 0 <= final <= 60:
    dict_ducks["Darth Vader Ducky"] += 1
  elif 60 < final < 121:
    dict_ducks["Thor Ducky"] +=1
  elif 120 < final < 181:
    dict_ducks["Big Blue Rubber Ducky"] += 1
  elif 180 < final < 241:
    dict_ducks["Small Yellow Rubber Ducky"] += 1
  else:
    integers1.append(TimeValue)
    TaskValue -= 2
    integers2.append(TaskValue)


print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for key,value in dict_ducks.items():
  print(f"{key}: {value}")
