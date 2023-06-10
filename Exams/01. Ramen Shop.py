from collections import deque
bowls_ramen = [things for things in map(int, input().split(", "))]
customers = deque([things for things in map(int, input().split(", "))])

while bowls_ramen and customers:

  bowl = bowls_ramen.pop()
  person  = customers.popleft()
              
  if bowl == person:
    continue

  if bowl > person:
    bowl -= person
    bowls_ramen.append(bowl)
    continue
    
  if person > bowl:
    person -= bowl
    customers.appendleft(person)
    continue

if not customers:
  print("Great job! You served all the customers.")
  if bowls_ramen:
    print(f"Bowls of ramen left: {', '.join(list(map(str, bowls_ramen)))}")
  quit()

if not bowls_ramen:
  print("Out of ramen! You didn't manage to serve all customers.")
  
  if customers:
    print(f"Customers left: {', '.join(list(map(str, customers)))}")
