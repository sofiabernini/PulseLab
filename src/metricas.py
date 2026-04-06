#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:33:57 2026

@author: catalinahawes
"""

from src.utils_ecg import detectar_picos_qrs


def calcular_promedio_senal(datos: list) -> float:
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
        return 0
    
    promedio= suma/cantidad

    return promedio

def calcular_maximo_senal(datos: list) -> float:
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
    
    maximo= None
    
    for i in datos:
        if i > maximo:
            maximo= i
    
    return maximo
        
def calcular_minimo_senal(datos: list) -> float:
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
    minimo= None
    
    for x in datos:
        if x < minimo:
            minimo= x
            
    return minimo


def calcular_frecuencia_cardiaca(picos: list) -> float:
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
        return 0

    tiempo_total = picos[-1] - picos[0]
    cantidad_latidos = len(picos)

    if tiempo_total == 0:
        return 0

    
    frecuencia = cantidad_latidos / tiempo_total

    frecuencia_bpm = frecuencia * 60

    return frecuencia_bpm


def calcular_fc_desde_datos(datos: list) -> float:
    """
    Calcula la frecuencia cardíaca directamente desde los datos crudos.

    Parameters
    ----------
    datos : list
        DESCRIPTION.

    Returns
    -------
    float
        DESCRIPTION.

    """
    tiempos = []
    senal = []

    for d in datos:
        tiempos.append(d["tiempo"])
        senal.append(d["valor"])

    picos = detectar_picos_qrs(tiempos, senal)

    return calcular_frecuencia_cardiaca(picos)