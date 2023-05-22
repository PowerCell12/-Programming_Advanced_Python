expression = input()
counter = 0

indexes = []

for i  in range(len(expression)):
    things = expression[i]

    if things == "(":
        indexes.append(i)


    if things == ")":
        

        print(expression[indexes[-1] : i + 1])
        
        index = indexes.pop()
