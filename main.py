from graphe import *

from balloon import *


def computeMoves(balloons):
    update balloons
    retourne la liste des mouvements ascensionnel des ballons
    return (balloonsMoves, score)

if __name__ == "__main__":
    print('Buiding graph...')
    g = Graph()
    print('Graph Built !')
    balloons = Balloon()

    turns = {}

    for turn in range(0, 400):
        balloonsMoves = computeMoves
        score = balloons.score
        turns[turn] = {}
        turns[turn]['B'] = balloonsMoves[0]
        turns[turn]['Score'] = balloonsMoves[1]

