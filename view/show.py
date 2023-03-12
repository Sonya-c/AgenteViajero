import matplotlib.pyplot as plt
import networkx as nx

def show(route):
  """
  Profe,
  
  no se moleste en ver esto. 

  Con amor, niñita
  
  referencia (meme) = https://www.youtube.com/watch?v=16Y6rwa6HOY
  """
  G=nx.Graph()
  
  fist_city = route[0]
  last_city = route[len(route) - 1]

  node_labels = dict([(city.id, city.name + "\n" + str(city.x) + "," + str(city.y)) for city in route])
  
  city = route[0] 
  G.add_node(city.id, pos=(city.x, city.y))
  # unir las ciudades 
  for id in range(len(route) - 1):
    next_city = route[id + 1]
    G.add_node(next_city.id, pos=(next_city.x, next_city.y))
    G.add_edge(next_city.id, city.id)
    city = next_city

  # unir la primera y ultima ciudad
  G.add_edge(fist_city.id, last_city.id)

  fig, ax = plt.subplots()
  
  pos=nx.get_node_attributes(G,'pos')
  nx.draw_networkx(G, pos=pos, labels = node_labels, with_labels=True, ax=ax)

  ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)

  fig_manager = plt.get_current_fig_manager()
  fig_manager.full_screen_toggle()
  plt.title("Mejor solución")
  plt.axis("on")
  plt.grid('on')
  plt.show()