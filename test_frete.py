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

"""
Tabela reduzida por don't care:
R1: Compra >= 200, premium e peso <= 30.
    Resultado: frete gratis.
R2: Compra >= 200, premium e peso > 30.
    Resultado: frete cobrado.
R3: Compra >= 200 e cliente sem premium.
    O peso nao importa, pois o frete sera cobrado.
R4: Compra < 200.
    Premium e peso nao importam, pois o frete sera cobrado.
A tabela reduzida possui quatro regras:
1. Todas as condicoes verdadeiras: frete gratis.
2. Peso acima de 30 kg: frete cobrado.
3. Cliente sem premium: frete cobrado, independentemente do peso.
4. Compra abaixo de R$ 200: frete cobrado, independentemente das
   outras condicoes.
"""