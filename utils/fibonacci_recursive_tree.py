import graphviz

def generate_fibonacci_tree(n, graph=None, parent_node=None, node_count=0):
    if graph is None:
        graph = graphviz.Digraph(format='svg')
        graph.attr(bgcolor='white', rankdir='TB', size='10,10')  # Top to Bottom direction and size
        graph.node('root', 'fib(6)')
        parent_node = 'root'
        node_count = 1

    if n <= 1:
        graph.node(f'node_{node_count}', f'{n}')
        graph.edge(parent_node, f'node_{node_count}')
        return graph, node_count

    left_child = f'node_{n-1}_{node_count}'
    right_child = f'node_{n-2}_{node_count}'

    graph.node(left_child, f'fib({n-1})')
    graph.node(right_child, f'fib({n-2})')

    graph.edge(parent_node, left_child)
    graph.edge(parent_node, right_child)

    graph, node_count = generate_fibonacci_tree(n-1, graph, left_child, node_count + 1)
    graph, node_count = generate_fibonacci_tree(n-2, graph, right_child, node_count + 1)

    return graph, node_count

# Generate the Fibonacci tree with n=6
graph, _ = generate_fibonacci_tree(6)

# Save the graph as an SVG file
svg_file_path = '../outputs/fibonacci_recursive_tree'
graph.render(svg_file_path, format='svg', cleanup=True)

print(f"SVG file saved at {svg_file_path}.svg")
