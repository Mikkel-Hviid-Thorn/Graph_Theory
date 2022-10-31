# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 17:41:29 2020

@author: Mikkel Hviid Thorn
"""

import random as r


def euklidisk(n):
    V, points = [], dict()
    for i in range(n):
        V.append(str(i))
        points[V[-1]] = [10*r.random(),10*r.random()]
        
    E = []
    for i in range(n-1):
        for j in range(i+1,n):
            xi, yi = points[str(i)]
            xj, yj = points[str(j)]
            l = ((xj-xi)**2 + (yj-yi)**2)**(1/2)
            E.append([str(i),str(j),l])
            
    return V, E, points


import matplotlib.pyplot as plt
import Grafteori_module as graf

def den_handelsrejsendes_problem():
    
    V, E, points = euklidisk(10)
    
    G = []
    for e in E:
        G += e[:2]
        
    x,y = [],[]
    for v in G:
        vx, vy = points[v]
        x.append(vx); y.append(vy)
    
    H_bf, w_bf = graf.brute_force(V, E)
    H_nn, w_nn = graf.nærmest_nabo(V, E)
    H_na, w_na = graf.nærmest_addition(V, E)
    
    H_dt, w_dt = graf.dobbelttræ(V, E)
    H_cf, w_cf = graf.christofides(V, E)
    H_op, w_op = graf.opt2(V, E)
    
    H_hu, w_hu = graf.hungarian(V, E)
    H_ma, w_ma = graf.my_algorithm(V, E)
    H_ao, w_ao = graf.ant_optimization(V, E, 10000)
    
    
    x_bf, y_bf = [], []; x_nn, y_nn = [], []; x_na, y_na = [], []
    x_dt, y_dt = [], []; x_cf, y_cf = [], []; x_op, y_op = [], []
    x_hu, y_hu = [], []; x_ma, y_ma = [], []; x_ao, y_ao = [], []
    
    for v in H_bf:
        vx, vy = points[v]
        x_bf.append(vx); y_bf.append(vy)
    for v in H_nn:
        vx, vy = points[v]
        x_nn.append(vx); y_nn.append(vy)
    for v in H_na:
        vx, vy = points[v]
        x_na.append(vx); y_na.append(vy)
        
    for v in H_dt:
        vx, vy = points[v]
        x_dt.append(vx); y_dt.append(vy)
    for v in H_cf:
        vx, vy = points[v]
        x_cf.append(vx); y_cf.append(vy)
    for v in H_op:
        vx, vy = points[v]
        x_op.append(vx); y_op.append(vy)
        
    for v in H_hu:
        vx, vy = points[v]
        x_hu.append(vx); y_hu.append(vy)
    for v in H_ma:
        vx, vy = points[v]
        x_ma.append(vx); y_ma.append(vy)
    for v in H_ao:
        vx, vy = points[v]
        x_ao.append(vx); y_ao.append(vy)
    
    fig, axs = plt.subplots(3, 3)
    #fig.suptitle('Den Handelsrejsendes Problem')
    
    (ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9) = axs
    ax1.plot(x, y, color='darkgray', linewidth=0.5)
    ax1.plot(x_bf, y_bf, 'o-', color='firebrick', linewidth=1)
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.set_title('Brute Force '+str(round(w_bf,2)), fontsize=12)
    
    ax2.plot(x, y, color='darkgray', linewidth=0.5)
    ax2.plot(x_nn, y_nn, 'o-', color='firebrick', linewidth=1)
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.set_title('Nærmest nabo '+str(round(w_nn,2)), fontsize=12)
    
    ax3.plot(x, y, color='darkgray', linewidth=0.5)
    ax3.plot(x_na, y_na, 'o-', color='firebrick', linewidth=1)
    ax3.set_xticks([])
    ax3.set_yticks([])
    ax3.set_title('Nærmest addition '+str(round(w_na,2)), fontsize=12)
    
    ax4.plot(x, y, color='darkgray', linewidth=0.5)
    ax4.plot(x_dt, y_dt, 'o-', color='firebrick', linewidth=1)
    ax4.set_xticks([])
    ax4.set_yticks([])
    ax4.set_title('Dobbelttræ '+str(round(w_dt,2)), fontsize=12)
    
    ax5.plot(x, y, color='darkgray', linewidth=0.5)
    ax5.plot(x_cf, y_cf, 'o-', color='firebrick', linewidth=1)
    ax5.set_xticks([])
    ax5.set_yticks([])
    ax5.set_title('Christofides '+str(round(w_cf,2)), fontsize=12)
    
    ax6.plot(x, y, color='darkgray', linewidth=0.5)
    ax6.plot(x_op, y_op, 'o-', color='firebrick', linewidth=1)
    ax6.set_xticks([])
    ax6.set_yticks([])
    ax6.set_title('2opt '+str(round(w_op,2)), fontsize=12)
    
    ax7.plot(x, y, color='darkgray', linewidth=0.5)
    ax7.plot(x_hu, y_hu, 'o-', color='firebrick', linewidth=1)
    ax7.set_xticks([])
    ax7.set_yticks([])
    ax7.set_title('Hungarian '+str(round(w_hu,2)), fontsize=12)
    
    ax8.plot(x, y, color='darkgray', linewidth=0.5)
    ax8.plot(x_ma, y_ma, 'o-', color='firebrick', linewidth=1)
    ax8.set_xticks([])
    ax8.set_yticks([])
    ax8.set_title('Min algoritme '+str(round(w_ma,2)), fontsize=12)
    
    ax9.plot(x, y, color='darkgray', linewidth=0.5)
    ax9.plot(x_ao, y_ao, 'o-', color='firebrick', linewidth=1)
    ax9.set_xticks([])
    ax9.set_yticks([])
    ax9.set_title('Ant optimization '+str(round(w_ao,2)), fontsize=12)

den_handelsrejsendes_problem()

def kortest_sti():
    
    V, E, points = euklidisk(10)
    
    E = []
    for i in range(9):
        k = 0
        for j in range(i+1,10):
            if k == 3:
                break
            xi, yi = points[str(i)]
            xj, yj = points[str(j)]
            l = ((xj-xi)**2 + (yj-yi)**2)**(1/2)
            E.append([str(i),str(j),l])
            k += 1
    
    G = []
    for e in E:
        G += e[:2]
        
    x,y = [],[]
    for v in G:
        vx, vy = points[v]
        x.append(vx); y.append(vy)
    
    S_di, w_di = graf.dijkstras(V, E, V[0], V[-1])
    x_di, y_di = [], []
    for v in S_di:
        vx, vy = points[v]
        x_di.append(vx); y_di.append(vy)
    
    S_gr, w_gr = graf.graadig(V, E, V[0], V[-1])
    x_gr, y_gr = [], []
    for v in S_gr:
        vx, vy = points[v]
        x_gr.append(vx); y_gr.append(vy)
    
    fig, axs = plt.subplots(2, 1)
    #fig.suptitle('Kortest sti')
    
    (ax1, ax2) = axs
    ax1.plot(x, y, 'o-', color='darkgray', linewidth=0.5)
    ax1.plot(x_di, y_di, 'o-', color='navy', linewidth=1)
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.set_title('Dijkstras algoritme '+str(round(w_di,2)), fontsize=12)
    
    ax2.plot(x, y, 'o-', color='darkgray', linewidth=0.5)
    ax2.plot(x_gr, y_gr, 'o-', color='navy', linewidth=1)
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.set_title('Grådig algoritme '+str(round(w_gr,2)), fontsize=12)

kortest_sti()

def minimum_udspændende_træer():
    
    V, E, points = euklidisk(10)
    
    G = []
    for e in E:
        G += e[:2]
        
    x,y = [],[]
    for v in G:
        vx, vy = points[v]
        x.append(vx); y.append(vy)
    
    V_p, E_p = graf.prims(V, E)
    
    fig, axs = plt.subplots(1, 1)
    #fig.suptitle('Kortest sti')
    
    ax1 = axs
    ax1.plot(x, y, 'o-', color='darkgray', linewidth=0.5)
    for e in E_p:
        x_p, y_p = [], []
        for v in e[:2]:
            vx, vy = points[v]
            x_p.append(vx); y_p.append(vy)
        ax1.plot(x_p, y_p, 'o-', color='forestgreen', linewidth=2)
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.set_title('Prims algoritme', fontsize=20)

#minimum_udspændende_træer()

def maksimal_minimum_parring():
    V, E, points = euklidisk(10)
    
    G = []
    for e in E:
        G += e[:2]
        
    x,y = [],[]
    for v in G:
        vx, vy = points[v]
        x.append(vx); y.append(vy)
        
    M = graf.min_maximal_matching(V, E)
    
    fig, axs = plt.subplots(1, 1)
    #fig.suptitle('Kortest sti')
    
    ax1 = axs
    ax1.plot(x, y, 'o-', color='darkgray', linewidth=0.5)
    for e in M:
        x_m, y_m = [], []
        for v in e[:2]:
            vx, vy = points[v]
            x_m.append(vx); y_m.append(vy)
        ax1.plot(x_m, y_m, 'o-', color='black', linewidth=2)
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.set_title('Maksimal minimum parring', fontsize=20)

#maksimal_minimum_parring()    
