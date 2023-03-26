def calculate_factorial(number):
    if number == 0 | number == 1:
        return 1
    else:
        return number * calculate_factorial(number - 1)


def calculate_triangle_number(number):
    if number == 0 | number == 1:
        return 1
    else:
        return number + calculate_triangle_number(number - 1)