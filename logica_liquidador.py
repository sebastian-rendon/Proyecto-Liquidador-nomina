
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
    valores_devengados = sum([salario, horas_extra, bonificaciones, comisiones, auxilios])
    salud_dinero = salud * salario 
    pension_dinero = pension * salario
    
    deducciones_de_ley = sum([salud_dinero, pension_dinero, impuesto_dinero])
    salario_neto = valores_devengados - deducciones_de_ley
    return (salario_neto)