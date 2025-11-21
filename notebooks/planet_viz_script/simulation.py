import pygame
import pygame.gfxdraw
import rebound as rb

import pandas as pd
import numpy as np
from random import choice
from os.path import join
from collections import deque

#DATA
ruta = join('..', 'data', 'exoplanets_physics_data.csv')
data = pd.read_csv(ruta).set_index('rowid').sort_values(by='hostname', ignore_index=True)

#CONSTANTES DISPLAY
ALTO, LARGO = 860, 860 #DIM pantalla
BLANCO  = (255, 255, 255) #RGB
NEGRO = (0, 0, 0) #RGB
STELLA = (200, 254, 255) #estela
STAR = (255, 255, 150)
PALETTE = [
    (100, 149, 237), (205, 92, 92),  
    (240, 230, 140), (255, 165, 0),
    (176, 196, 222), (0, 255, 255),
    (188, 143, 143),(147, 112, 219)
]

#CONSTANTES ESCALARES
QTY_DISPLAY = 2 # mejora la calidad
ESCALA = 250 # Escala los planetas al tamaño de la pantalla
TIMESTEP = 0.0001  # cada frame se actualizará por día
EARTHS_TO_SUNS = 332946.05 #transforma masa en tierras a masa en soles (para los exoplanetas)

#TRAILLING
cola = {} #trailling de los planetas
LARGO_COLA = 150

def planet_soft_finish(superficie, color, x, y, radio):
    x, y, radio = int(x), int(y), int(radio)
    
    pygame.gfxdraw.filled_circle(superficie, x, y, radio, color)
    pygame.gfxdraw.aacircle(superficie, x, y, radio, color)

class DataManager:
    def __init__(self, DataFrame : pd.DataFrame, host = None):
        self.df = DataFrame
        self.host = host
    # - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def validate(self):
        if self.host == None:
            random_host = choice(self.df['hostname'].unique())
            self.host = str(random_host).lower()
            return True
        elif (str(self.host).lower() in self.df['hostname'].str.lower().unique()):
            self.host = str(self.host).lower()
            return True
        else:
            False
    # - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def generate_system(self):
        #genera un sistema para self.bodies (Host(), [Plts()])

        if not self.validate():
            return False
        
        planets = []

        print('\n\nCargando display del sistema planetario:', self.host, '...')

        clean = self.df[self.df['hostname'].str.lower() == str(self.host).lower()]
        clean = clean.dropna(subset = ['pl_orbsmax', 'pl_orbeccen'], axis=0, ignore_index=True)

        if clean.empty:
            print(f"\nAdvertencia: No se encontraron datos válidos para {self.host}")
            return False

        star_mass = clean.iloc[0]['st_mass']

        if np.isnan(star_mass):
            star = Host(self.host, 1.0) #valor std
        else:
            star = Host(self.host, star_mass)

        for planeta in clean.itertuples():
            name = planeta.pl_name
            a = planeta.pl_orbsmax
            e = planeta.pl_orbeccen

            if np.isnan(planeta.pl_bmasse):
                mass = 0 #no afecta la simulación
            else:
                mass = planeta.pl_bmasse / EARTHS_TO_SUNS
            
            plt = Body(name, mass, a, e)
            planets.append(plt)
        
        return (star, planets) # -> Tupla(Host, [planets])


# Contenedor del sistema planetario
# ( REBOUND SIMULATION )
class SystemManager:

    def __init__(self, bodies):
         #si no nos pasan nada el modelo generará un sistema aleatorio
        self.sim = rb.Simulation()
        self.sim.integrator = 'whfast'
        self.sim.units = ('yr', 'AU', 'Msun')

        self.df = data
        self.bodies = bodies #Tupla ([estrella], [planetas])
    # - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def create_system(self): #añade los cuerpos identificando si es planeta o estrella
        host = self.bodies[0]
        planets = self.bodies[1] # [lista de planetas]

        self.sim.add(m = host.mass, hash = host.name) #host star

        for plt in planets:
            self.sim.add(m = plt.mass, a = plt.a, e = plt.e, hash = plt.name, inc = plt.inc,
                        omega = plt.omega, Omega = plt.OMEGA, M = plt.M) # exoplanetas

        self.sim.move_to_com()

    def steps(self, timestep):
        self.sim.integrate(self.sim.t + timestep)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Clase para la estrella andfitriona
