import logica_liquidador

try:
    entrada_salario = input("Ingrese el valor del salario mensual: ")
    entrada_horas_extra = input("Ingrese el valor de las horas extra: ")
    entrada_bonificaciones = input("Ingrese el valor de las bonificaciones: ")
    entrada_comisiones = input("Ingrese el valor de las comisiones: ")
    entrada_auxilios = input("Ingrese el valor de los auxilios: ")

    entrada_salud = input("Ingrese el porcentaje de la salud que usted paga (en decimal, ademas no mayor a 4%): ")
    entrada_pension = input("Ingrese el porcentaje de la pensión que usted paga (en decimal, ademas no mayor a 4%): ")
    entrada_impuesto_dinero = input("Ingrese el valor de los impuestos que usted paga: ")

    campos = [
        entrada_salario,
        entrada_horas_extra,
        entrada_bonificaciones,
        entrada_comisiones,
        entrada_auxilios,
        entrada_salud,
        entrada_pension,
        entrada_impuesto_dinero
    ]

    
    if any(campo == "" for campo in campos):
        raise ValueError("ERROR, Hay campos obligatorios vacíos")

    salario = float(entrada_salario)
    horas_extra = float(entrada_horas_extra)
    bonificaciones = float(entrada_bonificaciones)
    comisiones = float(entrada_comisiones)
    auxilios = float(entrada_auxilios)

    salud = float(entrada_salud)
    pension = float(entrada_pension)
    impuesto_dinero = float(entrada_impuesto_dinero)

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

    print("El salario neto es:", salario_neto)

except Exception as err:
    print("Ocurrió un error:", err)
    print(str(err))