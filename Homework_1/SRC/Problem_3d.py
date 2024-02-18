import matplotlib.pyplot as plt 
import numpy as np
from scipy.optimize import fsolve 

def SIR_model(N,S0,I0,R0,beta,gamma,times):
    S, I, R = S0, I0, 0 
    dt = 1 

    S_list, I_list, R_list = [S], [I], [R]

    for time in range(1,times+1):
        dS = ((-beta*S*I/N) * dt) 
        dI = (((beta*S*I/N)-(gamma*I))*dt) 
        dR = ((gamma*I)*dt)

        S += dS 
        I += dI
        R += dR

        S_list.append(S)
        I_list.append(I)
        R_list.append(R)

    return np.array(S_list), np.array(I_list), np.array(R_list)

N = 1000 
S0 = 999
I0 = 1
R0 = 0
beta = 1
times = 50



Params = [
                {"beta":1,"gamma":0.5, "label": "Beta = 1, gamma = 0.5"},
                # {"beta":1.5, "gamma":0.5, "label": "Beta = 1.5, gamma = 0.5"},
                # {"beta":2,"gamma":0.5, "label": "Beta = 2, gamma = 0.5"}
            ]
for Param in Params: 
    beta = Param["beta"]
    gamma = Param["gamma"]
    label= Param["label"]
    R_naught = beta/gamma

    S,I,R = SIR_model(N,S0, I0, R0, beta, gamma, times)
    r_infinity = fsolve(lambda r: r - (1-np.exp(-R_naught*r)),0.5)
    print(r_infinity)
    
    fig, ax = plt.subplots()
    ax.plot(range(times+1),S,label="S Sahana", linestyle = 'dashed')
    ax.plot(range(times+1),I,label="I Sahana",linestyle = 'solid')
    ax.plot(range(times+1),R,label="R Sahana", linestyle = 'dotted')
    plt.axhline(y = r_infinity, color = 'green', linestyle = 'dotted', label = 'f(r_infinity)')

    ax.set_xlabel("time")
    ax.set_ylabel("People")
    ax.legend()
    ax.set_title("SIR Model Sahana")
    ax.grid(True)