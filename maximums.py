def max_of_two(x, y):
        if x > y :
            max_number = x
        else:
            max_number = y
        return max_number

def max_of_three(x, y, z):
    max_number = max_of_two(x, y)
    max_number = max_of_two(max_number, z)
    return max_number
