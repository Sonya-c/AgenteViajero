# Controladores
from controller import get_data, initialize, select_parents, reproduction, survivals
from view import show

MAX_GENERATIONS: int = 100
MIN_GENERATIONS: int = 2

def accept(P):
  """
  Aceptar una generación. Si la genración actual es muy similar a la antieior, detenerse 
  """
  if len(P) < MIN_GENERATIONS: # se debe cumplir con un minimo de iteraciones 
    return False 
  else: 
    present_generation = P[len(P) - 1]
    past_generation = P[len(P) - 2]

    # contar el número de soluciones repetidas 
    repeated = 0
    for solution in present_generation:
      if solution.route in [route.route for route in past_generation]:
        repeated += 1

    return repeated == len(past_generation)
    #  Increible
    # wait, esta mal 
    # no, mentira, la generación 13 es igual a la anterior 
    #la generación 13 si, empiza en la 0
    # deberiamos aumentar el minimo? 
    # y si pongo (n - 1)! :D okay, no
    #maybe
    #No suena loco sabiendo que n varia
    #Ponle 150 solo para ver si se activa la condicion
    
def main():
  t: int = 0  # Generación

  # Obtener datos desde el .csv
  world_data = get_data("data/simple_test_data.csv")
  print("TODAS LAS CIUDADES")
  print(world_data)

  P = [0*MAX_GENERATIONS]  # Arreglo de poblaciones

  # Crear (de forma aleatoria) la primera población
  P[t] = initialize(world_data)
  print("\nGENERACIÓN 0")
  for solution in P[t]:
    print(solution)

  # Mientras que el número de interaciones no rebace el limite y no se haya aceptado la solución, seguir buscando
  while t < MAX_GENERATIONS and not accept(P):
    # Seleccionar los padres (los mejores, con el fitness mas pequeño)
    parents = select_parents(P[t], 6)

    # Reproducir los padres para crear la siguiente generación
    children = reproduction(parents)

    # Mutar a los hijos
    for child in children:
      child.mutate()

    # Construir la siguiente generación 
    next_generation = survivals(parents + children, min_size = 4)
    P.append(next_generation)
    t = t + 1

    print(f"\nGENRACIÓN {t}")
    for solution in P[t]:
      print(solution)

  # Seleccionar la mejor solución 
  print("\nNúmero total de generaciones =", t + 1)
  best_solution = min(P[t], key=lambda solution: solution.fitness)
  print("\nMEJOR SOLUCIÓN")
  print(best_solution)
  
  print("Mostrando representación grafica, si no aparece abrir una pestaña de Output...")
  show(best_solution.route)

if __name__ == '__main__':
  main()