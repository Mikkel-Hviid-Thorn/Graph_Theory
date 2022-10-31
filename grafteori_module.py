# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 20:33:17 2020

@author: Andreas Olsen og Mikkel Hviid Thorn

Modulet er en samling af funktioner og algoritmer indenfor grafteori.
Hver algoritme er også defineret som en funktion.
For at få et overblik anbefales det at minimere alle funktioner.

Flere algoritmer er skrevet ud fra pseudokoder fra:
"Discrete Mathematics and Its Applications 7th edition" Kenneth H. Rosen (2012) Kapitel 10-11

Grafer repræsenteres hovedsageligt i to forme.
1. som en nabo ordbog, hvor hvert punkt er en key og punktets naboliste er den tilhørende value.
2. som to lister, en liste af punkter og en liste af tilhørende kanter.

Til funktionerne som oftere bliver brugt til at danne et ønskede produkt, eller hvor der er 
flere funktioner med samme problemstilling, så er der en test funktion.
"""


"""
De følgende funktioner er basale og ikke brugt videre i algoritmerne.
De er i højere grad relateret til programmering og danner grafer, punkter og kanter.
For tilfældigheden i funktionerne skal seeded slås fra, hvilket vil ændre doctesten.

make_graph funktionen laver en graf af form 2 om til en af form 1.
generate_vertices og generate_edges funktionerne laver en graf af form 1 om til en af form 2.
"""

import random as r
#r.seed(1)


def make_random_graph(n):
    """
    Funktionen skal danne en tilfældig pseodugraf uden dobbelt kanter repræsenteret af en nabo ordbog.
    
    Input
    n -> antallet af punkter i grafen

    Output
    g -> en nabo ordbog for grafen dannet
    
    Eksempel
    #>>> make_random_graph(4)
    #{'0': ['0'], '1': ['3'], '2': ['3'], '3': []}
    """
    
    g = dict() #Nabo ordbogen
    for i in range(n): #Danner et punkt af gangen
        naboer, nabo_list, j = r.randint(0,n-2), [], 0
        while j < naboer: #Danner naboer
            nabo = r.randint(0,n-1)
            if str(nabo) not in nabo_list:
                nabo_list += [str(nabo)]
                j += 1
        g[str(i)] = nabo_list #Tilføjer punktet og nabolisten til ordbogen
    return g


def make_graph(V,E):
    """
    Danner en nabo ordbog for en graf ud fra en liste punkter og en liste kanter.
    Hvis listen af kanter er vægtet, så bliver den information glemt.
    
    Input
    V -> en af liste punkter
    E -> en af liste kanter
    
    Output
    g -> en nabo ordbog for en graf
    
    Eksempel
    >>> make_graph(['1','2','3'],[['1','3'],['2','3']])
    {'1': ['3'], '2': ['3'], '3': ['1', '2']}
    """
    
    g, nabo_liste = dict(), []
    for v in V: #Danner en key for hvert punkt
        for e in E: #Tjekker alle kanter
            if v == e[0] and v == e[1]: #Tjekker hvilket punkt skal tilføjes til nabo listen
                nabo_liste += [e[0]]
            elif v == e[0]:
                nabo_liste += [e[1]]
            elif v == e[1]:
                nabo_liste += [e[0]]
        g[v] = nabo_liste #Opretter key og value for et punkt
        nabo_liste = []
    return g


def complete_graph(n):
    """
    Funktionen skal danne en komplet graf med n punkter repræsenteret af en nabo ordbog.
    
    Input
    n -> antallet af punkter i grafen

    Output
    g -> en nabo ordbog for grafen dannet
    
    Eksempel
    >>> complete_graph(4)
    {'0': ['1', '2', '3'], '1': ['0', '2', '3'], '2': ['0', '1', '3'], '3': ['0', '1', '2']}
    """
    
    g = dict() #Nabo ordbogen
    V = [str(i) for i in range(n)] #Punkter
    for u in V: #Danner et punkt af gangen
        nabo_list = []
        for v in V: #Danner naboer
            if v not in nabo_list and u != v:
                nabo_list += [v]
        g[u] = nabo_list #Tilføjer punktet og nabolisten til ordbogen
    return g


def generate_vertices(g):
    """
    Laver en liste/mængde af punkter ud fra en nabo ordbog.
    
    Input
    g -> en nabo ordbog for en graf

    Output
    V -> en liste af punkter
    
    Eksempel
    >>> generate_vertices({'1':['3'],'2':['3'],'3':['1','2']})
    ['1', '2', '3']
    """
    
    V = [] #Mængde af kanter er tom
    for v in g: #Alle punkter tilføjes
        V += [v]
    return V


def generate_edges(g):
    """
    Laver en liste/mængde af kanter ud fra en nabo ordbog.
    
    Input
    g -> en nabo ordbog for en graf

    Output
    E -> en liste af kanter, som i sig selv er en liste af to punkter
    
    Eksempel
    >>> generate_edges({'1':['3'],'2':['3'],'3':['1','2']})
    [['1', '3'], ['2', '3']]
    """
    
    E = [] #Mængde af kanter er tom
    for u in g: #Et punkt u og dens nabo v
        for v in g[u]:
            if [u,v] not in E and [v,u] not in E: #Checker om kanten ikke allerede er tilføjes til mængden
                E += [[u,v]]
    return E


def add_weights(E,a,b):
    """
    Tilføjer heltals-positive vægte til en liste af kanter, hvor vægtende er mellem a og b.
    
    Input
    E -> en liste af kanter
    a -> nedre grænse for vægtene
    b -> øvre grænse for vægtene

    Output
    E -> en liste af kanter, som udover at være en liste af to punkter også indeholder en vægt
    
    Eksempel
    #>>> add_weights([['1', '3'], ['2', '3']],2,5)
    #[['1', '3', 3], ['2', '3', 2]]
    """
    
    if 0 < a < b: #Tilføjer en vægt
        for e in E:
            w = r.randint(a,b)
            e += [w]
        return E
    return print('Not correct interval for weights')



"""
De næste funktioner handler om graden af et punkt og kan anvendes i nogle af algoritmerne.
Nogle versioner af grad-funktionen giver forskellige resultater.
Den sidste funktion redegør for Håndtrykssætningen (Rosen, 10.2, s. 653).
"""


def degree(g):
    """
    Laver en ordbog med graderne af hvert punkt. Gælder for pseudografer.
    
    Input
    g -> en nabo ordbog til en graf

    Output
    deg -> en ordbog over hvert punkts grad
    
    Eksempel
    >>> degree({'1':['1','2'],'2':['1','3'],'3':['2']})
    {'1': 3, '2': 2, '3': 1}
    """
    
    deg = dict()
    for u in g: #Et punkt u og dens nabo v
        for v in g[u]:
            deg[u] = deg.get(u,0) + 1 #Tilføjer en grad for hver nabo
            if u == v:
                deg[u] = deg.get(u,0) + 1 #Tilføjer en grad hvis punktet er dens egen nabo
    return deg


def degree2(g):
    """
    Alternativ grad-funktion. Gælder for pseudografer.
    
    Input
    g -> en nabo ordbog til en graf

    Output
    deg -> en ordbog over hvert punkts grad
    
    Eksempel
    >>> degree2({'1':['1','2'],'2':['1','3'],'3':['2']})
    {'1': 3, '2': 2, '3': 1}
    """
    deg, deg_list = dict(), []
    for v in generate_edges(g): #Lister alle gange et punkt er incident med en kant
        deg_list += v
    for u in deg_list: #Tilføjer en grad for alle gange et punkt er incident med en kant
        deg[u] = deg.get(u,0) + 1
    return deg


def degree3(g):
    """
    Grad-funktion for ikke pseudografer.
    
    Input
    g -> en nabo ordbog til en graf

    Output
    deg -> en ordbog over hvert punkts grad
    
    Eksempel
    >>> degree3({'1':['2'],'2':['1','3'],'3':['2']})
    {'1': 1, '2': 2, '3': 1}
    """
    
    deg = dict() #Skaber en ordbog med alle ikke isolerede punkter, som angiver deres grad
    for v in g:
        for e in generate_edges(g):
            if v in e:
                deg[v] = deg.get(v,0) + 1
    return deg


def handshake_lemma(g):
    """
    Redegører for Håndtrykssætningen, hvor funktionen printer en forklaring.
    
    Input
    g -> en nabo ordbog til en graf

    Output
    print(deg+edges) -> printer en forklaring

    Eksempel
    >>> handshake_lemma({'1':['2'],'2':['1','3'],'3':['2']})
    Total degree of nodes is 4
    2 times nr. of edges is 4
    """
    
    sum_deg, z = 0, degree(g) #Sætter summen til nul og anvender grad-funktionen
    for v in z: #Summer alle graderne
        sum_deg += z[v]        
    e_count = len(generate_edges(g)) #Antallet af kanter via kant-funktionen
    deg, edges = f'Total degree of nodes is {sum_deg}\n', f'2 times nr. of edges is {2*e_count}'
    return print(deg+edges) #Returnerer en forklaring



"""
Denne sektion er om Eulerkredse og indeholder Fleurys algoritme (Rosen, appendiks S, s. S-64).
Fleurys algoritme kræver en sammenhængende multigraf, hvor graden af hvert punkt er lige.
"""


def fleurys(V,E): 
    """
    Fleurys algoritme for en multigraf, hvor den konstruerer en Eulerkreds.
    
    Input
    V -> en liste af punkter
    E -> en liste af kanter

    Output
    circuits -> printer en Eulerkreds som en punktsekvens
    
    Eksempel
    >>> fleurys(['1','2','3','4','5'],[['1','2'],['1','3'],['2','4'],['3','4'],['4','5'],['4','5']])
    ['1', '2', '4', '5', '4', '3', '1']
    """
    
    E0 = []
    E0 += E
    
    g = make_graph(V, E)
    deg = degree(g) #Skaber en ordbog med alle ikke isolerede punkter, som angiver deres grad
                
    for v in deg: #Hvis alle punkter ikke er af lige grad, så stopper algoritmen, da grafen ikke har en Eulerkreds
        if deg[v]%2 != 0:
            return print('Not all vertices are of even degree')
    
    not_finish = False
    circuits = [[E[0][0]]] #Gemmer alle kredse dannet
    
    while not_finish != True: #For alle punkter, der stadigvæk har naboer kan en ny kreds dannes
        count = 0
        for v in deg:
            if deg[v] == 0:
                count += 1
        if count == len(V):
            not_finish = True
            break
        for v in circuits[0]:
            if deg[v] > 0:
                for u,w in E0: #Først tilføjes den første kant og kredsen startes
                    if u == v or w == v:
                        if u == v:
                            circuit = [u,w]
                        if w == v:
                            circuit = [w,u]
                        E0.remove([u,w]) #Undervejs slettes kanterne i kredsene og graden for punkter går derfor 1 ned
                        deg[u] -= 1
                        deg[w] -= 1
                        break
                while deg[v] > 0: #Derefter tilføjes kanter indtil kredsen stopper ved startpunktet igen
                    for u1,v1 in E0:
                        if u1 == circuit[-1] or v1 == circuit[-1]:
                            if u1 == circuit[-1]:
                                circuit += [v1]
                            elif v1 == circuit[-1]:
                                circuit += [u1]
                            E0.remove([u1,v1])
                            deg[v1] -= 1
                            deg[u1] -= 1
                circuits += [circuit] #Når kredsen er lavet færdigt, så tilføjes den til samlingen af kredse
        
        delcircuits = []
        while len(circuits) > 1: #Laver alle kredsene til en kreds, ved at indsætte alle kredse ind i den første
            for i in range(1,len(circuits)):
                for v in circuits[0]:
                    if v == circuits[i][0]:
                        j = (circuits[0]).index(v)
                        circuits[0][j] = circuits[i]
                        delcircuits += [circuits[i]]
                        break
        
            for dc in delcircuits:
                circuits.remove(dc)
                delcircuits.remove(dc)
                    
        euler_circ = []
        for v in circuits[0]:
            if type(v) == list:
                for w in v:
                    euler_circ += [w]
            else:
                euler_circ += [v]
        circuits[0] = euler_circ
    
    return euler_circ #Eulerkredsen


def test_eulersti_alg(V,E,fu='n'):
    """
    Tester Eulersti algoritmerne.
    
    En algoritme testes, hvis den tilsvarende variabel er yes ('y').
    
    fu -> fleurys
    """
    
    if fu == 'y':
        C = fleurys(V, E)
        print('FLEURYS ALGORITME\nEulerkreds', C)



"""
Denne sektion er om korteste sti algortimer, som alle kræver sammenhængende vægtet grafer.
Dijkstras algoritme er den mest effektive og giver både længden og stien (Rosen, 10.6, s. 712).
Floyds algoritme giver længden på den korteste sti (Rosen, 10.6,s. 717).
Den grådige algoritme er selvlavet (ideen er fra Andreas) og kan ikke garanterer at finde den korteste sti, men den kan garantere at finde en sti.
"""


def dijkstras(V,E,v0,vn):
    """
    Dijkstras algoritme. Finder den korteste sti i en sammenhængende graf med positive vægte.
    
    Input
    V -> en liste af punkter
    E -> en liste af positivt vægtet kanter
    v0 -> et startpunkt for stien
    vn -> et slutpunkt for stien
    
    Output
    (path, length) -> giver den korteste sti som punktsekvens og længden af stien
    
    Eksempel
    >>> dijkstras(['1','2','3','4','5','6'],[['1','3',2],['2','3',5],['2','4',6],['3','4',10],['3','5',3],['4','5',4],['5','6',5]],'2','6')
    (['2', '3', '5', '6'], 13)
    """
    
    if v0 not in V or vn not in V: #Punkterne valgt er ikke en del af grafen
        return print('Mindst et af punkterne eksisterer ikke')

    i_0, i_n = V.index(v0), V.index(vn) #Finder index numrene for start og slutpunkt
    infty = 100000000 #Uendelige sat som et enormt stort tal
    
    L = [[infty,[]] for j in range(0,len(V))] #Label, viser længden fra v0 til en vilkårlig v. Sætter start labels til uendelig
    L[i_0] = [0,[]] #Sætter v0's label til 0
    
    S = [] #Mængden af punkter, som allerede er taget i betragtning
    
    while vn not in S: #Kører algoritmen indtil en sti mellem v0 og vn er dannet
        
        mini = infty #Sætter minimal til uendelig, og derefter finder det label, som har lavest værdi
        for j in range(0,len(V)):
            if V[j] not in S and mini >= L[j][0]:
                    mini, k = L[j][0], j #Label med lavest værdi gemmes i k
        
        S.append(V[k]) #Punktet med index k tilføjes til S
        
        for v in V: #Opdaterer alle labels for punkter v ikke i S, som er incident med samme kant e, som et punkt u i S
            if v not in S:
                for u in S:
                    for e in E:
                        if u in e and v in e:
                            i_v, i_u = V.index(v), V.index(u)
                            if L[i_u][0] + e[2] < L[i_v][0]:
                                L[i_v][0] = L[i_u][0] + e[2] #Opdatere labels, hvis det er lavere end før
                                L[i_v][1] = L[i_u][1] + [e] #Opdatere stien til et punkt
    
    length, path = L[i_n][0], [v0] #Omdanner labelt til længden af stien og en sti
    for u,v,w in L[i_n][1]:
        if u == v0 or v == v0:
            path = [v0]
        if u not in path:
            path.append(u)
        if v not in path:
            path.append(v)
    
    return path, length #Label for punktet vn, hvor værdien er længden og listen er de udforskede stier


def floyds(V,E,v0,vn):
    """
    Floyds algoritme. Finder længden på den korteste sti i en sammenhængende graf.
    
    Input
    V -> en liste af punkter
    E -> en liste af positivt vægtet kanter
    v0 -> et startpunkt for stien
    vn -> et slutpunkt for stien
    
    Output
    distance[(V[i_0],V[i_n])] -> længden af den korteste sti
    
    Eksempel
    >>> floyds(['1','2','3','4','5','6'],[['1','3',2],['2','3',5],['2','4',6],['3','4',10],['3','5',3],['4','5',4],['5','6',5]],'2','6')
    13
    """
    
    if v0 not in V or vn not in V: #Punkterne valgt er ikke en del af grafen
        return print('Mindst et af punkterne eksisterer ikke')

    i_0, i_n = V.index(v0), V.index(vn) #Finder index numrene for start og slutpunkt
    infty = 100000000 #Uendelige sat som et enormt stort tal
    
    distance = dict()

    for u in V: #Sætter distancen mellem to nabopunkter til vægten af kanten de er incident med og uendelig for ikke nabopunkter
        for v in V:
            distance[(u,v)] = infty
            for e in E:
                if u in e and v in e and u != v:
                    distance[(u,v)] = e[2]
                    break
    
    for u in V: #Opdaterer distancen mellem to punkter, hvis de kan forbindes af en sti med kortere vægt
        for v in V:
            for w in V:
                if distance[(v,u)] + distance[(u,w)] < distance[(v,w)]:
                    distance[(v,w)] = distance[(v,u)] + distance[(u,w)]
    
    return distance[(V[i_0],V[i_n])] #Længden af stien


def graadig(V,E,v0,vn):
    """
    Graadig sti-findende algoritme, men den kan ikke garantere en optimal løsning.
    
    Input
    V -> en liste af punkter
    E -> en liste af positivt vægtet kanter
    v0 -> et startpunkt for stien
    vn -> et slutpunkt for stien
    
    Output
    graadig(V,R,v0,vn) -> rekursivt prøver at finde en sti i grafen, hvor en den sidste kant i den fundne sti er slettet
    (S, W) -> stien og vægten af stien, dermed længden af stien
    
    Eksempel
    >>> graadig(['1','2','3','4','5','6'],[['1','3',2],['2','3',5],['2','4',6],['3','4',10],['3','5',3],['4','5',4],['5','6',5]],'2','6')
    (['2', '3', '5', '6'], 13)
    """
    if v0 not in V or vn not in V: #Punkterne valgt er ikke en del af grafen
        return print('Mindst et af punkterne eksisterer ikke')
    
    infty = 100000000 #Uendelige sat som et enormt stort tal
    
    W, S = 0, [v0] #Sætter den kumulerede vægt til 0 og stien starter i startpunktet
    
    R, E0 = [], [] #Kopier kanterne i grafen
    R += E
    E0 += E
    
    for j in range(len(E0)): #Kører algoritmen til en sti er fundet eller den møder en blindgyde
        
        w_min = infty #Sætter minimal vægt til uendelig og finder den kant incident med et punkt med mindst vægt
        for e in E0:
            if S[j] in e and e[2] < w_min:
                e_min, w_min = e, e[2] #Kanten med den mindste vægt gemmes
        
        if e_min not in E0: #Hvis algoritmen møder en blindgyde, så fjernes den sidste kant og algoritmen kører igen
            #print(S, W)
            R.remove(e_min)
            return graadig(V,R,v0,vn)
        
        E0.remove(e_min) #Fjerner kanten som lige er tilføjet til stien
        W += w_min #Tilføjer vægten af kanten
        
        if S[j] == e_min[0]: #Tilføjer det næste punkt til stien
            S += [e_min[1]]
        elif S[j] == e_min[1]:
            S += [e_min[0]]
    
        if vn in S: #Hvis stien har noget sit mål stop
            return S, W
    
    return print('No path found', S, W) #Hvis en fejl sker


def test_sti_alg(V,E,v0,vn,di='n',fl='n',gr='n'):
    """
    Tester kortest sti algoritmerne.
    
    En algoritme testes, hvis den tilsvarende variabel er yes ('y').
    
    di -> dijkstras
    fl -> floyds
    gr -> graadig
    """
    
    if di == 'y':
        S, W = dijkstras(V, E, v0, vn)
        print('DIJKSTRAS ALGORITME\nSti', S, '\nVægt', W)
    if fl == 'y':
        W = floyds(V, E, v0, vn)
        print('FLOYDS ALGORITME\nVægt', W)
    if gr == 'y':
        S, W = graadig(V, E, v0, vn)
        print('GRÅDIG ALGORITME\nSti', S, '\nVægt', W)



"""
Denne sektion er om udspændende træer og indeholder to algoritmer, dybde-først-søgning og bredde-først-søgning.
Dybde-først-søgning danner et langt træ med lange stier mellem punkter (Rosen, 11.4, s. 789).
Bredde-først-søgning danner et bredt træ med korte stier mellem punkter (Rosen, 11.4, s. 791).
"""


def depth_first(g):
    """
    Dybtesøgende algoritme.
    Finder det udspændende træ for en graf ved at starte i en rod og derefter danne en simpel sti, hvor hvert punkt kun besøges en gang.
    Når stien stopper, så ses tilbage på punkterne, om de er naboer med nogle punkter ikke i stien. 
    Udfra dem gentages proceduren til alle punkter er i stierne.
    Stierne danner tilsammen et træ.
    
    Input
    g -> en nabo liste til en simpel graf
    
    Output
    VT -> en liste punkter for det udspændende træ
    ET -> en liste kanter for det udspændende træ
    
    Eksempel
    >>> depth_first({'1':['2','3'],'2':['1','3'],'3':['1','2','4','5'],'4':['3','6'],'5':['3','6'],'6':['4','5']})
    (['1', '2', '3', '4', '6', '5'], [['1', '2'], ['2', '3'], ['3', '4'], ['4', '6'], ['5', '6']])
    """
    
    V, E = generate_vertices(g), generate_edges(g) #Danner setup, danner punkt og kant lister, samt en startværdi v
    g1 = dict()
    for v in g:
        g1[v] = []
        g1[v] += g[v]
    
    v = V[0]
    VT, ET = [v], []
    V.remove(v)
    
    while V != []: #Imens alle punkter ikke er i træet
        for e in E:
            if v in e: #Finder en kant incident på v. Nabopunktet incident på den kant sættes til v og listerne opdateres
                if v == e[0] and e[1] not in VT:
                    ET += [e]
                    v = e[1]
                    VT += [v]
                    V.remove(v)
                    break
                if v == e[1] and e[0] not in VT:
                    ET += [e]
                    v = e[0]
                    VT += [v]
                    V.remove(v)
                    break
                for u in g1: #Sletter nabopunkter i naboordbogen, hvis begge punkter er i træet
                    for w in g1:
                        if w in g1[u] and u in VT and w in VT:
                            g1[u].remove(w)
                j = 1 #Finder et punkt der har naboer som ikke er i træet. Punktet findes baglæns gennem stien.
                while g1[v] == []:
                    v = VT[-j]
                    j += 1
                    
    return VT, ET #Returnerer træet


def breadth_first(g):
    """
    Breddesøgende algoritme.
    Finder det udspændende træ for en graf ved at starte i en rod og derefter tilføje alle naboer til roden.
    Derefter tilføjes alle naboer til naboerne til roden, som ikke er i træet i forvejen.
    Den procedurer gentages.
    
    Input
    g -> en nabo liste til en simpel graf
    
    Output
    VT -> en liste punkter for det udspændende træ
    ET -> en liste kanter for det udspændende træ
    
    Eksempel
    >>> breadth_first({'1':['2','3'],'2':['1','3'],'3':['1','2','4','5'],'4':['3','6'],'5':['3','6'],'6':['4','5']})
    (['1', '2', '3', '4', '5', '6'], [['1', '2'], ['1', '3'], ['3', '4'], ['3', '5'], ['4', '6']])
    """
    
    V, E = generate_vertices(g), generate_edges(g) #Setup, hvor punkt og kant lister laves, samt en rod vælges.
    v = V[0]
    VT, ET, L = [v], [], [v] #L holder styr på alle punkter ikke i træet, men naboer med punkter i træet.
    
    while L != []: #Imens kører indtil alle punkter er i træet.
        v = L[0] #Først vælges et punkt der skal tjekkes.
        L.remove(v)
        for w in g[v]: #Tjekker alle nabopunkter til v, som ikke er i træet eller i L.
            if w not in L and w not in VT:
                for e in E:
                    if w in e and v in e: #Tilføjer nabopunkt til træet, L og kanten der forbinder nabopunktet til træet tilføjes til træet.
                        L += [w]
                        ET += [e]
                        VT += [w]
    
    return VT, ET #Returnerer træet

           
def test_trae_alg(g,DFS='n',BFS='n'):
    """
    Tester udspændende træ algoritmerne.
    
    En algoritme testes, hvis den tilsvarende variabel er yes ('y').
    
    DFS -> dybde først søgning
    BFS -> bredde først søgning
    """
    
    if DFS == 'y':
        V, E = depth_first(g)
        print('DYBDE FØRST SØGNING\nPunkter', V, '\nKanter', E)
    if BFS == 'y':
        V, E = breadth_first(g)
        print('BREDDE FØRST SØGNING\nPunkter', V, '\nKanter', E)



"""
Denne sektion er om minimum udspændende træer og indeholder to algoritmer, Prims og Kruskals.
Begge algoritmer giver det minimum udspændende træ.
Prims algoritme finder den mindst vægtet kant og danner et minimum udspændende træ ud fra kanten (Rosen, 11.5, s. 799).
Kruskals algoritme finder de mindst vægtet kanter og tilføjer dem, så længe de ikke danner en kreds (Rosen, 11.5, s. 800).
Boruvkas algoritme danner komponenttræer og finder de minimum vægtet kanter som forbinder to komponenttræer.
"""


def prims(V,E):
    """
    Prims algoritme for at finde et minimum udspændende træ i en vægtet sammenhængende graf.

    Input
    V -> en liste af punkter
    E -> en liste af vægtet kanter

    Output
    VT -> en liste af punkterne i træet
    ET -> en liste af kanterne i træet
    
    Eksempel
    >>> prims(['1','2','3','4','5'],[['1','2',50],['2','3',50],['2','4',1],['2','5',1],['4','5',1]])
    (['2', '4', '5', '1', '3'], [['2', '4', 1], ['2', '5', 1], ['1', '2', 50], ['2', '3', 50]])
    """
    
    infty = 100000000 #Uendelige sat som et enormt stort tal
    
    mini = infty #Finder den mindst vægtet kant i E
    for e in E:
        if e[2] < mini:
            e_min, mini = e, e[2]
            
    ET, VT = [e_min], [e_min[0], e_min[1]] #Tilføjer den mindst vægtet kant og punkterne incident med kanten
    
    for i in range(len(V)-2): #Tilføjer den mindst vægtet kant incident med et punkt i træet allerede
        mini = infty
        for e in E:
            if e[2] < mini:
                if e[0] in VT and e[1] not in VT:
                    e_min, v, mini = e, e[1], e[2]
                elif e[0] not in VT and e[1] in VT:
                    e_min, v, mini = e, e[0], e[2]
        
        ET += [e_min]
        VT += [v]
    
    return VT, ET


def kruskals(V,E):
    """
    Kruskals algoritme for at finde et minimum udspændende træ i en vægtet sammenhængende graf.

    Input
    V -> en liste af punkter
    E -> en liste af vægtet kanter

    Output
    VT -> en liste af punkterne i træet
    ET -> en liste af kanterne i træet
    
    Eksempel
    >>> kruskals(['1','2','3','4','5'],[['1','2',50],['2','3',50],['2','4',1],['2','5',1],['4','5',1]])
    (['2', '4', '5', '1', '3'], [['2', '4', 1], ['2', '5', 1], ['1', '2', 50], ['2', '3', 50]])
    """
    
    infty = 100000000 #Uendelige sat som et enormt stort tal
    
    ET, VT = [], []
    T, i = dict(), 0 #Danner en ordbog til at holde styr på alle dannede komponenter
    
    for i in range(len(V)-1):
        mini = infty #Finder den mindst vægtet kant
        for e in E:
            if e[2] < mini and e not in ET:
                if e[0] not in VT or e[1] not in VT: #Tjekker om et nyt punkt tilføjes, derfor dannes en kreds ikke
                    e_min, mini = e, e[2]
                    u, v = e[0], e[1]
                else:
                    in_tree = 0 #Begge punkter er i træet, men hvis de er i forskellige komponenter, så dannes en kreds ikke
                    for j in T:
                        if e[0] in T[j] and e[1] not in T[j]:
                            in_tree += 1
                        elif e[1] in T[j] and e[0] not in T[j]:
                            in_tree += 1
                    if in_tree == 2: #De er i forskellige komponenter
                        e_min, mini = e, e[2]
                        u, v = e[0], e[1]
        
        ET += [e_min] #Kanten minimal og punkter incident på kanten tilføjes til træet
        if u not in VT:
            VT += [u]
        if v not in VT:
            VT += [v]
        
        in_tree = 0 #Komponenterne opdateres
        for j in T:
            if u in T[j] and v not in T[j]:
                T[j] += [v]
                in_tree += 1
                uj = j
            elif v in T[j] and u not in T[j]:
                T[j] += [u]
                in_tree += 1
                vj = j
        if in_tree == 0: #En ny komponent dannes
            T[str(i)] = [u,v]
            i += 1
        elif in_tree == 2: #To komponenter er sammenhængende og bliver derfor til en komponent
            T[uj] += T[vj]
            del T[vj]
    
    return VT, ET


def boruvkas(V,E):
    """
    Boruvkas algoritme for at finde et minimum udspændende træ i en vægtet sammenhængende graf.

    Input
    V -> en liste af punkter
    E -> en liste af vægtet kanter

    Output
    V -> en liste af punkterne i træet
    ET -> en liste af kanterne i træet
    
    Eksempel
    >>> boruvkas(['1','2','3','4','5'],[['1','2',50],['2','3',50],['2','4',1],['2','5',1],['4','5',1]])
    (['1', '2', '3', '4', '5'], [['1', '2', 50], ['2', '4', 1], ['2', '3', 50], ['2', '5', 1]])
    """
    
    ET = [] #Kanterne i træet
    
    infty = 9999999999 #Sætter uendelige til et højt tal
    
    E_min, k = dict(), 0 #Gemmer de minimum vægtet kanter incident med hvert punkt
    for v in V: #Finder de minimum vægtet kanter incident med hvert punkt
        w_min = infty
        
        for e in E:
            if v in e and e[2] < w_min:
                w_min, e_min = e[2], e
                
        E_min[k] = e_min
        k += 1
      
    L_trees = [] #Gemmer de forskellige komponenttræer
        
    for k in E_min: #Tilføjer de minimum vægtet kanter til træet, hvis de ikke gentager sig
        if E_min[k] not in ET:
            ET.append(E_min[k])
            u, v, n = E_min[k]

            is_new_tree = True #Danner de forskellige komponenttræer løbende, mens kanterne tilføjes
            for t in L_trees:
                if u in t or v in t: #Punkterne er i et komponenttræ
                    is_new_tree = False
                    if u not in t:
                        t.append(u)
                    if v not in t:
                        t.append(v)
            if is_new_tree == True: #Punkterne er ikke i et komponenttræ
                L_trees.append([u,v])

    while len(L_trees) > 1: #Gentager en proces indtil et minimum udspændende træ er fundet
        
        for v in V: #Opdaterer komponenttræerne
            temp_t = []
            for t in L_trees:
                if v in t:
                    temp_t.append(t)
                    if len(temp_t) == 2: #To komponenter indeholder samme punkt, dermed er de en komponent
                        i = L_trees.index(temp_t[0])
                        L_trees[i] = temp_t[0] + temp_t[1]
                        L_trees.remove(temp_t[1])
    
        E_min, k = dict(), 0 #Gemmer de minimum vægtet kanter incident med et punkt i hver komponenttræ
        for t in L_trees: #For alle komponenttræer
            w_min = infty
            for v in t: #For alle punkter i komponenttræet
                for e in E:
                    if v in e and e[2] < w_min and e not in ET: #Kanten må ikke gentage sig
                        u1, u2, n = e
                
                        for t in L_trees: #Finder komponenttræerne for punkterne i kanten
                            if u1 in t:
                                t_u1 = t
                            if u2 in t:
                                t_u2 = t
                                
                        if t_u1 != t_u2: #Opdaterer komponenttræerne
                            w_min, e_min = e[2], e
                
            E_min[k] = e_min
            k += 1
        
        for k in E_min: #Tilføjer de minimum vægtet kanter til træet, hvis de ikke gentager sig
            if E_min[k] not in ET:
                u, v, n = E_min[k]
                
                for t in L_trees: #Finder komponenttræerne for punkterne i kanten
                    if u in t:
                        t_u = t
                    if v in t:
                        t_v = t
                        
                if t_u != t_v: #Opdaterer komponenttræerne
                    ET.append(E_min[k])
                    i = L_trees.index(t_u)
                    L_trees[i] = t_u + t_v
                    L_trees.remove(t_v)

    return V, ET #Returnerer træet


def test_min_trae_alg(V,E,p='n',k='n',b='n'):
    """
    Tester minimum udspændende træ algoritmerne.
    
    En algoritme testes, hvis den tilsvarende variabel er yes ('y').
    
    p -> prims
    k -> kruskals
    b -> boruvkas
    """
    
    if p == 'y':
        V, E = prims(V, E)
        print('PRIMS ALGORITME\nPunkter', V, '\nKanter', E)
    if k == 'y':
        V, E = kruskals(V, E)
        print('KRUSKALS ALGORITME\nPunkter', V, '\nKanter', E)
    if b == 'y':
        V, E = boruvkas(V, E)
        print('BORUVKAS ALGORITME\nPunkter', V, '\nKanter', E)



"""
Denne sektion er om minimum perfekte matchings.
Den første danner Hamiltonstier og derefter matchings. Den finder den minimum perfekte matchings.
Den anden er ikke optimal, men en del hurtigere. Den tjekker ikke alle matchings.
"""

from math import factorial


def min_perfect_matching(V,E):
    """
    Bruteforce minimum perfect matching for en komplet vægtet graf.
    Algoritmen finder alle Hamiltonstier og danner derefter matchings ved at vælge hver anden kant i Hamiltonstien.

    Input
    V -> en liste af et lige antal punkter
    E -> en liste af vægtet kanter

    Output
    M[k] -> kanterne i den perfekte matching uden vægte
    M_W[k] -> vægten af den perfekte matching
    
    Eksempel
    >>> min_perfect_matching(['1','2','3','4'],[['1','2',5],['1','3',7],['1','4',9],['2','3',8],['2','4',10],['3','4',6]])
    ([['1', '2'], ['3', '4']], 11)
    """
    
    infty = 100000000 #Uendelige sat som et enormt stort tal
    
    M = [] #Alle matchings tilføjes i listen M, hvor de starter ud med at være Hamiltonstier
    m = [factorial(i) for i in range(len(V))] #Antal kombinationer ved et hvis trin i at danne Hamiltonstierne
    
    for i in range(m[-1]): #Tilføjer det første punkt til alle Hamiltonstier
        M.append([])
    
    for j in range(len(V)): #Danner Hamiltonstier
        k = j
        for i in range(m[-1]): #Tilføjer et punkt af gangen
            if i % m[-(j+1)] == 0 and i != 0: #Ændrer hvilket punkt der skal tilføjes systematisk
                k += 1
                if k >= len(V):
                    k = 1
                while V[k] in M[i]:
                    k += 1
                    if k >= len(V):
                        k = 1
                        
            M[i].append(V[k]) #Tilføjer et punkt
    
    
    for i in range(len(M)): #Danner matchings fra Hamiltonstierne
        m = []
        for j in range(int(len(M[i])/2)):
            m.append([M[i][2*j],M[i][2*j+1]])
        M[i] = m

    M_W, W_min, i = [], infty, 0 #Setup til at finde vægte
    
    for m in M: #Danner vægt for hver matching
        M_W += [[]]
        for em in m:
            for e in E: #Tjekker hvilken kant er ens med kanten i matchingen
            
                if em[0] == e[0] and em[1] == e[1]:
                    if M_W[i] == []: #Tilføjer vægten
                        M_W[i] = e[2]
                    else:
                        M_W[i] += e[2]
                        
                if em[0] == e[1] and em[1] == e[0]:
                    if M_W[i] == []: #Tilføjer vægten
                        M_W[i] = e[2]
                    else:
                        M_W[i] += e[2]
        
        if M_W[i] < W_min: #Hvis vægten af matchingen er mindre end matchesne før, så sættes den til minimum
            W_min = M_W[i]
            k = i
        i += 1
    
    return M[k], M_W[k] #Returnere minimum perfekt matching


def min_maximal_matching(V,E):
    """
    Bruteforce minimum maximal matching for en komplet vægtet graf.
    Algoritmen finder alle Hamiltonstier og danner derefter matchings ved at vælge hver anden kant i Hamiltonstien.

    Input
    V -> en liste af et lige antal punkter
    E -> en liste af vægtet kanter

    Output
    M_min -> kanterne i den perfekte matching
    
    Eksempel
    >>> min_maximal_matching(['1','2','3','4'],[['1','2',5],['1','3',7],['1','4',9],['2','3',8],['2','4',10],['3','4',6]])
    [['1', '2', 5], ['3', '4', 6]]
    """
    
    infty = 100000000 #Uendelige sat som et enormt stort tal
    
    M = [] #Alle matchings tilføjes i listen M, hvor de starter ud med at være Hamiltonstier
    m = [factorial(i) for i in range(len(V))] #Antal kombinationer ved et hvis trin i at danne Hamiltonstierne
    
    for i in range(m[-1]): #Tilføjer det første punkt til alle Hamiltonstier
        M.append([])
    
    for j in range(len(V)): #Danner Hamiltonstier
        k = j
        for i in range(m[-1]): #Tilføjer et punkt af gangen
            if i % m[-(j+1)] == 0 and i != 0: #Ændrer hvilket punkt der skal tilføjes systematisk
                k += 1
                if k >= len(V):
                    k = 1
                while V[k] in M[i]:
                    k += 1
                    if k >= len(V):
                        k = 1
                        
            M[i].append(V[k]) #Tilføjer et punkt
    
    if len(V)%2 == 0:
        for i in range(len(M)): #Danner matchings fra Hamiltonstierne, hvis der er et lige antal punkter
            m = []
            for j in range(int(len(M[i])/2)):
                m.append([M[i][2*j],M[i][2*j+1]])
            M[i] = m
             
    else:
       for i in range(len(M)): #Danner to matchings fra hver Hamiltonsti, hvis der er et ulige antal punkter
           m1, m2 = [], []
           for j in range(int(len(M[i])/2)):
               m1.append([M[i][2*j],M[i][2*j+1]])
               m2.append([M[i][-(2*j+1)],M[i][-(2*j+2)]])
           M[i] = m1
           M.append(m2)
    
    M_W, W_min, i = [], infty, 0 #Setup til at finde vægte
        
    for m in M: #Danner vægt for hver matching
        M_W += [[]]
        for em in m:
            for e in E: #Tjekker hvilken kant er ens med kanten i matchingen
            
                if em[0] == e[0] and em[1] == e[1]:
                    if M_W[i] == []: #Tilføjer vægten
                        M_W[i] = e[2]
                    else:
                        M_W[i] += e[2]
                        
                if em[0] == e[1] and em[1] == e[0]:
                    if M_W[i] == []: #Tilføjer vægten
                        M_W[i] = e[2]
                    else:
                        M_W[i] += e[2]
        
        if M_W[i] < W_min: #Hvis vægten af matchingen er mindre end matchesne før, så sættes den til minimum
            W_min = M_W[i]
            k = i
        i += 1
    
    M_min = []
    for e0 in M[k]:
        u, v = e0
        for e in E:
            if u in e and v in e:
                M_min.append(e)
                break
                
           
    return M_min #Returnere minimum maximal matching



"""
Denne sektion er om dannelse af metriske grafer fra sammenhængende simple grafer.
make_complete funktionen er mere effektiv (hurtigere) end make_complete2, men de anvender begge Dijkstras algoritme.
"""


def make_complete(V,E):
    """
    Danner en komplet graf ud fra en sammenhængende graf.
    Hver kant er vægtet ud fra den korteste sti mellem de to punkter i kanten.
    Bedre end make_complete.
    
    Input
    V -> en liste med punkter
    E -> en liste af positivt vægtet kanter
    
    Output
    E0 -> en liste af positivt vægtet kanter
    
    Eksempel
    >>> make_complete(['1','2','3','4'],[['1','3',7],['2','3',3],['2','4',4]])
    [['1', '2', 10], ['1', '3', 7], ['1', '4', 14], ['2', '3', 3], ['2', '4', 4], ['3', '4', 7]]
    """
    
    E0 = [] #Kanterne i den metriske graf
    
    infty = 100000000 #Uendelige sat som et enormt stort tal
    
    for i in range(len(V)-1): #Gentager processen, så alle kanter dannes. Hver iteration starter med at vælge et punkt w
        
        L = [infty for j in range(0,len(V))] #Label, viser længden fra w til en vilkårlig v. Sætter start labels til uendelig
        L[i] = 0 #Sætter w's label til 0
        
        S = [] #Mængden af punkter, som allerede er taget i betragtning
        
        while len(S) != len(V): #Kører algoritmen indtil en sti mellem w og alle andre punkter er fundet
            
            mini = infty #Sætter minimal til uendelig, og derefter finder det label, som har lavest værdi
            for j in range(0,len(V)):
                if V[j] not in S and mini >= L[j]:
                        mini, k = L[j], j #Label med lavest værdi gemmes i k
            
            S.append(V[k]) #Punktet med index k tilføjes til S
                                        
            for v in V: #Opdaterer alle labels for punkter v ikke i S, som er incident med samme kant e, som et punkt u i S
                if v not in S:
                    for u in S:
                        for e in E:
                            if u in e and v in e:
                                i_v, i_u = V.index(v), V.index(u)
                                if L[i_u] + e[2] < L[i_v]:
                                    L[i_v] = L[i_u] + e[2] #Opdatere labels, hvis det er lavere end før
        
        for j in range(i+1, len(V)): #Danner kanter med vægt fra labels
            E0.append([V[i], V[j], L[j]])
        
    return E0
    

def make_complete2(V,E):
    """
    Danner en komplet graf ud fra en sammenhængende graf.
    Hver tilføjet kant er vægtet ud fra den mindste sti mellem punkterne i kanten.
    Værre end make_complete.
    
    Input
    V -> en liste med punkter
    E -> en liste af positivt vægtet kanter
    
    Output
    E0 -> en liste af positivt vægtet kanter
    
    Eksempel
    >>> make_complete2(['1','2','3','4'],[['1','3',7],['2','3',3],['2','4',4]])
    [['1', '3', 7], ['2', '3', 3], ['2', '4', 4], ['1', '2', 10], ['1', '4', 14], ['3', '4', 7]]
    """
    
    E0 = [] #Danner en ny liste med kanter
    E0 += E
    
    for i in range(len(V)-1): #For alle par punkter
        for j in range(i+1,len(V)):
            
            not_edge = True #Tjek om parret er i en kant
            for e in E:
                if V[i] in e and V[j] in e:
                    s, w = dijkstras(V,E0,V[i],V[j])
                    if e[2] > w:
                        e[2] = w
                    not_edge = False
                    break
                
            if not_edge == True: #Hvis nej, så dan en kant med længde på den mindste sti mellem punkterne.
                s, w = dijkstras(V,E0,V[i],V[j])
                E0.append([V[i],V[j],w])
    
    return E0 #Returnerer kanterne for en komplet graf



"""
Denne sektion er om Den Handelsrejsendes Problem (Travelling Salesman Problem, TSP).
De kræver alle positiv vægtet komplette metriske grafer.


