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
        id_p = participante ["ID participante"]
        encontrado = False
    
        for p in lista_participantes:
            if p["ID participante"] == id_p:
                p["Tiempo"].append(participante["Tiempo"])
                p["Valor"].append (participante ["Valor"])
                p["Hit"].append(participante["Hit"])
                encontrado = True
                break
        if not encontrado:
            nuevo = { "ID participante": id_p,
                "Tiempo": [participante["Tiempo"]],
                "Valor": [participante["Valor"]],
                "Fase": participante["Fase"],
                "Condición": participante["Condición"],
                "Hit": [participante["Hit"]]
                }
            lista_participantes.append(nuevo)
        
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
    
    dicc_participante = {
        "ID participante": int(id_participante),
        "Tiempo": float(tiempo),
        "Valor": float(valor),
        "Fase": fase,
        "Condición": condicion_experimental,
        "Hit": hit
    }
    
    return dicc_participante





