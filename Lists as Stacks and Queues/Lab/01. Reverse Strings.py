string = input()
list1 =[]

for i in range(len(string) -1 , -1, -1):

    list1.append(string[i])


list1 = "".join(list1)

print(list1)
