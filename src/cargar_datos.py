#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 13:53:32 2026

@author: victoriamochnacs
"""
    
import pandas as pd

def cargar_datos (ruta_archivo):
    '''
    La función lee un archivo CSV y separa cada participante según su ID (int), tiempo (lista de valores float), valor (lista de valores float) y hit (lista de valores bool)

    Parameters
    ----------
    ruta_archivo : str. Es la ruta hacia el archivo en el repositorio local

    Returns
    -------
    lista_participantes : lista (de diccionarios) tiene valores válidos y contiene datos.
    "El archivo que se abre con la ruta de archivo provista no contiene lineas": si el archivo no tiene lineas para parsear
    
    Raises:
        TyperError: si la ruta ingresada por parametro no es un string
        ValueError: 1) si el archivo no tiene lineas 2) si algun valor llamado por otra funcion tiene errores 3) si la lista de valores de tiempo no es válida
        FileNotFoundError: Si el archivo no se encuentra al abrirlo con la ruta de archivo ingresada por parámetro
    '''
    
#este bloque valida que la ruta de archivo sea un string
    if not isinstance (ruta_archivo, str):
        raise TypeError ("[ERROR CRÍTICO] Tipo de error encontrado: La ruta ingresada no es un string | Ubicación: función cargar_datos(ruta_archivo)")
     
#este bloque try/except maneja el error de apertura del archivo y lanza un error de tipo FileNotFoundError a la función principal
    try:
        df= pd.read_csv(ruta_archivo)
        
    except FileNotFoundError:
        raise FileNotFoundError ("[ERROR CRÍTICO] Tipo de error encontrado: La ruta ingresada no es correcta para abrir el archivo | Ubicación: función cargar_datos(ruta_archivo)")
               
    if len(df) == 0:
        raise ValueError ("[ERROR CRÍTICO] Tipo de error encontrado: El archivo está vacío| Ubicación: función cargar_datos")


#columnas esperadas

    columnas_esperadas = ["ID_participante", "Tiempo", "Valor ECG", "Fase", "Condición experimental", "Hit"].lower().strip()

    if df.columns not in columnas_esperadas:
        raise ValueError ("Las columnas no coinciden con las columnas esperadas")
    
    else:
        for columna in df.columns:
            columna.str.strip()
        
        

def validar_tiempos_crecientes(tiempos):
    '''
    Esta función valida si una lista de valores asociados al tiempo no está vacía y si sus elementos están escritos de forma creciente.

    Parameters
    ----------
    tiempos : list

    Raises
    ------
    ValueError
        La función lanza esta exception si la lista está vacía o si los tiempos no están ordenado de forma creciente

    Returns
    -------
    tiempos : list. mismo valor de entrada si es válido

    '''
    if len(tiempos) == 0:
        raise ValueError ("La lista de tiempos está vacía")
    
    for i in range (1, len(tiempos)):
        if tiempos[i] <= tiempos[i-1]:
            raise ValueError (f"Error en posición {i}: {tiempos[i]} <= {tiempos[i-1]}")   
    return tiempos



