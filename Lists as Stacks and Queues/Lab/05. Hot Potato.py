from collections import deque

people = deque(input().split(" "))

n = int(input())

counter = 1
while len(people) > 1:
    
    final = people.popleft()

    if counter == n:
        print(f"Removed {final}")
        counter = 1

    else:
        counter += 1
        people.append(final)


winner = people.popleft()
print(f"Last is {winner}")
