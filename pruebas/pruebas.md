## Pruebas unitarias

Las **pruebas unitarias** son aquellas que validan el comportamiento de componentes individuales de la aplicación (funciones, métodos, clases) de manera aislada. Son fundamentales porque:
- Permiten detectar errores de manera temprana.
- Facilitan la refactorización segura.
- Documentan el comportamiento esperado de las funciones.

**Cómo escribirlas**:
- Usa un marco de pruebas como `pytest` o `unittest`.
- Cubre casos normales, casos límite y casos de error.
- Mantén las pruebas cortas y legibles.

Ejemplo básico (con `pytest`):
```python
def suma(a, b):
    return a + b

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
```

## Configuración inicial
```bash
pip install pytest pytest-cov
```

## Ejecucion
```bash
pytest --cov=paquete_suma
```

## Ejecucion generando reporte HTML
```bash
pytest --cov=paquete_suma --cov-report=html tests/
```

