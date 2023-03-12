import random
from models import Solution


def initialize(world_data, num_routes=8):
  """
  Crea rutas iniciales aleatorias 

  Parameters:
  * World_data: información sobre las ciudades 
  * num_routes: número de rutas inciales a crear. Por defecto 4
    
  Returns:
  * P: lista de soluciones
  """

  routes = []
  P = []

  # Generar num_routes rutas
  while len(P) < num_routes:
    # Crear una copia del mundo (para no editar la orginal)
    route = world_data.cities.copy()

    # Crear una ruta aleatoria
    random.shuffle(route)

    # Si la ruta no esta repetida, añadirna 
    if route not in routes:
      # se tiene que crear un objeto solución 
      # al pasarle la ruta la evalua
      solution = Solution(route) 
      P.append(solution)

  return P
