from collections import deque

def BFS(a,b,target):
    #Create a map to store the altready visited cominations of the jugs.
    #Fvisited states are 1 and not visited are 0
    smap = {} #dictionary
    isSolvable = False
    path = []

    #Create a queue to maintain the BFS
    q = deque()
    #Initializing with the initial state (0,0)
    q.append((0,0))
    while (len(q) > 0):
        print(q)
        #Current state
        u = q.popleft() #pop the used state -- function pops the leftmost element in the queue and returns the value
        if((u[0], u[1]) in smap): #If this state is already visited..
            continue
        if ((u[0] > a or u[1] > b or u[0] < 0 or u[1] < 0)): #Doesnt meet jug contraints
            continue
        path.append([u[0], u[1]])
        #Now mark current state as visited
        smap[(u[0], u[1])] = 1
        #now if we reach solution state, put ans = 1
        if(u[0] == target or u[1] == target):
            isSolvable = True

            if (u[0] == target):
                if(u[1] != 0):
                    #Fill final state and now empty the other jug
                    path.append([u[0], 0])
            else:
                if (u[0] != 0):
                    path.append([0, u[1]])
            #print the solution path.

            sz = len(path)
            for i in range(sz):
                print("(", path[i][0], ",", path[i][1], ")")
            break

        #Now if we havent reached the final state yet
        #start developing intermediate states for the final target

        q.append([u[0], b]) #Fill jug2
        q.append([a, u[1]]) #Fill jug1

        for ap in range(max(a,b) + 1):
            #Pour amount ap from jug2 to jug1
            c = u[0] + ap
            d = u[1] - ap

            #Check if this state is possible or not

            if(c == a or (d == 0 and d >= 0)):
                q.append([c, d])

            #Pour amount ap from jug1 to jug2
            c = u[0] - ap
            d = u[1] + ap

            #Check if this is a valid state..
            if ((c == 0 and c >= 0) or d==b):
                q.append([c,d])

        #empty jug2

        q.append([a,0])

        #Empty jug1

        q.append([0,b])

    #No solution exists if ans=0
    if(isSolvable == False):
        print("No solution exists\n")

if __name__ == '__main__':
    Jug1 = int(input("Enter value in Jug1: "))
    Jug2 = int(input("Enter value in Jug2: "))
    target = int(input("Enter target litres in a jug: "))
    print("Path from the initial state (0,0) is: \n")
    BFS(Jug1, Jug2, target)