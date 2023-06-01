lists = input().split("|")
list_final = []

for  i in range(len(lists) - 1, -1, -1):
    things  = lists[i]


    things1 = things.split(" ")


    for things2 in things1:

      if things2 != "":
        list_final.append(things2)
        
print(f"{' '.join(list_final)}")
