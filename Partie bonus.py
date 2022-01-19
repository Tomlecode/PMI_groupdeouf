import numpy as np
import matplotlib.pyplot as plt
import math as m
M=[["Beat it", [4, 3, 18, 0, 132, 2.417, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0]]]

def permutation(Mat,i,j):
    s=Mat[i]
    Mat[i]=Mat[j]
    Mat[j]=s

def ajout_musique(M,nom,cre,decre,stac,porta,tempo,inter,A,Am,B,C,D,Dm,E,Em,F,G,Gm,ton):
    M.append([nom,[cre, decre, stac, porta, tempo, inter, A, Am, B, C, D, Dm, E, Em, F, G, Gm, ton]])
    return M

def seuils (M):
    N=[]
    for i in range(len(M)):
        N.append([])
        N[i].append(M[i][0])     #ajout du nom dans une autre matrice binaire
        N[i].append([])
        if (M[i][1][0])>=8:     #crescendo
            N[i][1].append(1)
        if (M[i][1][0])<8:
            N[i][1].append(0)

        if (M[i][1][1])>=2:     #decrescendo
            N[i][1].append(1)
        if (M[i][1][1])<2:
            N[i][1].append(0)


        if (M[i][1][2])>=22:     #staccato
            N[i][1].append(1)
        if (M[i][1][2])<22:
            N[i][1].append(0)

        if (M[i][1][3])>=10:     #portamento
            N[i][1].append(1)
        if (M[i][1][3])<10:
            N[i][1].append(0)

        if (M[i][1][4])>=109:     #tempo
            N[i][1].append(1)
        if (M[i][1][4])<109:
            N[i][1].append(0)

        if (M[i][1][5])>=4:     #intervals
            N[i][1].append(1)
        if (M[i][1][5])<4:
            N[i][1].append(0)
        for j in M[i][1][6:]:
            N[i][1].append(j)
    return N

def simil(M):
    tM=M.T
    S=np.dot(M,tM)
    return S

def recherche_2plusgrandes(D):
    dmax1=D[0]
    dmax2=np.amin(D)
    i_max1=0
    i_max2=0
    for i in range(len(D)):
        if D[i]>dmax1:
            dmax1=D[i]
            i_max1=i
        if D[i]<dmax1 and D[i]>=dmax2:
            dmax2=D[i]
            i_max2=i
    return dmax1,dmax2,i_max1,i_max2

ajout_musique(M,"How Will I know", 17, 4, 34, 0, 120, 5.281,0,0,0,1,1,0,0,1,0,1,0,1)
ajout_musique(M,"Together Again", 4, 2, 16, 0, 120, 5.875,0,1,0,1,1,1,0,1,1,1,1,1)
ajout_musique(M,"No Scrubs", 10, 4, 14, 24, 90, 5.563,0,0,0,0,0,0,0,0,0,0,0,0)
ajout_musique(M,"Poker Face", 4, 2, 16, 8, 120, 4.75,0,0,0,1,1,0,0,1,0,1,0,1)
ajout_musique(M,"Crazy in Love", 7, 4, 19, 24, 100, 5.563,0,1,0,1,0,0,0,0,0,0,1,0)
ajout_musique(M,"Only Girl", 18, 2, 56, 11, 126, 3.24,1,0,0,0,1,0,0,1,0,1,0,0)
ajout_musique(M,"Say My Name", 10, 2, 21, 26, 70, 5.25,0,1,0,0,0,1,0,0,1,1,0,0)
ajout_musique(M,"Dreamlover", 6, 4, 19, 8, 104, 5.375,0,0,0,0,0,0,0,0,1,0,1,1)
ajout_musique(M,"Like a Virgin", 4, 0, 14, 0, 118, 2.938,1,1,0,0,0,0,0,1,0,1,0,0)
ajout_musique(M,"Billie Jen", 9, 4, 14, 9, 117, 3.15,0,0,0,0,1,0,1,1,0,1,0,0)
ajout_musique(M,"I Wanna Dance", 10, 2, 38, 12, 120, 1.563,0,1,0,1,1,1,0,0,1,1,0,1)
ajout_musique(M,"All for You", 0, 4, 10, 15, 114, 4.389,0,1,0,0,1,0,1,1,0,0,0,1)
ajout_musique(M,"Waterfalls", 3, 2, 15, 8, 84, 1.5,0,0,0,1,1,0,0,0,1,1,0,1)
ajout_musique(M,"Born This Way", 9, 1, 14, 9, 124, 2.656,1,0,0,0,1,0,1,0,0,0,0,1)
ajout_musique(M,"Single Ladies", 8, 0, 36, 28, 96, 5.292,0,1,0,1,1,1,0,0,1,1,0,1)
ajout_musique(M,"Umbrella", 5, 6, 34, 4, 86, 4.375,0,0,1,0,0,0,0,0,1,0,0,1)
ajout_musique(M,"Bootylicious", 14, 2, 20, 16, 104, 7.75,0,0,0,0,0,0,0,0,0,0,0,0)
ajout_musique(M,"Fantasy", 7, 1, 16, 7, 112, 5.375,0,0,0,0,0,0,0,1,0,1,0,1)
ajout_musique(M,"Like a Prayer", 3, 1, 10, 0, 120, 4.375,0,1,0,1,1,1,1,0,1,0,1,1)

Mb=(seuils(M))
Mbi=[]
for i in range(len(Mb)):
    Mbi.append(Mb[i][1])
Mbi=np.array(Mbi)

Ms=simil(Mbi)
U,W,V=np.linalg.svd(Ms)
dmax1,dmax2,i_max1,i_max2=recherche_2plusgrandes(W)
Ud=U[:,:2]
Vd=V[:2,:]

I=np.eye(20)
for i in range(20):
    I[i,i]=W[i]
Wb=I[:2,:2]
Wb=np.dot(Wb,Vd)
Xb=np.dot(Ud,Wb)

D=np.eye(20)
for i in range(20):
    for j in range(20):
        n1=m.sqrt(np.dot(Xb[j],Xb[j].T))
        n2=m.sqrt(np.dot(Xb[i],Xb[i].T))
        d=np.dot(Xb[j],Xb[i].T)/(n1*n2)
        D[i,j]=d

plt.plot(X,1-D[7,:])
plt.plot(X,1-D[0,:])
for i in range(20):
#     plt.plot(X,1-D[i,:],'o-')
    plt.annotate(M[i][0], (X[i],1-D[0,i]))
plt.show()


