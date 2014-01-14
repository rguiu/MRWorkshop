#MapReduce con mincemeat.py workshop

Este workshop es una introducción a MapReduce de forma práctica. Para ello haremos unos cuantos ejercicios, yo dejare el esqueleto de la solución y tu tendras que completarla. Al final daré la solución que yo implementé por si tubiste algún problema.

Las secciones del Workshop seán.

1. **Introducción a MapReduce**. En la versión escrita pondré poco sobre esta sección. Basicamente explicaré un poco que es y de donde viene MapReduce aunqueno me extenderé mucho en esta parte.
2. **Algunos conceptos utiles de Python**. En principio cualquiera podria hacer este tutorial, voy a usar Python pero no es requisito imprescindible,cualquiera con conocimientos de programación podria hacer los ejemplos.
3. **Ejercicios**. Esta es la parte más interesante y cubrirá la mayor parte del tiempo del workshop. Los ejercicios consistiran en tres bloques, yo pondre un ejemplo ya resuelto y despues dejare unos cuantos problemas similares para resolver.


##El patrón Map Reduce 
Copio la definición tal cual de la página de Wikipedia en inglés

> MapReduce is a programming model for processing large data sets with a parallel, distributed algorithm on a cluster.[1]
A MapReduce program is composed of a Map() procedure that performs filtering and sorting (such as sorting students by first name into queues, one queue for each name) and a Reduce() procedure that performs a summary operation (such as counting the number of students in each queue, yielding name frequencies). The "MapReduce System" (also called "infrastructure" or "framework") orchestrates by marshalling the distributed servers, running the various tasks in parallel, managing all communications and data transfers between the various parts of the system, and providing for redundancy and fault tolerance.

> The model is inspired by the map and reduce functions commonly used in functional programming,[2] although their purpose in the MapReduce framework is not the same as in their original forms.[3] Furthermore, the key contributions of the MapReduce framework are not the actual map and reduce functions, but the scalability and fault-tolerance achieved for a variety of applications by optimizing the execution engine once.

