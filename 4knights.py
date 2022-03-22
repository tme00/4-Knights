import numpy as np
import networkx as nx

mouv = [21,12,19,8,-21,-12,-19,-8]

def parcourir(case):
  mouv_possible = []
  print("CASE: ")
  print(case)
  for m in mouv :
    x = case[0] + m
    if (x > 10 and x < 14) or (x > 20 and x < 24) or (x > 30 and x < 34):
      mouv_possible.append(x)
  return mouv_possible

def generate_graph(cases):
  g = []
  for case in cases:
    for node in parcourir(case): 
      g.append((case[0],node))
  return g

print("Voici l'échiquier qui se trouve dans le fichier texte:")
arr = np.loadtxt("Cell.txt", delimiter = ",")
print(arr)

print("\nOn voit la présence des cavaliers selon la case étudiée:\n")
pre_g = []
i = 11
for line in arr:
  for c in line:
    pre_g.append((i,c))
    i += 1
  i = i + 7
print(pre_g)

print("\nLa fonctione generate_graph nous donne les déplacements nécessaires pour répondre au problème:\n")
post_g = generate_graph(pre_g)
print(post_g)

G= nx.Graph()  
G.add_edges_from(post_g)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=600)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color = 'black')
nx.draw_networkx_labels(G, pos)

print("\nEn déplacant chaque cavalier d'un cran, en partant de 11 dans un sens, on peut voir qu'en répétant la boucle 4 fois, la position des cavaliers sera échangée.\n")
