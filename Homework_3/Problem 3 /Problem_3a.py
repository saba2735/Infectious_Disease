import numpy as np
from scipy.stats import nbinom

def simulate_branching_process(R0, k, generations):
    infections = np.array([1])

    for _ in range(generations):
        mean = R0
        vary = mean + (mean**2) / k
        prob = mean / vary
        n = mean**2 / (vary - mean)
        new_infections = nbinom.rvs(n=n, p=prob, size=len(infections))
        infections = np.concatenate((infections, new_infections))  # Wrap arrays in a tuple
        if np.sum(new_infections) == 0: # No need to continue if the epidemic dies out early
            return True
    return False

def prob_of_dying_out(R0, k, generations, trials): 
    count_die = sum(simulate_branching_process(R0, k, generations) for _ in range(trials))
    return count_die / trials

R0_vals = [3]
k_values = [0.1, 0.5, 1.0, 5.0, 10.0]
generations = 10 
trials = 100000
results = {}

for R0 in R0_vals: 
    for k in k_values: 
        die_out = prob_of_dying_out(R0, k, generations, trials)
        results[(R0, k)] = die_out

with open("probability_of_epidemic.txt", "w") as file: 
    file.write("Probability of not dying out:\n")
    file.write("R0\tk\tProbability (1 - q)\n")
    for R0, k in sorted(results.keys()):
        file.write(f"{R0}\t{k}\t{results[(R0, k)]:.3f}\n")

print("Table has been written to 'probability_of_epidemic.txt'.")
