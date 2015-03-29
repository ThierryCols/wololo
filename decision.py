from balloon import *
import random

def decide(balloons, graphe, turn):
    decidedBalloons = []
    scoreMax = 0
    moves = []

    for pos, b in enumerate(balloons):
        if pos > heuristDecollage(turn, balloons):
            bestMove = 0
            bestCandidate = None
            newPositions = graphe.getPossibleMoves(b.x, b.y, b.z)

            if len(newPositions) == 0:
                bestCandidate = b
                bestMove = 0
            else:
                randomPosition = random.choice(newPositions)
                bestMove = randomPosition[0]
                bestCandidate = Balloon(b.id, randomPosition[1][0], randomPosition[1][1], randomPosition[1][2])

            scoreMax = getScore(decidedBalloons)
            decidedBalloons.append(bestCandidate)
            moves.append(bestMove)
        else:
            decidedBalloons.append(b)
            moves.append(0)

    return (decidedBalloons, moves, scoreMax)

def heuristDecollage(turn, balloons):
    return min(len(balloons), int(len(balloons)*(1-(turn+1)/50)))
