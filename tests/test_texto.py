import pytest

from texto import envuelve


def test_envuelve_corta_por_palabras():
    assert envuelve("uno dos tres", 7) == ["uno dos", "tres"]


def test_envuelve_texto_corto():
    assert envuelve("uno dos", 20) == ["uno dos"]


def test_envuelve_ancho_invalido():
    with pytest.raises(ValueError):
        envuelve("uno dos", 0)
