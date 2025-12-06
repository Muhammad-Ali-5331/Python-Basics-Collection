    from collections import defaultdict
    from heapq import heappush,heappop
    def shortestReach(n, Edges, source):
        GRAPH = defaultdict(dict)
        for i, j, w in Edges:
        # --- We first check that if already and edge present between the "current source vertex" and "destination vertex" then we should have the vertex that makes less distance to travel.
        # E.g. 1-->2 30, 1-->2 5 there are two edges between 1-2 so we keep the minimum val (5)
            # Check if Graph has the Node i (current source vertex) Edge
            if i in GRAPH:
                #If it is in Graph then check that the j (destination vertex) in Edges of the "current source vertex" (checked previously).
                if j in GRAPH[i]:
                    #if it is then just simply then we should have the vertex that makes less distance to travel
                    GRAPH[i][j] = min(GRAPH[i][j],w)
                    GRAPH[j][i] = min(GRAPH[j][i], w)
                    continue
            #if it is not then just simply add the weight and vertex and weight
            GRAPH[i][j] = w
            GRAPH[j][i] = w

            # --- More Optimal Method --- #
            # GRAPH[i][j] = min(GRAPH[i].get(j, float('inf')), w)
            # GRAPH[j][i] = min(GRAPH[j].get(i, float('inf')), w)


        distances = [float("inf") for _ in range(n + 1)] # marking all the distances initially as infinite
        distances[source] = 0 # mark source as 0 (means source to source)
        que = [(0, source)] # Initialize the min-heap with the source index
        visited = set() # set to track if the destination vertex that we are checking from current vertex is seen/marked or not
        while que:
            current_distance, current_node = heappop(que) # get the minimum distance from the min-heap

            if current_distance > distances[current_node]: # check if the current distance is greater than the distance marked on the current Node then this is not the optimal path to reach from source vertex
                continue
            if current_node in visited: # if the current node (might be the neighbour of some vertex) has been marked or not
                continue
            visited.add(current_node) # add the current node to visited and start marking its neighbours
            for neighbour, weight in GRAPH[current_node].items():
                new_distance = current_distance + weight # If the distance from source to neighbour (calculated using: current vertex weight {that is being marked from source to this current node} + weight/distance required to travel to neighbour)
                if new_distance < distances[neighbour]: #if that distance is less than the marked distance on the current vertex neighbour then update the distance on neighbour
                    distances[neighbour] = new_distance
                    heappush(que, (new_distance, neighbour)) # add that min distance and the neighbour node to min-heap for further exploration

        ''' As initially we created distances array 0-n but vertex starts from 1 so we start the loop from 1 and also we don't need the 
        the distance of source-->source '''
        dists = []
        for i in range(1, n + 1):
            if i == source: continue
            val = distances[i]
            dists.append(val if val != float("inf") else -1)
        return dists

    edges = [[1,2,24],[1,2,9],[1,4,20],[3,1,3],[4,3,12]]
    print(*shortestReach(4,edges,1))
