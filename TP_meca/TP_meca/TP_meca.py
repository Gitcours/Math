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
    Rcombiner = produit_matrices(produit_matrices(Rz, Ry), Rx)
    print("Rcombiner = ", Rcombiner, "\n")
    return Rcombiner

def produit_matrices(A, B):
    C = [[0 for i in range(len(B[0]))] for j in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                C[i][j] += A[i][k] * B[k][j]
    return C

def determinant_matrice(M):
    n = len(M)
    if n == 1:
        det = M[0][0]
        return det
    det = 0
    for i in range(n):
        coefficient = M[i][0]
        signe = (-1) ** i
        delta = [row[1:] for j, row in enumerate(M) if j != i]
        det += signe * coefficient * determinant_matrice(delta)
    return det

def inverse_matrice(M):
    n = len(M)

    if determinant_matrice(M) == 0:
        raise ValueError("La matrice n'est pas inversible (determinant nul).")

    A = [[float(val) for val in row] for row in M]
    I = [[float(i == j) for j in range(n)] for i in range(n)]

    for i in range(n):
        pivot = A[i][i]
        if pivot == 0:
            for k in range(i + 1, n):
                if A[k][i] != 0:
                    A[i], A[k] = A[k], A[i]
                    I[i], I[k] = I[k], I[i]
                    pivot = A[i][i]
                    break

        A[i] = [x / pivot for x in A[i]]
        I[i] = [x / pivot for x in I[i]]

        for j in range(n):
            if j != i:
                coeff = A[j][i]
                A[j] = [A[j][k] - coeff * A[i][k] for k in range(n)]
                I[j] = [I[j][k] - coeff * I[i][k] for k in range(n)]
    return I


def position_camera(P):
    position = [P[0][3], P[1][3], P[2][3]]
    print("\nPosition camera :", position)
    return position

def dessiner_axes(ax, P, etiquette, couleur):
    origine = [P[0][3], P[1][3], P[2][3]]
    x_dir = [P[0][0], P[1][0], P[2][0]]
    y_dir = [P[0][1], P[1][1], P[2][1]]
    z_dir = [P[0][2], P[1][2], P[2][2]]
    ax.quiver(*origine, *x_dir, color=couleur, arrow_length_ratio=0.1)
    ax.quiver(*origine, *y_dir, color=couleur, arrow_length_ratio=0.1)
    ax.quiver(*origine, *z_dir, color=couleur, arrow_length_ratio=0.1)
    ax.text(*(origine[i] + x_dir[i] for i in range(3)), f"{etiquette}_x")
    ax.text(*(origine[i] + y_dir[i] for i in range(3)), f"{etiquette}_y")
    ax.text(*(origine[i] + z_dir[i] for i in range(3)), f"{etiquette}_z")

def afficher_world_et_camera(coordonnees_world, C, Pw):
    print("\n--- Affichage 3D ---")
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    world_x, world_y, world_z = coordonnees_world
    ax.scatter(world_x, world_y, world_z, c='b', marker='o',
    label='Coordonnees world', s=54)
    pos_cam = position_camera(C)
    ax.scatter(*pos_cam, c='r', marker='^', label='Position Camera', s=54)
    ax.scatter(*Pw, c='b', marker='^', label='Position Pw avion ennemi', s=54)
    print("Position avion ennemi Pw :", Pw)
    dessiner_axes(ax, C, "C", couleur="red")
    dessiner_axes(ax, [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], "W",
    couleur="blue")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_zlim(-4, 4)
    ax.legend()
    plt.show()

#### INTERFACE JOUEUR

T = [3,4,2]
T = matrice_translation(T)

A = [[1,2,0,3],[0,0,0,2],[1,2,1,5],[0,0,1,1]]
B = [[0,0,3,0],[0,1,0,1],[4,1,3,0],[1,2,1,0]]

print("--- Produit de matrices  ---")
C = produit_matrices(A, B)
print(C, "\n")

print("--- Matrice de rotation combiner ---")
D = [mt.pi, mt.pi / 2, mt.pi / 4]
D = matrice_rotation(D)

print("--- Matrice de passage ---")
E = produit_matrices(T, D)
print(E, "\n")

N = [
[1, 2, 3],
[2, 4, 6],
[0, 1, 1]
]

O = [
[1, 2, 3],
[0, 1, 4],
[5, 6, 0]
]

print("Inverse de la matrice A :", "\n")
print(inverse_matrice(O), "\n")

det=determinant_matrice(N)
print(f"\nLa matrice N est-elle inversible ? : {det != 0} , car det (N) = {det}")
det=determinant_matrice(E)
print(f"La matrice de passage est-elle inversible ? : {det != 0} , car det (M) = {det}")

origine_world = (0, 0, 0)
Pw = [[2],[2],[1]]
afficher_world_et_camera(origine_world, E, Pw)