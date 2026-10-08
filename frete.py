def tem_frete_gratis(valor_compra, cliente_premium, peso):
    return valor_compra >= 200 and bool(cliente_premium) and peso <= 30