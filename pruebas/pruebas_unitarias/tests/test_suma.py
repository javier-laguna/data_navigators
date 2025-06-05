import pytest
from paquete_suma.suma import suma

def test_suma():
    """
    Prueba unitaria para la función suma.
    
    Valida que la suma de dos números sea correcta para
    distintos casos: positivos, negativos y ceros.
    """
    # Caso normal
    assert suma(2, 3) == 5
    
    # Caso con número negativo
    assert suma(-1, 1) == 0
    
    # Caso con ambos números en cero
    assert suma(0, 0) == 0