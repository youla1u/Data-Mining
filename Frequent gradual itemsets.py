# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 10:19:58 2022

@author: cash
"""

import numpy as np


def Matrice_binaire_C(ls): # Cette fonction calcul la marice binaire d'un item graduel
    l=len(ls)
    Z=np.zeros((l, l))
    for i in range(l):
        for j in range(l):
            if i!=j and ls[i]<ls[j]:
               Z[i,j]=1
               Z[j,i]=abs(Z[i,j]-1)
    return Z   


def fils(i,Mb): # Cette fonction fornit la liste des fils d'un noeud(ou d'un objet i) 
    l=[]
    for j in range(np.shape(Mb)[1]):
        if int(Mb[i,j])==1:
           l.append(j)           
    return l 



def RecursiveCovering(i,Mb,M):  # implémentation de l'agoritme GRIT 
    if fils(i,Mb)==[]:
       M[i]=1
    else:
        for f in fils(i,Mb):
            if M[f]==-1:
               RecursiveCovering(f,Mb,M)
        for f in fils(i,Mb):     
            M[i] = max(M[i],M[f] + 1)   
    return M   
  
    
def support(Mb): # calcul du support de l'item graduel 
    M=[-1,-1,-1,-1,-1]
    S=[]
    for i in range(np.shape(Mb)[0]):
        M=RecursiveCovering(i,Mb,M)
        S.append(max(M)) 
    return max(S)

def est_il_frequent(minsup,Mb): # Afirmation de la fréquence ou la non fréquence de l'item graduel 
    if support(Mb)>= minsup:
       return "L'item graduel est fréquent !" 
    else:
       return "L'item graduel n'est pas fréquent !" 
 
      

"""Le programme principal."""

def main():  
     
    saisie1 = input('''Saisissez le chemin de votre fichier, sans les crochets " et '(Exemple: C:/Users/.../fichier.txt)  : \n''')
    chemin=str(saisie1)
    File_data = np.loadtxt(chemin)
    T = np.array( File_data)
    
    
    saisie2 = input('''Saisissez le numéro de colonne de l'item graduel: ''')    
    col = int(saisie2) 
    ls=list(T[:, col])
    Mb= Matrice_binaire_C(ls) 
    
    saisie3 = input('''Saisissez le minsup: ''')    
    minsup = int(saisie3) 
    
    print("-------------------------------------------------------------")
    print(est_il_frequent(minsup,Mb)) 
    print(" ")
    print("Son support est: "+str(support(Mb)))
       
     

if __name__ == "__main__":
    main()

