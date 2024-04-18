import numpy as np
import math
from tabulate import tabulate
import sympy as sp

# Golden Section Search for Univariate funtion
def uniGolden(a, b, e_tol):
    def f(x):
        # Change for specific problem
        return 1+2*(x)**2-np.exp(x)
    phi = 0.618034
    omega = math.ceil(np.emath.logn(phi, (e_tol)/(b-a)))
    answer_table = []
    for k in range(0, omega):
        alpha = b - phi*(b-a)
        beta = a + phi*(b-a)
        row = [k, a, b, alpha, beta]
        answer_table.append(row)
        # Change depending if minimizing/maximixing
        if f(alpha) < f(beta):
            b = beta
        else:
            a = alpha
    
    print(tabulate(answer_table, headers=['k','a_k','b_k','alpha_k','beta_k'], tablefmt='fancy_grid'))

# Golden Section Search for Bivariate function
def biGolden(a1, b1, a2, b2, e_tol):
    def f(x1, x2):
        # Change for specific problem
        return -(x1)**2 - 4*(x2)**2 +2*x1 +8*x2 - 5
    phi = 0.618034
    omega = max(math.ceil(np.emath.logn(phi, (e_tol)/(b1-a1))), math.ceil(np.emath.logn(phi, (e_tol)/(b2-a2))))
    answer_table = []
    for k in range(0, omega):
        alpha1 = b1 - phi*(b1 - a1)
        alpha2 = b2 - phi*(b2 - a2)
        beta1 = a1 + phi*(b1 - a1)
        beta2 = a2 + phi*(b2 - a2)
        A = [a1, a2]
        B = [b1, a2]
        C = [a1, b2]
        D = [b1, b2]
        E = [alpha1, alpha2]
        F = [beta1, alpha2]
        G = [alpha1, beta2]
        H = [beta1, beta2]
        row = [k, a1, b1, a2, b2, A, B, C, D, E, F, G, H]
        answer_table.append(row)

        # Change depending on problem
        if f(E[0], E[1]) == min(f(E[0], E[1]), f(F[0], F[1]), f(G[0], G[1]), f(H[0], H[1])):
            b1 = beta1
            b2 = beta2
        elif f(F[0], F[1]) == min(f(E[0], E[1]), f(F[0], F[1]), f(G[0], G[1]), f(H[0], H[1])):
            a1 = alpha1
            b2 = beta2
        elif f(G[0], G[1]) == min(f(E[0], E[1]), f(F[0], F[1]), f(G[0], G[1]), f(H[0], H[1])):
            b1 = beta1
            a2 = alpha2
        else:
            a1 = alpha1
            a2 = alpha2
        
    print(tabulate(answer_table, headers=['k','a1_k', 'b1_k','a2_k','b2_k','A_k','B_k','C_k','D_k','E_k','F_k','G_k','H_k'], tablefmt='fancy_grid'))

uniGolden(0, 1, 0.0005)
biGolden(0, 2, 0, 1.5, 0.0005)