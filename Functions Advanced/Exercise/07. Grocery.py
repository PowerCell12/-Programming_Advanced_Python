def grocery_store(**kwargs):
  kwargsSorted = dict(sorted(kwargs.items(), key = lambda x: (-x[1], -len(x[0]), x[0])))

  string = ""
  for key,value in kwargsSorted.items():
    string += f"{key}: {value}\n"

  return string
