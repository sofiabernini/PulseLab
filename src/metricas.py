#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:33:57 2026

@author: catalinahawes
"""

from src.función_detectar_picos import detectar_picos_qrs


def calcular_promedio_senal(datos):
    """
    Calcula el promedio de las senales ECG

    Parameters
    ----------
    datos : list
        Ingresa una lista con senales ECG.

    Returns
    -------
    float
        Sale el promedio de esa lista de senales.

    """
    suma = 0
    cantidad = 0

    for d in datos:
        suma += d
        cantidad += 1
 
    if cantidad == 0:
        raise ValueError ("[ERROR CRÍTICO] Tipo de error encontrado: La lista esta vacia.| Ubicación: función calcular_promedio_senal")
    
    promedio = suma/cantidad

    return promedio

def calcular_maximo_senal(datos):
    """
    Calcula cual es la senal mas alta

    Parameters
    ----------
    datos : list
        Ingresa una lista con senales ECG.

    Returns
    -------
    float
        Sale el valor mas alto de la lista.

    """
    
    maximo= -999999
    
    for i in datos:
        if i > maximo:
            maximo= i
    
    if len(datos)==0:
        raise("[ERROR CRÍTICO] Tipo de error encontrado: La lista esta vacia | Ubicación: función calcular_maximo_senal")
    
    else:
        return maximo
        
def calcular_minimo_senal(datos):
    """
    Calcula cual es la senal mas baja

    Parameters
    ----------
    datos : list
        Ingresa una lista con senales ECG.

    Returns
    -------
    float
        Sale el valor mas bajo de la lista.

    """
    minimo= 999999
    
    for x in datos:
        if x < minimo:
            minimo= x
            
    
    if len(datos)==0:
        raise("[ERROR CRÍTICO] Tipo de error encontrado: La lista esta vacia | Ubicación: función calcular_maximo_senal")
    
    else:
        return minimo
    

def calcular_frecuencia_cardiaca(picos):
    """
    Calcula la frecuencia cardiaca.

    Parameters
    ----------
    picos : list
        Ingresa una lista con los segundos en los que se dieron los latidos cardiacos.

    Returns
    -------
    float
        Sale la frecuencia por minuto en la que se dieron los latidos cardiacos.

    """
    if len(picos) < 2:
        raise ("[ERROR CRÍTICO] Tipo de error encontrado: No hay suficientes datos para calcular la frecuencia | Ubicación: funcion calcular_frecuencia_cardiaca")

    tiempo_total = picos[-1] - picos[0]
    cantidad_latidos = len(picos)

    if tiempo_total == 0:
        return ("Error, porque no se puede realizar division por cero")

    
    frecuencia = cantidad_latidos / tiempo_total

    frecuencia_bpm = frecuencia * 60

    return frecuencia_bpm

def calcular_fc_desde_datos(datos):
    """
    

    Parameters
    ----------
    datos : TYPE
>>>>>>> Stashed changes
        DESCRIPTION.

    Returns
    -------
<<<<<<< Updated upstream
    float
=======
    TYPE
>>>>>>> Stashed changes
        DESCRIPTION.

    """
    tiempos = []
    senal = []

    for d in datos["Tiempo"]:
        tiempos.append(d)

    for d in datos["Valor ECG"]:
        senal.append(d)
        
    picos = detectar_picos_qrs(tiempos, senal)


    return calcular_frecuencia_cardiaca(picos)
