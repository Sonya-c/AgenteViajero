import math 

class City:
  """
  Representa una ciudad (un gen de la solución).

  Attributes
  ----------
  * id: int 
    Identificador de la ciudad 
  * x: float 
    Posición del eje x
  * y: float 
    Posición del eje y
  * name: str (optional)
    Nombre de la ciudad
  * neighbors: dict
    Diccionario de vecinos
  
  Methods
  -------
  * distance(city: City)
    Calcula la distancia desde esta ciudad hasta la otra
  """

  def __init__(self, id, x, y, name=""):
    """
    Creación de una ciudad 
    
    Parameters: 
    * id: int 
      Identificador de la ciudad 
    * x: float 
      Posición del eje x
    * y: float 
      Posición del eje y
    * name: str (optional)
      Nombre de la ciudad
    """
    self.id = id
    self.x = x
    self.y = y
    self.name = name
    self.neighbors = dict()

  def distance(self, city) -> float: 
    """
    Calcular la distancia entre dos ciudades 

    Parametros 
    * city: City
      La otra ciudad (para la que queremos calcular la distancia)

    Retorno
    * distance: float 
      Distancia entre las dos ciudades
    """
    if city.id in self.neighbors: 
      # Si ya tenemos guardada esta ciudad, solo es necesario buscarla en el diccionario
      distance = self.neighbors[city.id]
    else: 
      # Si no tenemos esta ciudad guardada, 
      # Calculamos la distancia con el teorema de pitagoras (distancia entre dos puntos)
      # Guardamos la distancia en el diccionario de las dos ciudades     
      distance = math.sqrt(pow(self.x + city.x, 2) + pow(self.y + city.y, 2))
      self.neighbors[city.id] = distance
      city.neighbors[self.id] = distance 
      
    return distance 
    
  def __repr__(self):
    """
    Representación de la clase. Como se va a mostrar cuando se imprima
    """
    return self.name

  def __str__(self):
    """
    Representación de la clase. Como se va a mostrar cuando se imprima
    """
    return self.name