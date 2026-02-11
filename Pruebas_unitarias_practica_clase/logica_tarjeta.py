
def calcular_cuota(compra, interes, plazo):
    """
    compra: Valor de la compra con la tarjeta
    interes: Tasa de interés mensual expresada en decimal (por ejemplo, 3.1% se debe ingresar como 0.031)
    plazo: Número de meses para pagar la compra
    """
    return (compra * interes) / (1 - (1 + interes) ** (-plazo))