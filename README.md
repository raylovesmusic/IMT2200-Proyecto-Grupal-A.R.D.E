# IMT2200-2025-2_Proyecto_Semestral_(A.R.D.E)
## Proyecto Semestral introducción a Ciencia de Datos. 
## Integrantes:
* Agustín Pérez
* Rayén Godoy
* Dan Salgado
* Esperanza Oliva

## 🌌Análisis y Reconocimientos de Datos Exoplanetarios (A.R.D.E)
### About
Exploración de Datasets astronómicos con enfoque en los exoplanetas, con fines de divulgación científica y dirigido hacia adolescentes e infancias interesadas en la astronomía.

### Guía de Uso
El repositorio contiene las carpetas de `data`, `notebooks`, `output-figures`. Los archivos principales se encuentran en la carpeta de notebooks.
- `data`: archivos csv con los datos a analizar.
    - `Dataset PSComppars`: csv de data compuesta extraído del NASA Exoplanet Archive Planetary Systems Composite Data. Dataset Principal.
    - `exoplanets_physics_data`: csv subconjunto de PSComppars que solo contiene características orbitales y físicas de los exoplanetas. Utilizado en `simulación.py` para la simulación de las órbitas y en                                          `planet_visualizer` para mostrar una previa de el Dataset al usuario que interactua.
- `notebooks`: notebooks de investigación con carpetas `imagenes-notebook-entrega-inicial` y  `planet_viz_script`.
    - `imagenes-notebook-entrega-inicial`
    - `planet_viz_script`: Carpeta con el script de la simulación.
        - `__init__.py` : Archivo vacío que permite importar simulación.py en `planet_visualizer.ipynb`
        - `simulación.py` : Script que permite visualizar los sistemas planetarios del notebook `planet_visualizer.ipynb`
    - `notebook_principal` : Notebook principal donde se realiza la gran mayoría del proyecto. Incluye el análisis de datos, EDA, visualización de la información mediante gráficos de respaldo, aplicación de              Machine Learning y comentarios sobre la misma investigación del proyecto.
    - `planet_visualizer.ipynb` : Noteboook interactivo que permite visualizar el movimiento de los sistemas planetarios del Dataset. Su forma de uso e instrucciones se encuentran en él
- `output-figures`: Carpeta de las imágenes en formato png de todos los gráficos resultantes del análisis de Datos (outputs de `notebook_principal`.

### Notebooks
- `entrega_inicial.ipynb` : Se recomienda ejecutar este primero, y luego interactuar con la simulación
- `planet_visualizer.ipynb`

#### Listado de Datasets:
- `NASA Exoplanet Archive` : https://exoplanetarchive.ipac.caltech.edu/

#### Resumen del proyecto:
- El proyecto está compuesto por el notebook principal `entrega_inicial.ipynb`, en el cual se trabaja con los datos de exoplanetas del NASA Archive. Se hace una limpieza de los datos y se utilizan para responder preguntas de investigación que se plantean inicialmente. En cada una de estas preguntas se hace uso de gráficos para mejor análisis. Finalmente, el notebook de `planet_visualizer.ipynb` contiene un simulador de exoplanetas (utilizando los archivos dentro de `planet_viz_script`), con pasos para su uso. En la entrega final, se finaliza por completo la sección de EDA, se añade la simulación y modelos (clustering).

## Distribución de los Roles de Trabajo:

- Agustín Perez : Carga de datos inicial (creación de los DataFrames principales), creación de la función definitoria para el 'habitable_score' de un exoplaneta, contribuciones al EDA (gráficos en 2D sobre la proyección de los exoplanetas). 
- Rayén Godoy : Creación del simulador de órbita de los sistemas exoplanetarios. Contribuciones al EDA (análisis de las distribuciones de los datos y limpieza de los datos).
- Dan Salgado : Creación del README, contribuciones en el EDA. Encargado de la creación de la página web del proyecto.
- Esperanza Oliva : Implementación del modelo K-Means (Clustering) sobre la clasificación de exoplanetas según características fisicas. Contribuciones en el EDA, contribuciones en 'habitable_score' .

### Librerías
- numpy
- pandas
- MatPlotLib
- Seaborn
- Sklearn
- os
  
- Rebound
- Pygame
- collections


#### Bibliografias:

Referencias Científicas:

Fulton, B. J., & Petigura, E. (2017). The California-Kepler Survey: a gap in the radius distribution of small planets.
https://www.benjaminfulton.com/files/20170331_aspen.pdf

Chen, J., & Kipping, D. (2017). A Probabilistic Mass–Radius Relationship for Exoplanets.
https://arxiv.org/abs/1603.08614

Weiss, L., & Marcy, G. (2014). The Mass-Radius Relation for 65 Exoplanets.
https://www.researchgate.net/publication/259105987_The_Mass-Radius_Relation_Between_65_Exoplanets_Smaller_than_4_Earth_Radii

Fortney, J. et al. (2007). Planetary Structure Models for Gas Giants.
https://www.ucolick.org/~jfortney/papers/Fortney07.pdf

Burrows, A. et al. (1997). Theory and Limits of Brown Dwarfs.                                    
https://arxiv.org/abs/1008.5150

Revisited Mass‑Radius Relations for Exoplanets below 120 Earth Masses (Otegi et al., 2020)
https://arxiv.org/pdf/1911.04745

Equilibrium Temperatures of Planets 
https://burro.astr.cwru.edu/Academics/Astr221/SolarSys/equiltemp.html

Planetary Physical Parameters
https://ssd.jpl.nasa.gov/planets/phys_par.html

##
<img src="https://i.postimg.cc/LXMHqzxs/IMG_1543.png" alt="dibujo" width="200"/>

