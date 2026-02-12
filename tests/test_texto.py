import pytest

from texto import envuelve, resume, sangra, sin_acentos, titulo


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


def test_sin_acentos():
    assert sin_acentos("camion") == "camion"
    assert sin_acentos("camión") == "camion"


def test_sin_acentos_toca_la_enie():
    assert sin_acentos("año") == "ano"


def test_sin_acentos_tipo():
    with pytest.raises(TypeError):
        sin_acentos(None)


def test_titulo():
    assert titulo("el rio y la mar") == "El Rio y la Mar"


def test_titulo_capitaliza_la_primera():
    assert titulo("de norte a sur") == "De Norte a Sur"


def test_resume():
    assert resume("uno dos tres cuatro", 12) == "uno dos..."


def test_resume_deja_el_corto_igual():
    assert resume("uno dos", 12) == "uno dos"


def test_resume_ancho_menor_que_la_cola():
    with pytest.raises(ValueError):
        resume("uno dos tres", 2)
