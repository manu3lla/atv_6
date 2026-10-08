import pytest
from frete import tem_frete_gratis
@pytest.mark.parametrize("valor, premium, peso, esperado", [
    (200, True, 30, True),
    (200, True, 31, False),
    (200, False, 30, False),
    (200, False, 31, False),
    (199, True, 30, False),
    (199, True, 31, False),
    (199, False, 30, False),
    (199, False, 31, False),
], ids=["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8"])
def test_tabela_decisao_frete(valor, premium, peso, esperado):
    assert tem_frete_gratis(valor, premium, peso) == esperado