Finder den optimale Hamiltonkreds
Brute force finder den mindst vægtet Hamiltonkreds, ved at finde vægten af alle Hamiltonkredse.


Hermeneutiske metoder (almen logik)
Nærmest nabo algoritmen starter i et punkt og finder og tilføjer den tætteste nabo i hver iteration, som ikke allerede er i stien.
Nærmest addition algoritmen finder den laveste vægtet kant og danner langsomt en Hamiltonkreds ved at tilføje nærliggende punkter.


Grafteoretisk tekniske metoder
Dobbelttræ algoritmen finder det minimum udspændende træ og dobbler det, derefter findes Eulerkredsen og den forkortes.
Christofides algoritme finder det minimum udspændende træ, en minimum perfekt matching, derefter findes Eulerkredsen og den forkortes.
Min algoritme anvender både parringer og kant sammentrækninger.


Optimering via programmering
2opt metoden er en algoritme, som danner en forbedrelse af gangen. Det gøres ved at sammenligne to par af kanter ad gangen.
Den ungarske metode (The Hungarian Method) løser Den Handelsrejsendes Problem ved at optimere parringer i vægtmatricen for den metriske graf.

Simuleringer
Ant optimization anvender et princip ved myretue kolonier, hvor myre ligger feromoner på stier hen til mad eller andre resourcer.
"""


def brute_force(V,E):
    """
    Finder løsningen til Den Handelsrejsendes problem med Brute Force.
    Danner alle Hamiltonkredse og vælger den med mindst vægt.

    Input
    V -> en liste af punkter
    E -> en liste af vægtet kanter

    Output
    h_min -> punktsekvensen af Hamiltonkredsen med mindst vægt
    w_min -> den samlede vægt i Hamiltonkredsen med mindst vægt
    
    Eksempel
    >>> brute_force(['1','2','3','4'],[['1','2',5],['1','3',7],['1','4',9],['2','3',8],['2','4',10],['3','4',6]])
    (['1', '2', '3', '4', '1'], 28)
    """
    
    H = [] #Alle Hamiltonkredse tilføjes i listen H
    m = [factorial(i) for i in range(len(V))] #Antal kombinationer ved et hvis trin i at danne Hamiltonkredsene
    
    for i in range(m[-1]): #Tilføjer det første punkt til alle Hamiltonkredse
        H.append([])
    
    for j in range(len(V)): #Danner Hamiltonstier
        k = j
        for i in range(m[-1]): #Tilføjer et punkt af gangen
            
            if i % m[-(j+1)] == 0 and i != 0: #Ændrer hvilket punkt der skal tilføjes systematisk
                k += 1
                if k >= len(V):
                    k = 1
                while V[k] in H[i]:
                    k += 1
                    if k >= len(V):
                        k = 1
                        
            H[i].append(V[k]) #Tilføjer et punkt
    
    for h in H: #Tilføjer startpunktet, så Hamiltonstierne bliver til kredse
        h += [V[0]]
        
    w_min, h_min = 99999999999, []
    for h in H: #Udregner vægten af hver Hamiltonkreds og finder den mindste
        w = 0
        for j in range(len(h)-1):
            for e in E:
                if h[j] in e and h[j+1] in e:
                    w += e[2]
                    break
        if w_min > w:
            w_min = w
            h_min = h
    
    return h_min, w_min #Returnerer Hamiltonkredsen og længden af den


def nærmest_nabo(V, E):
    """
    Finder en Hamiltonkreds, ved at starte i et punkt og derefter fortsætte til det næste punkt ad kanten med lavest vægt.
    Starter i alle punkter og tager den mindst vægtet Hamiltonkreds.
    Grafen skal være metrisk (komplet og overholde trekantsuligheden).

    Input
    V -> en liste af punkter
    E -> en liste af vægtet kanter

    Output
    H -> punktsekvensen af Hamiltonkredsen med mindst vægt fundet
    w_min -> den samlede vægt i Hamiltonkredsen med mindst vægt fundet
    
    Eksempel
    >>> nærmest_nabo(['1','2','3','4'],[['1','2',5],['1','3',7],['1','4',9],['2','3',8],['2','4',10],['3','4',6]])
    (['1', '2', '3', '4', '1'], 28)
    """
    
    infty = 9999999999999
    
    H_liste = [] #Gemmer Hamiltonkredsene
    for k in range(len(V)):
        Vh, Eh = [], [] #Setup af mængder
        Vh += V
        Eh += E
        
        S, start, NP = [], Vh[k], Vh[k] #Setup af kredsen
        Vh.remove(NP)
        W = 0
     
        while Vh != []: #Fortsætter til en Hamiltonsti er dannet
            tempW = infty #Minimal vægt sættes til uendelig
            
            for i in range(len(Eh)): #Finder den kant incident med NP med mindst vægt, som ikke danner en kreds
                if Eh[i][0] == NP and Eh[i][1] in Vh and Eh[i][2] < tempW:
                    tempE, tempW = Eh[i], Eh[i][2]
                elif Eh[i][1] == NP and Eh[i][0] in Vh and Eh[i][2] < tempW:
                    tempE, tempW = Eh[i], Eh[i][2]
            
            Eh.remove(tempE) #Opdaterer det nuværende punkt
            if tempE[0] == NP:
                NP = tempE[1]
            elif tempE[1] == NP:
                NP = tempE[0]
            S.append(tempE) #Tilføjer kanten til Hamiltonstien
            Vh.remove(NP) #Tilføjer punktet til de besøgte punkter
            
        for i in range(len(Eh)): #Tilføjer en sidste kant for at færdiggøre Hamiltonkredsen
            if Eh[i][0] == NP and Eh[i][1] == start:
                S.append(Eh[i])
            elif Eh[i][1] == NP and Eh[i][0] == start:
                S.append(Eh[i])
                
        for i in range(len(S)): #Udregner vægten af Hamiltonkredsen
            W += S[i][2]

        H_liste.append([S,W,start]) #Tilføjer kredsen
        
    w_min = infty #Finder den kreds med mindst vægt
    for k in range(len(V)):
        if H_liste[k][1] < w_min:
            S, w_min, start_min = H_liste[k]
    
    H, incl = [V[0]], []
    while len(H) < len(V)+1: #Danner en punktssekvens for Hamiltonkredsen
        for e in S:
            if H[-1] in e and e not in incl:
                incl.append(e)

                if H[-1] == e[0]:
                    H.append(e[1])
                elif H[-1] == e[1]:
                    H.append(e[0])
     
    return H, w_min #Returnerer Hamiltonkredsen og vægten af den


def nærmest_addition(V,E):
    """
    Danner en kreds med to punkter med kanten af minimum vægt.
    Tilføjer det punkt, som er tættest på et punkt i kredsen.
    Tilføjelsen sker, så det resulterer i mindst mulig vægt.

    Input
    V -> en liste af punkter
    E -> en liste af vægtet kanter

    Output
    H0 -> punktsekvensen af Hamiltonkredsen med mindst vægt fundet
    W -> den samlede vægt i Hamiltonkredsen med mindst vægt fundet
    
    Eksempel
    >>> nærmest_addition(['1','2','3','4'],[['1','2',5],['1','3',7],['1','4',9],['2','3',8],['2','4',10],['3','4',6]])
    (['1', '4', '3', '2', '1'], 28)
    """
    
    infty = 100000000 #Uendelige sat som et enormt stort tal
    
    mini = infty #Finder den mindst vægtet kant i E
    for e in E:
        if e[2] < mini:
            e_min, mini = e, e[2]
            
    H = [e_min[0],e_min[1],e_min[0]] #Danner en kreds med kanten af minimum vægt

    while len(H) < len(V)+1: #Fortsætter til en Hamiltonkreds er dannet
        
        mini = infty #Finder den mindst vægtet kant i, som er incident med et punkt i kredsen H, og med et punkt ikke i H
        for e in E:
            if e[0] in H and e[1] not in H: #Identificerer om kanten overholder betingelserne
                if e[2] < mini:
                    e_min, mini = e, e[2]
                    u, v = e[:2]
                    
            if e[1] in H and e[0] not in H: #Identificerer om kanten overholder betingelserne
                if e[2] < mini:
                    e_min, mini = e, e[2]
                    v, u = e[:2]

        i = H.index(u) #Finder indexet af punktet både i e_min og H

        if i == 0: #Hvis indexet er nul, så u er i starten og slutningen
            for e in E:
                if v in e and H[1] in e: #Finder kanter med v og nabopunkterne til u i H
                    e1 = e
                if v in e and H[-2] in e:
                    e2 = e
            
            if e1[2] <= e2[2]: #Indsætter v i H, hvor det giver mindst mulig vægt
                H.insert(1,v)
            else:
                H.insert(-2,v)
        
        else: #Hvis indexet af u viser, at u ligger midt på stien
            for e in E:
                if v in e and H[i-1] in e: #Finder kanter med v og nabopunkterne til u i H
                    e1 = e
                if v in e and H[i+1] in e:
                    e2 = e
            
            if e1[2] <= e2[2]: #Indsætter v i H, hvor det giver mindst mulig vægt
                H.insert(i,v)
            else:
                H.insert(i+1,v)
    
    W = 0
    for i in range(len(H)-1): #Udregner vægten af Hamiltonkredsen
        for e in E:
            if H[i] in e and H[i+1] in e:
                W += e[2]
    
    if H[0] != V[0]: #Omformulerer punktssekvensen for Hamiltonkredsen
        i = H.index(V[0])
        H0 = H[i:] + H[1:i+1]
    else:
        H0 = H
    
    return H0, W #Returnerer Hamiltonkredsen og vægten af den


def dobbelttræ(V,E):
    """
    Finder en tilnærmet løsning for Den Handelsrejsendes Problem med dobbelttræ metoden.
    Finder et minimum udspændende træ.
    Dobbler det og finder en Eulerkreds.
    Forkorter Eulerkredsen og tæller vægten.
    Grafen skal være metrisk (komplet og overholde trekantsuligheden).

    Input
    V -> en liste af punkter
    E -> en liste af vægtet kanter

    Output
    H -> punktsekvensen af Hamiltonkredsen med mindst vægt fundet
    length -> den samlede vægt i Hamiltonkredsen med mindst vægt fundet
    
    Eksempel
    >>> dobbelttræ(['1','2','3','4'],[['1','2',5],['1','3',7],['1','4',9],['2','3',8],['2','4',10],['3','4',6]])
    (['1', '2', '3', '4', '1'], 28)
    """
    
    VT, ET = prims(V, E) #Finder det minimum udspændende træ
    
    E_dob = [] #Dobbler træet uden vægte
    for e in ET+ET:
        E_dob += [e[:2]]
    
    eu_kreds = fleurys(VT,E_dob) #Finder Eulerkredsen
    
    cut = [] #Cutter Eulerkredsen kort, danner Hamiltonkreds
    for v in eu_kreds:
        if v not in cut:
            cut.append(v)
    cut.append(eu_kreds[0])
    
    cut_edge = [] #Finder kanterne i Hamiltonkredsen
    for i in range(len(cut)-1):
        cut_edge.append([cut[i], cut[i+1]])
    
    hamilton = [] #Danner Hamiltonkredsen med vægte
    for u, v in cut_edge:
        for e in E:
            if u in e and v in e:
                hamilton.append(e)
    
    length = 0 #Udregner længden af Hamiltonkredsen
    for e in hamilton:
        length += e[2]
    
    H, incl = [V[0]], []
    while len(H) < len(V)+1: #Danner en punktssekvens for Hamiltonkredsen
        for e in hamilton:
            if H[-1] in e and e not in incl:
                incl.append(e)

                if H[-1] == e[0]:
                    H.append(e[1])
                elif H[-1] == e[1]:
                    H.append(e[0])
    
    return H, length #Returnerer Hamiltonkredsen og længden af den


def christofides(V,E):
    """
    Finder en tilnærmet løsning for Den Handelsrejsendes Problem med christofides algoritme.
    Finder et minimum udspændende træ.
    Finder en minimum perfekt matching mellem alle punkter af ulige grad i træet.
    Finder en Eulerkreds, forkorter Eulerkredsen og tæller vægten.
    Grafen skal være metrisk (komplet og overholde trekantsuligheden).

    Input
    V -> en liste af punkter
    E -> en liste af vægtet kanter

    Output
    H -> punktsekvensen af Hamiltonkredsen med mindst vægt fundet
    length -> den samlede vægt i Hamiltonkredsen med mindst vægt fundet
    
    Eksempel
    >>> christofides(['1','2','3','4'],[['1','2',5],['1','3',7],['1','4',9],['2','3',8],['2','4',10],['3','4',6]])
    (['1', '2', '4', '3', '1'], 28)
    """
    
    VT, ET = prims(V, E) #Finder det minimum udspændende træ
    T = make_graph(VT, ET)
    
    deg = degree(T) #Finder punkter af ulige grad i træet
    odd_deg = []
    for v in deg:
        if deg[v]%2 == 1:
            odd_deg += [v]
            
    M, W = min_perfect_matching(odd_deg, E) #Minimum perfekt matching
    
    E_dob = [] #Træet og matchingen uden vægte
    for e in ET+M:
        E_dob += [e[:2]]
    
    eu_kreds = fleurys(VT,E_dob) #Finder Eulerkredsen
    
    cut = [] #Cutter Eulerkredsen kort, danner Hamiltonkreds
    for v in eu_kreds:
        if v not in cut:
            cut.append(v)
    cut.append(eu_kreds[0])
    
    cut_edge = [] #Finder kanterne i Hamiltonkredsen
    for i in range(len(cut)-1):
        cut_edge.append([cut[i], cut[i+1]])
    
    hamilton = [] #Danner Hamiltonkredsen med vægte
    for u, v in cut_edge:
        for e in E:
            if u in e and v in e:
                hamilton.append(e)
  
    length = 0 #Udregner længden af Hamiltonkredsen
    for e in hamilton:
        length += e[2]
    
    H, incl = [V[0]], []
    while len(H) < len(V)+1: #Danner en punktssekvens for Hamiltonkredsen
        for e in hamilton:
            if H[-1] in e and e not in incl:
                incl.append(e)

                if H[-1] == e[0]:
                    H.append(e[1])
                elif H[-1] == e[1]:
                    H.append(e[0])
    
    return H, length #Returnerer Hamiltonkredsen og længden af den


def opt2(V,E):
    """
    Finder en Hamiltonkreds ved at tage punkterne i rækkefølge.
    Forbedre Hamiltonkredsen ved at sammenligne kanter i kredsen med alternative kanter.
    Sammenligner 2 par kanter adgangen.

    Input
    V -> en liste af punkter
    E -> en liste af vægtet kanter

    Output
    h -> punktsekvensen af Hamiltonkredsen med mindst vægt fundet
    W -> den samlede vægt i Hamiltonkredsen med mindst vægt fundet
    
    Eksempel
    >>> opt2(['1','2','3','4'],[['1','2',5],['1','3',7],['1','4',9],['2','3',8],['2','4',10],['3','4',6]])
    (['1', '4', '3', '2', '1'], 28)
    """
    
    h = V+[V[0]] #Danner en Hamiltonkreds
    
    k = 0 #Antal gennemgange uden forbedringer
    
    while k < len(V)-2: #Stopper, når der ikke har været flere forbedringer. De to sidste kanter gør igen forskel
    
        u1, u2 = h[k:k+2] #Finder den nedre kanten som skal sammenlignes
        for e in E:
            if u1 in e and u2 in e:
                w_u = e[2] #Gemmer vægten
                break
        
        for i in range(k+2,len(V)): #Sammenligner den nedre kant i kredsen med en øvre kant
            v1, v2 = h[i:i+2]
            for e in E:
                if v1 in e and v2 in e: #Finder den øvre kant
                    w_v = e[2] #Gemmer vægten
                    
                elif u1 in e and v1 in e: #Finder de alternative kanter og gemmer deres vægt
                    w_uv1 = e[2]
                elif u2 in e and v2 in e:
                    w_uv2 = e[2]
            
            if w_u + w_v > w_uv1 + w_uv2: #De to alternative kanter giver en forbedring
                Rh = h[k+1:i+1]
                Rh.reverse()
                h = h[:k+1] + Rh + h[i+1:] #Opdaterer Hamiltonkredsen
                k -= 1
                break
        k += 1
        
    W = 0
    for i in range(len(V)): #Udregner vægten af Hamiltonkredsen
        u, v = h[i:i+2]
        for e in E:
            if u in e and v in e:
                W += e[2]
                break
    
    return h, W #Returnerer Hamiltonkredsen og vægten af den


def hungarian(V,E):
    """
    Finder løsningen til Den Handelsrejsendes problem med 'the hungarian method'.
    Finder en kant i vægtmatricen som har lav vægt og hvor punkterne er incident med høj vægtet kanter.

    Input
    V -> en liste af punkter
    E -> en liste af vægtet kanter

    Output
    H -> punktsekvensen af Hamiltonkredsen med mindst vægt fundet
    W -> den samlede vægt i Hamiltonkredsen med mindst vægt fundet
    
    Eksempel
    >>> hungarian(['1','2','3','4'],[['1','2',5],['1','3',7],['1','4',9],['2','3',8],['2','4',10],['3','4',6]])
    (['1', '2', '3', '4', '1'], 28)
    """
    
    infty = 999999999999 #Sætter uendelige til et enormt stort tal
    
    M = []
    for i in range(len(V)): #Danner vægtmatricen for grafen
        M.append([])
        for j in range(len(V)):
            if j != i:
                for e in E:
                    if V[i] in e and V[j] in e:
                        M[i].append(round(e[2]))
                        break
            else:
                M[i].append('X') #Hvis de to punkter i kanten er ens, så eksisterer kanten ikke
    
    i_min, j_min = [[] for i in range(len(V))], [[] for j in range(len(V))] #Lister til at holde styr på minimum værdier i rækkerne og kolonnerne
    
    S, components = [], [] #Kanterne i Hamiltonkredsen
    k = 0
    while len(S) != len(V): #Tilføjer en kant af gangen
        new_round = False    
    
        for i in range(len(V)): #Finder minimum værdier i rækkerne
            i_min[i] = infty
            for j in range(len(V)):
                if M[i][j] != 'X' and M[i][j] < i_min[i]:
                    i_min[i] = M[i][j]
        
        for i in range(len(V)): #Trækker minimum værdierne fra i rækkerne
            for j in range(len(V)):
                if M[i][j] != 'X':
                    M[i][j] -= i_min[i]
                    if M[i][j] < 0:
                        M[i][j] = 0
            
        for j in range(len(V)): #Finder minimum værdier i kolonnerne
            j_min[j] = infty
            for i in range(len(V)):
                if M[i][j] != 'X' and M[i][j] < j_min[j]:
                    j_min[j] = M[i][j]
        
        for j in range(len(V)): #Trækker minimum værdierne fra i kolonnerne
            for i in range(len(V)):
                if M[i][j] != 'X':
                    M[i][j] -= j_min[j]
                    if M[i][j] < 0:
                        M[i][j] = 0

        zeroes = []
        for i in range(len(V)): #Finder alle nullerne i matricen og udregner summen af minimum værdierne i nullets række og kolonne
            for j in range(len(V)):
                if M[i][j] == k: #Fundet et nul
                    i0_min, j0_min = infty, infty
                    
                    for i2 in range(len(V)): #Finder minimum værdi i kolonnen
                        if M[i2][j] != 'X' and M[i2][j] < i0_min and i2 != i:
                            i0_min = M[i2][j]
                    for j2 in range(len(V)): #Finder minimum værdi i rækken
                        if M[i][j2] != 'X' and M[i][j2] < j0_min and j2 != j:
                            j0_min = M[i][j2]
                    
                    if i0_min == infty:
                        i0_min = 0
                    if j0_min == infty:
                        j0_min = 0
                    
                    zeroes.append([i,j,i0_min + j0_min]) #Husker nullets placering og summen af minimum værdierne i nullets række og kolonne

        legal = False
        while legal == False:
            max_zero = -1
            for zero in zeroes: #Finder den maximale label af nul i matricen
                if zero[2] > max_zero:
                    max_zero = zero[2]
                    mz = zero #Gemmer nul med max label
 
            legal = True
            u, v = V[mz[0]], V[mz[1]]
            for c in components:
                if u in c and v in c:
                    legal = False
                    if zeroes == []:
                        new_round = True
                        k += 1
                        break
                    zeroes.remove(mz)
                    if len(S) == len(V)-1:
                        legal = True
                    
            if new_round == True:
                break
        
        if new_round == False:
            k = 0
            S.append([V[mz[0]],V[mz[1]]]) #Danner en kant med nullet med max label
            M[mz[1]][mz[0]] = 'X' #Fjerner det inverse matrice element
                        
            for i2 in range(len(V)): #Fjerner alle værdier i kolonnen af nullet med max label
                M[i2][mz[1]] = 'X'
            for j2 in range(len(V)): #Fjerner alle værdier i rækken af nullet med max label
                M[mz[0]][j2] = 'X'
            
            if components == []:
                components.append(S[0])
                for v in V:
                    if v not in components[0]:
                        components.append([v])
            else:
                u, v = S[-1]
                for c in components: #Finder komponenttræerne for punkterne i kanten
                    if u in c:
                        c_u = c
                    if v in c:
                        c_v = c
                            
                if c_u != c_v: #Opdaterer komponenttræerne
                    i = components.index(c_u)
                    components[i] = c_u + c_v
                    components.remove(c_v)
                        
    W = 0
    for u,v in S: #Udregner vægten af alle kanterne
        for e in E:
            if u in e and v in e:
                W += e[2]
                break
    
    H, incl = [V[0]], []
    while len(H) < len(V)+1: #Danner en punktssekvens for Hamiltonkredsen
        for e in S:
            if H[-1] in e and e not in incl:
                incl.append(e)

                if H[-1] == e[0]:
                    H.append(e[1])
                elif H[-1] == e[1]:
                    H.append(e[0])
                 
    return H, W #Returnerer Hamiltonkredsen og vægten af den



"""
Original algoritme (fra Mikkel)
"""


def my_algorithm(V,E):
    """
    Finder løsningen til Den Handelsrejsendes problem med en originalt formuleret algoritme.
    Danner maximale minimum vægtet matching.
    Tilføjer kanterne til skoven.
    Finder punkter af lav grad.
    Danner en delgraph og gentager proceduren.
    Når kun en kant mangler, så tilføjes den manglende forbindelse.

    Input
    V -> en liste af punkter
    E -> en liste af vægtet kanter

    Output
    H -> punktsekvensen af Hamiltonkredsen med mindst vægt fundet
    W -> den samlede vægt i Hamiltonkredsen med mindst vægt fundet
    
    Eksempel
    >>> my_algorithm(['1','2','3','4'],[['1','2',5],['1','3',7],['1','4',9],['2','3',8],['2','4',10],['3','4',6]])
    (['1', '2', '4', '3', '1'], 28)
    """

    M = min_maximal_matching(V,E) #Laver den første maximale minimum matching
    
    Ef = []
    for e in M: #Tilføjer kanterne i matchingen til skoven
        Ef.append(e[:2])
    
    F = make_graph(V,Ef) #Danner skoven
    deg_f = degree(F) #Danner grad ordbog til skoven
    for v in V: #Finder alle punkter af grad nul og tilføjer dem til grad ordbogen
        if v not in deg_f:
            deg_f[v] = 0
    
    komponents = []
    for e in Ef: #Finder de forskellige komponenter i skoven
        komponents.append(e[:2])
    
    for v in V: #Tilføjer isoleret punkter som deres egen komponent
        isoleret = True
        for k in komponents:
            if v in k: #Punkt er ikke isoleret
                isoleret = False
                break
        
        if isoleret == True: #Punkt er isoleret
            komponents.append([v])
                
    Vm = []
    for v in deg_f: #Finder alle punkter af grad lavere end 2 i skoven
        if deg_f[v] < 2:
            Vm.append(v)
        
    while len(Vm) > 2: #Fortsætter indtil en Hamiltonsti er dannet
        Em = []
        for e in E: #Finder alle kanter i delgrafen med punkter af lav grad
            if e[0] in Vm and e[1] in Vm:
                Em.append(e[:])
        
        Vm2 = [] #Punkterne efter edge contractions
        nye_punkter, incl = dict(), [] #Setup til at lave edge contractions
        c = 0
        for i in range(len(Vm)-1): #For hvert par punkter i grafen
            for j in range(i+1,len(Vm)):
                samme_komponent = False
                
                for k in komponents:
                    if Vm[i] in k and Vm[j] in k: #Finder ud af om de to punkter er i samme komponent
                        samme_komponent = True
                        break
            
                if samme_komponent == True: #Danner et fælles punkt for de to punkter, hvis de er i samme komponent
                    Vm2.append('w'+str(c))
                    incl.append(Vm[i]); incl.append(Vm[j])
                    nye_punkter[Vm2[-1]] = [Vm[i],Vm[j]]
                    c += 1
        
        for v in Vm: #Tilføjer alle punkter som ikke er en del af en edge contraction
            if v not in incl:
                Vm2.append(v)
       
        edge_con, Emremove = dict(), [] #Setup
        for w in nye_punkter: #For hver edge contraction
            u, v = nye_punkter[w]
            for e in Em:
                if u in e and v in e:
                    Emremove.append(e) #Slet kanter mellem punkter, der er blevet til et fælles punkt
                
                if u in e and v not in e: #Kanten indeholder et punkt fra edge contraction
                    e0 = e[:]
                    if e[0] == u:
                        e0[0] = w
                    if e[1] == u:
                        e0[1] = w
                    if str(e) in edge_con: #Tilføjer en key til en ordbog, som tager den nye kant tilbage til den originale kant
                        edge_con[str(e0)] = edge_con[str(e)]
                    else:    
                        edge_con[str(e0)] = e[:]
                    if e[0] == u:
                        e[0] = w
                    if e[1] == u:
                        e[1] = w
                    
                
                if u not in e and v in e: #Kanten indeholder et punkt fra edge contraction
                    e0 = e[:]
                    if e[0] == v:
                        e0[0] = w
                    if e[1] == v:
                        e0[1] = w
                    if str(e) in edge_con: #Tilføjer en key til en ordbog, som tager den nye kant tilbage til den originale kant
                        edge_con[str(e0)] = edge_con[str(e)]
                    else:    
                        edge_con[str(e0)] = e[:]
                    if e[0] == v:
                        e[0] = w
                    if e[1] == v:
                        e[1] = w
                
        for e in Emremove: #Sletter de kanter der skal slettes
            Em.remove(e)
        
        Em2 = make_complete(Vm2,Em) #Danner en simpel graf med kanterne efter edge contractions
        
        M = min_maximal_matching(Vm2,Em2) #Finder maximal minimum matching i delgrafen efter edge contractions
        
        for e0 in M: #For hver kant i matchingen
            if str(e0) in edge_con: #Find den originale kant
                e = edge_con[str(e0)]
            else:
                e1 = [e0[1],e0[0],e0[2]]
                e = edge_con[str(e1)]
            Ef.append(e[:2]) #Tilføjer den originale kant til skoven
            u, v = e[:2] #Puntkerne i kanten
            
            for k in komponents: #Finder komponenterne som punkterne er i
                if u in k:
                    ku = k
                elif v in k:
                    kv = k
            
            i = komponents.index(ku) #Opdaterer komponenterne i skoven
            komponents[i] += kv
            komponents.remove(kv)
            
    
        F = make_graph(V,Ef) #Opdaterer skoven
        deg_f = degree(F) #Opdaterer grad ordbogen for skoven
        for v in V: #Finder alle punkter af grad nul og tilføjer dem til grad ordbogen
            if v not in deg_f:
                deg_f[v] = 0
        Vm = []
        for v in deg_f: #Finder alle punkter af grad lavere end 2 i skoven
            if deg_f[v] < 2:
                Vm.append(v)
    
    Ef.append(Vm) #Danner en Hamiltonkreds
    
    W = 0
    for ef in Ef: #Finder vægten af Hamiltonkredsen
        u, v = ef
        for e in E:
            if u in e and v in e:
                W += e[2]
                break
    
    H, incl = [V[0]], []
    while len(H) < len(V)+1: #Danner en punktssekvens for Hamiltonkredsen
        for e in Ef:
            if H[-1] in e and e not in incl:
                incl.append(e)

                if H[-1] == e[0]:
                    H.append(e[1])
                elif H[-1] == e[1]:
                    H.append(e[0])
                    
    return H, W #Returnerer Hamiltonkredsen og vægten af den


def prims_mod(V,E):
    """
    Modificeret prim
    """
    
    infty = 100000000 #Uendelige sat som et enormt stort tal
    
    E1 = E[:]
    
    deg = dict()
    for v in V:
        deg[v] = 0
    
    mini = infty #Finder den mindst vægtet kant i E
    for e in E1:
        if e[2] < mini:
            e_min, mini = e, e[2]
            
    ET, VT = [e_min], [e_min[0], e_min[1]] #Tilføjer den mindst vægtet kant og punkterne incident med kanten
    deg[e_min[0]], deg[e_min[1]] = 1, 1
    
    while len(ET) < len(V)-1: #Tilføjer den mindst vægtet kant incident med et punkt i træet allerede
        mini = infty
        for e in E1:
            if e[2] < mini:
                if e[0] in VT and e[1] not in VT:
                    e_min, v, mini = e, e[1], e[2]
                elif e[0] not in VT and e[1] in VT:
                    e_min, v, mini = e, e[0], e[2]
        
        deg[e_min[0]] += 1
        deg[e_min[1]] += 1
        
        if deg[e_min[0]] > 2 or deg[e_min[1]] > 2:
            deg[e_min[0]] -= 1
            deg[e_min[1]] -= 1
            E1.remove(e_min)
        else:
            ET += [e_min]
            VT += [v]
    
    e = []
    for v in deg:
        if deg[v] == 1:
            e.append(v)
    
    u, v = e[:2]
    for e in E1:
        if u in e and v in e:
            ET.append(e)
    
    W = 0
    for et in ET: #Finder vægten af Hamiltonkredsen
        W += et[2]
    
    H, incl = [V[0]], []
    while len(H) < len(V)+1: #Danner en punktssekvens for Hamiltonkredsen
        for e in ET:
            if H[-1] in e and e not in incl:
                incl.append(e)

                if H[-1] == e[0]:
                    H.append(e[1])
                elif H[-1] == e[1]:
                    H.append(e[0])

    return H, W #Returnerer Hamiltonkredsen og vægten af den
        

def kruskals_mod(V,E):
    """
    Modificeret kruskal
    """
    
    infty = 100000000 #Uendelige sat som et enormt stort tal
    
    E1 = E[:]
    
    deg = dict()
    for v in V:
        deg[v] = 0
    
    ET, VT = [], []
    T, i = dict(), 0 #Danner en ordbog til at holde styr på alle dannede komponenter
    
    while len(ET) < len(V)-1:
        mini = infty #Finder den mindst vægtet kant
        for e in E1:
            if e[2] < mini and e not in ET:
                if e[0] not in VT or e[1] not in VT: #Tjekker om et nyt punkt tilføjes, derfor dannes en kreds ikke
                    e_min, mini = e, e[2]
                    u, v = e[0], e[1]
                else:
                    in_tree = 0 #Begge punkter er i træet, men hvis de er i forskellige komponenter, så dannes en kreds ikke
                    for j in T:
                        if e[0] in T[j] and e[1] not in T[j]:
                            in_tree += 1
                        elif e[1] in T[j] and e[0] not in T[j]:
                            in_tree += 1
                    if in_tree == 2: #De er i forskellige komponenter
                        e_min, mini = e, e[2]
                        u, v = e[0], e[1]
        
        
        if deg[e_min[0]] == 2 or deg[e_min[1]] == 2:
            E1.remove(e_min)
        else:
            deg[e_min[0]] += 1
            deg[e_min[1]] += 1
            ET += [e_min] #Kanten minimal og punkter incident på kanten tilføjes til træet
            if u not in VT:
                VT += [u]
            if v not in VT:
                VT += [v]
            
            in_tree = 0 #Komponenterne opdateres
            for j in T:
                if u in T[j] and v not in T[j]:
                    T[j] += [v]
                    in_tree += 1
                    uj = j
                elif v in T[j] and u not in T[j]:
                    T[j] += [u]
                    in_tree += 1
                    vj = j
            if in_tree == 0: #En ny komponent dannes
                T[str(i)] = [u,v]
                i += 1
            elif in_tree == 2: #To komponenter er sammenhængende og bliver derfor til en komponent
                T[uj] += T[vj]
                del T[vj]
    
    e = []
    for v in deg:
        if deg[v] == 1:
            e.append(v)
    
    u, v = e[:2]
    for e in E1:
        if u in e and v in e:
            ET.append(e)
    
    W = 0
    for et in ET: #Finder vægten af Hamiltonkredsen
        W += et[2]
    
    H, incl = [V[0]], []
    while len(H) < len(V)+1: #Danner en punktssekvens for Hamiltonkredsen
        for e in ET:
            if H[-1] in e and e not in incl:
                incl.append(e)

                if H[-1] == e[0]:
                    H.append(e[1])
                elif H[-1] == e[1]:
                    H.append(e[0])

    return H, W #Returnerer Hamiltonkredsen og vægten af den


def boruvkas_mod(V,E):
    """
    Modificeret kruskal
    """
    
    infty = 100000000 #Uendelige sat som et enormt stort tal
    
    E1 = E[:]
    ET = [] #Kanterne i træet
    
    deg = dict()
    for v in V:
        deg[v] = 0
    
    E_min, k = dict(), 0 #Gemmer de minimum vægtet kanter incident med hvert punkt
    for v in V: #Finder de minimum vægtet kanter incident med hvert punkt
        w_min = infty
        
        for e in E:
            if v in e and e[2] < w_min:
                w_min, e_min = e[2], e
                
        E_min[k] = e_min
        k += 1
      
    L_trees = [] #Gemmer de forskellige komponenttræer
        
    for k in E_min: #Tilføjer de minimum vægtet kanter til træet, hvis de ikke gentager sig
        if E_min[k] not in ET:
            if deg[E_min[k][0]] == 2 or deg[E_min[k][1]] == 2:
                if E_min[k] in E1:
                    E1.remove(E_min[k])
            else:
                deg[E_min[k][0]] += 1
                deg[E_min[k][1]] += 1
                
                ET.append(E_min[k])
                u, v, n = E_min[k]
    
                is_new_tree = True #Danner de forskellige komponenttræer løbende, mens kanterne tilføjes
                for t in L_trees:
                    if u in t or v in t: #Punkterne er i et komponenttræ
                        is_new_tree = False
                        if u not in t:
                            t.append(u)
                        if v not in t:
                            t.append(v)
                if is_new_tree == True: #Punkterne er ikke i et komponenttræ
                    L_trees.append([u,v])

    for v in V:
        v_no = False
        for l in L_trees:
            if v in l:
                v_no = True
        if v_no == False:
            L_trees.append([v])
            
    while len(L_trees) > 1: #Gentager en proces indtil et minimum udspændende træ er fundet
        
        for v in V: #Opdaterer komponenttræerne
            temp_t = []
            for t in L_trees:
                if v in t:
                    temp_t.append(t)
                    if len(temp_t) == 2: #To komponenter indeholder samme punkt, dermed er de en komponent
                        i = L_trees.index(temp_t[0])
                        L_trees[i] = temp_t[0] + temp_t[1]
                        L_trees.remove(temp_t[1])
    
        E_min, k = dict(), 0 #Gemmer de minimum vægtet kanter incident med et punkt i hver komponenttræ
        for t in L_trees: #For alle komponenttræer
            w_min = infty
            for v in t: #For alle punkter i komponenttræet
                for e in E1:
                    if v in e and e[2] < w_min and e not in ET: #Kanten må ikke gentage sig
                        u1, u2, n = e
                
                        for t in L_trees: #Finder komponenttræerne for punkterne i kanten
                            if u1 in t:
                                t_u1 = t
                            if u2 in t:
                                t_u2 = t
                                
                        if t_u1 != t_u2: #Opdaterer komponenttræerne
                            w_min, e_min = e[2], e
                
            E_min[k] = e_min
            k += 1
        
        for k in E_min: #Tilføjer de minimum vægtet kanter til træet, hvis de ikke gentager sig
            if E_min[k] not in ET:
                if deg[E_min[k][0]] == 2 or deg[E_min[k][1]] == 2:
                    if E_min[k] in E1:
                        E1.remove(E_min[k])
                else:
                    deg[E_min[k][0]] += 1
                    deg[E_min[k][1]] += 1
                    
                    u, v, n = E_min[k]
                    
                    for t in L_trees: #Finder komponenttræerne for punkterne i kanten
                        if u in t:
                            t_u = t
                        if v in t:
                            t_v = t
                            
                    if t_u != t_v: #Opdaterer komponenttræerne
                        ET.append(E_min[k])
                        i = L_trees.index(t_u)
                        L_trees[i] = t_u + t_v
                        L_trees.remove(t_v)
    
    e = []
    for v in deg:
        if deg[v] == 1:
            e.append(v)
    
    u, v = e[:2]
    for e in E1:
        if u in e and v in e:
            ET.append(e)
    
    W = 0
    for et in ET: #Finder vægten af Hamiltonkredsen
        W += et[2]
    
    H, incl = [V[0]], []
    while len(H) < len(V)+1: #Danner en punktssekvens for Hamiltonkredsen
        for e in ET:
            if H[-1] in e and e not in incl:
                incl.append(e)

                if H[-1] == e[0]:
                    H.append(e[1])
                elif H[-1] == e[1]:
                    H.append(e[0])

    return H, W #Returnerer Hamiltonkredsen og vægten af den



"""
Ant optimization algoritme (simulering)
"""

import numpy as np
import numpy.random as npr
npr.seed(1)


def ant_optimization(V,E,n):
    """
    Ant optimization går ud på at simulere en myretue, hvor hver myre laver Hamiltonkredse og danner feromon i forhold til længden af Hamiltonkredsen.
    Efter simuleringerne af myrene, så dannes en Hamiltonkreds uden nogen tilfældighed.
    
    Input
    V -> en liste af punkter
    E -> en liste af vægtet kanter
    n -> en

    Output
    hv -> punktsekvensen af Hamiltonkredsen med mindst vægt
    l -> den samlede vægt i Hamiltonkredsen med mindst vægt
    
    Eksempel
    >>> ant_optimization(['1','2','3','4'],[['1','2',5],['1','3',7],['1','4',9],['2','3',8],['2','4',10],['3','4',6]],1000)
    (['1', '2', '3', '4', '1'], 28)
    """
    
    kant_nabo = dict()
    for v in V: #Danner en ordbog med alle kanter incident på et bestemt punkt
        nabo = []
        for e in E:
            if v in e:
                nabo.append(e)
        kant_nabo[v] = nabo
    
    feromoner = dict()
    for e in E: #Danner en ordbog med feromon niveauet per kant
        feromoner[str(e)] = 1
    
    for i in range(n): #Simuleringerne af n myre
        v0 = npr.choice(V) #Startpunkt
        hv, he, l = [v0], [], 0 #Hamiltonkredsen i punkter, kanter og vægt
        
        while len(hv) < len(V): #Danner en Hamiltonsti
            
            mulig_nabo, P = [], [] #Danner en liste af alle mulige kanter som kan vælges, når man er i et punkt og udregner sandsynligheden
            for e in kant_nabo[hv[-1]]:
                if e[0] != hv[-1] and e[0] not in hv:
                    mulig_nabo.append(e)
                    P.append(feromoner[str(e)]*(1/e[2]))
                elif e[1] != hv[-1] and e[1] not in hv:
                    mulig_nabo.append(e)
                    P.append(feromoner[str(e)]*(1/e[2]))
            
            P = P / np.sum(P) #Danner sandsynligheder i decimaltal
            i = npr.choice(np.arange(len(mulig_nabo)), p=P) #Vælger en kant
            e0 = mulig_nabo[i]
            
            if e0[0] != hv[-1]: #Tilføjer næste punkt til stien
                hv.append(e0[0])
            elif e0[1] != hv[-1]:
                hv.append(e0[1])
            he.append(e0) #Tilføjer næste kant til stien
            l += e0[2] #Tilføjer vægten
            
        for e in kant_nabo[v0]: #Tilføjer det sidste punkt/kant/vægt
            if hv[-1] in e:
                hv.append(v0)
                he.append(e)
                l += e[2]
                break
        
        for e in he: #Opdaterer feromon niveauet for alle kanterne i Hamiltonkredsen
            feromoner[str(e)] = feromoner.get(str(e)) + 1/l
    
    v0 = V[0] #Starter den sidste Hamiltonkreds
    hv, l = [v0], 0
    
    while len(hv) < len(V): #Danner den sidste Hamiltonsti
        
        mulig_nabo, P = [], [] #Danner en liste af alle mulige kanter som kan vælges, når man er i et punkt og udregner sandsynligheden
        for e in kant_nabo[hv[-1]]:
            if e[0] != hv[-1] and e[0] not in hv:
                mulig_nabo.append(e)
                P.append(feromoner[str(e)]*(1/e[2]))
            elif e[1] != hv[-1] and e[1] not in hv:
                mulig_nabo.append(e)
                P.append(feromoner[str(e)]*(1/e[2]))
        
        P = P / np.sum(P) #Danner sandsynligheder i decimaltal
        p0 = 0
        for i in range(len(P)): #Vælger den kant, som der er størst sandsynlighed for
            if P[i] > p0:
                p0, k = P[i], i
                
        e0 = mulig_nabo[k] #Kanten der tilføjes
        
        if e0[0] != hv[-1]: #Tilføjer punkt
            hv.append(e0[0])
        elif e0[1] != hv[-1]:
            hv.append(e0[1])
        l += e0[2] #Tilføjer vægt
        
    for e in kant_nabo[v0]: #Tilføjer sidste punkt og vægt
        if hv[-1] in e:
            hv.append(v0)
            l += e[2]
            break
    
    return hv, l #Returnerer Hamiltonkreds og vægten af den


def test_dhp_alg(V,E,bf='n',nn='n',na='n',dt='n',cf='n',op='n',hu='n',ma='n',ao='n'):
    """
    Tester Den Handelsrejsendes Problem algoritmerne.
    
    En algoritme testes, hvis den tilsvarende variabel er yes ('y').
    
    bf -> brute force
    nn -> nærmest nabo
    na -> nærmest addition
    dt -> dobbelttræ
    cf -> christofides
    op -> 2opt
    hu -> hungarian
    ma -> min algoritme
    ao -> ant optimization
    """
    
    if bf == 'y':
        H, W = brute_force(V, E)
        print('BRUTE FORCE ALGORITME\nHamiltonkreds', H, '\nVægt', W)
    if nn == 'y':
        H, W = nærmest_nabo(V, E)
        print('NÆRMEST NABO ALGORITME\nHamiltonkreds', H, '\nVægt', W)
    if na == 'y':
        H, W = nærmest_addition(V, E)
        print('NÆRMEST ADDITION ALGORITME\nHamiltonkreds', H, '\nVægt', W)
    if dt == 'y':
        H, W = dobbelttræ(V, E)
        print('DOBBELTTRÆ ALGORITME\nHamiltonkreds', H, '\nVægt', W)
    if cf == 'y':
        H, W = christofides(V, E)
        print('CHRISTOFIDES ALGORITME\nHamiltonkreds', H, '\nVægt', W)
    if op == 'y':
        H, W = opt2(V, E)
        print('2OPT ALGORITME\nHamiltonkreds', H, '\nVægt', W)
    if hu == 'y':
        H, W = hungarian(V, E)
        print('UNGARSK ALGORITME\nHamiltonkreds', H, '\nVægt', W)
    if ma == 'y':
        H, W = my_algorithm(V, E)
        print('MIN ALGORITME\nHamiltonkreds', H, '\nVægt', W)
    if ao == 'y':
        H, W = ant_optimization(V, E, 10000)
        print('ANT OPTIMIZATION ALGORITME\nHamiltonkreds', H, '\nVægt', W)


def test_dhp_alg_repeat(n,times,bf='n',nn='n',na='n',dt='n',cf='n',op='n',hu='n',ma='n',ao='n'):
    """
    Tester Den Handelsrejsendes Problem algoritmerne gentagne gange på tilfældige metriske grafer.
    
    En algoritme testes, hvis den tilsvarende variabel er yes ('y').
    
    bf -> brute force
    nn -> nærmest nabo
    na -> nærmest addition
    dt -> dobbelttræ
    cf -> christofides
    op -> 2opt
    hu -> hungarian
    ma -> min algoritme
    ao -> ant optimization
    """
    
    BF, NN, NA, DT, CF, OP, HU, MA, AO = [], [], [], [], [], [], [], [], []
    
    for i in range(times):
        g = complete_graph(n)

        V = generate_vertices(g)
        E = generate_edges(g)
        EW = add_weights(E,20,40)
        
        if bf == 'y':
            H, W = brute_force(V, EW)
            print('BRUTE FORCE ALGORITME\nHamiltonkreds', H, '\nVægt', W)
            BF.append(W)
            
        if nn == 'y':
            H, W = nærmest_nabo(V, EW)
            print('NÆRMEST NABO ALGORITME\nHamiltonkreds', H, '\nVægt', W)
            NN.append(W)
        
        if na == 'y':
            H, W = nærmest_addition(V, E)
            print('NÆRMEST ADDITION ALGORITME\nHamiltonkreds', H, '\nVægt', W)
            NA.append(W)
            
        if dt == 'y':
            H, W = dobbelttræ(V, EW)
            print('DOBBELTTRÆ ALGORITME\nHamiltonkreds', H, '\nVægt', W)
            DT.append(W)
            
        if cf == 'y':
            H, W = christofides(V, EW)
            print('CHRISTOFIDES ALGORITME\nHamiltonkreds', H, '\nVægt', W)
            CF.append(W)
            
        if op == 'y':
            H, W = opt2(V, EW)
            print('2OPT ALGORITME\nHamiltonkreds', H, '\nVægt', W)
            OP.append(W)
            
        if hu == 'y':
            H, W = hungarian(V, EW)
            print('UNGARSK ALGORITME\nHamiltonkreds', H, '\nVægt', W)
            HU.append(W)
        
        if ma == 'y':
            H, W = my_algorithm(V, E)
            print('MIN ALGORITME\nHamiltonkreds', H, '\nVægt', W)
            MA.append(W)
        
        if ao == 'y':
            H, W = ant_optimization(V, E)
            print('ANT OPTIMIZATION ALGORITME\nHamiltonkreds', H, '\nVægt', W)
            AO.append(W)
    
    if bf == 'y':
        print('BRUTE FORCE ALGORITME', np.mean(BF))
    if nn == 'y':
        print('NÆRMEST NABO ALGORITME', np.mean(NN))
    if na == 'y':
        print('NÆRMEST ADDITION ALGORITME', np.mean(NA))
    if dt == 'y':
        print('DOBBELTTRÆ ALGORITME', np.mean(DT))
    if cf == 'y':
        print('CHRISTOFIDES ALGORITME', np.mean(CF))
    if op == 'y':
        print('2OPT ALGORITME', np.mean(OP))
    if hu == 'y':
        print('UNGARSK ALGORITME', np.mean(HU))
    if ma == 'y':
        print('MIN ALGORITME', np.mean(MA))
    if ao == 'y':
        print('ANT OPTIMIZATION ALGORITME', np.mean(AO))



"""
Euklidiske grafer og visualisering af koncepter i grafteori
De Euklidiske grafer består af punkter spredt ud på et 10x10 Euklidisk plan.

