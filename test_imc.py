import pytest
from imc import calcular_imc, categorizar_imc, classificar_pessoa
# Exercício 1 - classes de equivalência
#   Válidas:   CE1: imc < 18,5          -> "abaixo do peso"
#              CE2: 18,5 <= imc < 25    -> "peso normal"
#              CE3: 25 <= imc < 30      -> "sobrepeso"
#              CE4: imc >= 30           -> "obesidade"
#   Inválidas (em calcular_imc): peso <= 0 ou altura <= 0 -> ValueError
def test_calcular_imc():
    assert calcular_imc(60, 2) == 15

def test_abaixo_do_peso():
    assert categorizar_imc(17) == "abaixo do peso"

def test_peso_normal():
    assert categorizar_imc(22) == "peso normal"

def test_sobrepeso():
    assert categorizar_imc(27) == "sobrepeso"

def test_obesidade():
    assert categorizar_imc(32) == "obesidade"

def test_classificar_pessoa():
    assert classificar_pessoa(70, 1.75) == "peso normal"

@pytest.mark.parametrize(
    "imc, esperado",
    [
        (18.49, "abaixo do peso"),
        (18.5, "peso normal"),
        (24.99, "peso normal"),
        (25, "sobrepeso"),
        (29.99, "sobrepeso"),
        (30, "obesidade"),
    ],
    ids=[
        "logo_abaixo_18_5",
        "fronteira_18_5",
        "logo_abaixo_25",
        "fronteira_25",
        "logo_abaixo_30",
        "fronteira_30",
    ],
)
def test_valores_limite_imc(imc, esperado):
    assert categorizar_imc(imc) == esperado

def test_peso_zero():
    with pytest.raises(ValueError):
        calcular_imc(0, 1.70)

def test_altura_negativa():
    with pytest.raises(ValueError):
        calcular_imc(70, -1.70)