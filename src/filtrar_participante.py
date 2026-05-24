# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 17:29:48 2026

@author: angie
"""

def filtrar_por_participante(df, id_participante):
    """
    Busca, en el Data

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
    Raises: 
        ValueError: Si la lista de datos está vacía

    """
    
    filtrado=df[df["id_participante"]==id_participante]
    return filtrado
    
