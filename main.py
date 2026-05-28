"""
Created on Sun Apr  5 20:30:13 2026

@author: sofia
"""

import pandas as pd

from src.cargar_datos import cargar_datos
from src.filtrar_participante import filtrar_por_participante
from src.metricas import calcular_promedio_senal, calcular_maximo_senal, calcular_minimo_senal, calcular_fc_desde_datos
from src.grafico_ECG_tiempo import grafico_ECG_tiempo

def ejecutar_programa (id_trabajado,todos_los_datos):
    """
    Ejecuta el programa para todos los ID o para uno solo según lo decida el usuario.

    Parameters
    ----------
    id_trabajado : int
        ID del participante que se va a analizar
    todos_los_datos : list
        Lista con todos los datos del participante

    Returns
    -------
    None.

    """  
    try:
        datos_participante = filtrar_por_participante(todos_los_datos, id_trabajado)
    
    except ValueError as e:
        print(f"[ERROR] {e}")
        return
            
    if datos_participante is None:
        print(f"El ID {id_trabajado} no se encuentra en el DataFrame de participantes.")
        return
    
    grafico_ECG_tiempo(datos_participante)
        
    try:
        promedio_ecg = calcular_promedio_senal(datos_participante["Valor ECG"])
        maximo_senal = calcular_maximo_senal(datos_participante["Valor ECG"])
        minimo_senal = calcular_minimo_senal(datos_participante["Valor ECG"])
        frecuencia_cardiaca = calcular_fc_desde_datos(datos_participante)
        
        print(f"Resultados del participante {id_trabajado}: ")
        print(f"Máximo de la señal ECG: {maximo_senal}")
        print(f"Mínimo de la señal ECG: {minimo_senal}")
        print(f"Promedio de la señal ECG: {promedio_ecg}")
        print(f"Frecuencia Cardíaca: {frecuencia_cardiaca} BPM")
        
    except Exception as e:
        print(f"Error al procesar las métricas del participante {id_trabajado}: {e}")


#PROGRAMA PRINCIPAL:
ruta = "datos/PulseLab_mock_data.csv"
todos_los_datos = None

try:
    todos_los_datos = cargar_datos(ruta)
except FileNotFoundError:
    print(f"Error: El archivo en {ruta} no fue encontrado.")
    
except Exception as e:
    print(f"Ocurrió un error inesperado al cargar la base de datos: {e}")
    
if todos_los_datos is not None:
    while True:
        id_inicial = input("¿Desea analizar todos los ID? (s/n): ").strip().lower()

        if id_inicial == 's':
            ids_unicos = todos_los_datos["ID participante"].unique()
            
            for id_posta in ids_unicos:
                ejecutar_programa(int(id_posta), todos_los_datos)
            break
        
        elif id_inicial == 'n':
            try:
                id_a_analizar = int(input("Ingrese el ID del participante a analizar: "))
                ejecutar_programa(id_a_analizar, todos_los_datos)
                break
            except ValueError:
                print("Entrada inválida. El ID debe ser un número entero.")
        else:
            print("Opción no válida. Escriba 's' o 'n'.")