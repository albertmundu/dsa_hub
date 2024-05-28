import graphviz

def draw_graph(graph):
    dot = graphviz.Graph(comment='Graph Visualization', strict=False)
    
    num_cities = len(graph)
    for i in range(num_cities):
        dot.node(str(i), f'{i}')
    
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            if graph[i][j] != 0:
                dot.edge(str(i), str(j), label=str(graph[i][j]))
    
    output_path = '../outputs/undirected_graph_visualization_one_edge'
    dot.format = 'svg'
    dot.render(output_path, view=False)
    return output_path + '.svg'

# Example graph (distance matrix)
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Draw the undirected graph with only one edge between vertices and save it as an SVG file
svg_path = draw_graph(graph)
print(f'Undirected graph with one edge between vertices saved as {svg_path}')
