# A* Pathfinding Algorithm
This is an implementation of the A* Pathfinding algorithm in Python, using the NetworkX library for creating and manipulating the graph and pyvis for visualization.

## Installation
Make sure you have the following libraries installed :
```
networkx
matplotlib
pyvis (optional)
```
You can install these libraries using pip :
```
pip install networkx matplotlib pyvis
```

## Usage
## Creating the graph

You can create a directed graph by initializing a DiGraph object from the networkx library and adding edges to it. Each edge should have a weight attribute that represents the cost of traversing that edge.

## Running the A* algorithm
You can use the a_star function provided to find the shortest path from a start node to a goal node. The function takes in three arguments: the graph, the start node, and the goal node.

The function returns a tuple containing two dictionaries:

- came_from: A dictionary containing the node that was traversed before reaching the key node
- cost_so_far: A dictionary containing the cost of reaching the key node

## Visualizing the graph
You can use matplotlib or pyvis libraries to visualize the graph

The visualization will open a window with the graph, you can customize the visualization by passing options to the nx.draw_networkx_* functions or the Network class of pyvis library.

Note: Keep in mind that the heuristic function used in this example is very basic, you should use a more accurate heuristic depending on the problem you're trying to solve.
