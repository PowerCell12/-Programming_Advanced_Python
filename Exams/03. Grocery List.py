def   shop_from_grocery_list(budget, grocery_list, *args):

    bought = []

    for products in args:

        if budget < products[1]:
            break


        if products[0] in grocery_list:
            bought.append(products[0])
            grocery_list.remove(products[0])
            budget -= products[1]
    
    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."
