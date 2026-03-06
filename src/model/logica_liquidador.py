class ErrorCampoObligatorio(Exception):
    "Error cuando no se reibe un dato que es obligatorio"

class ErrorTipoInvalido(Exception):
    "Error cuando el salario no es de tipo entero o float"


class ErrorSalarioNegativo(Exception):
    "Error cuando el salario es negativo"
    

class ErrorSalarioGrande(Exception):
    "Error cuando el salario es excesivamente grande"

class ErrorPorcentajesFueraRango(Exception):
    "Error cuando se ingresa un porcentaje de impuestos es mayor al legal"



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
    if salario == "":
        raise ErrorCampoObligatorio("ERROR, El salario es un campo obligatorio")

    # Tipo de dato
    if not isinstance(salario, (int, float)):
        raise ErrorTipoInvalido(f"ERROR, El valor ' {salario} ' es un tipo de dato inválido, ingrese un valor numérico")

    # Negativo
    if salario < 0:
        raise ErrorSalarioNegativo(f"ERROR, El salario ingresado ' {salario} ' no puede ser un valor negativo")

    # Número excesivamente grande
    if salario > MAX_VALOR:
        raise ErrorSalarioGrande(f"ERROR, El Valor {salario} ingresado esta fuera del rango permitido(1.000.000.000)")

    # Porcentaje fuera del rango legal
    if salud > 0.04 or pension > 0.04:
        raise ErrorPorcentajesFueraRango(f"ERROR, El Porcentaje de salud {salud * 100} o pension {pension * 100} son valores fuera del rango legal permitido(4%)")

    valores_devengados = sum([salario, horas_extra, bonificaciones, comisiones, auxilios])
    salud_dinero = salud * salario 
    pension_dinero = pension * salario
    
    deducciones_de_ley = sum([salud_dinero, pension_dinero, impuesto_dinero])
    salario_neto = valores_devengados - deducciones_de_ley
    return (salario_neto)