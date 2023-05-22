list_names = []

while True:

    names = input()

    if names == "End":
        print(f"{len(list_names)} people remaining.")
        break



    if names == "Paid":
        print('\n'.join(list_names))

        list_names.clear()
        continue




    list_names.append(names)
