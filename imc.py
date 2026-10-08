def calcular_imc(peso, altura):
    if peso <= 0 or altura <= 0:
        raise ValueError("Peso e altura devem ser positivos")
    return peso / (altura ** 2)
def categorizar_imc(imc):
    if imc < 18.5:
        return "abaixo do peso"
    if imc < 25:
        return "peso normal"
    if imc < 30:
        return "sobrepeso"
    return "obesidade"
def classificar_pessoa(peso, altura):
    imc = calcular_imc(peso, altura)
    return categorizar_imc(imc)