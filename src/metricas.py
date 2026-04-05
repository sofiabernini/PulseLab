#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:33:57 2026

@author: catalinahawes
"""

#Esto no sabemos si va o no
def calcular_promedio_senal(datos: list) -> float:

    
def calcular_maximo_senal(datos: list) -> float:

        
def calcular_minimo_senal(datos: list) -> float:
    
#Esto es lo que esta literal en la tarea
from src.utils_ecg import detectar_picos_qrs

def calcular_fc_desde_datos(datos):
    tiempos = []
    senal = []

    for d in datos:
        tiempos.append(d["tiempo"])
        senal.append(d["valor"])

    picos = detectar_picos_qrs(tiempos, senal)

    return calcular_frecuencia_cardiaca(picos)

#para hacer push origin