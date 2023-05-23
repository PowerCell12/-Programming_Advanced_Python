from collections import deque

quantity  = int(input())

integers = list(map(int, input().split(" ")))

queue = deque(integers)

biggest = max(integers)
print(biggest)

for  i in range(len(queue)):
    
    ## if error try only bigger then 0
    if quantity - queue[0] >= 0:
        quantity -= queue[0]
        queue.popleft()
    else:
        break

if len(queue) == 0:
    print("Orders complete")
else:
    final = " ".join(list(map(str, queue)))
    print(f"Orders left: {final}")