De fire funktioner med navne lig koncepter i grafteori, printer hver en graf, som både viser den Euklidiske graf og konceptet.

Den Handelsrejsendes Problem plotter de ni algoritmer for det problem.

Kortest sti plotter Dijkstras og den selvlavede grådig (fra Andreas) for en Euklidisk graf, men hvor antal kanter er formindsket, så det ikke er en komplet graf.

Minimum udspændende træer plotter tre ens minimum udspændende træer dannet af tre forskellige algoritmer.

Maksimal minimum parring plotter en maksimal minimum parring, dannet ved Brute force.
"""

import matplotlib.pyplot as plt
plt.style.use('seaborn')


def euklidisk(n):
    """
    Danner en komplet vægtet graf med n punkter.
    Vægten af kanterne er afstanden mellem punkterne i Euklidisk rum.
    
    Input
    n -> antallet af punkter

    Output
    V -> en liste af punkter
    E -> en liste af vægtet kanter, hvor vægten er afstanden mellem punkterne
    points -> en ordbog, der tager et punkt over til dens koordinater
    
    Eksempel
    #>>> euklidisk(3)
    #(['0', '1', '2'], [['0', '1', 3.678558531374192], ['0', '2', 5.6828783784090335], ['1', '2', 3.785905762085186]], {'0': [2.0487366605768145, 4.978508713767679], '1': [4.959068723940273, 7.228344296583554], '2': [7.721494686951621, 4.639505707897376]})
    """
    
    V, points = [], dict()
    for i in range(n): #Danner punktlisten og koordinat ordbog
        V.append(str(i))
        points[V[-1]] = [10*r.random(),10*r.random()]
        
    E = []
    for i in range(n-1): #Udregner afstand mellem punkter og danner kantlisten
        for j in range(i+1,n):
            xi, yi = points[str(i)]
            xj, yj = points[str(j)]
            l = ((xj-xi)**2 + (yj-yi)**2)**(1/2)
            E.append([str(i),str(j),l])
            
    return V, E, points


def den_handelsrejsendes_problem(n):
    """
    Funktionen tager et antal punkter, hvor der så dannes en Euklidisk graf med det antal punkter.
    Derefter anvendes alle ni DHP algoritmer på grafen.
    Til sidst dannes en figur, som viser alle de dannede Hamiltonkredse.
    """
    
    V, E, points = euklidisk(n) #Danner en Euklidisk graf
    
    G = []
    for e in E: #Danner en sti som går over alle kanter. Dannes for at plotte alle kanter
        G += e[:2]
        
    x,y = [],[]
    for v in G: #Finder koordinatsæt for alle punkterne i G stien
        vx, vy = points[v]
        x.append(vx); y.append(vy)
    
    H_bf, w_bf = brute_force(V, E) #Alle algoritmer anvendes og resultatet gemmes
    H_nn, w_nn = nærmest_nabo(V, E)
    H_na, w_na = nærmest_addition(V, E)
    
    H_dt, w_dt = dobbelttræ(V, E)
    H_cf, w_cf = christofides(V, E)
    H_op, w_op = opt2(V, E)
    
    H_hu, w_hu = hungarian(V, E)
    H_ma, w_ma = my_algorithm(V, E)
    H_ao, w_ao = ant_optimization(V, E, 10000)
    
    
    x_bf, y_bf = [], []; x_nn, y_nn = [], []; x_na, y_na = [], [] #Gemmer koordinatsæt i rækkefølge for alle Hamiltonkredsene
    x_dt, y_dt = [], []; x_cf, y_cf = [], []; x_op, y_op = [], []
    x_hu, y_hu = [], []; x_ma, y_ma = [], []; x_ao, y_ao = [], []
    
    for v in H_bf: #Finder koordinatsæt i rækkefølge fro alle Hamiltonkredse
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
    
    fig, axs = plt.subplots(3, 3, dpi=500) #Danner figuren
    #fig.suptitle('Den Handelsrejsendes Problem')
    
    (ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9) = axs #Plotter brute force
    ax1.plot(x, y, color='darkgray', linewidth=0.5)
    ax1.plot(x_bf, y_bf, 'o-', color='firebrick', linewidth=1)
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.set_title('Brute Force '+str(round(w_bf,2)), fontsize=12)
    
    ax2.plot(x, y, color='darkgray', linewidth=0.5) #Plotter nærmest nabo
    ax2.plot(x_nn, y_nn, 'o-', color='firebrick', linewidth=1)
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.set_title('Nærmest nabo '+str(round(w_nn,2)), fontsize=12)
    
    ax3.plot(x, y, color='darkgray', linewidth=0.5) #Plotter nærmest addition
    ax3.plot(x_na, y_na, 'o-', color='firebrick', linewidth=1)
    ax3.set_xticks([])
    ax3.set_yticks([])
    ax3.set_title('Nærmest addition '+str(round(w_na,2)), fontsize=12)
    
    ax4.plot(x, y, color='darkgray', linewidth=0.5) #Plotter dobbelttræ
    ax4.plot(x_dt, y_dt, 'o-', color='firebrick', linewidth=1)
    ax4.set_xticks([])
    ax4.set_yticks([])
    ax4.set_title('Dobbelttræ '+str(round(w_dt,2)), fontsize=12)
    
    ax5.plot(x, y, color='darkgray', linewidth=0.5) #Plotter christofides
    ax5.plot(x_cf, y_cf, 'o-', color='firebrick', linewidth=1)
    ax5.set_xticks([])
    ax5.set_yticks([])
    ax5.set_title('Christofides '+str(round(w_cf,2)), fontsize=12)
    
    ax6.plot(x, y, color='darkgray', linewidth=0.5) #Plotter 2opt
    ax6.plot(x_op, y_op, 'o-', color='firebrick', linewidth=1)
    ax6.set_xticks([])
    ax6.set_yticks([])
    ax6.set_title('2opt '+str(round(w_op,2)), fontsize=12)
    
    ax7.plot(x, y, color='darkgray', linewidth=0.5) #Plotter den ungarske metode
    ax7.plot(x_hu, y_hu, 'o-', color='firebrick', linewidth=1)
    ax7.set_xticks([])
    ax7.set_yticks([])
    ax7.set_title('Hungarian '+str(round(w_hu,2)), fontsize=12)
    
    ax8.plot(x, y, color='darkgray', linewidth=0.5) #Plotter min metode
    ax8.plot(x_ma, y_ma, 'o-', color='firebrick', linewidth=1)
    ax8.set_xticks([])
    ax8.set_yticks([])
    ax8.set_title('Min algoritme '+str(round(w_ma,2)), fontsize=12)
    
    ax9.plot(x, y, color='darkgray', linewidth=0.5) #Plotter ant optimization simulation
    ax9.plot(x_ao, y_ao, 'o-', color='firebrick', linewidth=1)
    ax9.set_xticks([])
    ax9.set_yticks([])
    ax9.set_title('Ant optimization '+str(round(w_ao,2)), fontsize=12)


def kortest_sti(n):
    """
    Funktionen tager et antal punkter, hvor der så dannes en Euklidisk graf med det antal punkter.
    Derefter anvendes to kortest sti algoritmer på grafen.
    Til sidst dannes en figur, som viser de to dannede stier.
    """
    
    V, E, points = euklidisk(n) #Danner en Euklidisk graf
    
    E = []
    for i in range(n-1): #Danner en færrer mængde kanter
        k = 0
        for j in range(i+1,n):
            if k == 2:
                break
            xi, yi = points[str(i)]
            xj, yj = points[str(j)]
            l = ((xj-xi)**2 + (yj-yi)**2)**(1/2)
            E.append([str(i),str(j),l])
            k += 1
    
    S_di, w_di = dijkstras(V, E, V[0], V[-1]) #Anvender Dijkstras algoritme
    x_di, y_di = [], []
    for v in S_di: #Finder rækkefølgen af punkternes koordinater i stien fra Dijkstras algoritme
        vx, vy = points[v]
        x_di.append(vx); y_di.append(vy)
    
    S_gr, w_gr = graadig(V, E, V[0], V[-1]) #Anvender den grådige algoritme
    x_gr, y_gr = [], []
    for v in S_gr: #Finder rækkefølgen af punkternes koordinater i stien fra den grådige algoritme
        vx, vy = points[v]
        x_gr.append(vx); y_gr.append(vy)
    
    fig, axs = plt.subplots(1, 2, figsize=(6, 3), dpi=500) #Danner figuren
    #fig.suptitle('Kortest sti')
    
    (ax1, ax2) = axs
    for e in E: #Plotter Dijkstras algoritme
        x, y = [], []
        for v in e[:2]:
            vx, vy = points[v]
            x.append(vx); y.append(vy)
        ax1.plot(x, y, 'o-', color='darkgrey', linewidth=0.5)
    ax1.plot(x_di, y_di, 'o-', color='navy', linewidth=1)
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.set_title('Dijkstras algoritme '+str(round(w_di,2)), fontsize=12)
    
    for e in E: #Plotter den grådige algoritme
        x, y = [], []
        for v in e[:2]:
            vx, vy = points[v]
            x.append(vx); y.append(vy)
        ax2.plot(x, y, 'o-', color='darkgrey', linewidth=0.5)
    ax2.plot(x_gr, y_gr, 'o-', color='navy', linewidth=1)
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.set_title('Grådig algoritme '+str(round(w_gr,2)), fontsize=12)


def minimum_udspændende_træer(n):
    """
    Funktionen tager et antal punkter, hvor der så dannes en Euklidisk graf med det antal punkter.
    Derefter anvendes Prims algoritme på grafen.
    Til sidst dannes en figur, som viser det dannede minimum udspændende træ.
    """
    
    V, E, points = euklidisk(n) #Danner en Euklidisk graf
    
    G = []
    for e in E: #Danner en sti som går over alle kanter. Dannes for at plotte alle kanter
        G += e[:2]
        
    x,y = [],[]
    for v in G: #Finder koordinatsæt for alle punkterne i G stien
        vx, vy = points[v]
        x.append(vx); y.append(vy)
    
    V_p, E_p = prims(V, E) #Anvender Prims algoritme
    V_k, E_k = kruskals(V, E) #Anvender Kruskals algoritme
    V_b, E_b = boruvkas(V, E) #Anvender Boruvkas algoritme
    
    fig, axs = plt.subplots(1, 3, figsize=(9, 3), dpi=500) #Danner figuren
    #fig.suptitle('minimum udspændende træ')

    (ax1, ax2, ax3) = axs
    ax1.plot(x, y, 'o-', color='darkgray', linewidth=0.5) #Plotter Prims algoritme
    for e in E_p:
        x_p, y_p = [], []
        for v in e[:2]:
            vx, vy = points[v]
            x_p.append(vx); y_p.append(vy)
        ax1.plot(x_p, y_p, 'o-', color='forestgreen', linewidth=1)
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.set_title('Prims', fontsize=20)
    
    ax2.plot(x, y, 'o-', color='darkgray', linewidth=0.5) #Plotter Kruskals algoritme
    for e in E_k:
        x_k, y_k = [], []
        for v in e[:2]:
            vx, vy = points[v]
            x_k.append(vx); y_k.append(vy)
        ax2.plot(x_k, y_k, 'o-', color='limegreen', linewidth=1)
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.set_title('Kruskals', fontsize=20)
    
    ax3.plot(x, y, 'o-', color='darkgray', linewidth=0.5) #Plotter Boruvkas algoritme
    for e in E_b:
        x_b, y_b = [], []
        for v in e[:2]:
            vx, vy = points[v]
            x_b.append(vx); y_b.append(vy)
        ax3.plot(x_b, y_b, 'o-', color='darkolivegreen', linewidth=1)
    ax3.set_xticks([])
    ax3.set_yticks([])
    ax3.set_title('Boruvkas', fontsize=20)


def maksimal_minimum_parring(n):
    """
    Funktionen tager et antal punkter, hvor der så dannes en Euklidisk graf med det antal punkter.
    Derefter anvendes en brute force maksimal minimum parring algoritme på grafen.
    Til sidst dannes en figur, som viser den dannede maksimal minimum parring.
    """
    
    V, E, points = euklidisk(n) #Danner en Euklidisk graf
    
    G = []
    for e in E: #Danner en sti som går over alle kanter. Dannes for at plotte alle kanter
        G += e[:2]
        
    x,y = [],[]
    for v in G: #Finder koordinatsæt for alle punkterne i G stien
        vx, vy = points[v]
        x.append(vx); y.append(vy)
        
    M = min_maximal_matching(V, E) #Anvender brute force maksimal minimum parring algoritme
    
    fig, axs = plt.subplots(1, 1, dpi=500) #Danner figuren
    #fig.suptitle('Kortest sti')
    
    ax1 = axs
    ax1.plot(x, y, 'o-', color='darkgray', linewidth=0.5) #Plotter maksimal minimum parring
    for e in M:
        x_m, y_m = [], []
        for v in e[:2]:
            vx, vy = points[v]
            x_m.append(vx); y_m.append(vy)
        ax1.plot(x_m, y_m, 'o-', color='black', linewidth=1)
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.set_title('Maksimal minimum parring', fontsize=20)


def tree_mod_dhp(n):
    """
    Funktionen tager et antal punkter, hvor der så dannes en Euklidisk graf med det antal punkter.
    Derefter anvendes brute force og træ modificationerne på grafen.
    Til sidst dannes en figur, som viser alle de dannede Hamiltonkredse.
    """
    
    V, E, points = euklidisk(n) #Danner en Euklidisk graf
    
    G = []
    for e in E: #Danner en sti som går over alle kanter. Dannes for at plotte alle kanter
        G += e[:2]
        
    x,y = [],[]
    for v in G: #Finder koordinatsæt for alle punkterne i G stien
        vx, vy = points[v]
        x.append(vx); y.append(vy)
    
    H_dt, w_dt = dobbelttræ(V, E) #Alle algoritmer anvendes og resultatet gemmes
    H_p, w_p = prims_mod(V, E)
    H_k, w_k = kruskals_mod(V, E) 
    H_b, w_b = boruvkas_mod(V, E)
    
    
    #Gemmer koordinatsæt i rækkefølge for alle Hamiltonkredsene
    x_dt, y_dt = [], []; x_p, y_p = [], []; x_k, y_k = [], []; x_b, y_b = [], []
    
    for v in H_dt: #Finder koordinatsæt i rækkefølge fro alle Hamiltonkredse
        vx, vy = points[v]
        x_dt.append(vx); y_dt.append(vy)
    for v in H_p:
        vx, vy = points[v]
        x_p.append(vx); y_p.append(vy)
    for v in H_k:
        vx, vy = points[v]
        x_k.append(vx); y_k.append(vy)  
    for v in H_b:
        vx, vy = points[v]
        x_b.append(vx); y_b.append(vy)
        
    
    fig, axs = plt.subplots(2, 2, dpi=500) #Danner figuren
    #fig.suptitle('Den Handelsrejsendes Problem')
    
    (ax1, ax2), (ax3, ax4) = axs #Plotter brute force
    
    ax1.plot(x, y, color='darkgray', linewidth=0.5)
    ax1.plot(x_dt, y_dt, 'o-', color='firebrick', linewidth=1)
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.set_title('Dobbelttræ '+str(round(w_dt,2)), fontsize=12)
    
    ax2.plot(x, y, color='darkgray', linewidth=0.5) #Plotter nærmest nabo
    ax2.plot(x_p, y_p, 'o-', color='firebrick', linewidth=1)
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.set_title('Prims mod '+str(round(w_p,2)), fontsize=12)
    
    ax3.plot(x, y, color='darkgray', linewidth=0.5) #Plotter nærmest addition
    ax3.plot(x_k, y_k, 'o-', color='firebrick', linewidth=1)
    ax3.set_xticks([])
    ax3.set_yticks([])
    ax3.set_title('Kruskals mod '+str(round(w_k,2)), fontsize=12)
    
    ax4.plot(x, y, color='darkgray', linewidth=0.5) #Plotter dobbelttræ
    ax4.plot(x_b, y_b, 'o-', color='firebrick', linewidth=1)
    ax4.set_xticks([])
    ax4.set_yticks([])
    ax4.set_title('Boruvkas mod '+str(round(w_b,2)), fontsize=12)
    


if __name__ == '__main__':
    import doctest #doctest tester om alle funktionerne giver samme resultat som eksemplerne
    
    print(doctest.testmod())
    print('dude')
    
