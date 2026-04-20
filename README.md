# PulseLab

Proyecto grupal "PulseLab"



Autoras del proyecto:

* Sofía Belén Bernini
* Catalina Hawes
* Angelina Marengo
* Victoria Mochnacs



Descripción general del proyecto:

Este proyecto analiza la señal de electrocardiograma (ECG) registrada durante la ejecución de una tarea motora (MotionLab), con el objetivo de construir un sistema que permita procesar señales en el tiempo y extraer métricas básicas de activación fisiológica.



El programa permite:

* Leer y estructurar datos fisiológicos
* Representar una señal continua en el tiempo
* Detectar eventos relevantes en la señal
* Calcular métricas básicas de activación



El programa recibe los siguientes datos:

"id\_participante":  identificador del participante. (int)
"tiempo": tiempo desde el inicio del registro. (list)
"valor": señal de ECG (en milivoltios). (list)
"fase": "baseline" o "tarea". (list)
"condicion\_experimental": "competencia" o "cooperacion". (list)
"hit": evento conductual. (list)



El programa produce los siguiente resultados:

* Describe la señal fisiológica
* Detecta eventos en la señal
* Calcula frecuencia cardíaca



Errores y Validaciones:

* En el programa principal, se considera y se prevee el caso en el que haya errores dentro del archivo con los datos del proyecto o que el ID que se ingrese no exista en los datos, o no sea un número entero como es pedido.
* En la función se manejaron los errores y se validaron todos los datos correspondientes para el funcionamiento del programa. Esto incluye, 1) validar el tipo de dato de la ruta ingresada por parámetro y que que el archivo abra con la ruta indicada  2) que el archivo no esté vacío, 3) que la función parsear_lineas maneje y propague errores de transformación de datos vacíos o de tipos de datos/rangos de datos 5) agregar la función validar_tiempos_crecientes para validar consistencia temporal de los participantes
* En la función filtrar_por_participante se manejaron dos posibles errores. 1) Que la lista esté vacía: si la longitud/cantidad de elementos de la lista es igual a cero, entonces se ejecuta un raise que indica que la lista está vacía. 2) Que el id buscado no esté en la lista de datos: se recorre la lista y si se encuentra un id igual al id buscado en uno de los valores de la clave ["ID participante"], entonces se devuelve el diccionario, en caso contrario se devuelve None.

