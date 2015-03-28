# -*- coding: utf-8 -*-

# Imports
# ------------------------------
import os
import sys

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







# Testing
# ------------------------------
if __name__ == "__main__":
    ballons = Ballon()
    print(ballons)
    os.system('pause')