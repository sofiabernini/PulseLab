# -*- coding: utf-8 -*-
"""
Created on Wed May 27 21:57:43 2026

"""

import os
import matplotlib.pyplot as plt

def grafico_ECG_tiempo(datos_participante):
    """
    Genera el gráfico y determina sus características visuales.
    Asegura de forma automatizada la existencia de la carpeta 'graficos/'y guarda la imagen en formato .png antes de mostrarla.

    Parameters
    ----------
    datos_participante : DataFrame
       Es el DataFrame que contiene los datos del participante cuyo id es el id buscado.

    Returns
    -------
    None.

    """
    carpeta_destino = "graficos"
    # si no existe la carpeta, se crea automáticamente:
    os.makedirs(carpeta_destino, exist_ok=True)
    
    plt.figure(figsize=(10, 4))
    plt.plot(datos_participante["Tiempo"], datos_participante["Valor ECG"], color="blue", alpha=0.7)
    plt.title(f"Gráfico de valores de ECG - Participante {datos_participante['ID participante'].iloc[0]}")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Valor ECG")
    plt.grid(True, linestyle="--", alpha=0.6)
    
    # para guardar en formato png:
    id_actual = datos_participante['ID participante'].iloc[0]
    nombre_archivo = f"ecg_participante_{id_actual}.png"
    ruta_completa = os.path.join(carpeta_destino, nombre_archivo)
    
    # guarda el gráfico en la carpeta:
    plt.savefig(ruta_completa, dpi=300, bbox_inches='tight')
    print(f"[INFO] Gráfico exportado correctamente a: {ruta_completa}")
    
   
    plt.show()
    plt.close()