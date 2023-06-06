def math_operations(*args, **kwargs):
  counter1 = 0
  counter2 = 1
  counter3 = 2
  counter4 = 3

  for i in range(len(args)):
    things = args[i]

    if i == counter1:
      kwargs['a'] += things
      counter1 += 4

    if i == counter2:
      kwargs['s'] = kwargs['s'] - things
      counter2 += 4

    if i == counter3:
      if things != 0:
        kwargs['d'] /= things
      counter3 += 4

    if i == counter4:
      kwargs['m'] *= things
      counter4 += 4


  sorted_kwargs = dict(sorted(kwargs.items(), key= lambda x: (-x[1], x[0])))

  string = ""

  for key,value in sorted_kwargs.items():

    string += f'{key}: {value:.1f}\n'

  return string
