# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 17:29:48 2026

@author: angie
"""

def filtrar_por_participante(df, id_participante):
    """
    Busca, en el DataFrame la(s) fila(s) del participante cuyo id es igual al id buscado.

    Parameters
    ----------
    df: DataFrame
        DataFrame con los datos de los participantes.
    id_participante : int
        Es el id del participante buscado.

    Returns
    -------
    filtrado : DataFrame
        Es el DataFrame con los datos del participante cuyo id es el igual al id buscado.
    None
        Si el id buscado no está en el DataFrame.
    Raises: 
        ValueError: Si el DataFrame está vacío.

    """
    if df.size==0:
        raise ValueError ("Error. El DataFrame se encuentra vacío")
    if id_participante not in df["id_participante"].values:
        return None
    filtrado=df[df["id_participante"]==id_participante]
    return filtrado
    
