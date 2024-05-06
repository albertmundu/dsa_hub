

def fractional_knapsack(n, weights, values, capacity):

    ratio = [values[i]/weights[i] for i in range(n)]

    items = list(zip(ratio, weights, values))

    items.sort(reverse=True)

    current_capacity = capacity
    total_value = 0
    selected_items = []
    for i, (r, w, v) in enumerate(items):
        if current_capacity >= w:
            current_capacity -= w             
            total_value += v
            selected_items.append((w,v))
        else:
            total_value += r*current_capacity
            selected_items.append((w,v))
            break 
    return total_value, selected_items



if __name__ == "__main__":
    n = 4
    W = 20
    weights = [5,10,12,17]
    values = [8,19,30,38]

    print(fractional_knapsack(n, weights, values, W))

    