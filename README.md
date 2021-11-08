# Fly-Simulator
This app will simulate a model of flies with various variables that will influence the number of flies living. 

The equation used in this simulation is derived from: https://mathbench.umd.edu/modules/popn-dynamics_housefly/page11.htm
# NUMBER OF FLIES EQUATION
let r be the rate of mortality
let K be the carrying capacity
Let N be the number of flies
N_t = N_t-1 + (r * (K-N_t-1) * (N_t-1)/K)
The main factors I could start off is with creating a rate of mortality through conditions such as :
* How fit the flies were (food, worked out)
* Number of flies reproduced per fly (seasonal amount)
* Number of eggs per fly (too many flies fighting over rotting food might lower egg production in the food)
* Carrying Capacity - Number of flies vs. Number of Resources


        
In addition to various functions/methods that may need to be used to simulate how the lives of flies would survive or even thrive under certain conditions. Prior to this, a simple solution to the exponential is needed.

DESIGN:
* UPDATE - Differential Equations do not need to be known since I was reading a more advanced fly study on a virus passed between flies. Insane stuff I'd be interested in the future, not as of right now.
* Using simpy - a library for simulations. UPDATE - not using this, I can do it all myself.
* Possible turtle or graph mapped out of the simulation. Visual if you will. UPDATE - I will be using matplotlib to graph my exponential. It will be a time (x axis) vs Number of flies (y axis) graph
    ** Before this, probably just cmd line app in order to test accuracy prior to spending time on a front end. Don't need to do this anymore since I will have a graph showing the results of the graph.
    ** Figure out how I will apply the constants needed to the functions. What the functions should even be doing and how they correlate with each other. 


FUNCTIONS:
* Develop rate of mortality.
* Recursive function to find the number of flies per time that also creates an array of number of flies and the time at it is returned. Could also create a dictionary that I could parse through to run into matplotlib.
* Graphing Function.