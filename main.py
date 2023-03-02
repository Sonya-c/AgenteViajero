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

import numpy as np
import csv

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
  def __init__(self):
    self.cromosoma = []
    self.fitness = 0    

  def evaluate(self):
    pass

  def mutate(self):
    pass


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
      print(line)
      
      name = line[0]
      x = float(line[1])
      y = float(line[2])

      world_data.add_city(x, y, name)      
  return world_data

def main():
  t: int = 0  
  world_data = get_data()
  
  # initialize()
  # evaluate()

  while False: 
    # select_parents()
    # reproduction()
    # mutate()
    # evaluate()
    
    # select_survivors()
    t = t + 1

main()