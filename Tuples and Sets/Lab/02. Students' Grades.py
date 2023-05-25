lines = int(input())
names_grade_dict = {}

for i in range(lines):

  name_grade = tuple(input().split())

  x,y = name_grade


  if x not in names_grade_dict.keys():
    names_grade_dict[x] = []
  names_grade_dict[x].append(float(y))

value1 = []
for key,value in names_grade_dict.items():

  average = sum(value) / len(value)


  ## see how to format it to the second decimal point and done
  for things in value:
    things = round(things,2)
    value1.append(f"{things:.2f}")
  last = " ".join(value1)
  
  print(f"{key} -> {last} (avg: {average:.2f})")
  value1  = []
