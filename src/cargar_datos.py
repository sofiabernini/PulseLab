#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 13:53:32 2026

@author: victoriamochnacs
"""

def cargar_datos (ruta_archivo):
    archivo = open (ruta_archivo,"r")
    lineas = archivo.readlines()
    archivo.close()
    
    lista_participantes = []
    
    for linea in lineas:
        participante = parsear_linea (linea)
        lista_participantes.append(participante)
    return lista_participantes

def parsear_linea (linea):
    linea = linea.strip("\n")
    id_participante, tiempo, valor, fase, condicion_experimental, hit = linea.split(",")
    
    dicc_participante = {
        "ID participante": int(id_participante),
        "Tiempo": float(tiempo),
        "Valor": float(valor),
        "Fase": fase,
        "Condición": condicion_experimental,
        "Hit": int(hit)
    }
    
    return dicc_participante