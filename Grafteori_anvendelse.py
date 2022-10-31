# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 19:22:28 2020

@author: Mikkel Hviid Thorn

Testfil for funktionerne i Grafteori
"""

import Grafteori_module as graf

#Euklidiske grafer

#graf.den_handelsrejsendes_problem(10)

#graf.kortest_sti(14)

#graf.minimum_udspændende_træer(100)

#graf.maksimal_minimum_parring(6)

#graf.tree_mod_dhp(100)



#Eksempel fra P1 projekt

V = ['v1','v2','v3','v4','v5','v6','v7','v8','v9','v10']
E = [['v1','v3',25],['v1','v4',30],['v1','v5',41],['v1','v7',27],['v1','v9',42],['v1','v10',26],['v2','v4',25],['v2','v5',28],['v2','v7',36],['v2','v9',31],['v2','v10',38],['v3','v4',26],['v3','v5',22],['v3','v6',35],['v3','v7',23],['v3','v9',30],['v4','v5',28],['v4','v6',22],['v4','v7',33],['v4','v8',100],['v4','v9',31],['v4','v10',33],['v5','v6',27],['v5','v8',31],['v5','v10',46],['v6','v9',32],['v6','v10',41],['v7','v8',37],['v7','v9',22],['v7','v10',22],['v8','v9',38],['v9','v10',34]]
E = graf.make_complete(V,E)

"""
print(graf.prims_mod(V,E))
print(graf.kruskals_mod(V,E))
print(graf.boruvkas_mod(V,E))

#graf.test_dhp_alg(V,E,  bf='y', nn='y', na='y', dt='y', cf='y', op='y', hu='y', ma='y', ao='y')
"""

#Tester random grafer

#graf.test_dhp_alg_repeat(10,5,  bf='n', nn='n', na='n', dt='n', cf='n', op='n', hu='n', ma='n', ao='n')



# Præsentation eksempel
V = ['v1','v2','v3','v4','v5']
E = [['v1','v2',11],['v1','v3',15],['v1','v4',17],['v1','v5',18],['v2','v3',13],['v2','v4',12],['v2','v5',16],['v3','v4',14],['v3','v5',10],['v4','v5',19]]

#graf.test_dhp_alg(V,E,  bf='y', nn='y', na='n', dt='y', cf='y', op='n', hu='n', ma='y', ao='n')



#Test af Eulerkreds algoritmer.
#Eksempel grafer G1=(V1,E1) og G2=(V2,E2)

V1 = ['a','b','c','d','e','z']
E1 = [['a','b'],['a','d'],['b','c'],['c','z'],['d','e'],['e','z']] 

V2 = ['a','b','c','d','e','f']
E2 = [['a','b'],['a','d'],['b','c'],['c','d'],['c','e'],['c','f'],['e','f']]+[['b','d'],['b','f'],['d','e'],['e','f']]

#graf.test_eulersti_alg(V1,E1,   fu='n')



#Test af kortest sti algoritmer. 
#Eksempel grafer G1=(V1,E1) og G2=(V2,E2).

V1 = ['a','b','c','d','e','z']
E1 = [['a','b',5],['a','d',8],['b','c',4],['b','e',3],['c','z',2],['d','e',1],['e','z',3]] 

V2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
E2 = [['b','e',1],['a','b',2],['a','c',4],['b','e',60],['b','g',10],['b','d',7],['c','d',3],['d','f',4],['e','h',6],['f','g',2],['g','h',3],['g','k',9],['h','i',2],['h','l',4],['h','j',7],['k','j',1],['k','m',8],['j','m',3],['l','m',5]]

#graf.test_sti_alg(V2,E2,'a','k',    di='n', fl='n', gr='n')



#Test af udspændende træ algoritmer. 
#Eksempel graf gt.

gt = {'1':['2','4','5','10'],'2':['1','3','5','11'],'3':['2','5','6'],'4':['1','5','7'],'5':['1','2','3','4','6','7','8','9'],'6':['3','5','9'],'7':['4','5','8'],'8':['5','7','9'],'9':['5','6','8'],'10':['1'],'11':['2']}
  
#graf.test_trae_alg(gt,    DFS='n', BFS='n')



#Test af minimum udspændende træ algoritmer. 
#Eksempel grafer G1=(V1,E1), G2=(V2,E2) og G3=(V3,E3).

V1 = ['a','b','c','d','e','f']
E1 = [['a','b',7],['a','c',3],['a','d',10],['b','c',6],['b','d',4],['c','d',11],['c','e',5],['c','f',8],['d','e',1],['d','f',9],['e','f',2]]

V2 = ['a','b','c','d','e']
E2 = [['a','b',50],['b','c',50],['b','d',1],['b','e',1],['d','e',1]]

V3 = ['a','b','c','d','e']
E3 = [['a','b',5],['a','c',4],['a','d',6],['a','e',1],['b','c',2],['b','d',8],['b','e',9],['c','d',10],['c','e',3],['d','e',7]]

graf.test_min_trae_alg(V1,E1,   p='n', k='n', b='n')



#Tre nabo ordbøger for tre grafer. De tre grafer er fra Programmering for matematikere kursus gang 6.

g1 = {'a':['c'],'b':['c'],'c':['a','b']}
g2 = {'a':['a','b','c','d'],'b':['a','b','c','d'],'c':['a','b','c','d'],'d':['a','b','c','d']}
g3 = {'a':['c','d','f'],'b':['d','e','g'],'c':['a','e','h'],'d':['a','b','i'],'e':['b','c','j'],'f':['a','g','j'],'g':['b','f','h'],'h':['c','g','i'],'i':['d','h','j'],'j':['e','i','f']}                      

#Tester make_graph, generate_vertices og generate_edges

#print(graf.make_graph(graf.generate_vertices(g2),graf.generate_edges(g2))==g2)