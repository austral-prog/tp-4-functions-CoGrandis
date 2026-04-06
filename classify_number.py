def is_even(n):
    """Dado un número entero n, retorna True si es par, False si es impar."""
    return n % 2 == 0

def is_positive(n):
    """Dado un número entero n, retorna True si es mayor a 0, False en caso contrario."""
    return n > 0


def classify_number(n):
    """
    Dado un número entero n, retorna un string que lo clasifica.
    Debe USAR las funciones is_even e is_positive para resolver el ejercicio.

    Clasificaciones posibles:
      - "positive even"   (positivo y par)
      - "positive odd"    (positivo e impar)
      - "negative even"   (negativo y par)
      - "negative odd"    (negativo e impar)
      - "zero"            (el número es 0)
    """
    
        
    if is_even(n) and is_positive(n):
       classify = "positive even"
       
    if not is_even(n) and is_positive(n):
        classify = "positive odd"

    if is_even(n) and not is_positive(n):
        classify = "negative even"
        
    if not is_even(n) and not is_positive(n):
        classify = "negative odd"

    if n == 0:
        classify = "zero"
        
    return classify
