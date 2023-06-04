def operate(operator, *args):

    def adding():
        base = 0

        for things in args:
            base += things

        return base
    

    def removing():
        base = args[0]

        for i in range(1, len(args)):
            
            base -= args[i]

        return base


    def multiplication():
        base  = 1

        for things in args:
            base *= things

        return base
    

    def division():

        base = args[0]

        for i  in range(1, len(args)):
            base /= args[i]

        return base
    
    if operator == '+':
        return adding()
    elif operator == '-':
        return removing()
    elif operator == '*':
        return multiplication()
    elif operator == '/':
        return division()
    
print(operate("/", 8, 4))
