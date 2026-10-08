import pytest
from classificadores import classificar_por_faixas, classificar_vento, categorizar_imc
@pytest.mark.parametrize("velocidade, esperado", [
    (19, "calmo"),
    (20, "moderado"),
    (21, "moderado"),
    (39, "moderado"),
    (40, "forte"),
    (41, "forte"),
    (59, "forte"),
    (60, "tempestade"),
    (61, "tempestade"),
], ids=[
    "abaixo_20",
    "fronteira_20",
    "acima_20",
    "abaixo_40",
    "fronteira_40",
    "acima_40",
    "abaixo_60",
    "fronteira_60",
    "acima_60"
])
def test_classificar_vento(velocidade, esperado):
    assert classificar_vento(velocidade) == esperado
def test_classificar_por_faixas():
    faixas = [
        (10, "baixo"),
        (20, "medio"),
        (float("inf"), "alto")
    ]

    assert classificar_por_faixas(5, faixas) == "baixo"
    assert classificar_por_faixas(10, faixas) == "medio"
    assert classificar_por_faixas(20, faixas) == "alto"
def test_categorizar_imc_generico():
    assert categorizar_imc(17) == "abaixo do peso"
    assert categorizar_imc(22) == "peso normal"
    assert categorizar_imc(27) == "sobrepeso"
    assert categorizar_imc(32) == "obesidade"