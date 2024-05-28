import graphviz

def tsp_recursive(current_city, remaining_cities, graph, graphviz_tree, parent_id, node_counter, cumulative_cost):
    node_id = str(node_counter[0])
    label = f'{current_city}->{remaining_cities}, Cost: {cumulative_cost}'
    graphviz_tree.node(node_id, label=label)
    if parent_id is not None:
        graphviz_tree.edge(parent_id, node_id, label=str(cumulative_cost))

    node_counter[0] += 1

    # Base case
    if not remaining_cities:
        total_cost = cumulative_cost + graph[current_city][0]  # Return to the starting city
        end_node_id = str(node_counter[0])
        graphviz_tree.node(end_node_id, label=f'{current_city}->0, Cost: {total_cost}')
        graphviz_tree.edge(node_id, end_node_id, label=str(graph[current_city][0]))
        node_counter[0] += 1
        return graph[current_city][0]

    min_cost = float('inf')

    # Recursive case
    for next_city in remaining_cities:
        remaining = tuple(c for c in remaining_cities if c != next_city)
        cost = graph[current_city][next_city]
        total_cost = cumulative_cost + cost
        cost += tsp_recursive(next_city, remaining, graph, graphviz_tree, node_id, node_counter, total_cost)
        if cost < min_cost:
            min_cost = cost

    return min_cost

def generate_tsp_recursive_tree(graph):
    # Initialize graphviz tree
    graphviz_tree = graphviz.Digraph(comment='TSP Recursive Tree')
    node_counter = [0]  # Counter to keep track of node ids

    # Set of remaining cities (excluding the starting city 0)
    remaining_cities = tuple(range(1, len(graph)))

    # Start recursive TSP from city 0
    tsp_recursive(0, remaining_cities, graph, graphviz_tree, None, node_counter, 0)

    # Save the graph as an SVG file
    output_path = '../outputs/tsp_recursive_tree'
    graphviz_tree.format = 'svg'
    graphviz_tree.render(output_path, view=False)
    return output_path + '.svg'

# Example graph (distance matrix)
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Generate the tree and save it as an SVG file
svg_path = generate_tsp_recursive_tree(graph)
print(f'Tree saved as {svg_path}')
