"""
Solución del problema del agente viajero utilizando algoritmos geneticos. 

Clases: 
  City
  WorldData
  Solution
  
Funciones: 
  get_data -> WorldData
  
Variables: 
"""

import csv
import random
import math

class City:
  """
  Representa una ciudad (un gen de la solución).

  Attributes
  ----------
  id: int 
    Identificador de la ciudad 
  x: float 
    Posición del eje x
  y: float 
    Posición del eje y
  name: str (optional)
    Nombre de la ciudad

  Methods
  -------
  
  """
  def __init__(self, id, x, y, name = ""):
    self.id = id
    self.x = x
    self.y = y
    self.name = name
    self.neighbors = dict()
    
  def __repr__(self):
    return self.name
    
class WorldData:
  """
  Representa el mundo. Contiene la información de todas las ciudades 

  Attributes 
  ----------
  total_cities: int 
    Representa el número de ciudades totales 
  cities
    Arreglo de todas las ciudades 
    
  Methods
  -------
  add_city()
    Añadir una ciudad
  """
  def __init__(self):
    self.total_cities = 0
    self.cities = []

  def add_city(self, x, y, name=""):
    city = City(self.total_cities, x, y, name)
    
    self.cities.append(city)
    self.total_cities += 1    

class Solution:
  """
  La clase solución tiene dos datos prinicipales

  Attributes
  ----------
  cromosoma
    es un arreglo de ciudades. Es decir, la ruta. 
  fitness: int
    es un valor númerico. Contiene el valor de la ruta. 
    Este se calcula con el método evaluate

  Methods
  -------
  evaluate()
    calcula el fitness 
  mutate()
    muta el cromosoma (cambia dos ciudades)
  """
  def __init__(self, route = []):
    self.route = route
    self.fitness = 0
    self.evaluate()

  def evaluate(self):
    """
    Evalua el fitness (la distancia total) de esta ruta
    
    """
    d = lambda x1, x2, y1, y2 : math.sqrt(pow(x1 + x2, 2) + pow(y1 + y2, 2))
    for city_id in range(0, len(self.route) - 1):
      c1 = self.route[city_id]
      c2 = self.route[city_id + 1]

      # guardar resultados para no andar calculandolos todo el tiempo
      if c2.id in c1.neighbors:
        distance = c1.neighbors[c2.id]
      else:
        distance = d(c1.x, c2.x, c1.y, c2.y)
        c1.neighbors[c2.id] = distance
        c2.neighbors[c1.id] = distance
      self.fitness += distance

    # hallar la distancia de la primera a la última
    c1 = self.route[0]
    c2 = self.route[len(self.route) - 1]
    self.fitness += d(c1.x, c2.x, c1.y, c2.y)
    
  def mutate(self):
    pass

  def __repr__(self):
    return f"ruta = {self.route} fitness = {self.fitness}"


def get_data(filename = "data.csv"):
  """
  Lee los datos desde un csv y crea las ciudades 

  Parameters:
    filename (str): nombre del archivo que contiene los datos (por defecto data.csv)

  Returns:
    world_data: conjunto de ciudades
  """
  world_data = WorldData()
    
  with open(filename, mode ='r') as file:
    csv_file = csv.reader(file)
    
    for line in csv_file:
      name = line[0]
      x = float(line[1])
      y = float(line[2])

      world_data.add_city(x, y, name)      
  return world_data


def initialize(world_data, num_routes = 4):
  """
  Crea rutas iniciales aleatorias 

  Parameters:
    World_data: información sobre las ciudades 
    num_routes: número de rutas inciales a crear. Por defecto 4
    
  Returns:
    P: lista de soluciones
  """
  
  routes = []
  P = []

  while len(P) < num_routes:
    route = world_data.cities.copy()
    random.shuffle(route)

    if route not in routes:
      P.append(Solution(route))

  return P
  

def select_parents(population, num_parents = 2):
  """
  Seleccionar los mejores padres

  Parameters: 
    population: población de soluciones actual 
    num_parents: número de padres a seleccionar (por defecto 2)

  Returns:
    parents: lista de padres 
  """
  population.sort(key=lambda solution: solution.fitness)
  
  return population[0:num_parents]
  
def main():
  t: int = 0  # Generación 
  P = [] # Arreglo de poblaciones 
  
  world_data = get_data()
  P.append(initialize(world_data))

  print("Ciudades iniciales")
  [print(solution) for solution in P[t]]
  
  while t == 0: 
    parents = select_parents(P[t])
    
    print("parents")
    [print(parent) for parent in parents]
    
    # reproduction()
    # mutate()
    # evaluate()
    
    # select_survivors()
    t = t + 1

main()