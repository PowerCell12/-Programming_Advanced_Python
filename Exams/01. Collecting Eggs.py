from collections import deque
sizes = deque([things for things in input().split(", ")])
papers = [things for things in input().split(", ")]
eggs_in = 0

while sizes and papers:

  first_egg = int(sizes.popleft())
  last_paper = int(papers.pop())

  if first_egg  <= 0:
      papers.append(last_paper)
      continue
  
  if first_egg == 13:
      papers.append(last_paper)
      papers[0], papers[-1] = papers[-1],  papers[0]
      continue
  
  wrapped = first_egg + last_paper

  if wrapped <= 50:
    eggs_in += 1
  

if eggs_in > 0:
  print(f"Great! You filled {eggs_in} boxes.")
else:
  print("Sorry! You couldn't fill any boxes!")

if sizes:
  print(f"Eggs left: {', '.join(sizes)}")

if papers:
  print(f"Pieces of paper left: {', '.join(list(map(str, papers)))}")
