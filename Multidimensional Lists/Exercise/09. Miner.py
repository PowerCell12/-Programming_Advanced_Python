size = int(input())
movements = input().split()

the_mining_zone = [[things for things in input().split()] for i in range(size)]

index_of_rows = 0
index_of_column = 0


for i in range(len(the_mining_zone)):
    things = the_mining_zone[i]

    if "s" in things:

        index_of_rows = i
        index_of_column = things.index("s")
        break


## first rows then columns !!!!


## check for all the coal
the_mining_zone_two = [things for thinsg1 in the_mining_zone for things in thinsg1]
the_mining_zone_two = " ".join(the_mining_zone_two)

import re
pattern = r'c'
all_coal = re.findall(pattern, the_mining_zone_two)
all_coal = len(all_coal)


collected_coal = 0
for  i in range(len(movements)):

    movement = movements[i]

## check if valid 

    if movement == "left":

        if index_of_column > 0:
         index_of_column  -= 1

    elif movement == "right":

        if index_of_column < len(the_mining_zone) - 1:
         index_of_column += 1

    elif movement == "up":

        if index_of_rows - 1 >= 0:
            index_of_rows -= 1
    
    elif movement == "down":

        if index_of_rows + 1  < size:
            index_of_rows += 1

    
    if the_mining_zone[index_of_rows][index_of_column] == "e":
        print(f"Game over! ({index_of_rows}, {index_of_column})")
        quit()
    elif the_mining_zone[index_of_rows][index_of_column] == "c":

        the_mining_zone[index_of_rows][index_of_column] = "*"
        collected_coal += 1
    
    if collected_coal == all_coal:
        print(f"You collected all coal! ({index_of_rows}, {index_of_column})")
        quit()


print(f"{all_coal - collected_coal} pieces of coal left. ({index_of_rows}, {index_of_column})")
