# Modelos
# from models import City, WorldData, Solution

# Controladores
from controller import get_data, initialize, select_parents, reproduction

MAX_INTERATIONS: int = 1

def accept(p) -> bool: 
  # TODO
  return False 
  
def main():
  t: int = 0  # Generación
  P = [0*MAX_INTERATIONS]  # Arreglo de poblaciones

  # Obtener datos desde el .csv
  print("### Todas las ciudades ###")
  world_data = get_data()
  print(world_data)

  # Crear (de forma aleatoria) la primera población
  print("### Ciudades iniciales ###")
  P[t] = initialize(world_data)
  for solution in P[t]:
    print(solution)

  # Mientras que el número de interaciones no rebace el limite y no se haya aceptado la solución, seguir buscando
  while t < MAX_INTERATIONS and not accept(P[t]):
    # Seleccionar los padres (los mejores, con el fitness mas pequeño)
    print("### Padres seleccionados ###")
    parents = select_parents(P[t], 4)
    for parent in parents:
      print(parent)

    # Reproducir los padres para crear la siguiente generación
    print("### Hijos (sin mutar) ###")
    children = reproduction(parents)
    for child in children:
      print(child)

    # children.mutate()
    # children.evaluate()

    # select_survivors()
    t = t + 1

if __name__ == '__main__':
  main()