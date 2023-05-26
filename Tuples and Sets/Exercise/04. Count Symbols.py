string = input()

tuple_final = tuple(string)

tuple_final = sorted(tuple_final)
already_typed = []

for things in tuple_final:

  if things not in already_typed:
    print(f"{things}: {tuple_final.count(things)} time/s")


  already_typed.append(things)
