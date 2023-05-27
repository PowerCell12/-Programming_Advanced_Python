integers1 = list(map(int, input().split(" ")))
integers2 = list(map(int, input().split(" ")))

set1 = set(integers1)
set2 = set(integers2)

lines = int(input())

for i in range(lines):

    commands = input().split(" ")


    if commands[0] == "Add":

        if commands[1] == "First":
            commands.pop(0)
            commands.pop(0)

            for things in commands:
                set1.add(int(things))

        elif commands[1] == "Second":

            commands.pop(0)
            commands.pop(0)

            for things in commands:
                set2.add(int(things))

            
    if commands[0] == "Remove":

            if commands[1] == "First":
                commands.pop(0)
                commands.pop(0)

                for things in commands:
                    set1.discard(int(things))

            
            if commands[1] == "Second":

                commands.pop(0)
                commands.pop(0)


                for things in commands:
                    set2.discard(int(things))

    if "Check"  == commands[0] and "Subset" == commands[1]:

        if set1 > set2 or set2 >  set1:
            print("True")
        else:
            print("False")


print(f"{', '.join(list(map(str, list(sorted(set1)))))}")
print(f"{', '.join(list(map(str, list(sorted(set2)))))}")
