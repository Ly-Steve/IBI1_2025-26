import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib
matplotlib.use('Agg')

N = 10000
beta = 0.3
gamma = 0.05

vaccination_rates = np.arange(0, 101, 10)

script_dir = os.path.dirname(os.path.abspath(__file__))

plt.figure(figsize=(8, 5), dpi=150)

for vac_rate in vaccination_rates:
    vaccinated = int(N * vac_rate / 100)
    S = N - 1 - vaccinated
    I = 1
    R = 0

    infected_list = [I]

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

        infected_list.append(I)

    plt.plot(infected_list, label=f'{vac_rate}% vaccination')

plt.xlabel('time')
plt.ylabel('number of infected people')
plt.title('SIR model with different vaccination rates')
plt.legend()

save_path = os.path.join(script_dir, 'SIR_vaccination.png')
plt.savefig(save_path, dpi=150, bbox_inches='tight')
plt.close()

print("SIR_vaccination.png is saved successfully！")
print("Location：", save_path)