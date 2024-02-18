#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 12:09:49 2024

@author: sahanabalaji
"""
import sys
import numpy as np
import matplotlib.pyplot as plt

def forward_euler_solver(beta, gamma, s_0, i_0, delta_t, t_final):
    t = 0
    s = s_0
    i = i_0
    R_0 = beta / gamma
    # analytical_i = 0
     
    susceptibles = [s]
    infected = [i]
    time = [t]
    analytical = [i]
    
    while t < t_final:
        i_t = (beta - gamma) * i * (1 - (i / (1 - (1 / R_0))))
        
        exponential_term = np.exp(-(beta - gamma) * t)
        analytical_soln = ((1 - (1 / R_0)) / (1 + ((1 - (1 / R_0)) - i_0) / i_0 * exponential_term))
        
        i += (i_t * delta_t)
        analytical_i = (analytical_soln * delta_t) + analytical[-1]
        
        t += delta_t
        time.append(t)
        
        infected.append(i)
        analytical.append(analytical_soln)
        
    return [susceptibles, infected, time, analytical]

beta = 3
gamma = 2
s0, i0 = 0.99, 0.01
max_t = 25

def plots(dt, label): 
    steps = int(max_t / dt) + 1 
    time = np.linspace(0, max_t, steps)
    
    # Use forward_euler_solver to get the results
    results = forward_euler_solver(beta, gamma, s0, i0, dt, max_t)
    susceptibles, infected, solver_time, analytical = results
    
    plt.plot(time, infected[:len(time)], 'r-', label='forward euler')
    plt.plot(solver_time, analytical, 'k--', label='Analytical')
    
    plt.xlabel('Time(t)')
    plt.ylabel('I(t)')
    plt.title('SIS Model')
    plt.legend()
    plt.ylim([0, 0.5])
    plt.show()
    # plt.savefig('sahana.png')

plots(dt=2, label='step size = 2')
plots(dt=1, label='step size = 1')
plots(dt=0.5, label='step size = 0.5')