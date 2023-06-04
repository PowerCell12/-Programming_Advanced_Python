def rectangle(length, width):

    if type(length) is not int or type(width) is not int:
        return "Enter valid values!"


    def area():
        area = length * width
        return area
    
    def perimeter():
        permiter = 2 * length + 2 * width
        return permiter
    

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"

print(rectangle("2", 10))
