from inpute import *
from copy import deepcopy

matrix = getInput()
# H = len(ref)
# W = len(ref[0])
# matrix = [[ref[i][W-1-j] for j in range(W)] for i in range(H)]

# fonction salement copiées sur Stan

def computeScore(shares):
    score = 0
    for share in shares:
        score += (share[2] - share[0] + 1) * (share[3] - share [1] + 1)
    return score

def saveResultsInFile(shareCount, shares, filename):
    with open(filename,"w") as file:
        file.write(str(shareCount) + "\n")
        for share in shares:
            file.write(str(share[0]) + " " + str(share[1]) + " " + str(share[2]) + " " + str(share[3]) + "\n")

# fin des fonctions de Stan

def mark(i, j, k, l):
    for row in range(i, k+1):
        for col in range(j, l+1):
            matrix[row][col] = 'X'

def build_rect(i, j):
    max_score = 0
    pos_finale = (i, j)
    H_max = 13
    for row in range(i, min(i+12, 180)):
        for col in range(j, max(j-12, -1),-1):
            a = area(i, col, row, j)
            if a <= 12:
                H = H_count(i, col, row, j)
                if H==3 :
                    if H < H_max or a > max_score:
                        H_max = H
                        max_score = a
                        pos_finale = (row, col)
    return pos_finale

def area(i, j, k, l):
    return (k-i+1)*(l-j+1)

def H_count(i, j, k, l):
    H = 0
    for row in range(i, k+1):
        for col in range(j, l+1):
            if matrix[row][col] == 'H':
                H += 1
            elif matrix[row][col] == 'X':
                return -1
    return H


def pick():
    for row in range(0, 180):
        for col in range(59, -1, -1):
            if matrix[row][col] != 'X':
                return (row, col)
    return (-1, -1)

if __name__ == "__main__":
    rects = []
    while pick() != (-1, -1):
        debut_coord = pick()
        fin_coord = build_rect(debut_coord[0], debut_coord[1])
        if debut_coord != fin_coord:
            rects.append((debut_coord[0], fin_coord[1], fin_coord[0], debut_coord[1]))
        mark(debut_coord[0], fin_coord[1], fin_coord[0], debut_coord[1])
    print(computeScore(rects))

    saveResultsInFile(len(rects), rects, 'test_xavier.txt')
