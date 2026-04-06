# Replace the "ANSWER HERE" for your answer
import math
def roots(a, b, c):
    d = b**2 - 4*a*c
    if d > 0:
        root_1 = (-b + math.sqrt(d))/(2*a)
        root_2 = (-b - math.sqrt(d))/(2*a)
        result = f"({root_1}, {root_2})"
    elif d == 0:
        root = -b/(2*a)
        result = f"({root})"

    else:
        result = "( )"
    
    return result
def value_y(a, b, c, x):
    y = a*(x**2) + b*x + c
    return y


def to_string(a, b, c):

    result = f"f(x) = "


    if a != 0 and b != 0 and c != 0: 
        result = f"f(x) = {a} * X^2 + {b} * X + {c}"
    
    if a != 0 and b == 0 and c != 0: 
        result = f"f(x) = {a} * X^2 + {c}"

    if a != 0 and b != 0 and c == 0: 
        result = f"f(x) = {a} * X^2 + {b} * X"

    if a == 0 and b != 0 and c != 0: 
        result = f"f(x) = {b} * X + {c}"

    if a == 0 and b == 0 and c != 0: 
        result = f"f(x) = {c}"

    if a != 0 and b == 0 and c == 0: 
        result = f"f(x) = {a} * X^2"



    return result


def derivation(a, b, c):
    function_derivated = f"f'(x) = {a * 2} * X + {b}"  
    if a == 0:
        function_derivated = f"f'(x) = {b}"  
    if b == 0:
        function_derivated = f"f'(x) = {a * 2} * X"

    if a == 0 and b == 0:
        function_derivated = f"f'(x) = 0"

    return  function_derivated 
