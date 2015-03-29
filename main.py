from graphe import *

from balloon import *

from decision import *

def initBalloons():
    listBalloon = []

    for b in range(0, 53):
        listBalloon.append(Balloon(b, 24, 167, 0))

    return(listBalloon, [], 0)


def saveResults(totalMoves, filename):
    with open(filename,"w") as file:
        string = ''
        for moves in totalMoves:
            for move in moves:
                string += str(move)+' '
            string += "\n"

        file.write(string)


if __name__ == "__main__":
    print('Buiding graph...')
    graphe = Graph()
    print('Graph Built !')

    (currentBalloons, moves, score) = initBalloons()

    scoreTotal = 0
    totalMoves = []

    for turn in range(0, 400):
        (currentBalloons, moves, score) = decide(currentBalloons, graphe, turn)
        scoreTotal += score
        totalMoves.append(moves)
        print('score at turn '+str(turn)+' : '+str(score))

    saveResults(totalMoves, "answer.txt")
    print(scoreTotal)
