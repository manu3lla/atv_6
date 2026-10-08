def classificar_por_faixas(valor, faixas):
    """Retorna o rótulo da primeira faixa cujo limite superior é > valor.

    `faixas` é uma lista ordenada de tuplas (limite_superior, rotulo).
    O limite superior é exclusivo: valor == limite pertence à faixa seguinte.
    Use float("inf") como limite da última faixa.
    """
    for limite, rotulo in faixas:
        if valor < limite:
            return rotulo
    raise ValueError(f"Nenhuma faixa cobre o valor {valor!r}")


def classificar_vento(velocidade):
    faixas = [
        (20, "calmo"),
        (40, "moderado"),
        (60, "forte"),
        (float("inf"), "tempestade"),
    ]
    return classificar_por_faixas(velocidade, faixas)