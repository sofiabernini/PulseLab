#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:33:57 2026

"""
import pandas as pd
import matplotlib.pyplot as plt
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
        TypeError: si no es valor float

    Returns
    -------
    float
        Sale el promedio de esa lista de senales.

    """
    serie = pd.Series(datos)

    if serie.empty:
        raise ValueError("[ERROR CRÍTICO] La lista está vacía.")

    return serie.mean()




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
    serie = pd.Series(datos)

    if serie.empty:
       raise ValueError("[ERROR CRÍTICO] La lista está vacía.")

    return serie.max()

        
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
    serie = pd.Series(datos)

    if serie.empty:
        raise ValueError("[ERROR CRÍTICO] La lista está vacía.")

    return serie.min()

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
    serie = pd.Series(picos)

    if len(serie) < 2:
        raise ValueError("[ERROR CRÍTICO] No hay suficientes picos.")

    tiempo_total = serie.iloc[-1] - serie.iloc[0]

    if tiempo_total == 0:
        raise ZeroDivisionError("No se puede dividir por 0.")

    frecuencia_bpm = (len(serie) / tiempo_total) * 60

    return frecuencia_bpm
    

def calcular_fc_desde_datos(datos):
   """
    Calcula la frecuencia cardíaca promedio (BPM) a partir de un DataFrame de ECG.

    La función extrae las secuencias de tiempo y señal del DataFrame, detecta 
    los picos QRS correspondientes a los latidos y calcula la frecuencia 
    cardíaca resultante en pulsos por minuto.

    Parameters
    ----------
    datos : DataFrame
        DataFrame de pandas que contiene las columnas "Tiempo" (valores float) 
        y "Valor ECG" (valores float) del participante bajo análisis.

    Returns
    -------
    float
        La frecuencia cardíaca calculada en latidos por minuto (BPM).

    Raises
    ------
    ValueError
        Si el algoritmo no logra detectar suficientes picos QRS (menos de 2) 
        para realizar el cálculo de la frecuencia.
    ZeroDivisionError
        Si el tiempo transcurrido entre el primer y último pico detectado 
        es igual a cero.
    """
   tiempos = []
   senal = []

   for d in datos["Tiempo"]:
        tiempos.append(d)

   for d in datos["Valor ECG"]:
        senal.append(d)
        
   picos = detectar_picos_qrs(tiempos, senal)

   plt.figure(figsize=(12, 5))
   plt.plot(tiempos, senal, label="Señal ECG")
   plt.scatter(picos, label="Picos QRS")
   plt.title("Señal ECG con detección de picos QRS")
   plt.xlabel("Tiempo (s)")
   plt.ylabel("Voltaje")
   plt.legend()
   plt.grid(True)
   plt.show()
   
   return calcular_frecuencia_cardiaca(picos)



