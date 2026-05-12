import numpy as np
import matplotlib.pyplot as plt
import os  

import matplotlib
matplotlib.use('Agg')

N = 10000 #total population
beta = 0.3 #infection pasibility
gamma = 0.05 #recovery pasibiility

S = 9999
I = 1
R = 0

susceptible = [S]
infected = [I]
recovered = [R]

for t in range(1000):
    if S > 0:
        prob_infect = beta * (I / N)
        new_infected = np.random.choice([0, 1], size=S, p=[1 - prob_infect, prob_infect]).sum()
    else:
        new_infected = 0

    if I > 0:
        new_recovered = np.random.choice([0, 1], size=I, p=[1 - gamma, gamma]).sum()
    else:
        new_recovered = 0

    S = S - new_infected
    I = I + new_infected - new_recovered
    R = R + new_recovered

    susceptible.append(S)
    infected.append(I)
    recovered.append(R)

script_dir = os.path.dirname(os.path.abspath(__file__))

plt.figure(figsize=(6, 4), dpi=150)
plt.plot(susceptible, label='susceptible', color='blue')
plt.plot(infected, label='infected', color='orange')
plt.plot(recovered, label='recovered', color='green')
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend()

save_path = os.path.join(script_dir, 'SIR_model.png')
plt.savefig(save_path, dpi=150, bbox_inches='tight')
plt.close()

print("Picture saved successfully")
print("Location：", save_path)