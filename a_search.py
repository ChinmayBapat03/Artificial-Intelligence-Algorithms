from queue import PriorityQueue

def bfs(start, goal, adjdict = {}, h = [], *args):
    q = PriorityQueue()
    q.put([h[start-1], 0, str(start)])
    while not (q.empty()):
        path = q.get()
        head = path[2][-1]
        if (head == str(goal)):
            return path
        #take neighbouring nodes
        neigh = []
        for v in adjdict:
            if (v == int(head)):
                neigh = adjdict.get(v)
        nodes = []
        costm = []
        for i in range(0,len(neigh)):
            if(neigh[i] > 0):
                nodes.append(i+1)
                costm.append(neigh[i])
        #put adjacent neighbours in queue with all details
        for i in range(0, len(nodes)):
            way = path[2] + ' ' + str(nodes[i])
            heu = h[nodes[i]-1]
            cost = path[1] + costm[i]

            q.put([heu, cost, way])


def a_search(start, goal, adjdict = {}, h = [], *args):
    q = PriorityQueue()
    start_add = h[start-1]
    q.put([start_add, 0,h[start-1], str(start)])
    while not (q.empty()):
        path = q.get()
        head = path[3][-1]
        if (head == str(goal)):
            return path
        #take neighbouring nodes
        neigh = []
        for v in adjdict:
            if (v == int(head)):
                neigh = adjdict.get(v)
        nodes = []
        costm = []
        for i in range(0,len(neigh)):
            if(neigh[i] > 0):
                nodes.append(i+1)
                costm.append(neigh[i])
        #put adjacent neighbours in queue with all details
        for i in range(0, len(nodes)):
            way = path[3] + ' ' + str(nodes[i])
            heu = h[nodes[i]-1]
            cost = path[1] + costm[i]
            node_add = heu + cost

            q.put([node_add, cost, heu, way])



if __name__ == '__main__':
    #take all necessary inputs
    n = int(input('Enter n: \n')) #no of nodes
    #take cost matrix
    costmat = []
    adjdict = {}
    for i in range(0,n):
        c = input()
        s_carray = c.split()
        carray = list(map(int, s_carray)) #weights array
        adjdict.update({i+1: carray})
        costmat.append(carray)
    #take heuristic function values for all nodes
    val = input()
    s_val = val.split()
    h = list(map(int, s_val))
    #take start node and end node
    start = int(input('Enter start node: '))
    goal = int(input('Enter goal node: '))

    vertex = list(range(1, n))

    w = a_search(start, goal, adjdict, h)
    a_search_cost = w[0]
    print(a_search_cost)
    p = bfs(start, goal, adjdict, h)
    bfs_cost = p[1]
    print(bfs_cost)
    print(a_search_cost - bfs_cost)