from heapq import heappush, heappop, heapify


# djikstra algorithm for directed graph works on the +ve edge-weight

def dijkstra(graph, start):

    # Initialize the priority queue
    pq = []
    heappush(pq, (0, start))
    
    # Initialize distances and parents
    distances = {node: float('infinity') for node in graph}
    parents = {node: None for node in graph}
    distances[start] = 0

    while pq:
        cur_dist, cur_node = heappop(pq)

        # If the distance for the current node is greater than the recorded distance, skip it
        if cur_dist > distances[cur_node]:
            continue

        # relax
        for neighbor, weight in graph[cur_node]:
            distance = cur_dist + weight

            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parents[neighbor] = cur_node
                heappush(pq, (distance, neighbor))

    return distances, parents


if __name__ == "__main__":
    # Example usage:
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }

    start_node = 'A'
    distances, parents = dijkstra(graph, start_node)

    print("Distances:", distances)
    print("Parents:", parents)
