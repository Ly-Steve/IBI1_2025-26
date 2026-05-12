import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib
matplotlib.use('Agg')

# initially
population = np.zeros((100, 100))   # 0=Susceptible, 1=Infected, 2=Recovered

# Randomly select one initial infected individual
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1


beta = 0.3
gamma = 0.05


"""
for each of 100 time steps:
# Step 1: Recovery
    Find all infected positions (where population == 1)
    For each infected cell:
        With probability gamma, change its state to 2 (recovered)
    
    # Step 2: Infection of neighbours
    Find all infected positions again
    For each infected cell (x, y):
        Check its 8 neighbouring cells
        For each neighbour (nx, ny):
            If the neighbour is within grid boundaries and is susceptible (0):
                With probability beta, infect it (set to 1)
    
    # Step 3: Save visualization
    if t % 10 == 0 or t == 99:
        Plot the current population as a heatmap and save the image
"""

script_dir = os.path.dirname(os.path.abspath(__file__))

for t in range(100):
    # Recovery
    infected_positions = np.argwhere(population == 1)
    for pos in infected_positions:
        if np.random.rand() < gamma:
            population[pos[0], pos[1]] = 2
    
    # Infection of neighbours
    infected_positions = np.argwhere(population == 1)
    for pos in infected_positions:
        x, y = pos
        neighbors = [(-1,-1), (-1,0), (-1,1),
                     (0,-1),          (0,1),
                     (1,-1),  (1,0),  (1,1)]
        for dx, dy in neighbors:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 100 and 0 <= ny < 100 and population[nx, ny] == 0:
                if np.random.rand() < beta:
                    population[nx, ny] = 1
    
    # Save plot every 10 steps and at the end
    if t % 10 == 0 or t == 99:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f'Spatial SIR - Time {t}')
        
        save_path = os.path.join(script_dir, f'spatial_time_{t}.png')
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        plt.close()
        print(f"spatial_time_{t}.png is saved")

print("All spatial SIR images are saved successfully！")