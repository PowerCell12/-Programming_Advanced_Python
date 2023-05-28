from collections import deque

strings = input().split()
strings = deque(strings)
first_colors = []
position = 0

while strings:
  if len(strings) == 1:
    final  = strings.pop()
    final1 = final[::-1]

    if final == "":
      break

    if final == "red" or final == "yellow" or final == "blue":
      first_colors.append(final)
      continue

    if final == "orange" or final == "purple" or final =="green":
      first_colors.append(final)
      continue

    if final1 == "red" or final1 == "yellow" or final1 == "blue":
      first_colors.append(final1)
      continue

    if final1 == "orange" or final1 == "purple" or final1 =="green":
      first_colors.append(final1)
      continue

    
    final = final[:-1]
    strings.insert(0, final)
    
  else:

    first =  strings.popleft()
    last = strings.pop()

    word = first + last
    word1 = word[::-1]
    word2 = last + first
    
    ## see how to search for the word

    if word == "red" or word == "yellow" or word == "blue":
      first_colors.append(word)
      continue

    if word == "orange" or word == "purple" or word =="green":
      first_colors.append(word)
      continue

    if word1 == "red" or word1 == "yellow" or word1 == "blue":
      first_colors.append(word1)
      continue

    if word1 == "orange" or word1 == "purple" or word1 =="green":
      first_colors.append(word1)
      continue

    if word2 == "red" or word2 == "yellow" or word2 == "blue":
      first_colors.append(word2)
      continue

    if word2 == "orange" or word2 == "purple" or word2 =="green":
      first_colors.append(word2)
      continue

    first = first[:-1]
    last = last[:-1]

    if len(strings) % 2 == 0:
      position = int(len(strings) / 2)
    else:
      position = int(len(strings) / 2) +  1

    if first != "":
     strings.insert(position, first)
    if last != "":
     strings.insert(position, last)
    

if first_colors:

  for things in first_colors:

    if things == "orange":
      if "red" in first_colors and "yellow" in first_colors:
        pass
      else:
        first_colors.remove(things)
    elif things == "purple":
      if "red" in first_colors and "blue" in first_colors:
        pass
      else:
        first_colors.remove(things)
    elif things == "green":
      if "yellow" in first_colors and "blue" in first_colors:
        pass
      else:
        first_colors.remove(things)


print(first_colors)
