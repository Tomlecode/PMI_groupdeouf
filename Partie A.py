import numpy as np
# A = [True,True,False,True,False]
# B = [True,False,True,True,True]
# C = [True,True,True,True,False]
# D = [True,False,False,True,True]
Nb_artefacts=4
A = [1,1,0,1,0]
B = [1,0,1,1,1]
C = [1,1,1,1,0]
D = [1,0,0,1,1]
M=np.array([A,B,C,D])

def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

# M=np.array([A,B,C,D])
# tM=M.T
# N=np.ones(4)
# S=np.dot(M,tM)
# N=5*N
# Diss=N-S
# print(Diss)
# s=0
# for i in range(len(Diss)-1):
#     s+=Diss[i,i+1]
# s+=Diss[len(Diss)-1,0]
# print(s)
#
# M2=np.array([A,C,B,D])
# print(M2)
# tM2=M2.T
# S2=np.dot(M2,tM2)
# Diss2=N-S2
# s=0
# for i in range(len(Diss2)-1):
#     s+=Diss2[i,i+1]
# s+=Diss2[len(Diss2)-1,0]
# print(s)
# P=[0,1,2,3]

# print(M[P])
# P=[0,1,3,2]
# print(M[P])

def permutation(Mat,i,j):
    s=Mat[i]
    Mat[i]=Mat[j]
    Mat[j]=s

def dissemblance(Mat):
    N=len(Mat[0])*np.ones(len(Mat))
    tMat=Mat.T
    S=np.dot(Mat,tMat)
    Diss=N-S
    s=0
    for i in range(len(Diss)-1):
        s+=Diss[i,i+1]
    s+=Diss[len(Diss)-1,0]
    return s


Mat_min=[]
Mat=[0,1,2,3]
diss_min=dissemblance(M)
for j in range(0,4):
    permutation(Mat,0,j)
    for i in range(3):
        permutation(Mat,2,3)
        diss=dissemblance(M[Mat])
        # print(diss)
        if diss_min>=diss:
            diss_min=diss
            Mat_min.append([diss,Mat[:]])
        permutation(Mat,1,2)
        diss=dissemblance(M[Mat])
        if diss_min>=diss:
            diss_min=diss
            Mat_min.append([diss,Mat[:]])
        # print(diss)
print("Le minimum vaut : ",diss_min)
# Mat_min=np.array(Mat_min)
print("Dans l'ordre : ",len(Mat_min))

i=0
while i<len(Mat_min):
    if (Mat_min[i][0])!=(Mat_min[-1][0]):
        Mat_min=Mat_min[i+1:]
    i+=1
print("les ordres pour lesquelles les dissemblance sont minimales sont : ",Mat_min)
print("Il y a ",len(Mat_min)," ordres optimals")



