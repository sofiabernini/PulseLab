# -*- coding: utf-8 -*-
"""
Created on Wed May 27 21:57:43 2026

@author: angie
"""

import matplotlib.pyplot as plt
def grafico_ECG_tiempo(datos_participante):
    plt.figure()
    plt.plot(datos_participante["Tiempo"], datos_participante["Valor ECG"])
    plt.title("Gráfico de valores de ECG en función del tiempo")
    plt.show