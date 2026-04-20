#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 19:05:53 2026

@author: victoriamochnacs
"""

def cargar_datos (ruta_archivo):
    '''
    La función lee un archivo CSV y separa cada participante según su ID (int), tiempo (lista de valores float), valor (lista de valores float) y hit (lista de valores bool)

    Parameters
    ----------
    ruta_archivo : str. Es la ruta hacia el archivo en el repositorio local

    Returns
    -------
    lista_participantes : lista (de diccionarios) si tiene valores
    None: si el archivo no se puede abrir o si el archivo no tiene lineas para parsear
    '''
    #bloque try/except para evitar atrapar errores de apertura del archivo
    
    if not isinstance (ruta_archivo, str):
        raise TypeError ("La ruta ingresada no es un string")
        
    try:
        archivo = open (ruta_archivo,"r")
        lineas = archivo.readlines() #no sé cómo atajar un error de esta variable
        archivo.close()
        
    except FileNotFoundError:
        raise FileNotFoundError ("La ruta ingresada no es correcta para abrir el archivo")
               
    if len(archivo) == 0:
        raise ValueError ("El archivo no contiene lineas")
        
    lista_participantes = []
   
    # revisar esto, no sé cómo hacer para que el raise sea específico. creo que es con lo de ValueError as e
    for linea in lineas:
        try:
            dato = parsear_linea(linea)
        except ValueError as e:
            raise ValueError (f"Error: {e}")
        
        encontrado = False
        
        for participante in lista_participantes:
            if participante["ID participante"] == dato["ID participante"]:
                participante["Tiempo"].append(dato["Tiempo"][0])
                participante["Valor"].append(dato["Valor"][0])
                participante["Fase"].append(dato["Fase"][0])
                participante["Hit"].append(dato["Hit"][0])
                
                encontrado = True  
                
        if encontrado:
            lista_participantes.append(dato)
                             
    #código que maneja el caso en el que se cree una lista vacía porque el archivo esté vacío (aunque en esta instancia no representa un error como tal)    
    
   
    return lista_participantes

def parsear_linea (linea):
    '''
    La función recorre cada string del archivo y separa los datos para luego guardarlos en un diccionario 

    Parameters
    ----------
    linea : str. es la linea del archivo

    Returns
    -------
    dicc_participante : dicc. es un diccionario con la información de cada participante, y lo devuelve si la linea parseada tiene contenido
    None: si la linea parseada no tiene contenido

    '''
    
    if len(linea.strip()) == 0: #esto contempla que la linea tenga un len pero de espacios vacíos, o de tabs
        raise ValueError ("La linea está vacía")
    
    try:
        linea = linea.strip("\n")
        id_participante, tiempo, valor, fase, condicion_experimental, hit = linea.split(",")
    except ValueError:
        raise ValueError ("La cantidad de columnas no coincide con la cantidad de datos")
        
     
    try:
        dicc_participante = {
            "ID participante": int(id_participante),
            "Tiempo": [float(tiempo)],
            "Valor": [float(valor)],
            "Fase": [fase],
            "Condición": condicion_experimental,
            "Hit": [bool(hit)]}
    except (TypeError, ValueError):
        raise TypeError ("El valor no es del tipo correcto")
        
    return dicc_participante
