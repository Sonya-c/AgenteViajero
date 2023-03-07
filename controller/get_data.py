import csv
from models import WorldData


def get_data(filename="data.csv"):
  """
  Lee los datos desde un csv y crea las ciudades 

  Parameters:
  * filename (str): nombre del archivo que contiene los datos (por defecto data.csv)

  Returns:
  * world_data: conjunto de ciudades
  """
  world_data = WorldData()

  with open(filename, mode='r') as file:
    csv_file = csv.reader(file)

    for line in csv_file:
      name = line[0]
      x = float(line[1])
      y = float(line[2])

      world_data.add_city(x, y, name)
      
  return world_data