import pytest
from classificadores import classificar_por_faixas, classificar_vento
# Exercício 3b - tabela de vento
# Classes de equivalência:
#   CE1: velocidade < 20         -> "calmo"
#   CE2: 20 <= velocidade < 40   -> "moderado"
#   CE3: 40 <= velocidade < 60   -> "forte"
#   CE4: velocidade >= 60        -> "tempestade"
# Valores-limite: 19/20, 39/40, 59/60 (logo abaixo e na fronteira), mais um representante do meio de cada classe.

@pytest.mark.parametrize(
    "velocidade, esperado",
    [
        (5, "calmo"),
        (19, "calmo"),
        (20, "moderado"),
        (30, "moderado"),
        (39, "moderado"),
        (40, "forte"),
        (50, "forte"),
        (59, "forte"),
        (60, "tempestade"),
        (100, "tempestade"),
    ],
    ids=[
        "meio_calmo",
        "logo_abaixo_20",
        "fronteira_20",
        "meio_moderado",
        "logo_abaixo_40",
        "fronteira_40",
        "meio_forte",
        "logo_abaixo_60",
        "fronteira_60",
        "meio_tempestade",
    ],
)
def test_classificar_vento(velocidade, esperado):
    assert classificar_vento(velocidade) == esperado
FAIXAS = [(10, "baixo"), (20, "medio"), (float("inf"), "alto")]

@pytest.mark.parametrize(
    "valor, esperado",
    [
        (5, "baixo"),
        (9.99, "baixo"),
        (10, "medio"),
        (19.99, "medio"),
        (20, "alto"),
        (1000, "alto"),
    ],
)
def test_classificar_por_faixas(valor, esperado):
    assert classificar_por_faixas(valor, FAIXAS) == esperado

def test_classificar_por_faixas_sem_faixa_correspondente():
    with pytest.raises(ValueError):
        classificar_por_faixas(50, [(10, "baixo"), (20, "medio")])