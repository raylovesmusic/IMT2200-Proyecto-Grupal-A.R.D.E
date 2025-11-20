import pygame
import rebound as rb
from math import pi

import pandas as pd
from random import choice
from os.path import join
from collections import deque

#DATA
ruta = join('..', 'data', 'exoplanets_physics_data.csv')
data = pd.read_csv(ruta)

#CONSTANTES 
ALTO, LARGO = 900, 900 #DIM
BLANCO  = (255, 255, 255) #RGB
NEGRO = (0, 0, 0) #RGB


class DataManager:
    def __init__(self, DataFrame : pd.DataFrame, host = None):
        self.df = DataFrame
        self.host = host
    # - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def validate(self):
        if (str(self.host).lower not in self.df['hostname'].str.lower().unique()):
            return False
        else:
            return True
    # - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def generate_system(self):
            #genera un sistema en self.bodies
            df = self.df

            if self.host == None:
                self.host = choice(df_clean['hostname'].unique)
            else:
                self.host = self.host.lower

            df_clean = df[df['hostname'].str.lower() == self.host].dropna(subset=['pl_name', 'pl_bmasse',])

            for planeta in df_clean.itertuples:
                x = 1
                pl = Body(x, 0, planeta.pl_name, planeta.pl_rade, BLANCO, planeta.pl_bmasse)

# Contenedor del sistema planetario
#      ( REBOUND SIMULATION )
class SystemManager:
    sim = rb.Simulation()
    sim.G = 4*pi**2
    sim.integrator = 'ias15'

    def __init__(self):
         #si no nos pasan nada el modelo generará un sistema aleatorio
        self.host = None
        self.df = data
        self.bodies = [] #lista de n cuerpos / rev
    # - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def add_body(self): #añade un cuerpo singular identificando si es planeta o estrella
        pass


# Clase que representa a los cuerpos en el sistema, 
# es decir una estrella andfitriona o exoplaneta.
#Nos sirve de auxiliar para poder dibujar los planetas en 
#pygame
class Body:
    #CONSTANTES
    AU = 149.6e6 * 1000 #valor de 1AU en metros 
    G = 6.67428e-11 #constante G
    ESCALA = 250 / AU # Escala los planetas al tamaño de la pantalla (100px per au)
    TIMESTEP = 3600 * 24  # cada frame se actualizará por día

    zoomed = False
    # - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def __init__(self, x, y, name, radius, color, mass):
        self.name = name
        self.rad = radius
        self.color = color
        self.mass = mass

        self.x = x #distancia al host en metros
        self.y = y #distancia al host en metros

        self.x_vel = 0
        self.y_vel = 0

        self.sydist = 0
        self.star = False #si es la host marcará True

        self.orbit = deque() #Trailling de la orbita
    # - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def add(self, win):

        #Escalamos las coords al tamaño de la pantalla y agregamos el offset del centro 
        x = self.x * self.ESCALA + LARGO / 2
        y = self.y * self.ESCALA + ALTO / 2

        pygame.draw.circle(win, self.color, (x, y), self.rad, )


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Inicialización de la ventana
def simulation(host=None): #pasamos una host star

    #Se crea el sistema
    system = SystemManager()

    if not system.validate(host): #revisamos la validez del sistema
        print('''
        No fué posible inicializar la simulación, asegurate
        de haber escrito un nombre válido para la estrella andfitriona.
        ''')
        return
    
    # se crea la lista con los cuerpos del sistema
    system.generate_system(host)
    pygame.init()

    screen = pygame.display.set_mode((ALTO, LARGO))
    pygame.display.set_caption('Simulación de Prueba')

    run = True
    clock = pygame.time.Clock()


    while run:
        clock.tick(60) #El programa correrá a 60fps como máximo

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
        for object in system.bodies:
            object.add(screen) #llama a Body().add()
        
        pygame.display.update()
    pygame.quit()
