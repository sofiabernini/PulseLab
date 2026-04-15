#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 13:53:32 2026

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
    try:
        archivo = open (ruta_archivo,"r")
        lineas = archivo.readlines()
        archivo.close()
        
    except FileNotFoundError:
        print ("El archivo que se quiere abrir no fue encontrado en la ruta indicada")
        return None #este no sé si es necesario ¿no era que si entraba el except ya se cortaba la función?
                    
    lista_participantes = []
   
    # acá manejé la posibilidad de que la linea parseada sea None, e indiqué que no se guarde en la lista si linea == None 
    for linea in lineas:
        dato = parsear_linea (linea)
        if dato == None:
            continue
        
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
    
    if len(lista_participantes) == 0:
        return None
    else:
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
    
    if len(linea.strip()) == 0: 
        return None
    
    linea = linea.strip("\n")
    id_participante, tiempo, valor, fase, condicion_experimental, hit = linea.split(",")
        
    dicc_participante = {
        "ID participante": int(id_participante),
        "Tiempo": [float(tiempo)],
        "Valor": [float(valor)],
        "Fase": [fase],
        "Condición": condicion_experimental,
        "Hit": [bool(hit)]}
    
    return dicc_participante






