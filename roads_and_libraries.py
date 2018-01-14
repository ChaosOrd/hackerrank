
def build_graph(edges):
    graph = {}
    for a, b in edges:
        if a not in graph:
            graph[a] = set()
        graph[a].add(b)

        if b not in graph:
            graph[b] = set()

        graph[b].add(a)

    return graph


def find_connectivities(graph: dict):
    graph_temp = dict(graph)
    connectivities = []
    while len(graph_temp) != 0:
        vertex, neighbours = graph_temp.popitem()
        edges = 0
        while len(neighbours) != 0:
            next_neighbours = []
            for neighbour in neighbours:
                if neighbour in graph_temp:
                    next_neighbours.extend(graph_temp[neighbour])
                    graph_temp.pop(neighbour)
                    edges += 1
            neighbours = next_neighbours
        connectivities.append(edges)

    return connectivities


def roadsAndLibraries(n, c_lib, c_road, cities):
    graph = build_graph(cities)
    con = find_connectivities(graph)
    cost = 0
    covered_vertices = 0
    for num_of_edges in con:
        num_of_vertices = (num_of_edges + 1)
        covered_vertices += num_of_vertices
        libs = c_lib * num_of_vertices
        roads = c_road * num_of_edges + c_lib
        if libs < roads:
            cost += libs
        else:
            cost += roads
    return cost + (n - covered_vertices) * c_lib


if __name__ == "__main__":
    f = open('input01.txt', 'r')
    q = int(f.readline().strip())
    for a0 in range(q):
        n, m, c_lib, c_road = f.readline().strip().split(' ')
        n, m, c_lib, c_road = [int(n), int(m), int(c_lib), int(c_road)]
        cities = []
        for cities_i in range(m):
           cities_t = [int(cities_temp) for cities_temp in f.readline().strip().split(' ')]
           cities.append(cities_t)
        result = roadsAndLibraries(n, c_lib, c_road, cities)
        print(result)
    f.close()