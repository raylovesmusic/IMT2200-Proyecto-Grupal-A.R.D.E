### Metodología para el manejo de datos

Para abordar el estudio de la habitabilidad y diversidad exoplanetaria, se diseñó un flujo de trabajo de Ciencia de Datos reproducible en Python (mediante Jupyter Notebook). 

El procedimiento inicia desde la extracción de datos del NASA Exoplanet Archive (Composite Data), seguida de una etapa de transformación y limpieza. Posteriormente, se realiza el Análisis Exploratorio (EDA) para identificar tendencias temporales y correlaciones astrofísicas entre las propiedades de los planetas. 

Finalmente, se aplican algoritmos de aprendizaje no supervisado, específicamente un modelo de Clustering (K-Means), para intentar segmentar los exoplanetas según sus características y detectar análogos terrestres.

### Planteamiento de preguntas de análisis:
* ¿Cómo ha evolucionado el número de descubrimientos de exoplanetas a lo largo de los años?

* ¿Cuál es la distribución de exoplanetas según su método de detección?

* ¿Qué instrumentos y telescopios han sido más efectivos en la detección de exoplanetas, a qué podría deberse esto?

* ¿Cuál es la distancia promedio de los exoplanetas registrados respecto a la Tierra?

* ¿Qué sistemas planetarios tienen más planetas detectados, a qué se le podría atribuir esto?

* ¿Qué caracteristicas son las que predominan para cada tipo de exoplaneta, cuál o cuales son los exoplanetas 'más comúnes'? (clustering)

* ¿Que exoplanetas poseen características o condiciones similares a la tierra? (clustering)

### Preguntas que surgieron en el camino:
* ¿En que afecta la composición de una estrella anfitriona en la formación de exoplanetas?
* ¿De qué forma podemos determinar el 'tipo' de un exoplaneta?
* ¿Qué parametros definen si un planeta es similar o no a la tierra?
