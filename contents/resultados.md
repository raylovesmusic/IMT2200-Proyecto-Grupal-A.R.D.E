‎ 

### Descubrimiento
‎ 
#### ¿Cómo ha evolucionado el número de descubrimientos de exoplanetas a lo largo de los años?

‎ 
El primer gráfico a visualizar cuenta el número de exoplanetas descubiertos por año. En contraste a lo que contestamos en el inciso de motivaciones, podemos observar que al contrario de lo que pensabamos, el alza no ocurre en 2015, sino que en general hay un alza grande entre 2014 y 2016. 

Investigando un poco sobre hitos astronómicos que ocurren en estos años, lo que principalmente destaca es el desarrollo de la misión K2 de NASA, que corresponde a la segunda parte y continuación de la misión Kepler dedicada a la busqueda de exoplanetas.

<img src="https://github.com/raylovesmusic/IMT2200-Proyecto-Grupal-A.R.D.E/blob/main/output-figures/planetas-por-a%C3%B1o-histograma.png?raw=true" width=100%>  
‎ 

#### ¿Cuál es la distribución de exoplanetas según su método de detección?  
La siguiente imagen un gráfico de barra múltiple, que compara la cantidad de exoplanetas descubiertos por año, entre los años 1992 y 2015 a tramos de 5 años (1990-2025), agrupados en barras por el método de descubrimiento utilizado.

<img src="https://github.com/raylovesmusic/IMT2200-Proyecto-Grupal-A.R.D.E/blob/main/output-figures/planetas-por-a%C3%B1o-y-metodo-layeredbars.png?raw=true" width=100%>
‎

Este gráfico simula la distancia de cada exoplaneta descubierto respecto de la tierra, haciendo uso de las coordenadas celestes

<img src="https://github.com/raylovesmusic/IMT2200-Proyecto-Grupal-A.R.D.E/blob/main/output-figures/proyeccion-2d-exoplanetas-por-metodo-scatter.png?raw=true" width=100%>
‎ 
Cantidad de exoplanetas descubiertos según el método

<img src="https://github.com/raylovesmusic/IMT2200-Proyecto-Grupal-A.R.D.E/blob/main/output-figures/cantidad-exoplanetas-por-metodo-histograma.png?raw=true" width=100%>
‎ 

El siguiente gráfico, a diferencia del anterior, representa el número de registros totales de todas las observaciones de cada exoplaneta, esta vez agrupados por el telescopio utilizado. A partir de su visualización podemos observar lo siguiente: 


<img src="https://github.com/raylovesmusic/IMT2200-Proyecto-Grupal-A.R.D.E/blob/main/output-figures/proyeccion-2d-exoplanetas-por-telescopio-2014-a-2016-scatter.png?raw=true" width=100%>
‎ 

#### ¿Qué instrumentos y telescopios han sido más efectivos en la detección de exoplanetas, a qué podría deberse esto?

<img src="https://github.com/raylovesmusic/IMT2200-Proyecto-Grupal-A.R.D.E/blob/main/output-figures/cantidad-exoplanetas-por-telescopio-2014-a-2016-histograma.png?raw=true" width=100%>
‎ 

#### ¿Cuál es la distancia promedio de los exoplanetas registrados respecto a la Tierra?

Gracias a que logramos obtener la ubicación de los exoplanetas respecto de la tierra (con la tierra en el origen), ahora podemos hacer el cálculo de la distancia de cada exoplaneta registrado a la tierra tomando a cada exoplaneta como un vector y calcular el módulo para cada uno. Dado que estamos trabajando en el plano celeste bidimensional, la unidad de medida de la distancia se mide en parsecs. Por lo que aplicando la operación se obtiene:

La distancia promedio de los exoplanetas divisados hasta la fecha respecto a tierra es de <b>549.4978255518711 parsecs.</b>

‎ 

### En búsqueda del exoplaneta promedio

‎ 

Una de las incógnitas más importantes de este proyecto es poder conocer qué propiedades físicas y cualidades caracterizan a la mayoría de los exoplanetas. Por lo que buscamos a partir de los datos del Nasa Exoplanet Archive, poder crear nuestro 'exoplaneta promedio' para responder a esa pregunta. De aquí se desprenden varias otras dudas las cuales es importante esclarecer para poder encaminarnos más cerca de nuestro objetivo :

#### ¿Qué parametros definen si un planeta es similar o no a la tierra?
A continuación visualizaremos de que forma se distribuyen los datos de algunas columnas del Data Frame. Sin outliers:

<img src="https://github.com/raylovesmusic/IMT2200-Proyecto-Grupal-A.R.D.E/blob/main/output-figures/distribucion-pl_bmasse-clean-boxplot.png?raw=true" width=100%>
<img src="https://github.com/raylovesmusic/IMT2200-Proyecto-Grupal-A.R.D.E/blob/main/output-figures/distribucion-pl_rade-clean-boxplot.png?raw=true" width=100%>
<img src="https://github.com/raylovesmusic/IMT2200-Proyecto-Grupal-A.R.D.E/blob/main/output-figures/distribucion-st_rad-clean-boxplot.png?raw=true" width=100%>

