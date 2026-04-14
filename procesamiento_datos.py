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
        Lista de diccionarios con los datos de los participantes.
    id_participante : int
        Es el id del participante buscado.

    Returns
    -------
    registro : dict
        Es el diccionario con los datos del id del participante buscado.
    None
        Si el id buscado no se encuentra en la lista de diccionarios.

    """
    if datos==None: 
        return "La lista está vacía" #hacer un raise aca tambien
    try: 
        for registro in datos:  
            if registro["id_participante"]== id_participante: 
                return registro
        return None
    except ValueError:
        return "Debe ingresar un id válido" #hacer unn raise para valueerror

    