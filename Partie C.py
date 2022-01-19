import numpy as np
import matplotlib.pyplot as plt
import math as m
M=[["Beat it", [4, 3, 18, 0, 132, 2.417]]]

def permutation(Mat,i,j):
    s=Mat[i]
    Mat[i]=Mat[j]
    Mat[j]=s

def ajout_musique(M,nom,cre,decre,stac,porta,tempo,inter):
    M.append([nom,[cre, decre, stac, porta, tempo, inter]])
    return M

ajout_musique(M,"How Will I know", 17, 4, 34, 0, 120, 5.281)
ajout_musique(M,"Together Again", 4, 2, 16, 0, 120, 5.875)
ajout_musique(M,"No Scrubs", 10, 4, 14, 24, 90, 5.563)
ajout_musique(M,"Poker Face", 4, 2, 16, 8, 120, 4.75)
ajout_musique(M,"Crazy in Love", 7, 4, 19, 24, 100, 5.563)
ajout_musique(M,"Only Girl", 18, 2, 56, 11, 126, 3.24)
ajout_musique(M,"Say My Name", 10, 2, 21, 26, 70, 5.25)
ajout_musique(M,"Dreamlover", 6, 4, 19, 8, 104, 5.375)
ajout_musique(M,"Like a Virgin", 4, 0, 14, 0, 118, 2.938)
ajout_musique(M,"Billie Jen", 9, 4, 14, 9, 117, 3.15)
ajout_musique(M,"I Wanna Dance", 10, 2, 38, 12, 120, 1.563)
ajout_musique(M,"All for You", 0, 4, 10, 15, 114, 4.389)
ajout_musique(M,"Waterfalls", 3, 2, 15, 8, 84, 1.5)
ajout_musique(M,"Born This Way", 9, 1, 14, 9, 124, 2.656)
ajout_musique(M,"Single Ladies", 8, 0, 36, 28, 96, 5.292)
ajout_musique(M,"Umbrella", 5, 6, 34, 4, 86, 4.375)
ajout_musique(M,"Bootylicious", 14, 2, 20, 16, 104, 7.75)
ajout_musique(M,"Fantasy", 7, 1, 16, 7, 112, 5.375)
ajout_musique(M,"Like a Prayer", 3, 1, 10, 0, 120, 4.375)

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


    return N
Mb=(seuils(M))  #binaire + nom
# print(Mb)
Mbi=[]
for i in range(len(Mb)):
    Mbi.append(Mb[i][1])
# print(Mbi)
# A=np.array(Mbi)
# print(Mbi)    #binaire uniquement
# print(A)      #binaire uniquement
# print(Mbi)
n = len(max(Mbi, key=len))
# Faire des listes de longueur égale
liste_2 = [x + [None]*(n-len(x)) for x in Mbi]
# print(liste_2)
# [[1, 2, 3, None], [4, 5, None, None], [6, 7, 8]]
# Convertissez le en tableau NumPy
A = np.array(liste_2)
Mbi=A[:,0:6]
# Imprimer le tableau résultant
# print(Mbi)

def simil(M):
    tM=M.T
    S=np.dot(M,tM)
    return S
Ms=simil(Mbi)
# print(Ms)
Ms=np.array(Ms, dtype=float)
U,W,V=np.linalg.svd(Ms)
# print("U : ",U," V : ",V," W : ",W)

# print(W)

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

# print(U)
dmax1,dmax2,i_max1,i_max2=recherche_2plusgrandes(W)
Ud=U[:,:2]
Vd=V[:2,:]
# Vd=Vd.T
# print(Ud)
I=np.eye(20)
for i in range(20):
    I[i,i]=W[i]
Wb=I[:2,:2]
Wb=np.dot(Wb,Vd)
Xb=np.dot(Ud,Wb)

# Udt=Ud.T
# X=np.array([i for i in range(20)])
# print(X)
# Xt=X.T
# print(X)
# Test=np.dot(Udt,W)
# print(Test)
# Test=np.dot(Test,Ud)
# print(recherche_2plusgrandes(W))
# plt.plot(X,Ud[0],'o-')
# for i in range(20):
#     plt.annotate(M[i][0], (X[i],Ud[0][i]))

