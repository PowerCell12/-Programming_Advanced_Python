pumps = int(input())
from_where = 0
petrol_left = 0

for i in range(pumps):

    commands = input().split(" ")

    ## first - amount of petrol
    ## second - distance to petrol

    petrol_left += int(commands[0]) - int(commands[1])
    

    if petrol_left < 0:
        from_where = i + 1
        petrol_left = 0


print(from_where)
