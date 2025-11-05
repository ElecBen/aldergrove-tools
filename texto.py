"""Utilidades de texto sin dependencias externas."""

from __future__ import annotations

import unicodedata

__all__ = ["envuelve", "sangra", "sin_acentos", "titulo"]


MENUDAS = {"a", "con", "de", "del", "el", "en", "la", "las",
           "los", "o", "por", "y"}


def envuelve(texto: str, ancho: int = 72) -> list[str]:
    """Parte el texto en lineas de `ancho` caracteres como maximo."""
    if ancho < 1:
        raise ValueError("ancho debe ser >= 1")
    lineas, actual = [], ""
    for palabra in texto.split():
        if not actual:
            actual = palabra
        elif len(actual) + 1 + len(palabra) <= ancho:
            actual += " " + palabra
        else:
            lineas.append(actual)
            actual = palabra
    if actual:
        lineas.append(actual)
    return lineas


def sangra(texto: str, prefijo: str = "    ") -> str:
    """Anade `prefijo` a cada linea que tenga contenido."""
    return "\n".join(prefijo + l if l.strip() else l
                     for l in texto.split("\n"))


def sin_acentos(texto: str) -> str:
    """Quita tildes y dieresis y deja el resto tal cual."""
    if not isinstance(texto, str):
        raise TypeError("texto debe ser str")
    suelto = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in suelto if not unicodedata.combining(c))


def titulo(texto):
    """Capitaliza cada palabra menos las menudas que no van primeras."""
    salida = []
    for i, palabra in enumerate(texto.lower().split()):
        salida.append(palabra if i and palabra in MENUDAS
                      else palabra.capitalize())
    return " ".join(salida)
