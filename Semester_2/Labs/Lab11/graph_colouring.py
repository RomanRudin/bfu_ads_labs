
def graph_coloring(graph: list[list[int]], num_colors: int) -> dict[int, int]:
    colors = {}
    nodes_ordered_by_degree = sorted(
        range(len(graph)), key=lambda x: -len(graph[x])
    )

    for node in nodes_ordered_by_degree:
        used_colors = set()

        for neighbor in graph[node]:
            if neighbor in colors:
                used_colors.add(colors[neighbor])
        
        for color in range(1, num_colors + 1):
            if color not in used_colors:
                colors[node] = color
                break

    return colors



if __name__ == "__main__":
    graph = [
        [1, 2],     
        [0, 2, 3],  
        [0, 1, 3],  
        [1, 2]       
    ]
    num_colors = 3

    coloring = graph_coloring(graph, num_colors)

    print("GRAPH:")
    for node, color in sorted(coloring.items()):
        print(f"TOP {node} COLOR {color}")
