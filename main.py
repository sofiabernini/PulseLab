"""
Created on Sun Apr  5 20:30:13 2026

@author: sofia
"""

from src.cargar_datos import cargar_datos
from src.filtrar_participante import filtrar_por_participante
from src.metricas import calcular_promedio_senal, calcular_maximo_senal, calcular_minimo_senal, calcular_fc_desde_datos

ruta = "datos/PulseLab_mock_data.csv"
todos_los_datos = None

def ejecutar_programa (id_trabajado,todos_los_datos):
    
    if todos_los_datos is not None:
        
        datos_participante = filtrar_por_participante(todos_los_datos, id_trabajado)
        
        if datos_participante == None:
            print(f"El ID {id_trabajado} no se encuentra en la lista de participantes.")
        
           
        promedio_ecg = calcular_promedio_senal(datos_participante["Valor ECG"])
                
        frecuencia_cardiaca = calcular_fc_desde_datos(datos_participante)
    
        maximo_senal = calcular_maximo_senal(datos_participante["Valor ECG"])
    
        minimo_senal = calcular_minimo_senal(datos_participante["Valor ECG"])
    
                
        print(f"Resultados del participante {id_trabajado}: ")
        print(f"Máximo de la señal ECG: {maximo_senal}")
        print(f"Mínimo de la señal ECG: {minimo_senal}")
        print(f"Promedio de la señal ECG: {promedio_ecg}")
        print(f"Frecuencia Cardíaca: {frecuencia_cardiaca} BPM")
        
    else:
        print("No se pudo proceder porque no hay datos cargados.")

try:
    todos_los_datos = cargar_datos(ruta)
except FileNotFoundError:
    print(f"Error: El archivo en {ruta} no fue encontrado.")
    
except Exception as e:
    print(f"Ocurrió un error inesperado durante la ejecución: {e}")
    

while True:
    
    id_inicial = input("¿Desea analizar todos los ID? (s/n): ").lower()

    if id_inicial == 's':
        for i in todos_los_datos:
            id_posta = i['ID participante']
            ejecutar_programa(id_posta, todos_los_datos)
        break
    
    elif id_inicial == 'n':
    
        try:
            id_a_analizar = int(input("Ingrese el ID del participante: "))
            id_trabajado = id_a_analizar
            ejecutar_programa(id_trabajado, todos_los_datos)
            break
       
        except ValueError:
            print("El ID debe ser un número entero.")
            break
        
    else:
        print("Si desea analizar todos los ID escriba 's' sino 'n'.")
