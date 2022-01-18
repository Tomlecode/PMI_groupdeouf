import numpy as np

M=[["Beat it", [4, 3, 18, 0, 132, 2.417]]]

def permutation(Mat,i,j):
    s=Mat[i]
    Mat[i]=Mat[j]
    Mat[j]=s

def ajout_musique(M,nom,cre,decre,stac,porta,tempo,inter):
    M.append([nom,[cre, decre, stac, porta, tempo, inter]])
    return M

ajout_musique(M,"How Will I know", 17, 4, 34, 0, 120, 5.281)
ajout_musique(M,"Together Again", 4, 2, 16, 0, 120, 5.876)
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
        if (M[i][1][0])<=8:
            N[i][1].append(0)

        if (M[i][1][1])>=2:     #decrescendo
            N[i][1].append(1)
        if (M[i][1][1])<=2:
            N[i][1].append(0)


        if (M[i][1][2])>=22:     #staccato
            N[i][1].append(1)
        if (M[i][1][2])<=22:
            N[i][1].append(0)

        if (M[i][1][3])>=10:     #portamento
            N[i][1].append(1)
        if (M[i][1][3])<=10:
            N[i][1].append(0)

        if (M[i][1][4])>=109:     #tempo
            N[i][1].append(1)
        if (M[i][1][4])<=109:
            N[i][1].append(0)

        if (M[i][1][5])>=4:     #intervals
            N[i][1].append(1)
        if (M[i][1][5])<=4:
            N[i][1].append(0)


    return N
Mb=(seuils(M))  #binaire + nom

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
# print(simil(Mbi))
Ms=simil(Mbi)
def diago(S):
    n=len(S)
    D=np.eye(n, dtype=int)
    for i in range(n):
        s=0
        for j in range(n):
            s+=S[i,j]
        D[i,i]=D[i,i]*s
    return D
# print(diago(Ms))

Md=diago(Ms)
# print(Md)
# Md=np.diag(Ms)
L=Md-Ms
L=np.array(L, dtype=float)
D, V=np.linalg.eig(L)
D=np.diag(D)
# print(D)   #matrice diago (valeurs propres)
# print(V)    #matrice de passage (vecteurs propres)

def recherche_2nd_mini(D):
    dmin1=D[0,0]
    dmin2=np.amax(D)
    i_min2=0
    for i in range(len(D)):
        if D[i,i]<dmin1:
            dmin1=D[i,i]
        if D[i,i]>dmin1 and D[i,i]<=dmin2:
            dmin2=D[i,i]
            i_min2=i
    return dmin2,i_min2         #Valeur de Fiedler
dmin2,i_min2 = recherche_2nd_mini(D)
# print(i_min2)
# print("valeur propre la seconde plus petite : ",dmin2)
# print("vecteur propre associé : ",V[i_min2])

def tri_croissant(V,M):
    for i in range(len(V)):
        i_min=i
        Vmin=V[i]
        for j in range(len(V[i+1:])+1):
            if Vmin>V[j+i]:
                Vmin=V[j+i]
                i_min=j+i
        # print(V)
        permutation(V,i,i_min)
        permutation(M,i,i_min)
    return V,M
M=np.array(M)
Vcroiss_min,Noms_ordonnés=tri_croissant(V[i_min2],M[:,0])
print("Rangé : ",Vcroiss_min)
print(Noms_ordonnés)