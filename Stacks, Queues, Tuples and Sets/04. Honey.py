from collections import deque

working_bees = list(map(int, input().split()))
nectar = list(map(int, input().split()))
symbols = input().split()

working_bees = deque(working_bees)
symbols = deque(symbols)

total = 0

while working_bees and nectar:

    bee = working_bees.popleft()
    nectar_last  = nectar.pop()

    if nectar_last >= bee:
        value_bee = bee
        value_nect = nectar_last
    else:
        working_bees.appendleft(bee)
        continue

    symbol = symbols.popleft()

    if symbol == "+":
        honey = value_bee + value_nect
        honey = abs(honey)
    elif symbol == "-":
        honey = value_bee - value_nect
        honey = abs(honey)
    elif symbol == "*":
        honey = value_bee * value_nect
        honey = abs(honey)
    elif symbol == "/":
        if value_bee != 0 and value_nect != 0 :
            honey = value_bee / value_nect
            honey = abs(honey)
        else:
            honey = 0 

    total += honey

print(f"Total honey made: {total}")

if working_bees:
    print(f"Bees left: {', '.join(list(map(str, working_bees)))}")

if nectar:
    print(f"Nectar left: {', '.join(list(map(str, nectar)))}")
