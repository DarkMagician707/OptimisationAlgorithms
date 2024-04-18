import numpy as np
import math
from tabulate import tabulate

def local(x_opt, a, eps, e_tol):
    # Change for specific problem
    def f(x1, x2):
        return -(x1)**2 - 4*(x2)**2 +2*x1 +8*x2 - 5
   
    answer_table = []
    while eps > e_tol:
        k = 0
        flag = True
        while flag:
            # Change this depending on problem dimensions
            fx = f(x_opt[0], x_opt[1])
            x1 = [x_opt[0] + eps, x_opt[1]]
            fx1 = f(x1[0], x1[1])
            x2 = [x_opt[0] - eps, x_opt[1]]      
            fx2 = f(x2[0], x2[1])
            x3 = [x_opt[0], x_opt[1] + eps]
            fx3 = f(x3[0], x3[1])
            x4 = [x_opt[0], x_opt[1] - eps]
            fx4 = f(x4[0], x4[1])
            neighbourhood = [x1, x2, x3, x4]
            f_neighbourhood = [fx1, fx2, fx3, fx4]
            row = [k, x_opt, fx, neighbourhood, f_neighbourhood]
            answer_table.append(row)
            # Change for specific problem
            if fx != max(fx, max(f_neighbourhood)):
                index = f_neighbourhood.index(max(f_neighbourhood))
                x_opt = neighbourhood[index]
                k = k+1
            else:
                flag = False
        eps = a*eps
    print(tabulate(answer_table, headers=['k','x_opt', 'f(x)','Neighbourhood','f(Neighbourhood)'], tablefmt='fancy_grid'))

local([0, 0.5], 0.5, 0.3, 0.01)