def students_credits(*args):
  dict_points = {}
  all_credits =0
  
  for credits in args:

    course = credits.split("-")

    percentage = int(course[3]) / int(course[2])
                                     
    final = int(course[1]) * percentage

    dict_points[course[0]] = final
    all_credits += final

  dict_points = dict(sorted(dict_points.items(), key= lambda x: -x[1]))

  string = ""
  if all_credits >= 240:
    string += f"Diyan gets a diploma with {all_credits:.1f} credits.\n"
  else:
    needs = 240 - all_credits
    string += f"Diyan needs {needs:.1f} credits more for a diploma.\n"


  for key,value in dict_points.items():
    string += f"{key} - {value:.1f}\n"

  return string
