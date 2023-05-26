lines = int(input())

set1 = set()
set2 = set()

biggest = 0
biggest_len = 0

##Note: in each range, there will always be an intersection. If there are two equal intersections, print the first one.

for i in range(lines):


    intersections1, intersections2 = input().split("-")



    list1 = list(map(int, intersections1.split(",")))
    while list1[0] <= list1[1]:

        set1.add(list1[0])
        list1[0] += 1


    list2 = list(map(int, intersections2.split(",")))
    while list2[0] <= list2[1]:
        set2.add(list2[0])
        list2[0] += 1



    final = set1 & set2


    if len(final) > biggest_len:
        biggest_len = len(final)
        biggest = final

    set1 = set()
    set2 = set()


print(f"Longest intersection is [{', '.join(map(str, list(biggest)))}] with length {biggest_len}")
