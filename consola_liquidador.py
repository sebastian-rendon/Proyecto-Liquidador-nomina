import logica_liquidador

salario = float(input("ingrese el valor del salario mensual: "))
horas_extra = input("ingrese el valor de las horas extra: ")
bonificaciones = input("ingrese el valor de las bonificaciones: ")
comisiones = input("ingrese el valor de las comisiones: ")
auxilios = input("ingrese el valor de los auxilios: ")

salud = float(input("ingrese el valor de la salud que usted paga (en decimal): "))
pension = float(input("ingrese el valor de la pension que usted paga (en decimal):"))
impuesto_dinero = input("ingrese el valor de los impuestos que usted paga: ")

salario_neto = logica_liquidador.calcular_salario(
    salario,
    horas_extra,
    bonificaciones,
    comisiones,
    auxilios,
    salud,
    pension,
    impuesto_dinero
)

print("El salario neto es: ", salario_neto)