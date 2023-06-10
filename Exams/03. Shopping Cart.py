def shopping_cart(*args):
  
  dict_food = {"Soup": [], "Pizza": [], "Dessert": []}
  # max soup = 3 pizza = 4 dessert = 2

  
  for things in args:

    if things == "Stop":
      break



    if things[0] == "Soup" and len(dict_food[things[0]]) < 3 and things[1] not in dict_food[things[0]]:
      dict_food[things[0]].append(things[1])
    if things[0] == "Pizza" and len(dict_food[things[0]]) < 4 and things[1] not in dict_food[things[0]]:
      dict_food[things[0]].append(things[1])
    if things[0] == "Dessert" and len(dict_food[things[0]]) < 2 and things[1] not in dict_food[things[0]]:
      dict_food[things[0]].append(things[1])

  sorted_dict = dict(sorted(dict_food.items(), key= lambda x: (-len(x[1]), x[0])))

  bool1 = True
  for things in sorted_dict.values():
    if things == []:
      bool1 = True
    else:
      bool1 = False
      break
  if bool1:
    return "No products in the cart!"
    

  string = ""
  for key,value in sorted_dict.items():
    string += f"{key}:\n"

    value = sorted(value)
    for things in value:
      string += f" - {things}\n"


  return string
