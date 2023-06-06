def fill_the_box(*args):

  size = args[0] * args[1] * args[2]

  for i in range(3, len(args)):

    things  = args[i]

    if things == "Finish":
      break

    things = int(things)
    
    
    if size - things > 0:
      size -= things
    else:
      remaining = abs(size - things)

      From = i + 1
        
      for j in range(From, len(args)):
        things1 = args[j]


        if things1 == "Finish":
          break

        things1 = int(things1)
        
        remaining += things1

      return f"No more free space! You have {remaining} more cubes."


  return f"There is free space in the box. You could put {size} more cubes."
