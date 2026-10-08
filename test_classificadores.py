import pytest
from classificadores import classificar_por_faixas, classificar_vento, categorizar_imc
@pytest.mark.parametrize("velocidade, esperado", [
    (10, "calmo"),
    (20, "moderado"),
    (30, "moderado"),
    (40, "forte"),
    (50, "forte"),
    (60, "tempestade"),
    (70, "tempestade"),
], ids=[
    "calmo",
    "fronteira_20",
    "moderado",
    "fronteira_40",
    "forte",
    "fronteira_60",
    "tempestade"
])
def test_classificar_vento(velocidade, esperado):
    assert classificar_vento(velocidade) == esperado
def test_classificar_por_faixas():
    faixas = [(10, "baixo"), (20, "medio"), (float("inf"), "alto")]
    assert classificar_por_faixas(5, faixas) == "baixo"
    assert classificar_por_faixas(10, faixas) == "medio"
    assert classificar_por_faixas(20, faixas) == "alto"

def test_categorizar_imc_generico():
    assert categorizar_imc(22) == "peso normal"
    assert categorizar_imc(27) == "sobrepeso"