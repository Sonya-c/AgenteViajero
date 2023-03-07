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
    break 

  return children