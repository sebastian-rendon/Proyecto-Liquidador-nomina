import sys
# --- CONFIGURACIÓN DE RUTAS ---
# Se añade la carpeta 'src' al path del sistema para permitir la importación 
# de módulos internos (como 'model') desde la raíz del proyecto.
sys.path.append('src')

from model import logica_liquidador

try:
    # --- SECCIÓN: CAPTURA DE DATOS (VISTA/CONSOLA) ---
    # Se solicita la información al usuario a través de entradas de texto por consola.
    entrada_salario = input("Ingrese el valor del salario mensual: ")
    entrada_horas_extra = input("Ingrese el valor (dinero mensual) de las horas extra: ")
    entrada_bonificaciones = input("Ingrese el valor (dinero mensual) de las bonificaciones: ")
    entrada_comisiones = input("Ingrese el valor (dinero mensual) de las comisiones: ")
    entrada_auxilios = input("Ingrese el valor (dinero mensual) de los auxilios: ")

    entrada_salud = input("Ingrese el valor del porcentaje de la salud que usted paga (ademas no mayor a 4%): ")
    entrada_pension = input("Ingrese el valor del porcentaje de la pensión que usted paga (ademas no mayor a 4%): ")
    entrada_impuesto_dinero = input("Ingrese el valor (dinero mensual) de los impuestos que usted paga: ")

    # --- SECCIÓN: VALIDACIÓN DE CAMPOS OBLIGATORIOS ---
    # Se agrupan las entradas en una lista para verificar que ninguna esté vacía.
    campos = [
        entrada_salario,
        entrada_horas_extra,
        entrada_bonificaciones,
        entrada_comisiones,
        entrada_auxilios,
        entrada_salud,
        entrada_pension,
        entrada_impuesto_dinero]

    # Identificación de los índices de aquellos campos que el usuario dejó en blanco.
    indices_vacios = [i for i, valor in enumerate(campos) if valor == ""]
    
    if indices_vacios:
        # Mapeo de nombres descriptivos para generar un mensaje de error legible.
        nombres_campos = [
            "salario", 
            "horas extra", 
            "bonificaciones", 
            "comisiones", 
            "auxilios", 
            "salud", 
            "pensión", 
            "impuesto" ]
        
        # Generación del reporte de campos faltantes y lanzamiento de la excepción.
        campos_faltantes = [nombres_campos[i] for i in indices_vacios]
        raise ValueError(f"ERROR: Campos obligatorios vacíos: {', '.join(campos_faltantes)}")

    # --- SECCIÓN: PROCESAMIENTO Y MODELADO ---
    # Conversión de las entradas de texto (string) a números decimales (float).
    salario = float(entrada_salario)
    horas_extra = float(entrada_horas_extra)
    bonificaciones = float(entrada_bonificaciones)
    comisiones = float(entrada_comisiones)
    auxilios = float(entrada_auxilios)

    salud = float(entrada_salud)
    pension = float(entrada_pension)
    impuesto_dinero = float(entrada_impuesto_dinero)

    # Comunicación con el Modelo: Se crea la instancia con los datos capturados.
    # La clase LiquidacionSalario centraliza los datos de la nómina.
    liquidacion = logica_liquidador.LiquidacionSalario(
        salario= float( entrada_salario ),
        horas_extra= float( entrada_horas_extra ),
        bonificaciones= float( entrada_bonificaciones ),
        comisiones= float( entrada_comisiones ),
        auxilios= float( entrada_auxilios ),
        salud= float( entrada_salud ),
        pension= float( entrada_pension ),
        impuesto_dinero = float( entrada_impuesto_dinero ))

    # Cálculo final: Se invoca la función lógica para obtener el salario neto.
    salario_neto = logica_liquidador.calcular_salario( liquidacion )

    # --- SECCIÓN: SALIDA ---
    # Muestra el resultado final al usuario.
    print("El salario neto es:", salario_neto)

except Exception as err:
    # Captura de cualquier error durante el proceso (datos no numéricos, campos vacíos, etc.).
    print("Ocurrió un error:", err)
    print(str(err))