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
    datos : dict
        Diccionario con los datos de los participantes.
    id_participante : int
        Es el id del participante buscado.

    Returns
    -------
    registro : dict
        Es el diccionario con los datos del id del participante buscado.

    """
    for registro in datos: 
        if registro["id_participante"]== id_participante:
            return registro
    return None

    