"""
Condições:C1 = valor >= 200, C2 = cliente premium, C3 = peso <= 30

Tabela completa (8 regras = 2^3):

  Condição     R1 R2 R3 R4 R5 R6 R7 R8
  Valor>=200?   S  S  S  S  N  N  N  N
  Premium?      S  S  N  N  S  S  N  N
  Peso<=30?     S  N  S  N  S  N  S  N
  Frete grátis  X
  Cobrar frete     X  X  X  X  X  X  X

Tabela reduzida por don't care (8 regras -> 4):

  Condição     Ra Rb Rc Rd
  Valor>=200?   S  S  S  N
  Premium?      S  S  N  -
  Peso<=30?     S  N  -  -
  Frete grátis  X
  Cobrar frete     X  X  X

  Ra: as três condições verdadeiras -> frete grátis.
  Rb: valor ok e premium, mas peso > 30 -> cobrado (peso é decisivo).
  Rc (junta R3 e R4): valor >= 200 e NÃO premium -> cobrado, o peso não
      importa, pois a falta de premium já impede o frete grátis.
  Rd (junta R5 a R8): valor < 200 -> cobrado, premium e peso não importam,
      pois o valor insuficiente já impede o frete grátis.
"""
import pytest
from frete import tem_frete_gratis
@pytest.mark.parametrize(
    "valor, premium, peso, esperado",
    [
        (200, True, 30, True),    
        (200, True, 31, False),   
        (200, False, 30, False),  
        (200, False, 31, False),  
        (199, True, 30, False),   
        (199, True, 31, False),   
        (199, False, 30, False),  
        (199, False, 31, False),  
    ],
    ids=["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8"],
)
def test_tabela_decisao_frete(valor, premium, peso, esperado):
    assert tem_frete_gratis(valor, premium, peso) == esperado

@pytest.mark.parametrize(
    "valor, premium, peso, esperado",
    [
        (200, True, 30, True),      
        (200, True, 31, False),     
        (200, False, 10, False),    
        (200, False, 100, False),   
        (50, True, 10, False),      
        (50, False, 100, False),    
    ],
    ids=["Ra", "Rb", "Rc_leve", "Rc_pesado", "Rd_premium", "Rd_sem_premium"],
)
def test_tabela_reduzida_frete(valor, premium, peso, esperado):
    assert tem_frete_gratis(valor, premium, peso) == esperado