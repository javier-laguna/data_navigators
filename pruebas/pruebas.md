## Pruebas unitarias

Las **pruebas unitarias** son aquellas que validan el comportamiento de componentes individuales de la aplicación (funciones, métodos, clases) de manera aislada. Son fundamentales porque:
- Permiten detectar errores de manera temprana.
- Facilitan la refactorización segura.
- Documentan el comportamiento esperado de las funciones.

**Cómo escribirlas**:
- Usa un marco de pruebas como `pytest` o `unittest`.
- Cubre casos normales, casos límite y casos de error.
- Mantén las pruebas cortas y legibles.


# ¿Qué es la cobertura de código?

La **cobertura de código** (en inglés: **code coverage**) es una métrica que indica **qué porcentaje de tu código fuente se ejecuta** cuando corres tus pruebas:

Te dice **cuántas líneas** (o ramas) del código se **ejecutaron** al menos una vez durante las pruebas.  
No te dice si tus pruebas están **bien escritas** o si **todas las rutas lógicas** fueron verificadas.

---

## ¿Por qué es útil?

- Te ayuda a detectar **partes del código que no tienen pruebas**.
- Puede guiarte para **mejorar la calidad de las pruebas**.
- Es especialmente útil en equipos grandes para identificar módulos descuidados.

---

## ¿Cómo se calcula?

El proceso típicamente funciona así:
1. Se ejecutan todas las pruebas.
2. Una herramienta (como `coverage.py` o `pytest-cov`) monitorea **qué líneas de código** fueron ejecutadas.
3. La herramienta genera un **reporte** (en la terminal o en HTML) mostrando:
   - Porcentaje total de cobertura.
   - Líneas o archivos no cubiertos.
   - Cobertura por archivo o módulo.

---

## Nota importante

**Cobertura alta no significa que las pruebas sean buenas.**  
Podrías cubrir todas las líneas, pero no verificar que el código se comporte como esperas. Por eso la cobertura es una métrica de apoyo, pero no una garantía de calidad.

---

## Herramientas recomendadas

- [`pytest-cov`](https://pytest-cov.readthedocs.io/) para integrarse con `pytest`.
- [`coverage.py`](https://coverage.readthedocs.io/) para reportes detallados.


Ejemplo básico (con `pytest`):
```python
def suma(a, b):
    return a + b

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
```

### Ejecución con `pytest-cov`

Instala las dependencias:
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

