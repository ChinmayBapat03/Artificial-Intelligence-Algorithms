import numpy as np
import matplotlib.pyplot as plt
def hill_climbing_1(start, h):
     current_par = start
     current = heu(current_par)
     flag = True
     print("Printing all values for Q1: ")
     ctr = 0
     while(flag):
         ctr = ctr+1
         result1_itr.append(ctr)
         next_par = current_par + h
         next = heu(next_par)
         print(next)
         result1_arr.append(current)
         if (next < current):
             return current
         else:
            current_par = next_par
            current = next
     return current

def hill_climbing_2(start):
    current_par = start
    current = heu(current_par)
    flag = True
    print("Printing all values for Q2: ")
    ctr = 0
    while(flag):
        ctr = ctr+1
        result2_itr.append(ctr)
        h_val = heu2(current)
        next_par = current_par + 0.01*h_val
        next = heu(next_par)
        print(next)
        result2_arr.append(current)
        if (next < current):
            return current
        else:
            current_par = next_par
            current = next
    return current

def heu(x):
    return np.sin(x)

def heu2(x):
    return np.cos(x)

if __name__ == '__main__':
    start = 0.1
    h = 0.2

    result1_arr = []
    result1_itr = []
    result2_arr = []
    result2_itr = []
    

    result1 = hill_climbing_1(start, h)
    plt.title("Q1")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.plot(result1_arr, result1_itr, color="red")

    result2 = hill_climbing_2(start)
    plt.title("Q2")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.plot(result2_arr, result2_itr, color="green")
    

    print("Answer for question1 is: ", result1)
    print("Answer for question2 is: ", result2)