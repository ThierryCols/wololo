# -*- coding: utf-8 -*-

# Imports
# ------------------------------
import os
import sys
from donneesEntree import *

# Class
# ------------------------------
class Ballon:
    """
    balloon call
    @args : dict {idBallon : {
                                int x
                                int y
                                int z
                                list casesCouvertes (tupl)
                                bool isLost 
                              }
                  }

    """
    def __init__(self):
        """
        Constructor. A simple boolean query is treated. It is a query without any OR statement. 
        Treated simply by creating a list of desired words and another one of not desired words.
        """
        self.balloons = {}

        for balloonId in range(53):
            self.balloons[balloonId] = {}
            self.balloons[balloonId]['x'] = 24
            self.balloons[balloonId]['y'] = 167
            self.balloons[balloonId]['z'] = 0
            self.balloons[balloonId]['casesCouvertes'] = []
            self.balloons[balloonId]['isLost'] = False



    

    def __str__(self):
        """
        Standard method allowing to print the boolean query inputed by the user
        """
        a = ''
        for ballon in self.balloons:
            a += ("Ballon "+str(ballon)+" aux coordonnées " + str(self.balloons[ballon]['x'])+ " , "+ str(self.balloons[ballon]['y'])+ " , "+ str(self.balloons[ballon]['z'])+'\n') 
        return a

    def getBalloonCoordinates(self, idBallon):
        return (self.balloons[idBallon]['x'], self.balloons[idBallon]['y'], self.balloons[idBallon]['z'])

    def setBalloonCoordinates(self, idBallon, x, y, z):
        self.balloons[idBallon]['x'] = x
        self.balloons[idBallon]['y'] = y
        self.balloons[idBallon]['z'] = z


    def setCoveredArea(self, idBallon):
        x = self.balloons[idBallon]['x']
        y = self.balloons[idBallon]['y']
        coveredArea = []
        #z = self.balloons[idBallon]['z']
        for row in range(x - 7, x+7):
            for col in range(y - 7, y + 7):
                if (x - row)*(x - row) + (y - col)*(y - col) <= 9 :
                    if row >= 0 and row <= 74:
                        if col >= 0 and col <= 299:
                            coveredArea.append((row,col))
                        elif col >= 299:
                            colFin = col - 300
                            coveredArea.append((row,colFin))
                        elif col < 0:
                            colFin = 300 + col
                            coveredArea.append((row,colFin))

        self.balloons[idBallon]['casesCouvertes'] = coveredArea

    def getCoveredArea(self, idBallon):
        self.setCoveredArea(idBallon)
        return self.balloons[idBallon]['casesCouvertes']

    def getScore(self):
        cibles = getCasesCibles()
        scoreDict = {}
        for ballon in self.balloons:
            couverture = self.getCoveredArea(ballon)
            for cible in cibles:
                if cible in couverture:
                    if cible in scoreDict.keys():
                        scoreDict[cible] += 1
                    else:
                        scoreDict[cible] = 1
        score = len(scoreDict)
        return score

        



# Testing
# ------------------------------
if __name__ == "__main__":
    ballons = Ballon()
    #print(ballons)
    test = ballons.getBalloonCoordinates(23)
    print(test)
    ballons.setBalloonCoordinates(23, 0, 0, 0)

    test = ballons.getBalloonCoordinates(23)
    print(test)

    print(ballons.getCoveredArea(23))
    print(ballons.getScore())
    os.system('pause')