# plt.plot(Vd[1],Ud[1],'o-')
# plt.show()
U1=[[0,0]for i in range(20)]
U2=[[0,0]for i in range(20)]
# print(U1)
for i in range(20):
    U1[i][0]=Ud[i,0]
    U1[i][1]=M[i][0]
    U2[i][0]=Ud[i,1]
    U2[i][1]=M[i][0]
# print(U2[0])
# print(U2[10])

## 3.

D=np.eye(20)
for i in range(20):
    for j in range(20):
        pds1=U1[i][0]*U1[j][0]
        pds2=U2[i][0]*U2[j][0]
        pds=pds1+pds2
        n1=m.sqrt(U1[i][0]**2+U2[i][0]**2)
        n2=m.sqrt(U1[j][0]**2+U2[j][0]**2)
        D[i,j]=pds/(n1*n2)
# print(D)
# print(D==D.T)
X=np.array([i for i in range(20)])
# print(D[0])

# plt.plot(X,D[0])
# plt.xlim(0,20)
# plt.ylim(-1,1)
# for i in range(20):
    # plt.annotate(M[i][0], (X[i],D[0][i]))


# plt.show()
C1=[[0,0]for i in range(20)]
# print(C1)
for i in range(20):
    C1[i][0]=D[0,i]
    C1[i][1]=M[i][0]
# print(C1)

def tri_croissant(V):
    for i in range(len(V)):
        i_min=i
        Vmin=V[i]
        for j in range(len(V[i+1:])+1):
            if Vmin>V[j+i]:
                Vmin=V[j+i]
                i_min=j+i
        # print(V)
        permutation(V,i,i_min)
        # permutation(M,i,i_min)
    return V

def permutation(Mat,i,j):
    s=Mat[i]
    Mat[i]=Mat[j]
    Mat[j]=s

C1=tri_croissant(C1)
C1=np.array(C1)
# print(C1)

Cb=[]    #j'arrive pas a tracer un array avec plot
Cn=[]
for i in range(20):
        Cb.append(C1[i,:1][0])
        Cn.append(C1[i,1:][0])
# print(Cb)
# plt.plot(X,Cb,'o-')
# for i in range(20):
    # plt.annotate(Cn[i], (X[i],Cb[i]))
# plt.xlim(0,20)
# plt.ylim(-1,10)
# plt.show()

D=np.eye(20)
S=[0]*20
# print(S)
for i in range(20):
    n1=m.sqrt(np.dot(Xb[0],Xb[0].T))
    n2=m.sqrt(np.dot(Xb[i],Xb[i].T))
    d=np.dot(Xb[0],Xb[i].T)/(n1*n2)
    D[i,i]=d
    S[i]=d
# print(S)
# plt.plot(X,S)
# for i in range(20):
#     plt.annotate(M[i][0], (X[i],S[i]))

# S2=S[1:]
# S2=tri_croissant(S2)
# plt.plot(X[:-1],S2)
# for i in range(19):
    # plt.annotate(M[i+1][0], (X[i],S[i]))
# plt.show()
D=np.eye(20)
for i in range(20):
    for j in range(20):
        n1=m.sqrt(np.dot(Xb[j],Xb[j].T))
        n2=m.sqrt(np.dot(Xb[i],Xb[i].T))
        d=np.dot(Xb[j],Xb[i].T)/(n1*n2)
        D[i,j]=d
# print(D)
# print(D[7,:])
plt.plot(X,1-D[7,:])
plt.plot(X,1-D[0,:])
for i in range(20):
    # plt.plot(X,1-D[i,:],'o-')
    plt.annotate(M[i][0], (X[i],1-D[0,i]))
plt.show()

## 4. Moyenne de Michael Jackson

S=np.array([0.]*20)
Xb1=np.array([0]*20, dtype=float)
for i in range(20):
    Xb1[i]=(Xb[0,i]+Xb[10,i])
    Xb1[i]=Xb1[i]/2
print(Xb1)
for i in range(20):
    n1=m.sqrt(np.dot(Xb1,Xb1.T))
    n2=m.sqrt(np.dot(Xb[i],Xb[i].T))
    d=np.dot(Xb1,Xb[i].T)/(n1*n2)
    S[i]=d
print(S)
plt.plot(X,S)
for i in range(20):
    plt.annotate(M[i][0], (X[i],S[i]))
plt.show()


















