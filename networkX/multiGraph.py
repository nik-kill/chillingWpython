# import networkx as nx
# G = nx.MultiGraph()
# G.add_edge('A', 'B', relation='neighbor')
# G.add_edge('A', 'B', relation='friend')
# G.add_edge('B', 'C', relation='neighbor')
# G.add_edge('D', 'C', relation='friend')

# nx.MultiEdgeDataView([('A', 'B', {'relation': 'neighbor'}), ('A', 'B', {'relation': 'friend'}), ('B', 'C', {
#                   'relation': 'neighbor'}), ('B', 'D', {'relation': 'neighbor'}), ('C', 'D', {'relation': 'friend'})])

import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(1, 3)
nx.draw(G, with_labels=True)
plt.show()
