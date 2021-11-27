# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 08:31:44 2021

@author: sasid
"""

import numpy as np
import matplotlib.pyplot as plt
#scipy
import vibration_toolbox as vtb
m0,m1,m2 = 7.5, 9, 6
k0,k1,k2=7000,15500,160
c0,c1,c2=100,0.1,45
# m0, m1, m2 = map(complex,input("Enter M1,M2,M3").split())
# k0, k1, k2 = map(complex,input("Enter K1,K2,K3").split())
alpha, beta = 1e-3, 1e-3
#proportional damping assumed
mass = np.array([[m0, 0, 0],
              [0, m1, 0],
              [0, 0, m2]])
spring = np.array([[k0+k1, -k1,   0],
              [-k1, k1+k2, -k2],
              [0,     -k2,  k2]])
#damper = alpha*mass + beta*spring
damper=np.array([[c0+c1,-c1,0],[-c1,c1+c2 ,-c2],[0,-c2,c2]])
print(damper)
sys = vtb.VibeSystem(mass, damper, spring, name='3 dof system')
print(" Natural frequencies : ",sys.wn)
print(" Damped frequencies : ",sys.wd)
f = plt.figure()
f.set_figwidth(10)
f.set_figheight(10)

ax = sys.plot_freq_response(0, 0)
#print(ax)

t = np.linspace(0, 25, 1000)
# force array with len(t) rows and len(inputs) columns
F1 = np.zeros((len(t), 3))
# in this case we apply the force only to the mass m1
F1[:, 1] = 1000*np.sin(40*t)
f = plt.figure()
f.set_figwidth(10)
f.set_figheight(10)


axs = sys.plot_time_response(F1, t)
t, yout, xout = sys.time_response(F1, t)

f = plt.figure()
f.set_figwidth(10)
f.set_figheight(10)
t, yout, xout = sys.time_response(F1, t)
ax = vtb.plot_fft(t, time_response=yout[:, 0])
