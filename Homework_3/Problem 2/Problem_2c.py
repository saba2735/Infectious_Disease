import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def SI_model(susceptibilities, I0_percentage, probabilities, omega, gamma, c_avg, delta_t):
    D_S = np.diag(susceptibilities)
    D_P = np.diag(probabilities)
    D_gamma = np.diag(gamma)
    D_inverse_omega = np.linalg.inv(np.diag(omega))
    Multiply_together = np.dot(np.dot(np.dot(D_S, D_P), c_avg), D_inverse_omega)
    dS_dt = -np.dot(Multiply_together,I0_percentage)
    dI_dt = np.dot(Multiply_together,I0_percentage) - np.dot(D_gamma,I0_percentage)
    new_S = susceptibilities + (dS_dt * delta_t)
    new_I = I0_percentage + (dI_dt * delta_t)

    return new_S, new_I
    
# Parameters
c_avg = np.array([[0.45, 0.45, 0.45, 0.45],
                  [0.45, 0.45, 0.45, 0.45],
                  [0.45, 0.45, 0.45, 0.45],
                  [0.45, 0.45, 0.45, 0.45]])  # Average contact rate
susceptibilities = np.array([0.99, 0.99, 0.99, 0.99])  # Susceptibilities for groups 1 to 4
probabilities = np.array([1, 2, 3, 4])
I0_percentage = np.array([0.001, 0.001, 0.001, 0.001])
gamma = np.array([3, 3, 3, 3])  # Recovery rate
omega = np.array([0.25, 0.25, 0.25, 0.25])


# Simulation parameters
max_time = 3  # Maximum simulation time
delta_t = 0.001
iterates = int(max_time / delta_t)  # Time step (smaller value for smoother curves)

# Simulation
time_points = np.linspace(0, max_time, iterates)
values_s = susceptibilities 
values_i = I0_percentage
for i in range(iterates - 1):
    susceptibilities, I0_percentage = SI_model(susceptibilities, I0_percentage, probabilities, omega, gamma, c_avg, delta_t)
    values_s = np.vstack((values_s, susceptibilities))
    values_i = np.vstack((values_i, I0_percentage))

lines = len(values_i[0])
colors = sns.color_palette("Greens", n_colors=lines)

for n in range(lines):
    lower_i = values_i[:, n]
    plt.plot(time_points, lower_i, label=f"Group {n+1} Sahana", color=colors[n])
    plt.grid(True)

# Plotting
plt.title('Epidemic Wave Simulation --Sahana')
plt.xlabel('Time')
plt.ylabel('Proportion of Infected Individuals')
plt.ylim(0,0.6)
plt.legend()
plt.show()

