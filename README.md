# Agente Viajero, algoritmo genetico 

## Algoritmo 
* Problema del agente viajero 
* Cromosoma: la ruta
* el fitness: valor de la ruta 

~~~
INICIO 
  t = 0 // t representa la generación 
  inicializar_población(P(t))
  evaluar(p(t))

  mientras no_terminado() hacer
    padres = seleccionar_padres()
    hijos = reproducir(padres)
    mutar(hijos)
    evaluar(hijos)
    P(t + 1) = seleccionar_supervivientes(hijos, P(t))
    t = t + 1
  fin-mientras
FIN
~~~

## Modelo de datos 
* City: representación de una ciudad (un elemento del cromosoma)
  ~~~
  City:
    id (int): identificador de ciudad
    x (float): posición en x
    y (float): posición en y
    name (str, opcional): nombre de la ciudad
    neighbors(dict[str, float]): diccionario de distancias. Guarda las distancia entre otras ciudades
    ----
    distance(ciudad) -> float:
      dada una ciudad, calcula la distancia entre esta y la otra ciudad
  ~~~
* WorldData: almacena todas las ciudades
  ~~~
  WorldData:
    total_cities (int): número total de ciudadaes
    cities ([City]): lista de ciudades
    -----
    add_city(x: float, y: float, name: (str, optional)):
      Añadir una ciudad 
  ~~~
* Solution: un cromosoma. Tiene una ruta y el fitness asociado a dicha ruta
  ~~~
  Solution:
    route ([City]): lista de ciudades (ruta, solución)
    fitness (float): fitness de la solución
    ---
    evaluate():
      Calcula el fitness. Para ello, calcula la distancia entre cada par de ciudades.
      La distancia total representa el fitness
    mutate():
      Mutar. Cambiar dos ciudades
  ~~~

## Componentes funcionales 
* get_data
* initialize
* reproduction
* select_parents