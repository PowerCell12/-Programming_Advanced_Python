from collections import deque
foods = [things for things in input().split(", ")]
staminas = deque([things for things in input().split(", ")])

goals = []


for i in range(7):

  food = float(foods.pop())
  stamina = float(staminas.popleft())
  final = food + stamina
  
  if final >= 80 and "Vihren" not in goals:
    goals.append("Vihren")

  if final >= 90 and "Vihren" in goals and "Kutelo" not in goals:
    goals.append("Kutelo")

  if final >= 100 and "Kutelo" in goals and "Banski Suhodol" not in goals:
    goals.append("Banski Suhodol")

  if final >= 60 and "Banski Suhodol" in goals and "Polezhan" not in goals:
    goals.append("Polezhan")

  if final >= 70 and "Polezhan" in goals and "Kamenitza" not in goals:
    goals.append("Kamenitza")

if len(goals) == 5:
  print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
  print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")


if goals:
  print("Conquered peaks:")
  for things in goals:
    print(things)
