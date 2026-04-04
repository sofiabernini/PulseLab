# PulseLab

Proyecto grupal "PulseLab"


Autoras del proyecto:

- Sofía Belén Bernini
- Catalina Hawes
- Angelina Marengo
- Victoria Mochnacs


Descripción general del proyecto:

Este proyecto analiza la señal de electrocardiograma (ECG) registrada durante la ejecución de una tarea motora (MotionLab), con el objetivo de construir un sistema que permita procesar señales en el tiempo y extraer métricas básicas de activación fisiológica.


El programa permite:

- Leer y estructurar datos fisiológicos
- Representar una señal continua en el tiempo
- Detectar eventos relevantes en la señal
- Calcular métricas básicas de activación


El programa recibe los siguientes datos:

"id_participante":  identificador del participante. (int)
"tiempo": tiempo desde el inicio del registro. (list)
"valor": señal de ECG (en milivoltios). (list)
"fase": "baseline" o "tarea". (list)
"condicion_experimental": "competencia" o "cooperacion". (list)
"hit": evento conductual. (list)


El programa produce los siguiente resultados:

- Describe la señal fisiológica
- Detecta eventos en la señal
- Calcula frecuencia cardíaca

