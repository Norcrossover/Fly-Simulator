# Fly-Simulator
This app will simulate a model of flies with various variables that will influence the amount of flies alive and dead.

First there will need to be a fly object:
    Class Fly:
        age, hunger, health points
        
In addition to various functions/methods that may need to be used to simulate how the lives of flies would survive or even thrive under certain conditions. 

Design Ideas:
    Using simpy - a library for simulations
    Using diffeqpy - a library for solving or representing differential equations? Still confused since I don't know how to solve them yet, but the knowledge is needed for this simulation to work.
    Possible turtle or graph mapped out of the simulation. Visual if you will.
        Before this, probably just cmd line app in order to test accuracy prior to spending time on a front end. 
    Figure out how I will apply the constants needed to the functions. What the functions should even be doing and how they correlate with each other. 

I have not taking any class with differential equations yet, so it looks all garbled to me. The only way to solve it in the given time I need to come up with a solution. From reading the documentation on the diffeqpy tutorial I know that I could probably use it to solve this system of equations and have it plotted out.

First line is the original equation whilst the second will be what I set the variables to in order to make it make sense to me.
1. dS_m/dt = delta((S_f + I_f) - A (S_f + I_f)** 2) - - epsilon*S_m + lower_beta*S_m - lower_gamma*S_m - lower_alpha* (S_m + I_m) * S_m - mew_one*S_m



2. dI_m/dt = epsilon*S_m + lower_beta*S_m + lower_alpha* (S_m + I_f) * S_m - mew_two*I_m

εSM +βSM +γSM +α⋅(SM +IM )⋅SM −μ2I


3. dS_f/dt = lower_delta((S_f + I_f) - A * (S_f + I_f)**2) - epsilon*S_f - lower_beta*S_f - lower_gamma*S_f - mew_three*S_f


4. dI_f/dt = epsilon*S_f + lower_beta*S_f + lower_gamma*S_f - mew_four*I_f
