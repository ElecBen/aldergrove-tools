# aldergrove-tools

Utilidades de texto para envolver, sangrar y limpiar cadenas.

## Uso

```python
from texto import envuelve

envuelve("uno dos tres", 7)  # ["uno dos", "tres"]
```

## Estructura

```
texto.py          modulo principal
tests/           tests con pytest
docs/            notas de diseno
```

## API

| funcion | que devuelve |
| --- | --- |
| `envuelve(texto, ancho)` | el texto partido en lineas de `ancho` como maximo |
| `sangra(texto, prefijo)` | el texto con `prefijo` delante de cada linea con contenido |
| `sin_acentos(texto)` | el texto sin tildes ni dieresis |
| `titulo(texto)` | el texto en mayusculas de titulo, sin tocar las menudas |
| `resume(texto, ancho, cola)` | el texto recortado por la ultima palabra que cabe |
