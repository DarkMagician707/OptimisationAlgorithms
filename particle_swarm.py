import numpy as np
import math
from tabulate import tabulate

import numpy as np
import math
from tabulate import tabulate

def particle_swarm(S, x_ini, iterations, w, C1, C2, random_num):

    def f(x):
        # Change for specific problem
        return -x[0]**3 +3*x[0] - x[1]**2
    
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
            velocities[i][0] = w*velocities[i][0] + p1*C1*(p_best[i][0] - x[i][0]) + p2*C2*(x_opt[0] - x[i][0])
            p1 = random_num.pop(0)
            p2 = random_num.pop(0)
            velocities[i][1] = w*velocities[i][1] + p1*C1*(p_best[i][1] - x[i][1]) + p2*C2*(x_opt[1] - x[i][1])
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
    print(str(x))
    print(str(x_opt))
    print(str(velocities))
    print(str(f_values))

# Change for specific problem
x_initial = np.array([[0.3, -0.2], [-0.9, 0.5], [-0.4, 0.5], [0.9, 0.7], [-0.4, -0.5]])
random_num = [0.43, 0.32, 0.77, 0.52, 0.45, 0.31, 0.98, 0.04, 0.89, 0.91, 0.46, 0.65, 0.12, 0.68, 0.81, 0.91, 0.13, 0.91, 0.63, 0.10, 0.28, 0.55, 0.96, 0.96, 0.16, 0.97, 0.96, 0.49, 0.80, 0.14, 0.42, 0.92, 0.79, 0.96, 0.66, 0.04, 0.85, 0.93, 0.68, 0.76, 0.74, 0.39, 0.66, 0.17]
particle_swarm(5, x_initial, 6, 0.8, 0.2, 0.2, random_num)