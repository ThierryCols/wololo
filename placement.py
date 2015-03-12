import parser
import rawData
from operator import itemgetter

rawServerList = rawData.getRawServerList()
serverList = parser.parseInd(rawServerList)

forbiddenPlaces = [(10,23),(0,40),(4,40),(3,57),(11,78),(10,82),(14,27),(1,39),(6,75),(0,47),(3,49),(8,8),(0,42),(3,18),(10,39),(8,71),(3,52),(9,42),(12,95),(0,10),(12,89),(11,17),(5,44),(2,48),(15,31),(5,38),(1,48),(1,54),(13,55),(9,65),(12,91),(11,67),(8,57),(15,56),(6,5),(8,83),(13,27),(9,89),(13,78),(9,23),(11,27),(0,73),(3,64),(4,63),(1,27),(3,72),(1,61),(4,44),(10,17),(5,83),(5,92),(3,35),(4,27),(14,98),(10,36),(9,74),(2,73),(11,66),(2,61),(6,7),(15,83),(8,91),(10,95),(13,48),(12,41),(3,66),(0,51),(5,4),(4,28),(3,37),(15,8),(14,2),(5,3),(10,48),(6,33),(14,63),(7,34),(4,23),(3,94),(8,98)];

rowList = [(0, [], 0),(1, [], 0),(2, [], 0),(3, [], 0),(4, [], 0),(5, [], 0),(6, [], 0),(7, [], 0),(8, [], 0),(9, [], 0),(10, [], 0),(11, [], 0),(12, [], 0),(13, [], 0),(14, [], 0),(15, [], 0)]

for forbiddenPlace in forbiddenPlaces:
	rowList[forbiddenPlace[0]][1].append(forbiddenPlace[1])

def calcRowHeuristic(row):
	if len(row[1]) == 0:
		return 0
	else:
		return (row[0], row[2]/len(row[1]))

rowHeuristicList = map(calcRowHeuristic, rowList)
rowHeuristicList.sort(key=itemgetter(1), reverse=True)

def calcServerHeuristic(server):
	return (server[0], (server[2]*1.0)/(server[1] * 1.0))

serverHeuristicList = map(calcServerHeuristic, serverList)
serverHeuristicList.sort(key=itemgetter(1), reverse=True)

placedServers = []

for serverHeuristic in  serverHeuristicList:
	server = serverList[serverHeuristic[0]]
	placed = False
	rowHeuristicIndex = 0
	place = -1
	while (not(placed)):
		candidateRow = rowList[rowHeuristicList[rowHeuristicIndex][0]]
		for i in range(100 - server[1]):
			possible = True
			for j in range(i, i + server[1]):
				if j in candidateRow[1]:
					possible=False
			if possible and not(placed):
				placedServers.append((server[0], server[1], server[2], candidateRow[0], i))
				for j in range(i, i + server[1]):
					rowList[candidateRow[0]][1].append(j)
				capa = rowList[candidateRow[0]][2] + server[2]
				rowList[candidateRow[0]] = (rowList[candidateRow[0]][0], rowList[candidateRow[0]][1], capa)
				placed= True
				break
		rowHeuristicIndex += 1
		if rowHeuristicIndex==16:
			placed = True
	rowHeuristicList = map(calcRowHeuristic, rowList)
	rowHeuristicList.sort(key=itemgetter(1), reverse=True)

print placedServers
# print serverList