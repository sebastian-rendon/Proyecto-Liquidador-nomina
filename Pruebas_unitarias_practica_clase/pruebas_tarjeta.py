
#from logica_tarjeta import calcular_cuota
import logica_tarjeta


def probar_caso_normal_1():
    #definir datos de entrada
    compra = 200_000
    #La cuota de interés se expresa en porcentaje, por lo que se debe dividir entre 100 para obtener el valor decimal
    interes = 3.1 / 100
    plazo = 36

    #Realizar el proceso
    cuota_calculada = logica_tarjeta.calcular_cuota(compra, interes, plazo)

    #Verificar las salidas
    cuota_esperada = 9297.96

    if(round(cuota_calculada, 2) == round(cuota_esperada,2)):
        print("La prueba fue exitosa")

    else:
        print("Prueba fallida! Se obtuvo: {cuota_calculada} y se esperaba: {cuota_esperada}")

def probar_caso_normal_2():
    #definir datos de entrada
    compra = 500_000
    #La cuota de interés se expresa en porcentaje, por lo que se debe dividir entre 100 para obtener el valor decimal
    interes = 2.5 / 100
    plazo = 24

    #Realizar el proceso
    cuota_calculada = logica_tarjeta.calcular_cuota(compra, interes, plazo)

    #Verificar las salidas
    cuota_esperada = 21_325.25

    if(round(cuota_calculada, 2) == round(cuota_esperada,2)):
        print("La prueba fue exitosa")

    else:
        print("Prueba fallida! Se obtuvo: {cuota_calculada} y se esperaba: {cuota_esperada}")


probar_caso_normal_1()