Como podemos ver en estos graficos sin los outliers, las estrellas anfitrionas de los exoplanetas tienden a tener masas y radios similares a los del sol, pero los exoplanetas, en cambio, presentan una mayor variabilidad en sus temperaturas, masas y radios. Esto sugiere que los exoplanetas pueden formarse en una amplia gama de condiciones y que la diversidad de exoplanetas es mucho mayor que la de sus estrellas anfitrionas. Algo interesante que podemos ver es como en el radio de los planetas, una disminucion entre 5 y 10 radios terrestres, lo que podría indicar una transición en la composición o estructura de los exoplanetas en ese rango de tamaño.

#### ¿Qué sistemas planetarios tienen más planetas detectados, a qué se le podría atribuir esto?

De acuerdo a los gráficos se puede ver que los sistemas con mas planetas detectados, son principalmente para los que se utilizó el método "Transit" y el método "Radial_velocity", donde transit detecta varios planetas en el mismo sistema, porque analiza continuamente la variacion de la luz de una estrella. Mientras que radial velocity mide como se mueve la estrella según la fuerza gravitatoria de los planetas, por lo que los planetas mas grandes y pesados son los que detecta con mayor facillidad. Lo que explica por qué detecta menos planetas que el metodo transit.

De igual forma, para ambos métodos les es mas fácil detectar una mayor cantidad de planetas de un sistema, a diferencia de los demás.

Ademas se puede ver en el otro grafico que las misiones con mayor cantidad de planetas descubiertos son de las misiones Kepler (en azul) y Tess (en rojo), ya que estas misiones utilizan metodo transit, telescopio espacial fotométrico y Tess (Transiting Exoplanet Survey Satellite), esta diseñado para usar metodo transit.

Y K2 (en verde) es una extensión de la misión original de Kepler enfocada en exoplanetas, por lo tanto esta misión tambien usa el metodo transit.

En conclusion, se puede ver que los 10 sistemas planetarios con mayor cantidad de planetas detectados, son por uso de metodo transit el cual detecta mayor cantidad de planetas mas facilmente. (<a href="https://science.nasa.gov/resource/exoplanet-detection-radial-velocity-method/">Fuente</a>)


### Modelo de Machine Learning (Clustering)
##### ¿De qué forma podemos determinar el 'tipo' de un exoplaneta?

Para poder agrupar lo planetas, se buscó información en diferentes fuentes para establecer los parámetros que nos permitirán clasificar los planetas.

De los cuales se concluyó que los principales son el radio y la masa.

Por lo que se dividió en 6 tipos de exoplanetas de los cuales no todos son habitables, según los datos que se tienen hasta ahora y obtenidos de las fuentes especificadas a continuación.

Tipos de planetas habitables:

* Planetas Rocosos: similares a la Tierra o Marte, por lo que algunos son aptos para vivir con ciertas condiciones

* Super-Tierras: rocosos más grandes que la Tierra, por lo que aun pueden ser habitables, dependiendo de su temperatura y orbitas.

Los siguientes tipos de exoplanetas en general ya no son habitables, por poseer temperaturas extremas:

* Sub-Neptunos / Mini-Neptunos: tienen helio.

* Neptunianos: como neptuno planetas helados y gaseosos

* Gigantes Gaseosos: se componen principalmente de hidrógeno y helio, como Júpiter o Saturno.

* Enanas Marrones: muy grandes por lo que estan entre la definicion de ser planeta o estrella
  
<img src="https://github.com/raylovesmusic/IMT2200-Proyecto-Grupal-A.R.D.E/blob/main/output-figures/metodo-del-codo-clasificacion-k-means.png?raw=true" width=100%>
  
<img src="https://github.com/raylovesmusic/IMT2200-Proyecto-Grupal-A.R.D.E/blob/main/output-figures/clusters-k-means-scatter.png?raw=true" width=100%>

##### Resumen de resultados
Por lo tanto los tipos de exoplanetas mas predominantes en el dataset son los tipo "Super-tierra", son mas grandes que la tierra , lo cual corresponde a las tendencias dadas por estudios del catálogo del archivo de la NASA siendo este tipo el más común detectado hasta ahora, superando en número a los gigantes gaseosos o a los planetas rocosos del tamaño de la Tierra. (Batalha 2014; NASA Science, 2025).

Después tenemos al "Gigante gaseoso" que es un tipo de planeta de los mas comunes y finalmente los neptunionanos y enanas, lo cuales son menos ya que son menos numerosos, según las tendencias dadas por la NASA.
Los transicionales, corresponden a tipos de planetas con varias caracteristicas por lo que no es posible englobarlo en solo un tipo.

Por último El metodo crosstab valida que el clustering hizo un buen trabajo separando los datos principalmente por tamaño/masa, lo que coincide con los principales grupos en la clasificación de tipo_exoplaneta

