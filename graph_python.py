# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation
class Graph:

    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Function to print a BFS of graph


def BFS(graph, source):
    # Mark all the vertices as not visited
    visited = [False] * (max(graph.graph) + 1)

    # Create a queue for BFS, the node in the queue hasn't finish the search
    queue = [source]

    # Mark the source node as
    # visited and enqueue it
    visited[source] = True

    while queue:

        # Dequeue a vertex from
        # queue and print it
        s = queue.pop(0)
        print(s, end=" ")

        # get all the related node of the node popped to act as a broad search
        for i in graph.graph[s]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


def DFS(graph, source):
    visited = [False] * (max(graph.graph) + 1)  # record whether a node is visited before
    visited[source] = True
    need_to_check = [source]
    while need_to_check:
        s = need_to_check.pop(0)
        print(s, end=" ")
        for neighbor_node in graph.graph[s]:
            if not visited[neighbor_node]:
                need_to_check = [neighbor_node] + need_to_check
            visited[neighbor_node] = True

# Driver code

# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
BFS(g, 2)
print('')
DFS(g, 2)

