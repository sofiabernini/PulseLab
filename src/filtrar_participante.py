# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 17:29:48 2026

@author: angie
"""

def filtrar_por_participante(datos, id_participante):
    """
    Busca, en la lista de diccionarios, el diccionario
    correspondiente al id ingresado

    Parameters
    ----------
    datos : lista
        lista con los datos de los participantes en diccionarios distintos.
    id_participante : int
        Es el id del participante buscado.

    Returns
    -------
    registro : dict
        Es el diccionario con los datos del id del participante buscado.
    None
        Si el id buscado no está en la lista datos.
    Errores: ValueError
        Si la lista de datos está vacía

    """
    if len(datos)==0:
        raise ValueError("La lista de datos está vacía.")
    for registro in datos: 
        if registro["ID participante"]== id_participante:
            return registro
    return None

    
