def multiply(*args):
    if args:
        total = 1
    else:
        total = 0
        return total

    for things in args:

        total *= things

    return total
