# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:30:13 2026

@author: sofia
"""

from src.carga_datos import cargar_datos
from src.procesamiento_datos import filtrar_datos
from src.metricas import calcular_promedio_senal, calcular_fc_desde_datos

ruta = "datos/datos_proyecto.csv"
    
todos_los_datos = cargar_datos(ruta)
    
# Seleccionamos un participante específico para el análisis 
id_objetivo = 1
datos_participante = filtrar_datos(todos_los_datos, id_objetivo)
   
if datos_participante:
   promedio_ecg = calcular_promedio_senal(datos_participante["valor"])
        
   frecuencia_cardiaca = calcular_fc_desde_datos(datos_participante)
        
   print(f"Resultados del participante {id_objetivo}: ")
   print(f"Promedio de la señal ECG: {promedio_ecg}")
   print(f"Frecuencia Cardíaca: {frecuencia_cardiaca:} BPM")
else:
    print(f"No se encontraron datos para el participante {id_objetivo}.")
