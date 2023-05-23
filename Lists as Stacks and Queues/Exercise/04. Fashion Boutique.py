integers = input().split(" ")

capacity  = int(input())
rack = 0
sum_final = 0

while integers:
    final = int(integers.pop())

    sum_final += final


    if sum_final == capacity:
        if len(integers) >= 0:
            rack += 1
        sum_final = 0

    if sum_final > capacity:
        rack += 1
        sum_final = final


## if error it is this 
if sum_final > 0:
    rack += 1

print(rack)
