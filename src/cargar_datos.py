#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 13:53:32 2026

@author: victoriamochnacs
"""
    

def cargar_datos (ruta_archivo):
    '''
    La función lee un archivo CSV y separa cada participante según su ID (int), tiempo (lista de valores float), valor (lista de valores float) y hit (lista de valores bool)

    Parameters
    ----------
    ruta_archivo : str. Es la ruta hacia el archivo en el repositorio local

    Returns
    -------
    lista_participantes : lista (de diccionarios) si tiene valores
    None: si el archivo no se puede abrir o si el archivo no tiene lineas para parsear
    
    Raises:
        TyperError: si la ruta ingresada por parametro no es un string
        ValueError: 1) si el archivo no tiene lineas 2) si algun valor llamado por otra funcion tiene errores 3) si la lista de valores de tiempo no es válida
        FileNotFoundError: Si el archivo no se encuentra al abrirlo con la ruta de archivo ingresada por parámetro
    '''
    
#este bloque valida que la ruta de archivo sea un string
    if not isinstance (ruta_archivo, str):
        raise TypeError ("[ERROR CRÍTICO] Tipo de error encontrado: La ruta ingresada no es un string | Ubicación: función cargar_datos(ruta_archivo)")
     
#este bloque try/except maneja el error de apertura del archivo y lanza un error de tipo FileNotFoundError a la función principal
    try:
        archivo = open (ruta_archivo,"r")
        lineas = archivo.readlines() #no sé cómo atajar un error de esta variable
        archivo.close()
        
    except FileNotFoundError:
        raise FileNotFoundError ("[ERROR CRÍTICO] Tipo de error encontrado: La ruta ingresada no es correcta para abrir el archivo | Ubicación: función cargar_datos(ruta_archivo)")
               
    if len(lineas) == 0:
        raise ValueError ("[ERROR CRÍTICO] Tipo de error encontrado: El archivo no contiene lineas | Ubicación: función cargar_datos (ruta_archivo)")
        
    lista_participantes = []
   
# este bloque "recibe" los raises de la función de parsear_lineas y lanza una excepcion al programa principal si algún dato viene con un error (además de especificarlo)
    for linea in lineas:
        try:
            dato = parsear_linea(linea)
        except ValueError as e:
            raise ValueError (f"Error en parseado de linea: {e}")
        
        encontrado = False
        
        for participante in lista_participantes:
            if participante["ID participante"] == dato["ID participante"]:
                participante["Tiempo"].append(dato["Tiempo"][0])
                participante["Valor ECG"].append(dato["Valor"][0])
                participante["Fase"].append(dato["Fase"][0])
                participante["Hit"].append(dato["Hit"][0])
                
                encontrado = True  
                
        if not encontrado:
            lista_participantes.append(dato)
            
#este bloque maneja el error de una lista que no está ordenada de forma creciente o esté vacía   
    for participante in lista_participantes:
        try:
            participante["Tiempo"] = validar_tiempos_crecientes(participante["Tiempo"])
        except ValueError as e:
            raise ValueError(f"[ERROR CRÍTICO] Tipo de error encontrado: Error en tiempos del participante {participante['ID participante']}: {e} | Ubicación: función cargar_datos(ruta_archivo) ")
    
   
    return lista_participantes

def parsear_linea (linea):
    '''
    La función recorre cada string del archivo y separa los datos para luego guardarlos en un diccionario 

    Parameters
    ----------
    linea : str. es la linea del archivo

    Raises
    ----------
    ValueError
        La función lanza este tipo de exception si 1) la linea está vacía 2) no se puede desempaquetar los valores según la cantidad de columnas 
        3)si el valor de tiempo, valor ECG, fase, condicion experimental y/o hit están vacíos, no son del tipo correcto o no son del rango correcto
    
    
    Returns
    -------
    dicc_participante : dicc. es un diccionario con la información de cada participante, y lo devuelve si la linea parseada tiene contenido

    '''
    
#esto contempla que la linea tenga un len pero de espacios vacíos, o de tabs
    if len(linea.strip()) == 0: 
        raise ValueError ("La linea está vacía")
    
#esto maneja el error de que los valores de las lineas no coincidan con la cantidad de columnas
    try:
        linea = linea.strip("\n")
        id_participante, tiempo, valor, fase, condicion_experimental, hit = linea.split(",")
    except ValueError:
        raise ValueError ("La cantidad de columnas no coincide con la cantidad de datos")
        
#creo el diccionario del participante vacío
    dicc_participante = {}
    
    
#estos if y try except validan el valor de id_participante. si el valor es correcto, se crea la clave y el valor asociado
    if id_participante.strip() == "":
        raise ValueError ("[ERROR CRÍTICO] Tipo de error encontrado: El valor de id del participante está vacío | Ubicación: función parsear_lineas(linea)")
    
    try:
        id_participante = int(id_participante)
    except ValueError:
        raise ValueError("[ERROR CRÍTICO] Tipo de error encontrado: El id del participante no es un número | Ubicación: función parsear_lineas(linea)")
    
    if id_participante <= 0:
        raise ValueError ("[ERROR CRÍTICO] Tipo de error encontrado: ID debe ser mayor a 0 | Ubicación: función parsear_lineas(linea)")
        
    dicc_participante["ID participante"] = id_participante
    
#estos if y try validan el valor de tiempo. si el valor es correcto, se crea la clave y el valor asociado
    if tiempo.strip() == "":
        raise ValueError ("[ERROR CRÍTICO] Tipo de error encontrado: Valor de tiempo vacío | Ubicación: función parsear_lineas(linea)")
    try:
        tiempo = float(tiempo)
    except ValueError:
        raise ValueError ("[ERROR CRÍTICO] Tipo de error encontrado: El valor de tiempo no es del tipo correcto (float o str que pueda convertirse a float) | Ubicación: función parsear_lineas(linea)")
    
    if tiempo < 0:
        raise ValueError ("[ERROR CRÍTICO] Tipo de error encontrado: El valor del tiempo no puede ser menor a 0 | Ubicación: función parsear_lineas(linea)")
    
    dicc_participante["Tiempo"]=[tiempo]
   
#estos if y try validan el valor ECG. si el valor es correcto, se crea la clave y el valor asociado
    if valor.strip() == "":
        raise ValueError ("[ERROR CRÍTICO] Tipo de error encontrado: Valor de ECG vacío | Ubicación: función parsear_lineas(linea)")
    
    try:
        valor = float(valor)
    except ValueError:
        raise ValueError ("[ERROR CRÍTICO] Tipo de error encontrado: Valor de ECG no es del tipo correcto | Ubicación: función parsear_lineas(linea)")
    
    dicc_participante["Valor ECG"] = [valor]
        
#  ---- acá faltaría un if para validar el rango porque no tengo los valores de rango ---

#estos if validan el valor de la variable 'fase'. si el valor es correcto, se crea la clave y el valor asociado
    if fase.strip() == "":
        raise ValueError ("[ERROR CRÍTICO] Tipo de error encontrado: La variable 'fase' está vacía  | Ubicación: función parsear_lineas(linea)")
    
    if fase.lower() != "tarea" and fase.lower() != "baseline":
        raise ValueError ("[ERROR CRÍTICO] Tipo de error encontrado: La variable 'fase' no tiene el valor correspondiente a 'baseline' o 'tarea' | Ubicación: función parsear_lineas(linea)")
 
    dicc_participante["Fase"] = [fase]

#estos if validan el valor de la variable 'condicion_experimental'. si el valor es correcto, se crea la clave y el valor asociado
    if condicion_experimental.strip == "":
        raise ValueError ("[ERROR CRÍTICO] Tipo de error encontrado: La variable 'condicion_experimental' está vacía  | Ubicación: función parsear_lineas(linea)")
    
    if condicion_experimental.lower != "competencia" and condicion_experimental.lower() != "cooperacion":
        raise ValueError ("[ERROR CRÍTICO] Tipo de error encontrado: La variable 'condicion_experimental' no tiene el valor correspondiente a 'cooperación' o 'competencia' | Ubicación: función parsear_lineas(linea)")
        
    dicc_participante["Condicion experimental"] = condicion_experimental
    
#estos if validan el valor de hit y lo transforman en booleano. si el valor es correcto, se crea la clave y el valor asociado
    if hit.strip() == "":
        raise ValueError ("[ERROR CRÍTICO] Tipo de error encontrado: El valor de la variable 'hit' está vacío | Ubicación: función parsear_lineas(linea)")
    if hit.lower() == "true":
        hit = True
    elif hit.lower() == "false":
        hit = False
    else:
        raise ValueError ("[ERROR CRÍTICO] Tipo de error encontrado: La variable 'hit' no tiene valor correspondiente a 'true' o 'false'  | Ubicación: función parsear_lineas(linea)")
        
    dicc_participante["Hit"] = [hit]
        
    return dicc_participante


def validar_tiempos_crecientes(tiempos):
    '''
    Esta función valida si una lista de valores asociados al tiempo no está vacía y si sus elementos están escritos de forma creciente.

    Parameters
    ----------
    tiempos : list

    Raises
    ------
    ValueError
        La función lanza esta exception si la lista está vacía o si los tiempos no están ordenado de forma creciente

    Returns
    -------
    tiempos : list. mismo valor de entrada si es válido

    '''
    if len(tiempos) == 0:
        raise ValueError ("La lista de tiempos está vacía")
    
    for i in range (1, len(tiempos)):
        if tiempos[i] <= tiempos[i-1]:
            raise ValueError (f"Error en posición {i}: {tiempos[i]} <= {tiempos[i-1]}")   
    return tiempos



