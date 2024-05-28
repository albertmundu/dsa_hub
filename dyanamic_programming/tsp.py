def tsp_iterative(graph):
    n = len(graph)
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0  # Starting at city 0 with only city 0 visited

    for mask in range(1 << n):
        for u in range(n):
            if mask & (1 << u):
                for v in range(n):
                    if not mask & (1 << v):
                        new_mask = mask | (1 << v)
                        dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + graph[u][v])

    # Print the dp table
    for i in range(len(dp)):
        print(f"dp[{i:0{n}}] = {dp[i]}")

    # Return the minimum cost to visit all cities and return to the starting city
    min_cost = float('inf')
    for u in range(1, n):
        min_cost = min(min_cost, dp[(1 << n) - 1][u] + graph[u][0])
    
    return min_cost

# Example graph (distance matrix)
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Solve TSP and print the minimum cost
min_cost = tsp_iterative(graph)
print(f'The minimum cost to visit all cities is: {min_cost}')
