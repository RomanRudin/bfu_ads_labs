
def graph_coloring(graph: list[list[int]], num_colors: int) -> dict[int, int]:
    colors = {}

    for node in range(len(graph)):
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