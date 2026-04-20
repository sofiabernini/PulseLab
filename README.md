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
* En el archivo cargar\_datos.py, en la función cargar\_datos(ruta\_archivo) se utilizó un bloque try/except para controlar un posible error en la apertura del archivo a partir de la ruta ingresada por parámetro. Luego, utilizando la función parsear\_lineas(linea) se puede manejar el caso de tener una linea vacía. Si la linea está vacía, no se incluye dentro de la lista de participantes. Si todo el archivo está vacío (no hay ningún valor en la lista de participantes) la función cargar\_datos devuelve None.

