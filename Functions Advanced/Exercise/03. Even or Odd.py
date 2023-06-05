def even_odd(*args):

    def even():
        even = []
        
        for i in range(len(args) - 1):
            thing = args[i]

            if thing % 2 == 0:
                even.append(thing)

        return even

    def odd():
        odd = []

        for i in range(len(args) - 1):
            things = args[i]

            if things % 2 != 0:
                odd.append(things)

        return odd


    if args[-1] == "even":
        return even()
    elif args[-1] == "odd":
        return odd()
