import matplotlib.pyplot as plt
import numpy as np 

def f(r,R0): 
    return r 
def g(r, R0): 
    return 1 - np.exp(-R0*r)

R0_values = [0.9,1.0,1.1,1.2]

fig, axs = plt.subplots(2,2,figsize = (10,8))
axs = axs.flatten()
for i, R0 in enumerate(R0_values):
    r_values = np.linspace(0,1,100)
    axs[i].plot(r_values, f(r_values,R0),color = 'red', label = 'f(r_infinity)')
    axs[i].plot(r_values, g(r_values,R0), color = 'black', label = 'g(r_infinity)')
    intersect = fsolve(lambda r: f(r,R0)-g(r,R0),0.5)[0]
    axs[i].scatter(intersect, f(intersect,R0),color = 'blue', label = 'Intersection')
    axs[i].set_xlabel('r_infinity')
    axs[i].set_ylabel('Value')
    axs[i].set_title(f'R0 = {R0}')
for ax in axs :
    ax.legend()
    plt.tight_layout()
    plt.show()