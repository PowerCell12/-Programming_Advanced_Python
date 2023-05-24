parentheses = input()
open = ["(", "[", "{"]
closed = [")", "]", "}"]
all = ["()", "[]", "{}"]


opened_list = []
closed_list = []


for i in range(len(parentheses)):

    paren = parentheses[i]

    if paren in open:
        opened_list.append(paren)

    
    elif paren in closed:

        if not opened_list:
            print("NO")
            quit()
            
        string = opened_list[-1] + paren
        if string in all:
            opened_list.pop()
        else:
            print("NO")
            quit()

print("YES")
