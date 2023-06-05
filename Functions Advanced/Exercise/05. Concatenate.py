def concatenate(*args, **kwargs):

    string = ""

    for things in args:
        string += things

    
    for key,value in kwargs.items():


        if key in string:

            string = string.replace(key, value)


    return string
