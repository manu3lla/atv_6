def classificar_por_faixas(valor, faixas):
    for limite, rotulo in faixas:
        if valor < limite:
            return rotulo
def categorizar_imc(imc):
    faixas = [
        (18.5, "abaixo do peso"),
        (25, "peso normal"),
        (30, "sobrepeso"),
        (float("inf"), "obesidade")
    ]
    return classificar_por_faixas(imc, faixas)
def classificar_vento(velocidade):
    faixas = [
        (20, "calmo"),
        (40, "moderado"),
        (60, "forte"),
        (float("inf"), "tempestade")
    ]
    return classificar_por_faixas(velocidade, faixas)