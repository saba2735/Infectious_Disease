import sys
import numpy as np
import matplotlib.pyplot as plt

def forward_euler_solver(beta, gamma, s0, i0, dt, max_t):
    t = 0
    s = s0
    i = i0
    R0 = beta / gamma
    
    susceptibles = [s]
    infected = [i]
    time = [t]
    analytical = [i]
    
    while t < max_t:
        i_t = (beta - gamma) * i * (1 - (i / (1 - (1 / R0))))
        
        exponential_term = np.exp(-(beta - gamma) * t)
        analytical_soln = ((1 - (1 / R0)) / (1 + ((1 - (1 / R0)) - i0) / i0 * exponential_term))
        
        i += i_t * dt
        analytical_i = analytical_soln * dt + analytical[-1]
        
        infected.append(i)
        analytical.append(analytical_soln)
        
        t += dt
        time.append(t)
    
    return time, infected, analytical

def calculate_max_absolute_error(dt, max_t):

    time, I, ana = forward_euler_solver(beta, gamma, s0, i0, dt, max_t)
    absolute_error = (np.array(I) - np.array(ana))
    max_absolute_error = np.max(abs(absolute_error))
    
    return max_absolute_error

beta = 3
gamma = 2
s0, i0 = 0.99, 0.01
max_t = 25
dts = [2, 1, 0.5]

for dt in dts:
    max_error = calculate_max_absolute_error(dt, max_t)
    print(f"Max Absolute Error for dt = {dt}: {max_error}")
