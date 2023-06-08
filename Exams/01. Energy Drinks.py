from collections import deque
milligrams = [things for things in map(int, input().split(", "))]
energy_drinks = deque([things for things in map(int, input().split(', '))])

max = 300
current = 0

while milligrams and energy_drinks:

  milligram =  milligrams.pop()
  energy_drink = energy_drinks.popleft()

  both = milligram * energy_drink

  if both < 300 and current + both < 300:
    current += both
  else:
    energy_drinks.append(energy_drink)
    current -= 30
    if current < 0:
      current = 0


if energy_drinks:
  print(f"Drinks left: {', '.join(list(map(str, energy_drinks)))}")
else:
  print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {current} mg caffeine.")
