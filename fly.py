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
months = 12

# Creation of a rate to be used in the exponential
def rate_of_mortality():
    return 1.2

# will recursively return the number of flies
def number_of_flies(months):
    if (months != 0): 
        return (rate_of_mortality * number_of_flies(months-1))
    #return number_of_flies() + (rate_of_mortality * (K - number_of_flies()) / K)

def graph_data(months):
    x = []
    x.append(number_of_flies(months, x))
    
    print(x)
    y = [0, months]
    plt.title("Fly Simulation Test")
    plt.xlabel("Time")
    plt.ylabel("Number of Flies")
    plt.plot(x, y)
    plt.show()


def main():
    graph_data(months)

if __name__ == "__main__":
    main()