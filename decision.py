from balloon import *
import random

def decide(balloons, graphe):
    decidedBalloons = []
    score = 0
    moves = []

    # heuristicchoix ballon?
    for b in balloons:
        scoreMax = -1
        bestMove = 0
        bestCandidate = None
        newPositions = graphe.getPossibleMoves(b.x, b.y, b.z)
        for newPosition in newPositions:
            candidateBalloon = Balloon(b.id, newPosition[1][0], newPosition[1][1], newPosition[1][2])
            candidateDecidedBalloons = decidedBalloons[:]
            candidateDecidedBalloons.append(candidateBalloon)
            s = getScore(candidateDecidedBalloons)

            if s > scoreMax:
                bestCandidate = candidateBalloon
                scoreMax = s
                bestMove = newPosition[0]
        if scoreMax == 0:
            randomPosition = random.choice(newPositions)
            bestMove = randomPosition[0]
            bestCandidate = Balloon(b.id, randomPosition[1][0], randomPosition[1][1], randomPosition[1][2])
        if len(newPositions) == 0:
            bestCandidate = b
            bestMove = 0
        decidedBalloons.append(bestCandidate)
        moves.append(bestMove)
        if scoreMax != -1:
            score += scoreMax

    return (decidedBalloons, moves, score)


