# Решить задачу о раскраске графа, использовать перебор.

def is_valid_coloring(graph, colors):
    for vertex in graph:
        for neighbor in graph[vertex]:
            if colors[vertex] == colors[neighbor]:
                return False
    return True


def graph_coloring_brute_force(graph, max_colors):
    vertices = list(graph.keys())
    n = len(vertices)

    from itertools import product

    # Перебор всех возможные комбинации цветов для вершин
    for coloring in product(range(1, max_colors + 1), repeat=n):
        colors = dict(zip(vertices, coloring))
        if is_valid_coloring(graph, colors):
            return colors
    return None


def find_chromatic_number(graph):
    chromatic_number = 1
    while True:
        coloring = graph_coloring_brute_force(graph, chromatic_number)
        if coloring is not None:
            return chromatic_number, coloring
        chromatic_number += 1


if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['B', 'C']
    }

    chromatic_number, coloring = find_chromatic_number(graph)
    print(f"Хроматическое число графа: {chromatic_number}")
    print(f"Раскраска графа: {coloring}")
