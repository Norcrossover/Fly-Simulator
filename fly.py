import matplotlib.pyplot as plt
import numpy as np
import random as rand
# constants/globals 
months = 12
initial_flies = 3
x = []
y = []

# Creation of a rate to be used in the exponential
def rate_of_mortality():
    return 120

# defines a carrying capacity, or an amount of food 
def carrying_capacity():
    return (rand.randint(1, 200))

# will recursively return the number of flies
def number_of_flies():
    ''' Recursive Solution, can't figure it out
    if (months == 0): 
        return initial_flies
    #x.append(rate_of_mortality * flies)
    return (rate_of_mortality * number_of_flies(months-1))    
    #return number_of_flies() + (rate_of_mortality * (K - number_of_flies()) / K)
    '''
    flies = initial_flies
    x.append(initial_flies)
    for i in range(months):
        K = carrying_capacity()
        flies = (flies + (rate_of_mortality() * (K - flies) * (flies / K)))
        x.append(flies)
        y.append(i)
    y.append(months)


def graph_data():
    number_of_flies()
    print(x)
    print(y)
    plt.title("Fly Simulation Test")
    plt.xlabel("Time")
    plt.ylabel("Number of Flies")
    #plt.plot(x_np, y_np)
    plt.plot(y, x)
    plt.show()


def main():
    graph_data()

if __name__ == "__main__":
    main()