def sorting_cheeses(**kwargs):

    sorted_kwargs = sorted(kwargs.items(),key= lambda x: (-len(x[1]), x[0]))

    output = ""

    for i in range(len(sorted_kwargs)):

        thing = sorted_kwargs[i]

        cheeses = sorted(thing[1], reverse=True)
        if i == len(sorted_kwargs) - 1:
            output += f"{thing[0]}\n" + "\n".join(map(str, cheeses))
        else:
            output += f"{thing[0]}\n" + "\n".join(map(str, cheeses)) + "\n"

    return output
