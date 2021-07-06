import networkx as nx
import matplotlib.pyplot as plt
G_weighted = nx.Graph()
G_weighted.add_edge('Amitabh Bachchan', 'Abhishek Bachchan', weight=25)
G_weighted.add_edge('Amitabh Bachchan', 'Aaamir Khan', weight=8)
G_weighted.add_edge('Amitabh Bachchan', 'Akshay Kumar', weight=11)
G_weighted.add_edge('Amitabh Bachchan', 'Dev Anand', weight=1)
G_weighted.add_edge('Abhishek Bachchan', 'Aaamir Khan', weight=4)
G_weighted.add_edge('Abhishek Bachchan', 'Akshay Kumar', weight=7)
G_weighted.add_edge('Abhishek Bachchan', 'Dev Anand', weight=1)
G_weighted.add_edge('Dev Anand', 'Aaamir Khan', weight=1)

nx.draw_networkx(G_weighted)
plt.show()