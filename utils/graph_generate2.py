import graphviz

def draw_graph(graph):
    dot = graphviz.Digraph(comment='Graph Visualization')
    
    num_cities = len(graph)
    for i in range(num_cities):
        dot.node(str(i), f'City {i}')
    
    for i in range(num_cities):
        for j in range(num_cities):
            if i < j and graph[i][j] != 0:
                dot.edge(str(i), str(j), label=str(graph[i][j]))
    
    output_path = '../outputs/graph_visualization'
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

# Draw the graph and save it as an SVG file
svg_path = draw_graph(graph)
print(f'Graph saved as {svg_path}')
