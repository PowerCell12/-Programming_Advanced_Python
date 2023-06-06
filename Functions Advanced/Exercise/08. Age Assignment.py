def age_assignment(*args, **kwargs):
  dict_names_age = {}
  
  for keys,value in kwargs.items():

    for names in args:
      if keys == names[0]:
        dict_names_age[names] = value


  sorted_dict  = dict(sorted(dict_names_age.items()))

  string = ""
  for key,value in sorted_dict.items():
    string += f'{key} is {value} years old.\n'

  return string
