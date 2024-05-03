from heapq import heappop, heappush 
import functools 


def prims(graph):
    '''
    @param
        graph: input adjacency matrix 

    @return
        mst: minimum spanning tree

    @complexity:
        O(E log E)
    '''

    n = len(graph)

    mst = [[float('inf'), -1] for i in range(n)]

    visited = [ False for _ in range(n)]

    r = 0
    mst[r][0]=0

    pq=[(0, r)]

    while pq:
        _, u = heappop(pq)
        visited[u] = True
        for v, w in enumerate(graph[u]):
            if w!=0 and not visited[v] and w < mst[v][0]:
                mst[v][0] = w
                mst[v][1] = u 
                heappush(pq, (w,v))
    return [(k,  (v, u)) for v, (k,u) in enumerate(mst)]


if __name__=="__main__":

    graph = [
        [ 0, 3, 0, 0, 0, 12, 0],
        [ 3, 0, 5, 0, 0, 0,  4],
        [ 0, 5, 0, 6, 0, 0,  3],
        [ 0, 0, 6, 0, 1, 0,  0],
        [ 0, 0, 0, 1, 0, 10, 7],
        [12, 0, 0, 0, 10, 0, 2],
        [ 0, 4, 3, 0, 7, 2,  0]
    ]

    mst = prims(graph)
    print(mst)
    print(f'Total Weight: {sum([e[0] for e in mst])}')
    # print(f'Total Weight: {functools.reduce(lambda a,b: a+b, mst)}')


