# -*- coding: utf-8 -*-
"""
Created on Wed May 27 21:57:43 2026

@author: angie
"""

import matplotlib.pyplot as plt

def grafico_ECG_tiempo(datos_participante):
    """
    Genera el gráfico y determina sus características visuales.

    Parameters
    ----------
    datos_participante : DataFrame
       Es el DataFrame que contiene los datos del participante cuyo id es el id buscado.

    Returns
    -------
    None.

    """
    plt.figure(figsize=(10, 4))
    plt.plot(datos_participante["Tiempo"], datos_participante["Valor ECG"], color="blue", alpha=0.7)
    plt.title(f"Gráfico de valores de ECG - Participante {datos_participante['ID participante'].iloc[0]}")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Valor ECG")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()