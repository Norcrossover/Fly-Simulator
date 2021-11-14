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
    human_interaction = rand.randint(0, rand.randint(5, 10))
    flies_health = rand.randint(0, rand.randint(5, 25))
    return (human_interaction + flies_health)

# defines a carrying capacity, or an amount of food 
def carrying_capacity():
    return (rand.randint(1, 200))

# will recursively return the number of flies
def number_of_flies():
    flies = initial_flies
    x.append(initial_flies)
    for i in range(months):
        K = carrying_capacity()
        if (flies < 1):
            print("All of the flies have died")
            break
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
    plt.plot(y, x)
    plt.show()
    plt.ion()


def main():
    graph_data()

if __name__ == "__main__":
    main()