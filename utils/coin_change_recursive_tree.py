import graphviz

def generate_recursive_tree(coins, amount, graph=None, parent_node=None, node_count=0):
    if graph is None:
        graph = graphviz.Digraph(format='svg')
        graph.attr(bgcolor='white', rankdir='TB', size='100,100')  # Top to Bottom direction and size
        graph.node('root', f'amount={amount}')
        parent_node = 'root'
        node_count = 1

    if amount == 0:
        graph.node(f'node_{node_count}', 'amount=0\ncoins=0')
        graph.edge(parent_node, f'node_{node_count}')
        return graph, node_count

    for coin in coins:
        if amount - coin >= 0:
            child_node = f'node_{amount - coin}_{coin}_{node_count}'
            graph.node(child_node, f'amount={amount - coin}')
            graph.edge(parent_node, child_node)
            graph, node_count = generate_recursive_tree(coins, amount - coin, graph, child_node, node_count + 1)
    
    return graph, node_count

# Define the coins and amount
coins = [1, 2, 5]
amount = 11

# Generate the recursive tree
graph, _ = generate_recursive_tree(coins, amount)

# Save the graph as an SVG file
svg_file_path = '../outputs/coin_change_recursive_tree'
graph.render(svg_file_path, format='svg', cleanup=True)

