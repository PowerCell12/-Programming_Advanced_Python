lines = int(input())
set_valid = set()

for i in range(lines):

    codes = input()



    set_valid.add(codes)


while True:

    came = input()

    if came == "END":
        break


    set_valid.remove(came)


print(len(set_valid))

sorted_set = sorted(set_valid)

for things  in sorted_set:

    print(things)
