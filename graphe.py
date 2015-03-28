from donneesEntree import *


class Graph:

    def __init__(self):
        self.data = getWinds()
        self.graph = self.buildGraph()

    def __str__(self):
        return str(self.graph)


    # methodes de construction
    def buildGraph(self):
        graphDict = {}
        for x in range(0, 75):
            for y in range(0, 300):
                for z in range(0, 8):
                    key = (x, y, z)
                    graphDict[key] = {}
                    graphDict[key]['x'] = x
                    graphDict[key]['y'] = y
                    graphDict[key]['z'] = z
                    graphDict[key]['listeAdjacence'] = self.getLAdj(x, y, z)
        return graphDict


    def getLAdj(self, x, y, z):
        L = []
        newZ = 0
        for altDelta in [-1, 0, 1]:
            newZ = z + altDelta
            if newZ < 8 and newZ >= 0:
                # vent
                newCoordXY = self.applyWind(x, y, newZ)
                newX = newCoordXY[0]
                newY = newCoordXY[1]
                if newX != -1:
                    L.append((newX, newY, newZ))
        return L


    def applyWind(self, x, y, z):
        C = 299
        wind = self.data[z][x][y]
        X = x + wind[0]
        Y = y + wind[1]
        if X > 74 or X < 0:
            X = -1
        elif Y > C:
            Y = Y - C
        elif Y < 0:
            Y = Y + C
        return (X, Y)


    # methodes publiques
    def getPossibleMoves(self, x, y, z, graph):
        key = (x, y, z)
        return graph[key]['listeAdjacence']


if __name__ == "__main__":
    g = Graph()
    print(g)
