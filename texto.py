import unicodedata


MENUDAS = {"a", "con", "de", "del", "el", "en", "la", "las",
           "los", "o", "por", "y"}


def envuelve(texto, ancho=72):
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
