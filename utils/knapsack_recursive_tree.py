import graphviz

def generate_knapsack_tree(weights, values, W, n, graph=None, parent_node=None, node_count=0):
    if graph is None:
        graph = graphviz.Digraph(format='svg')
        graph.attr(bgcolor='white', rankdir='TB', size='20,20')  # Top to Bottom direction and size
        graph.node('root', f'KS({n}, {W})')
        parent_node = 'root'
        node_count = 1

    if n == 0 or W == 0:
        graph.node(f'node_{node_count}', f'{0}')
        graph.edge(parent_node, f'node_{node_count}')
        return graph, node_count

    if weights[n-1] > W:
        child_node = f'node_{W}_{n-1}_{node_count}'
        graph.node(child_node, f'KS({n-1}, {W})')
        graph.edge(parent_node, child_node)
        graph, node_count = generate_knapsack_tree(weights, values, W, n-1, graph, child_node, node_count + 1)
    else:
        include_child = f'node_{W-weights[n-1]}_{n-1}_{node_count}_include'
        exclude_child = f'node_{W}_{n-1}_{node_count}_exclude'

        graph.node(include_child, f'KS({n-1},{W-weights[n-1]})')
        graph.node(exclude_child, f'KS({n-1},{W})')

        graph.edge(parent_node, include_child, label=f'include\nv={values[n-1]}')
        graph.edge(parent_node, exclude_child, label='exclude')

        graph, node_count = generate_knapsack_tree(weights, values, W - weights[n-1], n-1, graph, include_child, node_count + 1)
        graph, node_count = generate_knapsack_tree(weights, values, W, n-1, graph, exclude_child, node_count + 1)

    return graph, node_count

if __name__ == "__main__":
    # Define the weights, values, and capacity
    weights = [1, 2, 3, 4]
    values = [1, 2, 5, 6]
    W = 7
    n = len(weights)

    # Generate the knapsack recursive tree
    graph, _ = generate_knapsack_tree(weights, values, W, n)

    # Save the graph as an SVG file
    svg_file_path = '../outputs/knapsack_recursive_tree'
    graph.render(svg_file_path, format='svg', cleanup=True)

    print(f"SVG file saved at {svg_file_path}.svg")
