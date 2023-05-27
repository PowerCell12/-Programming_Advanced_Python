from collections import deque

chocolates = list(map(int, input().split(", ")))
cups = list(map(int, input().split(", ")))
cups = deque(cups)
milkshakes = 0

while chocolates and cups:

  chocolate = chocolates.pop()
  cup = cups.popleft()

  if chocolate <= 0 and cup <= 0:
    continue
  
  if chocolate <= 0 and cup > 0:
    cups.appendleft(cup)
    continue

  if cup <= 0 and chocolate > 0:
    chocolates.append(chocolate)
    continue

  
  if chocolate == cup:
    milkshakes += 1
  else:
    cups.append(cup)
    chocolate -= 5
    chocolates.append(chocolate)

  if milkshakes == 5:
    break

  

if milkshakes >= 5:
  print("Great! You made all the chocolate milkshakes needed!")
else:
  print("Not enough milkshakes.")

if chocolates:
  print(f"Chocolate: {', '.join(list(map(str, chocolates)))}")
else:
  print("Chocolate: empty")

if cups:
  print(f"Milk: {', '.join(list(map(str, cups)))}")
else:
  print("Milk: empty")
