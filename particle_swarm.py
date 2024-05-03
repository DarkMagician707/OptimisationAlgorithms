import numpy as np
import math
from tabulate import tabulate

def particle_swarm(S, x_ini, iterations, w, C1, C2, random_num):

    def f(x):
        # Change for specific problem
        return 20 + x[0]**2 + x[1]**2 -10*(math.cos(2*math.pi*x[0]) + math.cos(2*math.pi*x[1]))
    
    #Initialize swarm:
    x = np.array((S, 2))
    x = x_ini
    velocities = np.zeros((S, 2))
    p_best = np.array((S, 2))
    p_best = np.copy(x_ini)
    x_opt = x[0]
    answer_table = []
    f_values = []

    for i in range(S):
        f_values.append(np.round(f(x[i]), 3))
        if f(x[i]) > f(x_opt):
            x_opt = x[i]

    for t in range(iterations):
        row = [t, str(x), str(p_best), str(x_opt), str(velocities), str(f_values)]
        f_values.clear()
        
        for i in range(S):   
            p1 = random_num.pop(0)
            p2 = random_num.pop(0)         
            velocities[i] = w*velocities[i] + p1*C1*(p_best[i] - x[i]) + p2*C2*(x_opt - x[i])
            x[i] = x[i] + velocities[i]

            #Change for specific problem
            if f(x[i]) > f(p_best[i]):
                p_best[i] = x[i]
        # Change for specific problem
        for i in range(S):
            if f(x[i]) > f(x_opt):
                x_opt = x[i]
            f_values.append(np.round(f(x[i]), 3))
        answer_table.append(row)        
    print(tabulate(answer_table, headers=['t','Particles', 'p_best', 'x_opt','Velocities','Objective function values'], tablefmt='fancy_grid'))
    
# Change for specific problem
x_initial = np.array([[0.3, -0.2], [-0.9, 0.5], [-0.4, 0.5], [0.9, 0.7], [-0.4, -0.5]])
particle_swarm(5, x_initial, 6, 0.8, 0.2, 0.2, [])