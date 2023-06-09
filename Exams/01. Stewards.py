from collections import deque

seats = [seat for seat in input().split(", ")]
sequence1 = deque([int(num) for num in input().split(", ")])
sequence2 = [int(num) for num in input().split(", ")]

seats_in = []
matches = 0

for i in range(11):
    if len(seats_in) == 3:
        break
  
    first = sequence1.popleft()
    last = sequence2.pop()

    sum1 = first + last

    ascii_num = chr(sum1)

    if f"{first}{ascii_num}" in seats:
        if f"{first}{ascii_num}" in seats_in:
            sequence1.append(first)
            continue
        else:
            seats_in.append(f"{first}{ascii_num}")
            continue
    elif f"{last}{ascii_num}" in seats:
        if f"{last}{ascii_num}" in seats_in:
            sequence2.insert(0, last)
            continue
        else:
            seats_in.append(f"{last}{ascii_num}")
            continue

    sequence1.append(first)
    sequence2.insert(0, last)

print(f"Seat matches: {', '.join(seats_in)}")
print(f"Rotations count: {i}")
