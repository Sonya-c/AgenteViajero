# Agente Viajero, algoritmo genetico 

Problema del agente viajero 

Cromosoma: la ruta

el fitness: valor de la ruta 
Algoritmo general 

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

