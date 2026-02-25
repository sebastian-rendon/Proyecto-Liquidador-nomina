import unittest
import logica_liquidador

class TestCalculoSalario(unittest.TestCase):

    def test_normal1_salario(self):

        #entradas
        salario = 5000000
        horas_extra = 150000
        bonificaciones = 50000
        comisiones = 100000
        auxilios = 0
        salud = 0.04
        pension = 0.04
        impuesto_dinero = 50000

        #proceso
        salario_calculado = logica_liquidador.calcular_salario(salario, horas_extra, bonificaciones, comisiones, auxilios, salud, pension, impuesto_dinero)

        #Datos de salida esperados
        salario_esperado = 4850000

        #verificar la salida
        self.assertEqual(salario_calculado, salario_esperado)

    def test_normal2_salario(self):

        #entradas
        salario = 6200000
        horas_extra = 100000
        bonificaciones = 100000
        comisiones = 20000
        auxilios = 0
        salud = 0.04
        pension = 0.04
        impuesto_dinero = 62000

        #proceso
        salario_calculado = logica_liquidador.calcular_salario(salario, horas_extra, bonificaciones, comisiones, auxilios, salud, pension, impuesto_dinero)

        #Datos de salida esperados
        salario_esperado = 5862000

        #verificar la salida
        self.assertEqual(salario_calculado, salario_esperado)

    def test_normal3_salario(self):

        #entradas
        salario = 4500000
        horas_extra = 50000
        bonificaciones = 50000
        comisiones = 20000
        auxilios = 0
        salud = 0.04
        pension = 0.04
        impuesto_dinero = 45000

        #proceso
        salario_calculado = logica_liquidador.calcular_salario(salario, horas_extra, bonificaciones, comisiones, auxilios, salud, pension, impuesto_dinero)

        #Datos de salida esperados
        salario_esperado = 4215000

        #verificar la salida
        self.assertEqual(salario_calculado, salario_esperado)

    def test_normal4_salario(self):

        #entradas
        salario = 4000000
        horas_extra = 200000
        bonificaciones = 60000
        comisiones = 10000
        auxilios = 0
        salud = 0.04
        pension = 0.04
        impuesto_dinero = 40000

        #proceso
        salario_calculado = logica_liquidador.calcular_salario(salario, horas_extra, bonificaciones, comisiones, auxilios, salud, pension, impuesto_dinero)

        #Datos de salida esperados
        salario_esperado = 3910000

        #verificar la salida
        self.assertEqual(salario_calculado, salario_esperado)

    #casos extraordinarios
    def test_empleado_no_trabajo(self):

        #entradas
        salario = 0
        horas_extra = 0
        bonificaciones = 0
        comisiones = 0
        auxilios = 0
        salud = 0.04
        pension = 0.04
        impuesto_dinero = 0

        #proceso
        salario_calculado = logica_liquidador.calcular_salario(salario, horas_extra, bonificaciones, comisiones, auxilios, salud, pension, impuesto_dinero)

        #Datos de salida esperados
        salario_esperado = 0

        #verificar la salida
        self.assertEqual(salario_calculado, salario_esperado)

    def test_salario_en_limite_de_impuestos(self):

        #entradas
        salario = 3500000
        horas_extra = 0
        bonificaciones = 0
        comisiones = 0
        auxilios = 0
        salud = 0.04
        pension = 0.04
        impuesto_dinero = 35000

        #proceso
        salario_calculado = logica_liquidador.calcular_salario(salario, horas_extra, bonificaciones, comisiones, auxilios, salud, pension, impuesto_dinero)

        #Datos de salida esperados
        salario_esperado = 3185000

        #verificar la salida
        self.assertEqual(salario_calculado, salario_esperado)
    
    def test_salario_muy_alto(self):

        #entradas
        salario = 25000000
        horas_extra = 200000
        bonificaciones = 100000
        comisiones = 30000
        auxilios = 0
        salud = 0.04
        pension = 0.04
        impuesto_dinero = 250000

        #proceso
        salario_calculado = logica_liquidador.calcular_salario(salario, horas_extra, bonificaciones, comisiones, auxilios, salud, pension, impuesto_dinero)

        #Datos de salida esperados
        salario_esperado = 23080000

        #verificar la salida
        self.assertEqual(salario_calculado, salario_esperado)
    

    def test_ingresos_solo_por_auxilios(self):

        #entradas
        salario = 0
        horas_extra = 0
        bonificaciones = 0
        comisiones = 0
        auxilios = 249095
        salud = 0.04
        pension = 0.04
        impuesto_dinero = 0

        #proceso
        salario_calculado = logica_liquidador.calcular_salario(salario, horas_extra, bonificaciones, comisiones, auxilios, salud, pension, impuesto_dinero)

        #Datos de salida esperados
        salario_esperado = 249095

        #verificar la salida
        self.assertEqual(salario_calculado, salario_esperado)

    def test_salario_none(self):

        # ENTRADAS
        salario = None
        horas_extra = 0
        bonificaciones = 0
        comisiones = 0
        auxilios = 0
        salud = 0.04
        pension = 0.04
        impuesto_dinero = 0

        # Verifica que se genere una excepción
        with self.assertRaises(logica_liquidador.ErrorCampoObligatorio):
            logica_liquidador.calcular_salario(
                salario, horas_extra, bonificaciones,
                comisiones, auxilios, salud, pension, impuesto_dinero)
            
    def test_salario_tipo_invalido(self):

        # ENTRADAS
        salario = "5000000"
        horas_extra = 0
        bonificaciones = 0
        comisiones = 0
        auxilios = 0
        salud = 0.04
        pension = 0.04
        impuesto_dinero = 0

        with self.assertRaises(logica_liquidador.ErrorTipoInvalido):
            logica_liquidador.calcular_salario(
                salario, horas_extra, bonificaciones,
                comisiones, auxilios, salud, pension, impuesto_dinero)
            
    def test_salario_negativo(self):

        # ENTRADAS
        salario = -1000
        horas_extra = 0
        bonificaciones = 0
        comisiones = 0
        auxilios = 0
        salud = 0.04
        pension = 0.04
        impuesto_dinero = 0

        with self.assertRaises(logica_liquidador.ErrorSalarioNegativo):
            logica_liquidador.calcular_salario(
                salario, horas_extra, bonificaciones,
                comisiones, auxilios, salud, pension, impuesto_dinero)
            
    def test_salario_fuera_rango(self):

        # ENTRADAS
        salario = 2_000_000_000
        horas_extra = 0
        bonificaciones = 0
        comisiones = 0
        auxilios = 0
        salud = 0.04
        pension = 0.04
        impuesto_dinero = 0

        with self.assertRaises(logica_liquidador.ErrorSalarioGrande):
            logica_liquidador.calcular_salario(
                salario, horas_extra, bonificaciones,
                comisiones, auxilios, salud, pension, impuesto_dinero)
            
    def test_porcentaje_fuera_rango(self):

        # ENTRADAS
        salario = 5000000
        horas_extra = 0
        bonificaciones = 0
        comisiones = 0
        auxilios = 0
        salud = 0.30
        pension = 0.04
        impuesto_dinero = 0

        with self.assertRaises(logica_liquidador.ErrorPorcentajesFueraRango):
            logica_liquidador.calcular_salario(
                salario, horas_extra, bonificaciones,
                comisiones, auxilios, salud, pension, impuesto_dinero)


if __name__ == '__main__':
    unittest.main()