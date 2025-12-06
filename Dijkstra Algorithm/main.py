from collections import defaultdict
from heapq import heappush,heappop
def shortestReach(n, Edges, source):
    GRAPH = defaultdict(dict)
    for i, j, w in Edges:
        GRAPH[i][j] = min(GRAPH[i].get(j, float('inf')), w)
        GRAPH[j][i] = min(GRAPH[j].get(i, float('inf')), w)

    distances = [float("inf") for _ in range(n + 1)]
    distances[source] = 0
    que = [(0, source)]
    visited = set()
    while que:
        current_distance, current_node = heappop(que)

        if current_distance > distances[current_node]:
            continue
        if current_node in visited:
            continue
        visited.add(current_node)
        for neighbour, weight in GRAPH[current_node].items():
            new_distance = current_distance + weight
            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance
                heappush(que, (new_distance, neighbour))
    dists = []
    for i in range(1, n + 1):
        if i == source: continue
        val = distances[i]
        dists.append(val if val != float("inf") else -1)
    return dists

edges = [[1,2,24],[1,2,9],[1,4,20],[3,1,3],[4,3,12]]
print(*shortestReach(4,edges,1))
