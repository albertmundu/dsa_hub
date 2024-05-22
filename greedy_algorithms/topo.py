from queue import deque

def topological_sort_kahn(graph):
    in_degree = {u:0 for u in graph } #Initialize in-degree to 0
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1#Compute in_degrees
    queue = deque([u for u in graph if in_degree[u] ==0 ])
    #Vertices with 0 in_degree
    topo_order = []
    
    while queue:
        u= queue.popleft()
        topo_order.append(u)
        for v in graph[u]:
            in_degree[v] -=1
            if in_degree[v] == 0:
                queue.append(v)
                
    if len(topo_order) == len(graph):
        return topo_order
    else:
        return "Graph has a cycle,topological sort not possilble "


if __name__ == "__main__":
    graph = {1: [2,3], 2:[3,4], 3: [4,5], 4:[],5:[]}

    print(topological_sort_kahn(graph))