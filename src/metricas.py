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
        
    Raises:
        ValueError: si la lista esta vacia
        ValueError: si no hay lista de participantes
        TypeError: si no es valor float

    Returns
    -------
    float
        Sale el promedio de esa lista de senales.

    """
    suma = 0
    cantidad = 0
    
    if datos == None:
        raise ValueError ("[ERROR CRÍTICO] Tipo de error encontrado: No existe el participante.| Ubicación: función calcular_promedio_senal")
     
    if len(datos) == 0:
        raise ValueError ("[ERROR CRÍTICO] Tipo de error encontrado: La lista esta vacia.| Ubicación: función calcular_promedio_senal")
    
       
    try:
        for d in datos:
            suma += d
            cantidad += 1
            promedio = suma/cantidad
    
    except TypeError:
        raise TypeError("[ERROR CRÍTICO] Tipo de error encontrado: No pueden realizarse las operaciones porque alguno de los valores empleados no es un float | Ubicación: función calcular_promedio_senal.")
        
    except ZeroDivisionError:
        raise ZeroDivisionError ("[ERROR CRÍTICO] Tipo de error encontrado: No se puede dividir por 0 | Ubicación: función calcular_promedio_senal")
        
    else:
        return promedio
    
    
def calcular_maximo_senal(datos):
    """
    Calcula cual es la senal mas alta

    Parameters
    ----------
    datos : list
        Ingresa una lista con senales ECG.
    
    Raises:

        ValueError: si la lista esta vacia
        TypeError: si no es valor float

    Returns
    -------
    float
        Sale el valor mas alto de la lista.

    """
    

    maximo= -999999

    if maximo == None:
        raise ValueError("[ERROR CRÍTICO] Tipo de error encontrado: La lista esta vacia | Ubicación: función calcular_maximo_senal")

    for i in datos:
        if i > maximo:
            maximo= i
    
    if len(datos)==0:
        raise("[ERROR CRÍTICO] Tipo de error encontrado: La lista esta vacia | Ubicación: función calcular_maximo_senal")

    for i in datos:
        try:

    maximo= datos[0]
    
    if len(datos)==0:
        raise ValueError("[ERROR CRÍTICO] Tipo de error encontrado: La lista esta vacia | Ubicación: función calcular_maximo_senal")
  
    try:
        for i in datos:
            if i > maximo:
                maximo= i
        
    except ValueError:
        raise TypeError("[ERROR CRÍTICO] Tipo de error encontrado: El valor de la lista que se busca comparar no es del tipo correcto.| Ubicación: función calcular_maximo_senal ")
    
    return maximo
        
def calcular_minimo_senal(datos):
    """
    Calcula cual es la senal mas baja

    Parameters
    ----------
    datos : list
        Ingresa una lista con senales ECG.
    
    Raises:
        ValueError: si la lista esta vacia
        TypeError: si no es valor float
        
    Returns
    -------
    float
        Sale el valor mas bajo de la lista.

    """

    minimo= None
    raise ("[ERROR CRÍTICO]: Tipo de error encontrado: La lista esta vacia | Ubicación: función cargar_minimo_senal")os:

    minimo= 999999

    
    for i in datif minimo == None: 
        try:
            if i < minimo:
            maximo= i
        
        except:
            raise TypeError("No esta en float")
    

    return minimo

    if len(datos)==0:
        raise("[ERROR CRÍTICO] Tipo de error encontrado: La lista esta vacia | Ubicación: función calcular_maximo_senal")
    
    else:
        return minimo


    minimo= datos[0]

    if len(datos) == 0:
        raise ValueError ("[ERROR CRÍTICO]: Tipo de error encontrado: La lista esta vacia | Ubicación: función cargar_minimo_senal")
        
    try:
        for i in datos: 
            if i < minimo:
                minimo = i
        
    except TypeError:
        raise TypeError("[ERROR CRÍTICO]: Tipo de error encontrado:| Ubicación: función cargar_minimo_senal")
        
    else:
        return minimo


    

def calcular_frecuencia_cardiaca(picos):
    """
    Calcula la frecuencia cardiaca.

    Parameters
    ----------
    picos : list
        Ingresa una lista con los segundos en los que se dieron los latidos cardiacos.
    
    Raises:
        ValueError: si la lista no tiene los suficientes atributos
        ZeroDivisionError: no se puede dividir por 0
        
    Returns
    -------
    float
        Sale la frecuencia por minuto en la que se dieron los latidos cardiacos.

    """
    
    if len(picos) < 2:
        raise ValueError("[ERROR CRÍTICO] Tipo de error encontrado: No hay suficientes datos para calcular la frecuencia | Ubicación: funcion calcular_frecuencia_cardiaca")

    tiempo_total = picos[-1] - picos[0]
    cantidad_latidos = len(picos)

    if tiempo_total == 0:
        raise ValueError ("[ERROR CRÍTICO] Tipo de error encontrado: No se puede dividir por 0 | Ubicación: funcion calcular_frecuencia_cardiaca")

       
    frecuencia = cantidad_latidos / tiempo_total

    frecuencia_bpm = frecuencia * 60

    return frecuencia_bpm

def calcular_fc_desde_datos(datos):
   """
    

    Parameters
    ----------
    datos : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
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
