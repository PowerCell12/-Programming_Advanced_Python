columns, rows = map(int, input().split())

new_matrix = []
starting = 96
main_ones = 96

for i in range(columns):

    new_row = []
    main_ones += 1

    for j in range(rows):
        starting += 1

        strings =  f"{chr(main_ones)}{chr(starting)}{chr(main_ones)}"

        new_row.append(strings)


    new_matrix.append(new_row)


    starting = main_ones



for things in new_matrix:

    print(f"{' '.join(things)}")
