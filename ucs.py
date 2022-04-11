from collections import deque
from os import sep
if __name__ == '__main__':
    #take input and convert to arrays
    
    h = int(input())
    wmax = 2**(h+1)-1 # total no of nodes that can exist
    w = input()
    s_warray = w.split()
    warray = list(map(int, s_warray)) #weights array
    node_arr = list(range(1, wmax+1)) #all possible nodes

    #take start and goal node
    start = int(input())
    goal = int(input())

    #create list of edges and adjacency list
    edge_list = []
    adj_list = {}
    for i in range(0, len(node_arr)):
        node_list = []
        if (node_arr[i]*2 in node_arr):
            left = [node_arr[i], node_arr[i]*2, warray[((i+1)*2)-1]]
            edge_list.append(left)
            node_list.append(node_arr[i]*2)

        if ((node_arr[i]*2)+1 in node_arr):
            right = [node_arr[i], node_arr[i]*2+1, warray[((i+1)*2+1)-1]]
            edge_list.append(right)
            node_list.append(node_arr[i]*2+1)
        tpl = {node_arr[i]: node_list}
        adj_list.update(tpl)

    #print(edge_list)
    #print(adj_list)

    #Queue operations
    path = []
    edge_cost = []
    #append start node
    path.append(start)
    q = deque()
    while(path[-1] != goal):
        last_node = path[-1]
        a = adj_list.get(int(last_node))
        for node in a:
            for edge in edge_list:
                if(edge[0] == last_node and edge[1] == node):
                    q.append(edge)
        while(len(q) != 0):
            min_list = []
            for j in q:
                min_list.append(j[2])
            min_cost = min(min_list)
            for k in q:
                if(min_cost == k[2]):
                    q.remove(k)
                    edge_cost.append(k[2])
                    path.append(k[1])
                    break
                min_list.clear()
            q.clear()

    costsum = 0
    for i in range(0, len(edge_cost)):
        costsum = costsum + edge_cost[i]
        print(edge_cost[i], end = " ")
    print("\n", costsum)