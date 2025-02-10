"""
Graph theory algorithms implemented in python

The focus is on algorithms for simple weighted graphs.
"""

import numpy as np

def random_graph(N=10, weight_max=10, directed=False):
    """
    Construct the matrix for a randomly created graph.
    """
    if directed:
        return np.random.randint(0, weight_max, (N, N)) + np.diag(N * [np.inf])

    else:
        graph = np.random.randint(0, weight_max, (N, N)) + np.diag(N * [np.inf])
        for i in range(1, N - 1):
            for j in range(i + 1, N):
                graph[j, i] = graph[i, j]
        return graph

def random_euclidean_graph(N=10, weight_max=10):
    """
    Construct the matrix for a randomly created Euclidean graph in two dimensions.
    """
    coordinates = np.random.uniform(0, weight_max, (2, N))
    graph = np.array(
        [[np.linalg.norm(coordinates[:, i] - coordinates[:, j])
          for i in range(N)] for j in range(N)]
    )
    graph = graph + np.diag(N * [np.inf])
    return graph, coordinates

def dijkstra(graph, directed=False):
    """
    Find all minimal distances between elements in a weighted graph.
    """
    N = len(graph)
    distances = graph.copy()

    if directed:
        for i in range(N):
            vertices_not_traversed = list(range(N)).remove(i)
            for _ in range(N - 1):
                next_vertex = vertices_not_traversed[np.argmin(
                    distances[i, vertices_not_traversed]
                )]
                vertices_not_traversed.remove(next_vertex)
                for k in vertices_not_traversed:
                    if distances[i, k] > distances[i, next_vertex] + graph[next_vertex, k]:
                        distances[i, k] = distances[i, next_vertex] + graph[next_vertex, k]

        return distances

    else:
        for i in range(1, N - 1):
            vertices_not_traversed = list(range(i + 1, N))
            for _ in range(i + 1, N - 1):
                next_vertex = vertices_not_traversed[np.argmin(
                    distances[i, vertices_not_traversed]
                )]
                vertices_not_traversed.remove(next_vertex)

                for k in vertices_not_traversed:
                    if distances[i, k] > distances[i, next_vertex] + graph[next_vertex, k]:
                        distances[i, k] = distances[i, next_vertex] + graph[next_vertex, k]

        for i in range(1, N - 1):
            for j in range(i + 1, N):
                distances[i, j] = distances[j, i]

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

