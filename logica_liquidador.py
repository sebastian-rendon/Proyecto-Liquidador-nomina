class ErrorCampoObligatorio(Exception):
    pass

class ErrorTipoInvalido(Exception):
    "Error cuando el salario no es de tipo entero o float"
    pass



def calcular_salario(salario, horas_extra, bonificaciones, comisiones, auxilios, salud, pension, impuesto_dinero):
    """
    salario: El salario base del trabajador
    horas_extra: En caso de que el trabajador haya realizado horas extra, caso contrario ingresa 0
    bonificaciones: En caso de que el trabajador obtuviera bonificaciones, caso contrario ingresa 0
    comisiones: En caso de que el trabajador haya recibido comisiones, caso contrario ingresa 0
    auxilios: En caso de que el trabajador obtuviera auxilios, caso contrario ingresa 0
    salud: Porcentaje de salud del trabajador, en Colombia permanece generalmente sin cambios expresado en decimal (ejemplo: 4% ingresar 0.04)
    pension: Porcentaje de pension del trabajador, en Colombia permanece generalmente sin cambios expresado en decimal (ejemplo: 4% ingresar 0.04)
    impuesto_dinero: Cualquier tipo de impuesto aplicado, expresado en dinero (un entero), caso contrario ingresa 0
    """

    MAX_VALOR = 1_000_000_000  # Límite máximo permitido

    # Campo obligatorio
    if salario is None:
        raise ErrorCampoObligatorio("ERROR, El salario es un campo obligatorio")

    # Tipo de dato
    if not isinstance(salario, (int, float)):
        raise TypeError("ERROR, Tipo de dato inválido")

    # Negativo
    if salario < 0:
        raise ValueError("ERROR, El salario no puede ser negativo")

    # Número excesivamente grande
    if salario > MAX_VALOR:
        raise ValueError("ERROR, Valor fuera del rango permitido")

    # Porcentaje fuera del rango legal
    if salud > 0.20 or pension > 0.20:
        raise ValueError("ERROR, Porcentaje fuera del rango legal permitido")

    valores_devengados = sum([salario, horas_extra, bonificaciones, comisiones, auxilios])
    salud_dinero = salud * salario 
    pension_dinero = pension * salario
    
    deducciones_de_ley = sum([salud_dinero, pension_dinero, impuesto_dinero])
    salario_neto = valores_devengados - deducciones_de_ley
    return (salario_neto)