class Host:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

# Clase que representa a los cuerpos en el sistema
class Body:
    def __init__(self, name, mass, a, e):
        self.name = name #pl_name
        self.mass = mass #pl_bmasse
        self.a = a #pl_orbsmax / AU
        self.e = e #pl_orbeccen

        self.inc = 0 #pl_orbincl / pasar a radianes
        self.omega = 0 #pl_orblper / pasar a radianes
        self.OMEGA = 0
        self.M = 0

        self.star = False

# Inicialización de la ventana
def simulation(host=None): #pasamos una host star

    #Se crea el sistema
    mng = DataManager(DataFrame = data, host=host).generate_system() # (host, [plt])

    if mng == False:
        print('''
        Algo salió mal :(, asegurate de haber ingresado el nombre de una estrella válida
        dentro del Dataset. Si la visualización no es la esperada podría ser a causa de 
        información faltante de algún exoplaneta.''')
        return
    
    simulator = SystemManager(mng) 
    simulator.create_system()
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # se crea la lista con los cuerpos del sistema
    pygame.init()

    screen = pygame.display.set_mode((ALTO, LARGO))
    pygame.display.set_caption('Simulación de Prueba')

    lienzo = pygame.Surface((int(ALTO * QTY_DISPLAY), int(LARGO * QTY_DISPLAY)))

    run = True
    clock = pygame.time.Clock()

    # Calculamos la escala óptima para ver todos los planetas,
    # se activará al presionar BARSPACE
    farest_plt = max(simulator.sim.particles[1:], key=lambda p: p.a)
    max_dist = farest_plt.a
    screen_rad = min(ALTO, LARGO) / 2
    
    MARGES = 0.9
    ideal_zoom = (screen_rad * MARGES) / max_dist

    # Mantiene la simulación corriendo hasta que 
    # cerremos la ventana. 
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('Finalizando la simulación ...')
                run = False
        
        # Maneja el Zoom de la cámara
        keys = pygame.key.get_pressed()
        # Mientras barspace esté presionada
        #la escala será la escala ideal
        if keys[pygame.K_SPACE]:
            zoom = ideal_zoom
        else:
            zoom = ESCALA

        simulator.steps(TIMESTEP)
        lienzo.fill(NEGRO)

        # Agregamos la Host Star
        star = simulator.sim.particles[0]
        sx = LARGO/2 + star.x * zoom
        sy = ALTO/2 - star.y * zoom

        sx_scaled = sx * QTY_DISPLAY
        sy_scaled = sy * QTY_DISPLAY
        planet_soft_finish(lienzo, STAR, sx_scaled, sy_scaled, 6 * QTY_DISPLAY)

        # Agregamos los exoplanetas
        k = 0
        for plt in simulator.sim.particles[1:]:
            x, y = plt.x, plt.y

            if k not in cola:
                cola[k] = deque(maxlen=LARGO_COLA)
            
            #Posiciones de la estela de un exoplaneta
            x_tail = x - star.x
            y_tail = y - star.y
            cola[k].append((x_tail, y_tail))

            #posiciones del planeta
            px = LARGO/2 + x * zoom
            py = ALTO/2 - y * zoom

            #Dibujamos la estela solo si hay mas de 2 puntos
            if len(cola[k]) >= 2:
                stella = []
                
                for xp, yp in cola[k]:
                    trailling_x = LARGO / 2 + xp * zoom
                    trailling_y = ALTO / 2 - yp * zoom
                    stella.append((trailling_x * QTY_DISPLAY, trailling_y * QTY_DISPLAY))
                
                pygame.draw.aalines(lienzo, STELLA, False, stella)
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

            planet_soft_finish(lienzo, PALETTE[k], px * QTY_DISPLAY, py * QTY_DISPLAY, 3 * QTY_DISPLAY)
            k+=1
        pygame.transform.smoothscale(lienzo, (ALTO, LARGO), screen)
        pygame.display.update()
        clock.tick(60) #El programa correrá a 60fps como máximo

    pygame.quit()