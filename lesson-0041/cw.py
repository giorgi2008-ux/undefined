def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 / value2
print(basic_op("*",4,5))


def area_or_perimeter(l , w):
    if l == w:
        return l * w 
    else:
        return 2 * (l + w)
print(area_or_perimeter(5,5))

