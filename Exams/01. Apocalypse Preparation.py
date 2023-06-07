from collections import deque
textfiles = deque([things for things in list(map(int, input().split()))])
medicaments = [things for things in list(map(int, input().split()))]

dict_medicin = {"Patch": 0, "Bandage": 0, "MedKit":0}

while True:

  if not len(textfiles) and not len(medicaments):
    print("Textiles and medicaments are both empty.")
    break
  if not len(textfiles):
    print("Textiles are empty.")
    break
  elif not len(medicaments):
    print("Medicaments are empty.")
    break

  
  textfile = textfiles.popleft()
  medicament = medicaments.pop()


  final = textfile + medicament

  if final == 30:
    dict_medicin["Patch"] += 1
    continue
  elif final == 40:
    dict_medicin["Bandage"] += 1
    continue
  elif final == 100:
    dict_medicin["MedKit"] += 1
    continue
  
  if final > 100:
    final -= 100
    dict_medicin["MedKit"] += 1    
    
    medicaments[-1] += final
  else:
    medicament += 10
    medicaments.append(medicament)


sorted_dict = dict(sorted(dict_medicin.items(), key=lambda x: (-x[1], x[0])))
for key,value in sorted_dict.items():
  if value != 0:
    print(f"{key} - {value}")


if len(medicaments):
  final = list(map(str, medicaments))
  final.reverse()
  print(f"Medicaments left: {', '.join(final)}")

if len(textfiles):
  print(f"Textiles left: {', '.join(list(map( str, textfiles)))}")
