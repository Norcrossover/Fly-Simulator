import matplotlib.pyplot as plt
import numpy as np
# constants/globals 
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
initial_flies = 3
x = []
y = []

# Creation of a rate to be used in the exponential
def rate_of_mortality():
    return 120

# will recursively return the number of flies
def number_of_flies(months):
    ''' Recursive Solution, can't figure it out
    if (months == 0): 
        return initial_flies
    #x.append(rate_of_mortality * flies)
    return (rate_of_mortality * number_of_flies(months-1))    
    #return number_of_flies() + (rate_of_mortality * (K - number_of_flies()) / K)
    '''
    flies = initial_flies
    x.append(initial_flies)
    y.append(0)
    for i in range(months):
        flies = (rate_of_mortality() * flies)
        x.append(flies)
        y.append(i)


def graph_data(months):
    number_of_flies(months)
    print(x)
    print(y)
    # change them to numpy arrays 
    x_np = np.array(x)
    y_np = np.array(y)
    plt.title("Fly Simulation Test")
    plt.xlabel("Time")
    plt.ylabel("Number of Flies")
    plt.plot(x_np, y_np)
    plt.show()


def main():
    graph_data(months)

if __name__ == "__main__":
    main()