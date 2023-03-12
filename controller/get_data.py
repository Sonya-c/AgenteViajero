import csv
from models import WorldData


def get_data(filename="data/simple_test_data.csv"):
  """
  Lee los datos desde un csv y crea las ciudades 

  Parameters:
  * filename (str): nombre del archivo que contiene los datos (por defecto data.csv)

  Returns:
  * world_data: conjunto de ciudades
  """
  world_data = WorldData()

  # Leer el archivo csv
  with open(filename, mode='r') as file:
    csv_file = csv.reader(file)

    for line in csv_file:
      name = line[0] # Nombre de la ciudad
      x = float(line[1]) # Posición en x
      y = float(line[2]) # Posición en y 

      # Añadir la ciudad 
      world_data.add_city(x, y, name)
      
  return world_data