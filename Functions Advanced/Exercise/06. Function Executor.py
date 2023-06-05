def func_executor(*args):


    results =  []

    for func, args_tuple in args:

        result = func(*args_tuple)
        results.append(f"{func.__name__} - {result}")

    return "\n".join(results)
