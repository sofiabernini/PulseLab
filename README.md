# PulseLab

Proyecto grupal "PulseLab"



**Autoras del proyecto:**

* Sofía Belén Bernini
* Catalina Hawes
* Angelina Marengo
* Victoria Mochnacs



**Descripción general del proyecto:**

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



**Errores y Validaciones:**

* En el programa principal (main.py), se considera y se prevee el caso en el que haya errores dentro del archivo con los datos del proyecto o que el ID que se ingrese no exista en los datos, o no sea un número entero como es pedido.
* En las funciones de cargar\_datos.py se manejaron los errores y se validaron todos los datos correspondientes para el funcionamiento del programa. Esto incluye, 1) validar el tipo de dato de la ruta ingresada por parámetro y que que el archivo abra con la ruta indicada (función cargar\_datos) 2) que el archivo no esté vacío (cargar\_datos), 3) que la función parsear\_lineas maneje y propague errores de transformación de datos vacíos o de tipos de datos/rangos de datos 5) agregar la función validar\_tiempos\_crecientes para validar consistencia temporal de los participantes
* En la función filtrar\_por\_participante se manejaron dos posibles errores. 1) Que la lista esté vacía: si la longitud/cantidad de elementos de la lista es igual a cero, entonces se ejecuta un raise que indica que la lista está vacía. 2) Que el id buscado no esté en la lista de datos: se recorre la lista y si se encuentra un id igual al id buscado en uno de los valores de la clave \["ID participante"], entonces se devuelve el diccionario, en caso contrario se devuelve None.
* En las funcion calcular\_promedio\_senal, calcular\_maximo\_senal y calcular\_minimo\_senal se manejaron 3 posibles errores (en las 3 se manejaron los mismos errores, porque ingresan por parametro la misma lista de datos). 1) Que no haya un participante: es decir si la datos = None. 2) Que la lista no este vacia: que la lista de datos tenga por lo menos 1 valor, porque eso ademas va a prevenir que se realice una division por 0 (porque por cada valor de la lista se suma '1' a la variable que va a ser el divisor). 3) Que el tipo de dato, de cada elemento de la lista sea float y no str.
* En la funcion calcular\_frecuencia\_cardiaca se manejaron 2 posibles errores. 1) Que la lista tenga por lo menos 2 elementos, porque sino no se puede cauclar la funcion. 2)Que el tipo de valor ingresado sea float y no str.



**Objetos que se podrían utilizar:**
1)
Objeto:

* Participante: guarda la informacion sobre los pacientes

Atributos:

* ID
* Tiempo
* Valor
* Fase
* Condición
* Hit

Metodos:

* obtener\_metricas(): llama a los datos de los archivos para devolver un resumen de los resultados del participante.
* es\_valido(): verifica si el participante tiene datos suficientes para ser analizado.
2. 

Objeto:

* ManejoDeDatos: se encarga de la interacción con el sistema de archivos (entrada/salida).

Atributos:

* ruta\_archivo: ubicación del archivo CSV.
* Participante (objeto 1)

Métodos:

* cargar\_desde\_csv(): lee el archivo y transforma cada fila o grupo de filas en un objeto de la clase Participante.
* buscar\_por\_id(id): filtra en la lista de objetos y devuelve la instancia del Participante correspondiente.



**Implementación de la librería Pandas:**

La implementación de Pandas serviría para simplificar el código del programa. Por ejemplo, se podría reemplazar el almacenamiento de datos original por un DataFrame. En este caso, al cargar el archivo de datos de PulseLab, Pandas asignaría los tipos de datos a las 5 columnas correspondientes (Tiempo, Valor ECG, Fase, Condición experimental y Hit) por cada fila correspondiente a un id_participante. De esta manera, el acceso a los datos podría ser por medio de indexación lógica (retornando valores booleanos) en vez de por bucles.



Además, en el caso de que se implementara Pandas, también se modificarían las siguientes funciones:



* src/cargar\_datos.py:

-Se modificaría la función cargar_datos para reemplazar la apertura de archivos (método Open) y el procesamiento línea por línea por una única instrucción: pd.read_csv(ruta_archivo). Dentro de la instrucción se incluirían las columnas que habría que asignarle al archivo.

-La validación de la ruta de archivo se mantendría igual y la del tamaño del archivo (que contenga datos) cambiaría levemente, utilizando la linea if df.size == 0. 

-Se eliminaría por completo la función parsear_linea, ya que Pandas resuelve el split por comas. En todo caso, podría validarse la cantidad de columnas con el try anterior y, a su vez, implementar una función de validacion de datos, que analice si cada dato corresponde al tipo y rango correcto, y si no es así, que lance un error. 

-La forma de validación de los tiempos crecientes depende estrictamente del diseño de programa y lo que se quiera obtener:

    -Por un lado, si el error del orden de los tiempos no afecta qué datos se obtuvieron, podría pensarse en reordenar los datos con una linea de código que ordene los valores del tiempo (y el resto de datos asociados) de cada participante de menor a mayor. Primero deberían dividirse los participantes según su id con el método .groupby(id_participante), definiendo la variable “grupos” para esa linea (df.groupby(“id_participante”)) Luego, con un for id_participante, grupo in grupos, se puede utilizar el método .sort_values() (grupo.sort_values(“tiempo”). 

    -Por otro lado, si se considera que un error en el orden de los tiempos pudo haber afectado la calidad de los datos del CSV, se debería utilizar la misma estructura del .groupby() y el for, pero se debería utilizar un condicional que pregunte if not tiempos.is_monotonic_increasing, y que haga un raise si se cumple la condición.

-El return de la función cambiaría y, en lugar de devolver una lista de diccionarios, devolvería un DataFrame.



* src/filtrar\_participante.py (filtrar\_por\_participante):

\-Recibiría el DataFrame, en lugar de la lista de diccionarios, con los datos de los participantes. 

\-Se utilizaría el método de máscaras booleanas en lugar de la búsqueda secuencial con bucle for. 



* &#x20;src/metricas.py:

\-En las funciones calcular\_promedio\_senal, maximo y minimo, se dejarían de usar acumuladores para directamente usar los métodos .mean(), .max() y .min() sobre la serie de Pandas.

\-En calcular\_fc\_desde\_datos, se sacarían los bucles iterativos encargados de armar las listas independientes, extrayendo y enviando las columnas de tiempo y señal directamente al algoritmo de detección de picos.

