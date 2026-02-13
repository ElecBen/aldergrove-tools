"""Mide envuelve() sobre un texto largo.

Se ejecuta desde la raiz del repo para que `texto` este en la ruta:

    python -m bench.medir
"""
import random
import string
import time

from texto import envuelve


def parrafo(palabras):
    letras = string.ascii_lowercase
    return " ".join("".join(random.choice(letras)
                            for _ in range(random.randrange(3, 11)))
                    for _ in range(palabras))


def main():
    largo = parrafo(40000)
    arranque = time.perf_counter()
    lineas = envuelve(largo, 72)
    print("%d lineas en %.3f s" % (len(lineas), time.perf_counter() - arranque))


if __name__ == "__main__":
    main()
