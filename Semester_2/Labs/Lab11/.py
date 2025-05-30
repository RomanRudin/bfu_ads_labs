from typing import Optional, Literal

def can_color(graph, k) -> Optional[dict]:
    nodes = sorted(graph.keys(), key=lambda node: -len(graph[node]))
    colors = {}

    def backtrack(node_index) -> Optional[dict]:
        if node_index == len(nodes):
            return colors.copy()
        current_node = nodes[node_index]
        for color in range(1, k + 1):
            if all(colors.get(neighbor) != color for neighbor in graph[current_node]):
                colors[current_node] = color
                result = backtrack(node_index + 1)
                if result is not None:
                    return result
                del colors[current_node]
        return None

    return backtrack(0)

def find_min_colors(graph) -> tuple[Literal[0], dict] | tuple[int, dict]:
    max_degree = max(len(node) for node in graph.values())
    for k in range(1, max_degree + 2):
        coloring = can_color(graph, k)
        if coloring is not None:
            return k, coloring
    return len(graph), {node: i + 1 for i, node in enumerate(graph)}



if __name__ == "__main__":
    graphS = [{
        0: [1, 3],
        1: [0, 2],
        2: [1, 3],
        3: [0, 2]
    }, 
    {
        0: [1, 2],     
        1: [0, 2, 3],  
        2: [0, 1, 3],  
        3: [1, 2]       
    },
    {
        0: [1, 4, 5],
        1: [0, 2, 3, 7],
        2: [1, 3, 7],
        3: [1, 2, 4, 6],
        4: [0, 3, 5, 6],
        5: [0, 4, 6],
        6: [3, 4, 5, 7],
        7: [1, 2, 6]
    }]
    for graph in graphS:
        k, coloring = find_min_colors(graph)
        print(f"Минимальное количество цветов: {k}")
        print(f"Раскраска вершин: {coloring}")