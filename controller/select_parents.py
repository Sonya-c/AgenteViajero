def select_parents(population, num_parents = 4):
  """
  Seleccionar los mejores padres

  Parameters: 
  * population: población de soluciones actual 
  * num_parents: número de padres a seleccionar (por defecto 2)

  Returns:
  * parents: lista de padres 
  """
  population.sort(key=lambda solution: solution.fitness)
  
  return population[0:num_parents]