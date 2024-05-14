def color_graph(graph):
    colors = {}
    for node in graph:
        neighbor_colors = {colors[neighbor] for neighbor in graph[node] if neighbor in colors}
        for color in range(len(graph)):
            if color not in neighbor_colors:
                colors[node] = color
                break
    return colors

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

coloring = color_graph(graph)
print("Node colors:", coloring)
