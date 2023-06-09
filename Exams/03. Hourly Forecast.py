def forecast(*args):

  dict_weather = {"Sunny": [], "Cloudy": [], "Rainy": []}
  
  for forecasts in args:
    
    if forecasts[1] == "Sunny":
      dict_weather["Sunny"].append(forecasts[0])
    elif forecasts[1] == "Rainy":
      dict_weather["Rainy"].append(forecasts[0])
    elif forecasts[1] == "Cloudy":
      dict_weather["Cloudy"].append(forecasts[0])

  string = ""
  for key,value in dict_weather.items():
    value = sorted(value)

    for things in value:
      string += f"{things} - {key}\n"

  return string


print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
