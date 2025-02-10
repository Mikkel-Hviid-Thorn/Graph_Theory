"""
Graph theory algorithms implemented in python

A graph is represented by a set of vertices and a list of edges. Each edge is a tuple with a start vertex, end vertex,
and possibly a weight. The algorithms are only guaranteed to work for positively weighted graphs.
"""

from typing import Set, List, Tuple, Any, Hashable

inf = float('inf')

class Graph:

    def __init__(self, vertices: Set[Hashable] | List[Hashable] | Tuple[Hashable],
                 edges: List[Tuple[Any, Any] | Tuple[Any, Any, int | float]],
                 directed: bool = False):
        self.vertices = set(vertices)
        self.edges = list(edges)
        self.directed = directed

        if all(len(e) == 3 for e in self.edges):
            self.weighted = True
        else:
            self.weighted = False

    def add_vertex(self, vertex: Hashable):
        self.vertices.add(vertex)

    def add_vertices(self, vertices: Set[Hashable] | List[Hashable] | Tuple[Hashable]):
        self.vertices.union(set(vertices))

    def add_vertex(self, vertex: Hashable):
        self.vertices.add(vertex)

    def add_vertices(self, vertices: Set[Hashable] | List[Hashable] | Tuple[Hashable]):
        self.vertices.union(set(vertices))

    def add_weights(self, ):





def dijkstra(graph, directed=False, path=None) -> tuple:
    """"""
    V = graph[0].copy()
    E = graph[1].copy()

    if directed:
        edges_on_pair = {(u, v) : [e[3] for e in E if e[:2] == (u, v)] for u in V for v in V}
    else:
        edges_on_pair = {(u, v): [e[3] for e in E if e[:2] == (u, v) or e[:2] == (v, u)] for u in V for v in V}

    distances = {(u, v) : min(edges_on_pair[(u, v)] + [inf if u != v else 0]) for u in V for v in V}

    for u in V:
        vertices_not_traversed = V.copy().remove(u)
        for _ in range(len(V) - 1):
            minimum_vertex = min({v : distances[(u, v)] for v in vertices_not_traversed})
            vertices_not_traversed.remove(minimum_vertex)
            for v in vertices_not_traversed:
                if distances[(u, v)] > distances[(u, minimum_vertex)] + min(edges_on_pair[(minimum_vertex, v)]):
                    distances[(u, v)] = distances[(u, minimum_vertex)] + min(edges_on_pair[(minimum_vertex, v)])

    return distances

def floyd_warshall(graph, directed=False):
    """
    Find all minimal distances between elements in a weighted graph.
    """
    N = len(graph)
    distances = graph.copy()

    if directed:
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    if j != k and distances[j, k] > distances[j, i] + distances[i, k]:
                        distances[j, k] = distances[j, i] + distances[i, k]

        return distances

    else:
        for i in range(N):
            for j in range(1, N - 1):
                for k in range(j + 1, N):
                    if distances[j, k] > distances[j, i] + distances[i, k]:
                        distances[j, k] = distances[j, i] + distances[i, k]

        for i in range(1, N - 1):
            for j in range(i + 1, N):
                distances[j, i] = distances[i, j]

        return distances

def fleury(multigraph, max_iterations=10 ** 3):
    """
    Find an Euler circuit in a multigraph.
    """
    if np.any(np.nan_to_num(multigraph % 2, 0)):
        raise

    N = len(multigraph)
    multigraph_copy = multigraph.copy()
    euler_circuit = []

    iteration_counter_1 = 0
    while np.max(multigraph) > 0:
        sub_circuit = [np.argmin(multigraph_copy) % N]
        multigraph_copy[np.argmin(multigraph_copy) % N, np.argmin(multigraph_copy) % N]
        sub_circuit.append(np.argmax(multigraph_copy[sub_circuit[-1], :] > 0))


        iteration_counter_2 = 0
        while sub_circuit[0] == sub_circuit[-1]:
            sub_circuit.append(np.argmax(multigraph_copy[sub_circuit[-1], :] > 0))

            iteration_counter_2 += 1
            if iteration_counter_2 >= max_iterations:
                break

        euler_circuit += sub_circuit

        iteration_counter_1 += 1
        if iteration_counter_1 >= max_iterations:
            break

    return euler_circuit

