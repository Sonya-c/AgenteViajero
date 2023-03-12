
def survivals(population, min_size = 2):
  """
  """
  population.sort(key=lambda solution: solution.fitness)

  if len(population) > min_size:
    return population[0:len(population) - 1]
  else: 
    return population
  