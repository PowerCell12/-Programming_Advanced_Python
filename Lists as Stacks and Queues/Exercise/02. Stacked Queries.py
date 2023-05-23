lines = int(input())
stack = []

for i in range(lines):

  commands = input()

  if commands[0] == "1":
    stack.append(int(commands.split(" ")[1]))

  if commands[0] == "2":
    if len(stack) > 0:
      stack.pop()

  if commands[0] == "3":
    if len(stack) > 0:
        print(max(stack))

  if commands[0] == "4":
    if len(stack) > 0:
        print(min(stack))

print(", ".join(list(map(str, stack[::-1]))))
