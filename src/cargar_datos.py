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
    lista_participantes : lista (de diccionarios)

    '''
    archivo = open (ruta_archivo,"r")
    lineas = archivo.readlines()
    archivo.close()
    
    lista_participantes = []
        
    for linea in lineas:
        participante = parsear_linea (linea)
        lista_participantes.append(participante)
        
    return lista_participantes

def parsear_linea (linea):
    '''
    La función recorre cada string del archivo y separa los datos para luego guardarlos en un diccionario 

    Parameters
    ----------
    linea : str. es la linea del archivo

    Returns
    -------
    dicc_participante : dicc. es un diccionario con la información de cada participante

    '''
    
    linea = linea.strip("\n")
    id_participante, tiempo, valor, fase, condicion_experimental, hit = linea.split(",")
    
    dicc_participante = {}
   
    dicc_participante ["ID participante"] = int(id_participante)
    dicc_participante ["Tiempo"] = float (tiempo)
    dicc_participante["Valor"] = float (valor)
    dicc_participante ["Fase"] = fase
    dicc_participante ["Condición"] = condicion_experimental
    dicc_participante ["Hit"] = hit
    
    return dicc_participante





