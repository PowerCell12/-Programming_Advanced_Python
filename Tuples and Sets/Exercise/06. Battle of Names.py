lines = int(input())
row  = 0

set_odd = set()
set_even = set()

for i in range(lines):
    row += 1

    name = input()


    values = [ord(things) for things in name]

    values = int(sum(values) / row)

    if values % 2 == 0:
        set_even.add(values)
    else:
        set_odd.add(values)




sum1 = sum(set_even) ## even
sum2 = sum(set_odd) ## odd

if sum1 == sum2: ## i think it is right
    all_set = set_odd & set_even
    print(f"{', '.join(list(map(str, list(all_set))))}")
elif sum1 < sum2: ## the most keen for a error
    all_set = set_odd
    print(f"{', '.join(list(map(str, list(all_set))))}")
elif sum1 > sum2:
    all_set = set_odd ^ set_even
    print(f"{', '.join(list(map(str, list(all_set))))}")  ## it is right
