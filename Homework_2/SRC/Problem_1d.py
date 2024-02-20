import sys
import numpy as np
import matplotlib.pyplot as plt

def forward_euler_solver(beta, gamma, s_0, i_0, delta_t, t_final):
    t = 0
    s = s_0
    i = i_0
    R_0 = beta / gamma
    
    susceptibles = [s]
    infected = [i]
    time = [t]
    analytical = [i]
    
    while t < t_final:
        i_t = (beta - gamma) * i * (1 - (i / (1 - (1 / R_0))))
        
        exponential_term = np.exp(-(beta - gamma) * t)
        analytical_soln = ((1 - (1 / R_0)) / (1 + ((1 - (1 / R_0)) - i_0) / i_0 * exponential_term))
        
        i += i_t * delta_t
        analytical_i = analytical_soln * delta_t + analytical[-1]
        
        infected.append(i)
        analytical.append(analytical_soln)
        
        t += delta_t
        time.append(t)
    
    return time, infected, analytical

def calculate_max_absolute_error(dt, t_final):
    time, I, ana = forward_euler_solver(beta, gamma, s0, i0, dt, t_final)
    absolute_error = np.abs(np.array(I) - np.array(ana))
    max_absolute_error = np.max(absolute_error)
    return max_absolute_error

beta = 3
gamma = 2
s0, i0 = 0.99, 0.01
max_t = 25
dts = [2,1,0.5,0.25,0.125,0.0625,0.03125]


max_error = [calculate_max_absolute_error(dt, max_t) for dt in dts]
plt.loglog(dts,max_error,marker='o',linestyle='-',color='b')
plt.xlabel('dt Sahana')
plt.ylabel("Max absolute error Sahana")
plt.title('Max absolute error vs dt Sahana')
plt.show()