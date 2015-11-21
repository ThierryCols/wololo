from donneesEntree import *


class Graph:

    def __init__(self):
        self.data = getWinds()
        self.graph = self.buildGraph()
        self.removeLeaf(self.graph)

    def __str__(self):
        return str(self.graph)


    # methodes de construction
    def buildGraph(self):
        graphDict = {}
        for x in range(0, 75):
            for y in range(0, 300):
                for z in range(0, 9):
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
            if newZ < 9 and newZ > 0:
                # vent
                newCoordXY = self.applyWind(x, y, newZ)
                newX = newCoordXY[0]
                newY = newCoordXY[1]
                if newX != -1:
                    L.append((altDelta, (newX, newY, newZ)))
        return L


    def applyWind(self, x, y, z):
        wind = self.data[z-1][x][y]
        X = x + wind[0]
        Y = y + wind[1]
        if X > 74 or X < 0:
            X = -1
        if Y > 299:
            Y = Y - 300
        elif Y < 0:
            Y = Y + 300
        return (X, Y)

    def removeLeaf(self, graphe):
        terminalLeaves = findTerminalLeaf(graphe)
        print('graphe cleaning ... ')

        while len(terminalLeaves) > 0:
            for key, value in graphe.items():
                lAdj = value['listeAdjacence'][:]
                lFiltered = []
                for element in lAdj:
                    if len(graphe[element[1]]['listeAdjacence']) != 0:
                        lFiltered.append(element)
                value['listeAdjacence'] = lFiltered

            for leave in terminalLeaves:
                del graphe[leave]

            terminalLeaves = findTerminalLeaf(graphe)

    # methodes publiques
    def getPossibleMoves(self, x, y, z):
        key = (x, y, z)
        return self.graph[key]['listeAdjacence']

def findTerminalLeaf(graphe):
    leaveTerminal = []
    for key, value in graphe.items():
        if len(value['listeAdjacence']) == 0:
            leaveTerminal.append(key)
    return leaveTerminal


if __name__ == "__main__":
    print('Buiding graph...')
    g = Graph()
    print('Done !')
    print(g.graph[(0, 139, 1)])
    print(g.getPossibleMoves(0, 139, 1))
