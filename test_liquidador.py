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

if __name__ == '__main__':
    unittest.main()