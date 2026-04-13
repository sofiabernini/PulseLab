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
    None: si el archivo no tiene lineas para parsear
    '''
    
    #validación de ruta de archivo con un bloque try/except --> esto podría obviarse, preguntar a Euge hoy o a Marcos x mail. 
    while True:
        try:
            archivo = open (ruta_archivo,"r")
        
        except FileNotFoundError:
            print ("El archivo que se quiere abrir no fue encontrado en la ruta indicada")
            ruta_archivo = input ("Ingrese una ruta de archivo existente")
            
        else:
            lineas = archivo.readlines()
            archivo.close()
            break
        
    lista_participantes = []
   
    # acá manejé la posibilidad de que la linea parseada sea None, e indiqué que no se guarde en la lista sea == a None 
    for linea in lineas:
        participante = parsear_linea (linea)
        if participante == None:
            continue
        else:
            lista_participantes.append(participante)
        
    #código que maneja el caso en el que se cree una lista vacía porque el archivo esté vacío (aunque en esta instancia no representa un error como tal)    
    
    if not lista_participantes:
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
    if linea: 
        linea = linea.strip("\n")
        id_participante, tiempo, valor, fase, condicion_experimental, hit = linea.split(",")
        
        dicc_participante = {}
       
        dicc_participante ["ID participante"] = int(id_participante)
        
        if dicc_participante ["ID participante"] not in dicc_participante:
            dicc_participante ["Tiempo"] = [float(tiempo)]
            dicc_participante["Valor"] = [float(valor)]
            dicc_participante ["Fase"] = [fase]
            dicc_participante ["Condición"] = condicion_experimental
            dicc_participante ["Hit"] = [hit]
        
        else:
            dicc_participante["Tiempo"].append(float(tiempo))
            dicc_participante["Valor"].append(float(valor))
            dicc_participante["Fase"].append (fase)
            dicc_participante["Hit"].append(hit)
    
        return dicc_participante

    else:
        return None






