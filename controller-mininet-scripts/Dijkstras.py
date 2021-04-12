distances_of_edges = [5, 2, 6, 8, 5, 2, 12, 19, 26, 4, 2, 15, 6, 4, 3, 3, 8, 3, 4, 1, 2]
def dijkstraHelperFunction(topo,src,dst):
    ''' dijkstra's helper function:

    makes link dictionary
    calls dijkstras on it

    '''
    output = open('results'+"/data.html",'a')
    def getDistance(src, dst):
        # return 5
        if ((src == '0_0_1' and dst == '1_0_1') or (src == '1_0_1' and dst == '0_0_1')):
            return distances_of_edges[0]
        elif ((src == '0_0_2' and dst == '1_0_1') or (src == '1_0_1' and dst == '0_0_2')):
            return distances_of_edges[1]
        elif ((src == '1_0_2' and dst == '1_0_1') or (src == '1_0_1' and dst == '1_0_2')):
            return distances_of_edges[2]
        elif ((src == '1_0_3' and dst == '1_0_1') or (src == '1_0_1' and dst == '1_0_3')):
            return distances_of_edges[3]
        # s2
        elif ((src == '0_0_3' and dst == '1_0_2') or (src == '1_0_2' and dst == '0_0_3')):
            return distances_of_edges[4]
        elif ((src == '0_0_4' and dst == '1_0_2') or (src == '1_0_2' and dst == '0_0_4')):
            return distances_of_edges[5]
        elif ((src == '1_0_3' and dst == '1_0_2') or (src == '1_0_2' and dst == '1_0_3')):
            return distances_of_edges[6]
        elif ((src == '1_0_5' and dst == '1_0_2') or (src == '1_0_2' and dst == '1_0_5')):
            return distances_of_edges[7]
        elif ((src == '1_0_4' and dst == '1_0_2') or (src == '1_0_2' and dst == '1_0_4')):
            return distances_of_edges[8]
        # s3
        elif ((src == '0_0_5' and dst == '1_0_3') or (src == '1_0_3' and dst == '0_0_5')):
            return distances_of_edges[9]
        elif ((src == '0_0_6' and dst == '1_0_3') or (src == '1_0_3' and dst == '0_0_6')):
            return distances_of_edges[10]
        elif ((src == '1_0_6' and dst == '1_0_3') or (src == '1_0_3' and dst == '1_0_6')):
            return distances_of_edges[11]
        elif ((src == '1_0_5' and dst == '1_0_3') or (src == '1_0_3' and dst == '1_0_5')):
            return distances_of_edges[12]
        # s4
        elif ((src == '0_0_7' and dst == '1_0_4') or (src == '1_0_4' and dst == '0_0_7')):
            return distances_of_edges[13]
        elif ((src == '0_0_8' and dst == '1_0_4') or (src == '1_0_4' and dst == '0_0_8')):
            return distances_of_edges[14]
        elif ((src == '1_0_5' and dst == '1_0_4') or (src == '1_0_4' and dst == '1_0_5')):
            return distances_of_edges[15]
        elif ((src == '1_0_6' and dst == '1_0_4') or (src == '1_0_4' and dst == '1_0_6')):
            return distances_of_edges[16]
        # s5
        elif ((src == '0_0_9' and dst == '1_0_5') or (src == '1_0_5' and dst == '0_0_9')):
            return distances_of_edges[17]
        elif ((src == '1_0_6' and dst == '1_0_5') or (src == '1_0_5' and dst == '1_0_6')):
            return distances_of_edges[18]
        # s6
        elif ((src == '0_0_10' and dst == '1_0_6') or (src == '1_0_6' and dst == '0_0_10')):
            return distances_of_edges[19]
        elif ((src == '0_0_11' and dst == '1_0_6') or (src == '1_0_6' and dst == '0_0_11')):
            return distances_of_edges[20]



    topoG = topo.g
    print "TopoG", topoG

    graphDic = {} #empty dictionary
    for node in topoG.nodes(): # make switch dictionary without links
        # print "NODE", node
        graphDic[node] = {}
    for id, edge in enumerate(topoG.edges()): # adds each link to each switch
        print "Edge: [", edge[0], "-", edge[1], "] Distance: ", getDistance(edge[0], edge[1])
        graphDic[edge[0]][edge[1]] = getDistance(edge[0], edge[1])
        graphDic[edge[1]][edge[0]] = getDistance(edge[0], edge[1])

    path = dijkstra(graphDic,src,dst,visited=[],distances={},predecessors={})

    print "After Running Algorithm on SRC: ", src, " Destination: ", dst, "\n The PATH is: \n"
    # HTML Code output for results
    output.write("<h3>Dijkstra's Algorithm from " + src +" to " + dst + ":</h3>")
    output.write("<p>After Running Algorithm from SRC: " + src + " to Destination: " + dst + " The path is:</p></br>")
    output.write("<b>" + str(path) + "</b>")
    print path

    dpidPath = []
    for switch in path:
        print switch
        dpidPath.append(topo.id_gen(name = switch).dpid)

    return path



def dijkstra(graph,src,dest,visited=[],distances={},predecessors={}):
    """ calculates a shortest path tree routed in src
    """
    # a few sanity checks
    if src not in graph:
        raise TypeError('The root of the shortest path tree cannot be found')
    if dest not in graph:
        raise TypeError('The target of the shortest path cannot be found')
    # ending condition
    if src == dest: #if source and destination are the same print out shorest path and exit
        # We build the shortest path and display it
        path=[]
        pred=dest
        while pred != None: # create
            path.append(pred) # append list path to show the prgevious predecessors
            pred=predecessors.get(pred,None) # get next predecessor and if none return none this breaks the next loop
        return tuple(reversed(path))

    else :
        # if it is the initial  run, initializes the cost
        if not visited: #this sets the source destination to 0 once because visited list
            distances[src]=0
        # visit the neighbors
        for neighbor in graph[src] : #each neighbor for the new starting node
            if neighbor not in visited: # if the neighbor hasnt been visited, check for new better paths
                new_distance = distances[src] + graph[src][neighbor] # create new weight for this new node + weight of source node
                if new_distance < distances.get(neighbor,float('inf')): # if new distance is less than the neightbor weight(if no weight assume infinity)
                    distances[neighbor] = new_distance #set distances of this new neighboring node to the new distance
                    predecessors[neighbor] = src #set the predecessors of this new neighbor to the "current node"
        # mark as visited
        visited.append(src) # add "current node" to visited

        unvisited={} # create unvisited dictionary
        for k in graph: # for each node
            if k not in visited: #if node is not in visited,
                unvisited[k] = distances.get(k,float('inf')) # add the weigths of every unvisited node
        x=0
        x=min(unvisited, key=unvisited.get) # get the lowest weighted node
        return dijkstra(graph,x,dest,visited,distances,predecessors) # run dijkstra's algorithm on cheapest node