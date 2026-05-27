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
    df = es un dataframe con los valores del archivo
    
    Raises:
        TyperError: si la ruta ingresada por parametro no es un string
        ValueError: si el archivo no puede convertirse a Dataframe, si existe algún error en los datos (se usa la función de validación de datos)
        FileNotFoundError: Si el archivo no se encuentra al abrirlo con la ruta de archivo ingresada por parámetro
    '''
    
#este bloque valida que la ruta de archivo sea un string
    if not isinstance (ruta_archivo, str):
        raise TypeError ("[ERROR CRÍTICO] Tipo de error encontrado: La ruta ingresada no es un string | Ubicación: función cargar_datos(ruta_archivo)")
     
#se maneja la apertura del archivo, la conversión a Dataframe, y la creación de las columnas
    try:
        df= pd.read_csv(ruta_archivo,
                        header = None, 
                        names = [
                            "ID participante",
                            "Tiempo",
                            "Valor ECG",
                            "Fase",
                            "Condicion experimental",
                            "Hit"
                        ]
                    )
        
    except FileNotFoundError:
        raise FileNotFoundError ("[ERROR CRÍTICO] Tipo de error encontrado: La ruta ingresada no es correcta para abrir el archivo | Ubicación: función cargar_datos(ruta_archivo)")
        
    except ValueError:
        raise ValueError ("[ERROR CRÍTICO] Cantidad de columnas no es correcta o no se pudo dividir en columnas el archivo")
               
    if df.size == 0:
        raise ValueError ("[ERROR CRÍTICO] Tipo de error encontrado: El archivo está vacío| Ubicación: función cargar_datos")

#validar datos dentro del Dataframe
    try:
        df = validar_datos(df)
        #no devuelve nada el dataframe (None)
    except ValueError as e:
        raise ValueError (e)
        
    
    return df
        

def validar_datos(df):
    '''
    Parameters:
    ----------
    df = es el dataframe con los datos que se deben validar
      
    Return:
    ---------
    None
    
    Raises:
    ---------
    ValueError: si cualquiera de los valores en la lista no es del valor esperado (ya sea no se puede convertir el valor al tipo de dato deseado, el valor no está en el rango, o, en el caso de los tiempos, no está ordenado de forma creciente)
    
    '''
    
#Si el archivo tiene valores tipo Nan, lanza error    
    if df.isna().sum().sum() > 0:
        raise ValueError("[ERROR CRÍTICO] Hay valores vacíos")

#validacion de IDs
    try:
        df["ID participante"] = df["ID participante"].astype(int)
    except ValueError:
        raise ValueError ("Error: ID inválido")
        
    if (df["ID participante"]<= 0).any():
        raise ValueError ("Error crítico: Hay IDs menores o iguales a 0")
        
        
#valida tiempos:
    try:
        df["Tiempo"] = df["Tiempo"].astype(float)
        
    except ValueError:
        raise ValueError ("Error crítico: El valor de tiempo no es del tipo correcto")
        
    if (df["Tiempo"]<0).any():
        raise ValueError ("Error crítico: Hay tiempos negativos")
         
#valida tiempos crecientes y raisea un ValueError si no están ordenados de forma creciente
    try:
        validar_tiempos_crecientes(df)
        
    except ValueError as e:
        raise ValueError (e)
        
#Validación de valor ECG

    try:
        df["Valor ECG"] = df["Valor ECG"].astype(float)
    except ValueError:
        raise ValueError ("Error crítico: el valor ECG es inválido")
        
#Validación de fase

    fases_validas = ["baseline", "tarea"]
    
    if ~df["Fase"].str.lower().isin(fases_validas).all():
        raise ValueError ("Error crítico: hay fases que no son del valor correcto")
        
#Validacion de condicion experimental
    condiciones_validas = ["competencia", "cooperacion"]
    
    if not df["Condicion experimental"].str.lower().isin(condiciones_validas).all():
        raise ValueError ("Error crítico: alguno de los valores de la condicion experimental no es del valor correcto")
        
#Validación de hit
    
    #if not df["Hit"].str.lower().isin(mapa_hit.keys()).all():
    if not df["Hit"].isin([True,False]).all():
    #if df["Hit"] != False and df["Hit"] != True:
        raise ValueError ("Error crítico, los valores de hit no son válidos")
        
#no hay ningún return porque es una función de validación

    return df  
        

def validar_tiempos_crecientes(df):
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
    None (no hace falta retornear nada, solo valida)
    '''
    
    for id_participante, grupo in df.groupby("ID participante"):
        
       if not grupo["Tiempo"].is_monotonic_increasing:
           raise ValueError (f"Error crítico: el participante de id: {id_participante} no tiene tiempos crecientes")
           


