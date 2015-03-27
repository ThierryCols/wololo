# -*- coding: utf-8 -*-
from inpute import *
import random

def greedLol():
	allowedShapes = [(3,4), (4,3), (2,6), (6,2), (1,12), (12,1)]
	pizza = getInput()
	sharesCounter = 0
	shares = []
	# On parcourt la grande pizza
	for x in range(180):
		for y in range(60):
			case = pizza[x][y]
			jambonShapes = []
			for shape in allowedShapes:
				forbidden = False
				compteurDeJambon = 0
				if ((x + shape[0]) <= 180 and (y + shape[1]) <= 60):
					for i in range(x, x + shape[0]):
						for j in range(y, y + shape[1]):
							candidate = pizza[i][j]
							if candidate == "X":
								forbidden = True
							else:
								if candidate == "H":
									compteurDeJambon += 1
					if (not forbidden) and compteurDeJambon >= 3:
						jambonShapes.append((compteurDeJambon, shape))
			if (len(jambonShapes) != 0):
				jambonShapes.sort(key=lambda tup: tup[0])
				shape = jambonShapes[0][1]
				sharesCounter += 1
				pizza = placeShapeAndReturnThePizzaLol(x, y, shape, pizza)
				shares.append((x, y, x + shape[0] - 1, y + shape[1] - 1))
	return (sharesCounter, shares)


def placeShapeAndReturnThePizzaLol(x, y, shape, pizza):
	for i in range(x, x + shape[0]):
		for j in range(y, y + shape[1]):
			pizza[i][j] = "X"
			# TODO add shape to result
	return pizza

def saveResultsInFile(shareCount, shares, filename):
	with open(filename,"w") as file:
		file.write(str(shareCount) + "\n")
		for share in shares:
			file.write(str(share[0]) + " " + str(share[1]) + " " + str(share[2]) + " " + str(share[3]) + "\n")

def computeScore(shares):
	score = 0
	for share in shares:
		score += (share[2] - share[0] + 1) * (share[3] - share [1] + 1)
	return score


(shareCount, shares) = greedLol()
print(computeScore(shares))
saveResultsInFile(shareCount, shares, "lolilol.txt")