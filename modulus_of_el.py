# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 18:33:02 2023

@author: GoffX
"""

import numpy as np
import matplotlib.pyplot as plt

def E_ci(alpha_E: float, f_ck: float) -> float:
    '''The function returns modulus of elasticity according
    formula 7-1 FIB70'''
    
    E_c0 = 21.5*10**3 #MPa
    delta_f = 8 #MPa
    E_ci = E_c0 * alpha_E * ((f_ck + delta_f)/10)**(1/3) #MPa
    
    return E_ci #MPa

def E_c(E_ci: float, f_cm: float) -> float:
    '''The function returns modulus of elasticity according
    formula 7-2 FIB70'''
    
    alpha_i = np.where(0.8 + 0.2 * f_cm/88 >= 1, 1, 0.8 + 0.2 * f_cm/88)
            
    E_c = alpha_i * E_ci #MPa
    
    return E_c #MPa

def E_c_ACI(f_c: float) -> float:
    '''The function returns modulus of elasticity according
    formula 19.2.2.1.b ACI 318M-19'''
    
    E_c_ACI = 4700 * np.sqrt(f_c) #MPa
    
    return E_c_ACI #MPa    

f_ck_arr = np.linspace(12, 120)
f_ck_arr_EN = np.linspace(12, 55)

f_cm = f_ck_arr + 8

E_c = E_c(E_ci(1, f_ck_arr), f_cm)/1000 #GPa

E_c_ACI = E_c_ACI(f_ck_arr_EN)/1000 #GPa

plt.plot(f_ck_arr, E_c, label='FIB 70')
plt.plot(f_ck_arr_EN, E_c_ACI, label='ACI 318M-19')
plt.xlabel(r'$f_{ck}\ [MPa]$')
plt.ylabel(r'$E_c\ [GPa]$')
plt.title('Modulus of Elasticity')
plt.grid(True)
plt.annotate(r'$Inflection\ point$', xy=(80, 44.4), xytext=(90, 40),\
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.legend()
plt.show()