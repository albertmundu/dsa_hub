import graphviz

def coin_change_recursive(amount, coins, graph, parent_id, node_counter, edge_label):
    current_id = str(node_counter[0])
    if parent_id is not None:
        graph.edge(parent_id, current_id, label=edge_label)

    # Base cases
    if amount == 0:
        graph.node(current_id, label=f'{amount} (Goal)')
        node_counter[0] += 1
        return 1
    if amount < 0 or not coins:
        graph.node(current_id, label=f'{amount} (Invalid)')
        node_counter[0] += 1
        return 0

    graph.node(current_id, label=f'{amount}')
    node_counter[0] += 1

    # Recursive calls
    ways_with_coin = coin_change_recursive(amount - coins[0], coins, graph, current_id, node_counter, f'Include {[i for i in coins]}\ntarget={amount-coins[0]}')
    ways_without_coin = coin_change_recursive(amount, coins[1:], graph, current_id, node_counter, f'Exclude {[i for i in coins[1:]]}\ntarget={amount}')

    return ways_with_coin + ways_without_coin

def generate_coin_change_tree(amount, coins):
    # Initialize graph
    graph = graphviz.Digraph(comment='Coin Change Problem')
    graph.attr(bgcolor='white', rankdir='TB', size='30,30')
    node_counter = [0]  # Counter to keep track of node ids
    coin_change_recursive(amount, coins, graph, None, node_counter, '')
    
    # Save the graph as an SVG file
    output_path = '../outputs/coin_change_tree'
    graph.format = 'svg'
    graph.render(output_path, view=False)
    return output_path + '.svg'

# Parameters
amount = 4
coins = [1, 2, 3]

# Generate the tree and save it as an SVG file
svg_path = generate_coin_change_tree(amount, coins)
print(f'Tree saved as {svg_path}')
