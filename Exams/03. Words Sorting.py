def words_sorting(*args):

    dict_word = {}

    for word in args:

        sum1 = sum([ord(things) for things in word])

        dict_word[word] = sum1

    sum_final = 0
    for value in dict_word.values():
        sum_final += value

    sorted_dict = {}

    if sum_final % 2 == 0:
        sorted_dict = dict(sorted(dict_word.items(), key=lambda x: x[0]))
    else:
        sorted_dict = dict(sorted(dict_word.items(), key=lambda x: -x[1]))

    string = ""

    for key,value in sorted_dict.items():
        string += f"{key} - {value}\n"

    return string
