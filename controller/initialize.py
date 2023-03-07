import random
from models import Solution


def initialize(world_data, num_routes=4):
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

  while len(P) < num_routes:
    route = world_data.cities.copy()
    random.shuffle(route)

    if route not in routes:
      solution = Solution(route)
      solution.evaluate()
      P.append(solution)

  return P
