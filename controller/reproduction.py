from models import Solution 
import itertools

def make_child(p1, p2): 
  rutaTemp = []
    
  rutaTemp.append(p1.route[0])
  abort_child = False
    
  # buscar el resto de ciudades 
  for j in range(0, len(p1.route) - 1):
    # Obtener los vecinos 
    vecinos = p1.get_neighbors(j) + p2.get_neighbors(j)

    # verificar que no haya repetidos
    vecinos2 = [] # no supe ponerle nombre
    for vecino in vecinos: 
      if vecino not in rutaTemp: 
        vecinos2.append(vecino)

    # warn: puede que vecinso2 quede vacio 
    if len(vecinos2) == 0: 
      abort_child = True
      return []   
    
    # esta función te da la ciudad con menor distancia 
    next_city = min(vecinos2, key=lambda city: city.distance(rutaTemp[j]))
    rutaTemp.append(next_city)
  
  return rutaTemp
  
def reproduction(parents): 
  """
  0. La primera ciudad siempre será la primera ciudad de la mejor solución 
  2. Para hallar la segunda ciudad se bucan los vecino s de la primera ciudad en ambas soluciones y se toma el vecino mas cercano (ojo de no repetir)
  3. Para las siguientes ciudades, se buscan los vecinos de la anterior y se escoje la más proxima (reptir )

  Parameters:
    parents: lista de padres 
  Returns: 
    children
  """
  children = []
  relationships = list(itertools.combinations(parents, 2))
  
  # tomar los pdres de dos en dos
  for p1, p2 in relationships: 
  
    child = make_child(p1, p2)
      
    if not len(child) == 0:
      child = Solution(child)
      children.append(child)
    else: 
      print("Aborted child")
      
  return children

