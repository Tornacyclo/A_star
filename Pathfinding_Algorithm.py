import networkx as nx
from heapq import heappop, heappush



# Create a directed graph
G = nx.DiGraph()


# Add edges to the graph
G.add_edge('A', 'B', weight=2)
G.add_edge('A', 'C', weight=5)
G.add_edge('B', 'D', weight=3)
G.add_edge('C', 'D', weight=4)
G.add_edge('D', 'E', weight=2)


# Define the A* algorithm
def a_star(graph, start, goal):
    frontier = [(0, start)]  # Heap of (cost, node)
    came_from = {}  # Dictionary of how we reached a node
    cost_so_far = {start: 0}  # Dictionary of the cost to reach a node
    while frontier:
        current = heappop(frontier)[1]
        if current == goal:
            break
        for next_node, edge_attrs in graph[current].items():
            new_cost = cost_so_far[current] + edge_attrs['weight']
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + heuristic(goal, next_node)
                heappush(frontier, (priority, next_node))
                came_from[next_node] = current
    return came_from, cost_so_far

# Define the heuristic function
def heuristic(goal, next_node):
    return 1  # In this example, we're using a very simple heuristic


# Run the A* algorithm
came_from, cost_so_far = a_star(G, 'A', 'E')


# Print the results
print("Came from:", came_from)
print("Cost so far:", cost_so_far)



import matplotlib.pyplot as plt



# Visualize the graph
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
plt.show()


# from pyvis.network import Network



# # Visualize the graph
# net = Network(notebook=True)
# net.from_nx(G)
# net.show("mygraph.html")
