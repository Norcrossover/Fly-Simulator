# Fly-Simulator
This app will simulate a model of flies with various variables that will influence the number of flies living. 

The equation used in this simulation is derived from: https://mathbench.umd.edu/modules/popn-dynamics_housefly/page11.htm
The equation simplifies to: flies_t = (rate_of_mortality)*flies_t-1
The main factors I could start off is with creating a rate of mortality through conditions such as :
    How fit the flies were (food, worked out)
    Number of flies reproduced per fly (seasonal amount)
    Number of eggs per fly (too many flies fighting over rotting food might lower egg production in the food)
    Carrying Capacity - Number of flies vs. Number of Resources

N_t = N_t-1 + (r * (K-N_t-1) * (N_t-1)/K)
        
In addition to various functions/methods that may need to be used to simulate how the lives of flies would survive or even thrive under certain conditions. Prior to this, a simple solution to the exponential is needed.

Design:
UPDATE - Differential Equations do not need to be known since I was reading a more advanced fly study on a virus passed between flies. Insane stuff I'd be interested in the future, not as of right now.
    Using simpy - a library for simulations
    Possible turtle or graph mapped out of the simulation. Visual if you will.
        Before this, probably just cmd line app in order to test accuracy prior to spending time on a front end. 
    Figure out how I will apply the constants needed to the functions. What the functions should even be doing and how they correlate with each other. 