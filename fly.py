import matplotlib.pyplot as plt
import numpy as np
# constants 
#plt.use('fast')
flies = 100
tspan = 10
mew_one = 0.16
mew_two = 0.21
mew_three = 0.08
mew_four = 0.16
capital_alpha= 10**-6
epsilon_beta_gamma = 0.0016
delta = 1.14226
lower_alpha = 0.003 * 10**-6

# Creation of a rate to be used in the exponential
def rate_of_mortality():
    return 0

# will recursively return the number of flies
def number_of_flies():
    return 0

def graph_data():
    fig, ax = plt.subplots()
    plt.draw()
    plt.ion()
    plt.title("Fly Simulation Test")
    plt.xlabel("Time")
    plt.ylabel("Number of Flies")
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
    plt.show()

def main():
    graph_data()

if __name__ == "__main__":
    main()