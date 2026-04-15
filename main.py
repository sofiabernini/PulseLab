"""
Created on Sun Apr  5 20:30:13 2026

@author: sofia
"""

from src.cargar_datos import cargar_datos
from src.filtrar_participante import filtrar_por_participante
from src.metricas import calcular_promedio_senal, calcular_maximo_senal, calcular_minimo_senal, calcular_fc_desde_datos

try:
    ruta = "datos/PulseLab_mock_data.csv"
    todos_los_datos = cargar_datos(ruta)
    
except FileNotFoundError:
    print(f"Error: El archivo en {ruta} no fue encontrado.")
    
except Exception as e:
    print(f"Ocurrió un error inesperado durante la ejecución: {e}")
    
try:
    id_a_analizar = int(input("Ingrese el ID del participante: "))
    
except TypeError:
    raise TypeError ("El ID debe ser un número entero.")


datos_participante = filtrar_por_participante(todos_los_datos, id_a_analizar)
   
promedio_ecg = calcular_promedio_senal(datos_participante)
        
frecuencia_cardiaca = calcular_fc_desde_datos(datos_participante)

maximo_senal = calcular_maximo_senal(datos_participante)

minimo_senal = calcular_minimo_senal(datos_participante)

        
print(f"Resultados del participante {id_a_analizar}: ")
print(f"Máximo de la señal ECG: {maximo_senal}")
print(f"Mínimo de la señal ECG: {minimo_senal}")
print(f"Promedio de la señal ECG: {promedio_ecg}")
print(f"Frecuencia Cardíaca: {frecuencia_cardiaca} BPM")


