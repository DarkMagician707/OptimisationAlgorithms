import numpy as np
import math
from tabulate import tabulate

def tabu(x_current, eps):
    # Change for specific problem:
    def f(x1, x2):
        return (x1 - 3.14)**2 + (x2 - 2.72)**2 + math.sin(3*x1 + 1.41) + math.sin(4*x2 - 1.73)

    k = 0
    tabu_list = {}
    flag = True
    answer_table = []
    x_opt = x_current
    # Counts how many times a non-optimal x is chosen as the current, since termination criteria is that non-optimals may only chosen 5 times
    # Directly after eachother before terminating search
    count = 0
    while flag:
        fx = f(x_current[0], x_current[1])
        x1 = [x_current[0] + eps, x_current[1]]
        fx1 = f(x1[0], x1[1])
        x2 = [x_current[0] - eps, x_current[1]]      
        fx2 = f(x2[0], x2[1])
        x3 = [x_current[0], x_current[1] + eps]
        fx3 = f(x3[0], x3[1])
        x4 = [x_current[0], x_current[1] - eps]
        fx4 = f(x4[0], x4[1])
        fx_opt = f(x_opt[0], x_opt[1])
        neighbourhood = [x1, x2, x3, x4]
        f_neighbourhood = [fx1, fx2, fx3, fx4]
        row = [k, x_current, fx, x_opt, fx_opt, neighbourhood, f_neighbourhood, tuple(tabu_list.keys())]
        answer_table.append(row)
        n_temp = neighbourhood[:]
        f_temp = f_neighbourhood[:]
        temp_flag = True
        # Find the new current:
        while temp_flag:
            current_min_f = min(f_temp)
            index = f_temp.index(current_min_f)
            # Check if current best is in tabu list. Note: no aspiration criteria included
            if f_neighbourhood.index(current_min_f) in tabu_list.keys():
                f_temp.pop(index)
                n_temp.pop(index)
            else:
                f_index = f_neighbourhood.index(f_temp[index])
                x_current = neighbourhood[f_index]
                fx = f_temp[index]
                # First decrement tabu list:
                for key in tabu_list:
                    tabu_list[key] -= 1

                # Remove all points in the tabu list whose count is zero
                keys_to_remove = []
                for key, value in tabu_list.items():
                    if value == 0:
                        keys_to_remove.append(key)
                for key in keys_to_remove:
                    del tabu_list[key]

                # Add to tabu list
                if neighbourhood.index(x_current)%2 == 0:
                    # Point can only be in tabu list for 3 iterations
                    tabu_list[neighbourhood.index(x_current)+1] = 3
                else:
                    tabu_list[neighbourhood.index(x_current)-1] = 3
                temp_flag = False

        if fx < fx_opt:
            x_opt = x_current
            fx_opt = fx
            count = 0
        else:
            count = count +1
        # Termination criteria
        if count > 5:
            flag = False
        else:
            k += 1
    
    print(tabulate(answer_table, headers=['k','x_current', 'f(x_current)','x_opt','f(x_opt)','Neighbourhood','f(Neighbourhood)', 'Tabu List'], tablefmt='fancy_grid'))

tabu([1, 1], 0.3)