##### ¿Que podría salir mal de este modelo?
Este modelo clasifica primero según medidas obtenidas de las diferentes bilbiografias, pero no se encontró todas las medidas de los tipo de exoplanetas y tampoco estas fueron exactas por lo que le da un rango de  error en los datos que se obtienen.

Ademas solo se seleccionaron las filas en donde se botaran los Nan de columna "pl_bmasse" y "pl_rade", que son 68 38 de masa y 32 de radio, por lo que no son tantas versus las 6045 filas, por lo que si se pierde información pero no demasiada.

Por ultimo existen planetas en donde no se puede identificar a que tipo de exoplantes corresponden, por lo que se les denominó "transicional", ya que no pretenecen a un tipo de exoplaneta especifico, por lo que eso puede afectar a los resultados que se obtienen, pero ya que no se tienen esos datos se deja como un grupo aparte, del cual finalmente no son los mas predominantes en el dataset.


#### Preguntas:
* ¿Qué parametros definen si un planeta es similar o no a la tierra y habitables? 
* ¿Que exoplanetas son habitables según lo anterior y que tipos de exoplanetas?

Para ello se busca informacion para obtener los parametros de valores refernciales de la tierra de las siguientes fuentes:

    - https://burro.astr.cwru.edu/Academics/Astr221/SolarSys/equiltemp.html
    - https://ssd.jpl.nasa.gov/planets/phys_par.html

Además se dan valores de tolerancia y weight que correspondes a valores definidos por nosotros para poder penalizar y centrar en un rango los valores de similitud de la tierra con cada exoplaneta
<img src="https://github.com/raylovesmusic/IMT2200-Proyecto-Grupal-A.R.D.E/blob/main/output-figures/exoplanets-habitable-scores-barplot.png?raw=true" width=100%>

<img src="https://github.com/raylovesmusic/IMT2200-Proyecto-Grupal-A.R.D.E/blob/main/output-figures/exoplanets-habitable-score-exo-type-barplot.png?raw=true" width=100%>

##### Resumen de resultados
Con este grafico de barras podemos ver que el tipo de exoplaneta con mayor probabilidad de habitabilidad es el rocoso/super-tierra, lo cual concuerda con la informacion, ya que la tierra es un tipo de planeta rocoso, con una superficie solida y metales, además ubicado mas cerca del sol, por lo que posee una temperatura mas elevada, necesaria para subsistir.

#### ¿Que puede salir mal?

* Se toman referencias de datos de tierra, según datos obtenidos por la fuentes descritas anteriormente
por lo que puede existir cierto sesgo en la toma de datos.
* Se toma como referencia de habitabilidad a la tierra, por que posee datos que se consideran importanes para ser habitables, pero:


_¿Que nos dice que no existan planetas que no sean similares a la tierra pero que sean potencialmente habitables?_

Lamentablemente para responder esa pregunta se necesitan más datos. Actualmente existen teorías de vida basada en diferentes condiciones a estas, pero no se tienen suficientes datos de ellas como para poder añadirlo al análisis. Por lo tanto un sesgo importante es que el modelo puede ser antropocéntrico (el tomar solo a la tierra como el estereotipo para definir si un planeta es habitable) y limitar el análisis por ello.

* Los valores de tolerancia y weight fueron definidos manualmente por lo que estos introducen un sesgo humano, ya que pequeños cambios en pesos y tolerancias pueden afectar al outcome del modelo.

* Los planetas con valores Nan son descartados, sin imputación, por lo que algunos planetas pueden tener habitabilidad 0 solo por falta de datos.

* Se tomaron en cuenta columnas que se consideran importantes para la habitabilidad pero existen otros valores importantes que no se incluyeron en el modelo, lo que afecta en la respresentacion de la habitabilidad completa del planeta. Por ejemplo las siguientes:

    * Composición atmosférica

    * Campo magnético

    * Actividad geológica

    * Radiación

    * Estabilidad orbital

    * Presencia de agua líquida 

Que a su vez bajo un buen contexto podrían contribuir a un modelo más completo y acertado.

<img src="https://github.com/raylovesmusic/IMT2200-Proyecto-Grupal-A.R.D.E/blob/main/output-figures/params-correlation-heatmap.png?raw=true" width=100%>

Gracias al heatmap, podemos ver que existe una correlacion alta entre pl_orbper (periodo orbital) y la columna "habitable_score" (probabilidad de habitabilidad), lo cual tiene sentido ya que  el periodo orbital es un indicador directo de la distancia del planeta a su estrella anfitriona, la cual es el factor más crítico para determinar la temperatura superficial del planeta y, por lo tanto, la posibilidad de que exista agua líquida.

Además podemos ver una alta correlacion de los clusters con pl_rade y pl_bmasse, pero es de esperarse ya que estos fueron usados para sacar los clusters (y hacer el modelo KMeans) se utilizó esas 2 columnas.
