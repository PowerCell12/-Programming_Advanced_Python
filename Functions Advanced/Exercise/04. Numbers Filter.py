def even_odd_filter(**kwargs):

    for key,value in kwargs.items():

        if key == "odd":
            odd_ones = []

            for things in value:
                if things % 2 != 0:
                    odd_ones.append(things)


            kwargs[key]  = odd_ones


        if key == "even":
            even_ones = []

            for things in value:
                if things % 2 == 0:
                    even_ones.append(things)


            kwargs[key] = even_ones

    return dict(sorted(kwargs.items()))
