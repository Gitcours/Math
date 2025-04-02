import math as mt
import matplotlib.pyplot as plt

### FONCTIONS

def matrice_translation(vecteur_translation):
    a, b, c = vecteur_translation
    T = [
        [1, 0, 0, a],
        [0, 1, 0, b],
        [0, 0, 1, c],
        [0, 0, 0, 1]
        ]
    print("--- Matrice de translation ---")
    print("T =", T)
    print("\n")
    return T


def matrice_rotation(vecteur_rotation):
    rx, ry, rz = vecteur_rotation
    Rx = [
        [1, 0, 0, 0],
        [0, mt.cos(rx), -mt.sin(rx), 0],
        [0, mt.sin(rx), mt.cos(rx), 0],
        [0, 0, 0, 1]
        ]
    Ry = [
        [mt.cos(ry), 0, mt.sin(ry), 0],
        [0, 1, 0, 0],
        [-mt.sin(ry), 0, mt.cos(ry), 0],
        [0, 0, 0, 1]
        ]
    Rz = [
        [mt.cos(rz), -mt.sin(rz), 0, 0],
        [mt.sin(rz), mt.cos(rz), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
        ]
    #print("--- Matrice de rotation ---")
    #print("Rx =\n", Rx)
    #print("Ry =\n", Ry)
    #print("Rz =\n", Rz)
    Rcombiner = produit_matrices(Rx, Ry)
    Rcombiner = produit_matrices(Rcombiner, Rz)

    print("--- Matrice de rotation combiner ---")
    print(Rcombiner)
    print("\n")
    return Rcombiner #Rx, Ry, Rz

def produit_matrices(A, B):
    C = [[0 for i in range(len(B[0]))] for j in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                C[i][j] += A[i][k] * B[k][j]
    return C


#### INTERFACE JOUEUR

T = [3,4,2]
matrice_translation(T)

E = [mt.pi, mt.pi / 2, mt.pi / 4]
matrice_rotation(E)

A = [[1,2,0,3],[0,0,0,2],[1,2,1,5],[0,0,1,1]]
B = [[0,0,3,0],[0,1,0,1],[4,1,3,0],[1,2,1,0]]

C = produit_matrices(A, B)
print(C, "\n")