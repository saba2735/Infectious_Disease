import numpy as np
from scipy.stats import nbinom
import matplotlib.pyplot as plt

def simulate_branching_process(R0, k, generations):
    infections = np.array([1])
    outbreaks = []

    mean = R0
    vary = mean + (mean**2) / k
    prob = mean / vary
    n = mean**2 / (vary - mean)

    for _ in range(generations): 
        new_infections = np.random.negative_binomial(n=n, p=prob, size=len(infections))
        infections = np.concatenate((infections, new_infections))  # Wrap arrays in a tuple
        if np.sum(new_infections) == 0:
            outbreaks.append(len(infections))
            break
        outbreaks.append(len(infections)) # No need to continue if the epidemic dies out early
    return outbreaks

def prob_of_dying_out(R0, k, generations, trials): 
    count_die = 0
    outbreaks = []
    for _ in range(trials): 
       outbreak = simulate_branching_process(R0,k,generations)
       if len(outbreak) == generations + 1:
           count_die += 1
       else: 
           outbreaks.extend(outbreak)
    probability = count_die/trials
    return probability,outbreaks

R0_vals = 3.0
k_values = 10
generations = 10 
trials = 100000

probability, outbreaks = prob_of_dying_out(R0_vals,k_values,generations,trials)


plt.figure(figsize=(10,6))
plt.hist(outbreaks,bins = 10, alpha = 0.7)
plt.title(f"Outbreaks of size k = {k_values}")
plt.xlabel("size of outbreaks")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()