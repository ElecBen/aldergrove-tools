import pytest

from texto import envuelve, sangra


def test_envuelve_corta_por_palabras():
    assert envuelve("uno dos tres", 7) == ["uno dos", "tres"]


def test_envuelve_texto_corto():
    assert envuelve("uno dos", 20) == ["uno dos"]


def test_envuelve_ancho_invalido():
    with pytest.raises(ValueError):
        envuelve("uno dos", 0)


def test_sangra():
    assert sangra("uno\ndos") == "    uno\n    dos"


def test_sangra_respeta_las_vacias():
    assert sangra("uno\n\ndos") == "    uno\n\n    dos"
