def add_songs(*args):

  dict_songs = {}
  
  for things in args:

    title = things[0]
    lyrics = things[1] 

    if title in dict_songs.keys():
      dict_songs[title] += lyrics
    else:
        dict_songs[title] = lyrics

  string = ""
  for key,value in dict_songs.items():
    if value:
      string += f"- {key}\n"
      for things in value:
        string += f"{things}\n"
    else:
        string += f"- {key}\n"    

  return string
