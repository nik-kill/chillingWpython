import networkx as nx
import matplotlib.pyplot as plt
G_asymmetric = nx.DiGraph()
G_asymmetric.add_edge('A', 'B')
G_asymmetric.add_edge('A', 'D')
G_asymmetric.add_edge('C', 'A')
G_asymmetric.add_edge('D', 'E')
nx.spring_layout(G_asymmetric)
nx.draw_networkx(G_asymmetric)

plt.show()