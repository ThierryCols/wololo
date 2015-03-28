from donneesEntree import *


class graph:

    def __init__(self):
        self.data = getInput()
        self.graph = self.buildGraph(data)


# methodes de construction
def buildGraph(self):
    graphDict = {}
    for x in range(0, 75):
        for y in range(0, 5):
            for z in range(0, 8):
                key = str(x)+str(y)+str(z)
                graphDict[key]['x'] = x
                graphDict[key]['y'] = y
                graphDict[key]['z'] = z
                graphDict[key]['L_adj'] = self.getLAdj(x, y, z)
    return graphDict


def getLAdj(self, x, y, z):
    L = []
    if z < 8:
        L.append((x, y, z+1))
    elif z > 0:
        L.append((x, y, z-1))
    w = self.wind(x, y, z)
    L.append((x+w[0], y+w[1], z))
    return L


# methodes publiques
def getPossibleMoves(self, x, y, z, graph):
    key = str(x)+str(y)+str(z)
    return graph[key]['L_adj']


def wind(self, x, y, z):
    return self.data[x][y][z]


if __name__ == "__main__":
    print(self.graph)
