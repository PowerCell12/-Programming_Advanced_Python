lines = int(input())
set_final = set()

for i in range(lines):


    InOrOut = input().split(", ")

    if InOrOut[0] == "IN":

        set_final.add(InOrOut[1])

    if InOrOut[0] == "OUT":

        set_final.remove(InOrOut[1])



if len(set_final) == 0:
    print(f"Parking Lot is Empty")
else:

    for things in set_final:

        print(things)
