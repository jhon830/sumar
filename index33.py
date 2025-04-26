def sumar(x, y):
    """
    Suma dos númerso. Si la suma se halla entre 10 y 30, se retorna 30.
    """
    suma=x + y
    
    if suma in range(10, 30+1):
        return 30
    else:
        return suma
    
    
print(sumar(17,23))