
from disjointset import DisjointSet


def kruskal(graph):
    """
    @params:
        graph: adjacency matrix
    
    @return:
        mst: minimum spanning tree
    """

    n = len(graph)
    mst = []
    ds = DisjointSet(n) #makeset
    edges = []

    for u in range(n):
        for v in range(u+1, n):
            if graph[u][v]:
                edges.append((graph[u][v], (u,v)))
    
    edges.sort()

    for w, (u,v) in edges:
        if ds.find(u)!=ds.find(v):
            mst.append((w,(u,v)))
            ds.union(u,v)
    return mst


if __name__ == "__main__":

    graph = [
            [ 0, 3, 0, 0, 0, 12, 0],
            [ 3, 0, 5, 0, 0, 0,  4],
            [ 0, 5, 0, 6, 0, 0,  3],
            [ 0, 0, 6, 0, 1, 0,  0],
            [ 0, 0, 0, 1, 0, 10, 7],
            [12, 0, 0, 0, 10, 0, 2],
            [ 0, 4, 3, 0, 7, 2,  0]
        ]

    mst = kruskal(graph)
    print(mst)
    print(f'Total Weight: {sum([e[0] for e in mst])}')



