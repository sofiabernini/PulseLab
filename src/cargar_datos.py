#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 13:53:32 2026

@author: victoriamochnacs
"""

def cargar_datos (ruta_archivo):
    archivo = open ("datos.csv","r")
    lineas = archivo.readlines()
    archivo.close()
    
    for linea in lineas:
        return linea

def parsear_linea (linea):
    linea = linea.split(",")
    linea = linea.strip ("/n")
    lista_participantes = []
    dicc_participante = {}
    lista_tiempo = []
    lista_valores = []
    for id_participante, tiempo, valor, fase, condicion_experimental, hit in linea:
        dicc_participante["ID participante"] = id_participante
        lista_tiempo.append (tiempo)
        dicc_participante["Tiempo"] = lista_tiempo
        lista_valores.append (valor)
        dicc_participante ["Valor"] = lista_valores
        dicc_participante["Fase"] = fase
        dicc_participante ["Condición"] = condicion_experimental
        dicc_participante["Hit"] = hit
        
    lista_participantes.append (dicc_participante)
    
