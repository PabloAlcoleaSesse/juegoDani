

import os


def clear(): 
    """Limpia la consola."""
    
    os.system('cls' if os.name == 'nt' else 'clear')



def salto_de_linea(n: int = 1):
    """Imprime saltos de línea en la consola.
    
    Args:
        n (int): Número de saltos de línea a imprimir. Por defecto es 1.
    """
    
    for _ in range(n):
        print()

def pasarFase(): 
    input("Presiona Enter para continuar...")
    clear()
    