[ver más](http://en.wikipedia.org/wiki/MapReduce)


##Herramientas de programación funcional en Python

Voy a empezar por poner algunas notas sobre Python. Es interesante para gente que no este familiarizada con Python. Si ya estás familiarizado con Python o si ya conoces estos conceptos de otros lenguajes puedes saltar a la parte donde escribo los ejemplos.

Empiezo con algunas funciones en python para la manipulación de listas:

`map(función, secuencia)`

Aplica una función a todos los elementos de una lista.

	$ python
	>>> def cube(x): return x*x*x
	...
	>>> map(cube, range(1, 11))
	[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]


`reduce(función, secuencia, valor_inicial)`

Aplica una función a todos los elementos de una lista.

	$ python
	>>> def add(x,y): return x+y
	...
	>>> reduce(add, range(1, 11))
	55

Otras funciones similares. 

`sum`,  `filter`, `zip`

Más:
<http://docs.python.org/2/tutorial/datastructures.html>

##Python iterables, generators and the keyword yield
###Iterables
Cuando iteramos sobre una lista en python llamamos a sus elementos uno a uno:

	$ python
	>>> list_of_numbers = [1, 3, 5]
	>>> for i in list_of_numbers:
	...    print i
	...
	1
	3
	5

Todo lo que podemos iterar con un for in es un iterable. A pesar de su utilidad tiene un problema y es que los iterables guardan en memoria toda la lista y esto puede ser contraproducente si la lista es muy grande. Para eso existen los generadores de los que hablamos ahora.

###Generators
Los generators son como los iterators pero estos se pueden iterar una sola vez. Esto es porque no guardan los valores en memoria sino que los generan bajo demanda:

	$ python
	>>> my_generator = (x*x for x in range(3))
	>>> for i in my_generator:
	...    print i
	...
	0
	1
	4


Como se ve en el ejemplo generator son muy similares. De hecho en el ejemplo solo se aprecia la diferencia de usar () en vez de []. Pero debemos recordar que no podemos hacer un nuevo loop for in en el generator ya que estos solo se pueden pasar una vez.

###Yield

El yield funciona de forma muy similar a un return pero en su caso devuelve un generador

	$ python
	>>> def countdown_generator(x):
	...   for i in range(x,0,-1):
	...     yield i
	...
	>>> for i in countdown_generator(3):
	...   print i
	...
	3
	2
	1

El generador es util para usar menos memoria, ademas cuesta menos inicializar que una lista iterable, por ejemplo. Pero en cada ciclo del loop tiene que efectuar las operaciones que no hizo al inicializar, así que iterar en un generador será más lento.

En este link en StackOverflow explican esto en ingles:

[http://stackoverflow.com/questions/231767/the-python-yield-keyword-explained](http://stackoverflow.com/questions/231767/the-python-yield-keyword-explained)

Y otro artículo que habla de Iterables y Generadores:

[http://www.learningpython.com/2009/02/23/iterators-iterables-and-generators-oh-my/](http://www.learningpython.com/2009/02/23/iterators-iterables-and-generators-oh-my/)

Podemos encontrar cientos de artículos que explican Iterators, Generators y Yield en profundidad con solo unos rezos a San Google.


###mincemeat.py
mincemeat.py es una implementación muy fácil de usar de MapReduce en python. [Ver su página](https://github.com/michaelfairley/mincemeatpy).

Podemos bajarnos mincemeat.py de su página o instalarlo usando easy_install:

	$ easy_install mincemeat

###Instalando el código del workshop

1. Bajarse el proyecto de github.
2. Instalar mincemeat.py con easy_install mincemeat (si no se 
3. Instalar simplejson con easy_install simplejson (vale,un poco frivolidad instalar una libreria que no es estándar).

###Los Datos
Como datos usaremos resultados de partidos de futbol de la Liga inglesa. La fuente es [http://www.football-data.co.uk/matches.php](http://www.football-data.co.uk/matches.php).

Esta colección de datos no se puede ni remotamente calificar de "BigData" pero nos sirve como ejemplo para practicar creando MapReducers.

Dentro del proyecto tendremos un directorio "data" con los datos que vamos a estudiar. Estos datos estan en ficheros csv separados por commans. El fichero data/notes.txt explica el formato de los csv.

Los datos estan en directorios data/premier/<temporada>, temporada puede ser por ejemplo **10-11**. En nuestros datos tenemos las temporadas **10-11, 11-12, 12-13** y **13-14** (hasta el momento en que me baje los ficheros que no era el final de tempoarada exactamente). Nota: los ficheros bajados directamente del site mencionado arriba tenian algunos cambios de uno a otro, los hice mas homogeneos añadiendo algunas columnas (ver: **code/load_csv.py**)

Aunque en este caso no lo hemos aplicado, una estrategia comun para organizar los ficheros en directorios por fechas. Por ejemplo: año/mes/dia/hora/minuto (puede tener más o menos profundidad) Así podemos filtrar de inicio, por ejemplo, si queremos los ficheros del marzo del 2013 podriamos mirar en 2013/marzo/\*\*, si queremos de las 14h del dia 5, podemos mirar en 2013/marzo/05/14/\*\*.
 
En nuestro caso podemos simmplemente filtrar por temporada usando esta estrategia.

##Ejemplos de MapReduce

### 1. Calculando totales(SQL SUM&COUNT)

Para empezar un ejemplo sencillo. Vamos a calcular el número de partidos en total jugados por cualquier equipo. 

Si observamos el ejemplo de mincemeat.py para contar palabras ([en el README de su página](https://github.com/michaelfairley/mincemeatpy)) podemos ver que hay algunas lineas que seran comunes cada vez que escribamos un Map Reduce con mincemeat.py.

Nota: Así dentro del proyecto en **code/01/matches_raw.py** tenemos el código que calcularia los partidos. Pero para evitar estar escribiendo el código comun en cada map reducer he estraido la parte que lee los ficheros y arranca el servidor a un fichero comun, **code/common/basemr.py**. 

El ejemplo que calcularia el número total de ataques queda como.

Ejemplo de mincemeat.py. This is in the file …… in the code provided:

    import sys
	sys.path.append('code/common')
	from basemr import *

	data_dir = 'data/premier'

	def mapfn(k, v):
    	for row in v:
        	yield 'total number of games', 1

	def reducefn(k, vs):
    	return sum(vs)

	def display(results):
    	print results

	if __name__ == "__main__":
  		mr = BaseMR(data_dir, mapfn, reducefn)
  		mr.start(display)


Para ejecutarlo:

1. Nos situamos en el directorio raiz del proyecto (esto es importante ya que he usado paths relativos).

2. En una consola arranco el servidor:

		$ python code/01/matches.py
3. En otra el cliente (esta se puede arrancar desde cualquier sitio):
 
		$ mincemeat.py -p changeme localhost

El resultado que obtengo, basandome en los datos que tenia cuando escribi esto es:

	{'total number of games': 1250}



Para experimentar un poco con Mincemeat podemos hacer lo mismo arrancando dos clientes (esto lo podriamos hacer con ejemplos con más datos, con los datos que tenemos estos se ejecutan bastante rapido y no da tiempo posiblemente a arrancar dos clientes). Debemos tener en cuenta que el servidor es quien debe acceder a los ficheros, así el path es relativo al servidor, pero el proceso se realiza en los clientes. Para verlo más claro pon un *print k* en el *mapfn* y/o en el *reducefn* y compruebalo. 

#### Ejercicios:
**Las soluciones a los ejercicios las podemos encontrar en la rama soluciones de este proyecto.**

1. Calcular el total de partidos jugados por cada equipo y mostrar los que han jugado el máximo número posible o lo que es lo mismo, encuentra los equipos que han estado estas 4 temporadas permanentemente en la premier league. **code/01/01_exercise.py**.
2. Calcular la clasificacion final de la liga 12-13. 3 puntos por victoria 1 punto por empate **code/01/02_exercise.py**.
3. Extender la solucion anterior y añadir el número de goles a favor y el número de goles en contra. **code/01/03_exercise.py**.
**Hint 1:** En el ejemplo emitimos un 1 pero podriamos emitir una tupla.
**Hint 2:** las funciones de python map, sum y zip pueden ser útiles si queremos hacer un reducer de una sola línea.
4. Vamos a mirar los datos de las apuestas. ¿Cuanto habriamos ganado o perdido si hubieramos apostado un euro al favorito en todos los partidos de la temporada 12-13? (Usamos los campos 23, 24 y 25 en el csv son las apuestas en una casa de apuestas, ignorar las otras. El empate no lo consideraremos). Si quereis podeis ver que ocurriria si se eligiera el mejor precio entre todas las casas de apuestas. Nota: Para calcular, asumimos que se apuesta 1 euro cada vez, si pierdes, pierdes 1 euro, si ganas, ganas la cuota de la apuesta, menos el euro original, por ejemplo si el precio es 1.4 y la apuesta se gana ganariamos 0.4 euros (estamos apostando por el favorito). [Aqui lo explican, mirar la explicación del formato europeo.](http://www.lasapuestasdeas.com/teoria/tipos-cuotas.html)

### Calculando el máximo número de goles a favor y en contra de cada equipo en un solo partido(SQL MAX, MIN)

El ejemplo anterior era el ejemplo más básico que podemos encontrar. Vamos a seguir con ejemplos de “sumarización numérica” y vamos a intentar buscar el máximo y el mínimo.

	import sys
	sys.path.append('code/common')
	from basemr import *
	
	data_dir = 'data/premier/12-13'	
	
	# Now the real deal
	def mapfn(k, v):
    	"""
    	Los campos 2 y 3 son los nombres de los equipos
    	Los campos 4 y 5 son los goles
    	"""
    	for row in v:
        	yield row[2], (int(row[4]), int(row[5]))
        	yield row[3], (int(row[5]), int(row[4]))
	
	def reducefn(k, vs):
    	return map(max,zip(*vs))
	
	def display(results):
    	print results
	
	if __name__ == "__main__":
  		mr = BaseMR(data_dir, mapfn, reducefn)
  		mr.start(display)


Como de costumbre ejecutamos:

Servidor:

	$ python code/02/max_min.py

Cliente:

	$ mincemeat.py -p changeme localhost


####Ejercicios
**Las soluciones a los ejercicios las podemos encontrar en la rama soluciones de este proyecto.**

1. Encontrar el mejor precio que podria haber sido pagado por un partido victoria local (columna 23), empate(24) y victoria visitante(25). Es irrelevante en este caso si se pago o no.
2. Extender la solución anterior y listar en que fecha y entre que equipos y por que resultado fué. Hint: Aunque no sea lo más óptimo, podriamos emitir en el mapper los tres posibles resultados como una tupla del valor, y una cadena de texto con la descripción del resultado (fecha y quienes jugaban y porque resultado se pagaba ese precio). Pongo la solución que me sale a mi: 26.0 pagaron el 31/12/11 por un Man United 2 Blackburn 3.
3. Considerando las columnas con los precios de una casa de apuestas, victoria local (columna 23), empate(24) y victoria visitante(25). Encontrar la posible apuesta que habria generado mas dinero. ¿Puedes tambien listar la fecha, los equipos involucrados y el resultado? Sorpresa?

### Calcular el media de goles por partido que consigue un equipo (SQL AVG)

Podria bastarnos calcular la suma de goles y el total de partidos y al final dividir el uno por el otro. Pero vamos a tener el average calculado a cada paso para mostrar otro patrón típico de Map Reduce. 

La media no es asociativa, si la media de un grupo de elementos es 2 y la media de otro grupo es 3, ¿cual es la media de los dos grupos juntos? Con esos datos no puedo saberlo, necesito saber cuantos elementos forman parte de cada grupo. Así lo que haremos es incluir el total de partidos.

Y así lo hacemos:

	import sys
	sys.path.append('code/common')
	from basemr import *
	
	data_dir = 'data/premier/'
	
	# Now the real deal
	def mapfn(k, v):
    	"""
    	Los campos 2 y 3 son los nombres de los equipos
    	Los campos 4 y 5 son los goles
    	"""
    	for row in v:
        	# la tupla tiene como primer campo la media de goles
        	# en un solo partido. Casualmente es el total de goles 
        	# de un solo partido. El segundo campo es el total
        	# de partidos, 1 en este caso
        	yield row[2], (int(row[4]), 1)
        	yield row[3], (int(row[5]), 1)
	
	def reducefn(k, vs):
    	total_num_matches = sum(v[1] for v in vs)
    	goals             = sum(v[0] * v[1] for v in vs)
    	return (goals/float(total_num_matches), total_num_matches) 
	
	def display(results):
    	# los ordeno por la media y
    	# lo presento un poco mas bonito.
    	list_of_teams = sorted(results.items(), key=lambda team: team[1], reverse=True)
    	for team in list_of_teams: 
        	print "%20s: %s" % (team[0],team[1][0])

	if __name__ == "__main__":
  		mr = BaseMR(data_dir, mapfn, reducefn)
  		mr.start(display)


Y para ejecutar, como en las veces anteriores. 

Servidor:

	$ python code/02/victories.py

Cliente:

	$ mincemeat.py -p changeme localhost

Esta vez hemos hecho un esfuerzo un poco mayor presentando los resultados.

####Ejercicios:
**Las soluciones a los ejercicios las podemos encontrar en la rama soluciones de este proyecto.**

1. Calcular la media de goles por partido por mes y año.



###Ejemplo de visualización

Voy a usar el resultado del ejercicio anterior. 
No copio el código aquí, pero mencionar que en este caso crea un CSV.  Este CSV lo mostraremos en una gráfica usando D3.js.

Servidor:

	$ python code/04/generate_csv.py

Cliente:

	$ mincemeat.py -p changeme localhost
	
Esto generara un csv con los resultados en **web/data/monthly_average.csv**

Entrar en el directorio web/ y escribir:

	$ python -m SimpleHTTPServer

En el navegador se puede acceder en: 
	
	http://localhost:8000
