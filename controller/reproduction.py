from models import Solution 

  
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
  
  # tomar los pdres de dos en dos
  for i in range(0, len(parents) - 1, 2): 
    rutaTemp = []
    
    rutaTemp.append(parents[i].route[0])
    abort_child = False
    
    # buscar el resto de ciudades 
    for j in range(0, len(parents[i].route) - 1):
      # Obtener los vecinos 
      vecinos = parents[i].get_neighbors(j) + parents[i + 1].get_neighbors(j)

      # verificar que no haya repetidos
      vecinos2 = [] # no supe ponerle nombre
      for vecino in vecinos: 
        if vecino not in rutaTemp: 
          vecinos2.append(vecino)

      # warn: puede que vecinso2 quede vacio 
      if len(vecinos2) == 0: 
        abort_child = True
        break   
      
      # esta función te da la ciudad con menor distancia 
      next_city = min(vecinos2, key=lambda city: city.distance(rutaTemp[j]))
      rutaTemp.append(next_city)
      
    if not abort_child:
      child = Solution(rutaTemp)
      print(child)
      children.append(child)
    else: 
      print("Aborted child")
      
  return children

