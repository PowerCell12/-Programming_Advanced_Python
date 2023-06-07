def movie_organizer(*args):

    dict_genres = {}
  
    for things in args:

      movie_name, Genre = things[0], things[1]


      if Genre not in dict_genres.keys():
          dict_genres[Genre] = []  
      dict_genres[Genre].append(movie_name)

      dict_sorted = dict(sorted(dict_genres.items(), key = lambda x: (-len(x[1]), x[0])))

    string = ""
    for key,value in dict_sorted.items():
    
        string += f"{key} - {len(value)}\n"

        value = sorted(value)
        for things in value:
          string += f"* {things}\n"

    return string
