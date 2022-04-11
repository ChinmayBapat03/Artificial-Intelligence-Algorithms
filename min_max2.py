# When depth is n, starting index of the leaf node is: (2^n)-1
#Store all the leaf nodes in an array and now picturize a full binary tree where
# i is the parent node and 2i+1(left child) and 2i+2(right child) are leaf nodes

#(2**(depth+1))-1 is size of array

import math
import random

if __name__ == "__main__":
    #take input of all leaf nodes where depth is n, no of leaf nodes will be 2^n
    depth = int(input("Enter depth of the tree: "))
    no_leaf = 2**depth
    size = (2**(depth+1))-1
    leaf_arr = []
    for i in range(0, no_leaf):
        #val = int(input())
        val = random.randint(-1, 1)
        leaf_arr.append(val)
    # print(leaf_arr)
    while (depth >= 1):
        print("Considering leaf nodes from depth", depth, "and parents from depth ", depth-1)
        leaf_start = (2**depth)-1
        level_start = (2**(depth-1))-1
        if ((depth-1) % 2 == 1): #odd == min
            print("Min players are playing: ")
            temp = []
            iterator = 0
            for i in range(level_start, leaf_start): #travelling through parent nodes.
                index1 = i - (2**(depth-1)-1) + iterator
                val1 = leaf_arr[index1]
                index2 = i - (2**(depth-1)-1) + iterator +1
                val2 = leaf_arr[index1]

                mm = min(val1, val2)
                print("Minimum value selected out of ", val1, "and ", val2, "is ", mm)
                temp.append(mm)
                iterator = iterator+1
            leaf_arr = temp + leaf_arr
        else: #even == max
            print("Max players are playing: ")
            temp = []
            iterator = 0
            for i in range(level_start, leaf_start): #travelling through parent nodes.
                index1 = i - (2**(depth-1)-1) + iterator
                val1 = leaf_arr[index1]
                index2 = i - (2**(depth-1)-1) + iterator +1
                val2 = leaf_arr[index2]

                mm = max(val1, val2)
                print("Maximum value selected out of ", val1, "and ", val2, "is ", mm)
                temp.append(mm)
                iterator = iterator+1
            leaf_arr = temp + leaf_arr
        depth = depth - 1
    
    print(leaf_arr)
