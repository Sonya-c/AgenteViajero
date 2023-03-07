from .City import City 

class WorldData:
  """
  Representa el mundo. Contiene la información de todas las ciudades 

  Attributes 
  ----------
  * total_cities: int 
    Representa el número de ciudades totales 
  * cities: [City]
    Arreglo de todas las ciudades 
  
  Methods
  -------
  * add_city()
    Añadir una ciudad
  """
  def __init__(self):
    self.total_cities = 0
    self.cities = []

  def add_city(self, x, y, name=""):
    """
    Añadir una ciudad a los datos del mundo 

    Parametros 
    * x: float
      Posición x de la ciudad 
    * y: float
      Posición y de la ciudad
    * name: str (opcional)
      Nombre de la ciudad 
    """
    # se usa total_cities como el id de la ciudad 
    city = City(self.total_cities, x, y, name)
    
    self.cities.append(city)
    self.total_cities += 1

  def __repr__(self):
    return ", ".join(str(city) for city in self.cities)
  