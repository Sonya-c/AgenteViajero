import random 

class Solution:
  """
  La clase solución tiene dos datos prinicipales

  Attributes
  ----------
  * route: [City]
    es un arreglo de ciudades. Es decir, la ruta. 
  * fitness: float
    es un valor númerico. Contiene el valor de la ruta. 
    Este se calcula con el método evaluate
  
  Methods
  -------
  * evaluate()
    calcula el fitness 
  * mutate()
    muta el cromosoma (cambia dos ciudades)
  """
  def __init__(self, route = []):
    self.route = route
    self.route_len = len(route)
    self.fitness = 0
    self.evaluate()

  def evaluate(self):
    """
    Evalua el fitness (la distancia total) de esta ruta
    """
    
    for city_id in range(0, len(self.route) - 1):
      # Calcular la distancia entre dos ciudades 
      c1 = self.route[city_id]
      c2 = self.route[city_id + 1]

      distance = c1.distance(c2)
      
      self.fitness += distance

    # hallar la distancia de la primera a la última
    c1 = self.route[0]
    c2 = self.route[len(self.route) - 1]
    self.fitness += c1.distance(c2)
    
  def mutate(self):
    # Se mutara bajo una probabilidad muy pequela
    if random.randint(0, 100) == 1:
      print("Mutación!")

      # se toman dos ciudades de forma al azar y se intercambian
      city1, city2 = random.sample(set(range(0, self.route_len)), 2)
      self.route[city1], self.route[city2] = self.route[city2], self.route[city1]

  def get_neighbors(self, pos):
    """
    Dada una posición, te halla los vecinos de dicha posición
    """
    neighbors = []
    
    if pos == 0: 
      neighbors.append(self.route[self.route_len - 1])
    else: 
      neighbors.append(self.route[pos - 1])

    if pos == self.route_len - 1:
      neighbors.append(self.route[0])
    else: 
      neighbors.append(self.route[pos + 1])
      
    return neighbors
    
  def __repr__(self):
    """
    Representación impresa de la clase
    """
    return f"ruta = {self.route}\nfitness = {self.fitness}"
