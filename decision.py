from balloon import *

def decide(balloons, graphe):
    decidedBalloons = []
    score = 0
    moves = []

    # heuristicchoix ballon?
    for b in balloons:
        scoreMax = -1
        bestMove = 0
        bestCandidate = Balloon(0, 0, 0, 0)
        newPositions = graphe.getPossibleMoves(b.x, b.y, b.z)
        for newPosition in newPositions:
            candidateBalloon = Balloon(0, newPosition[1][0], newPosition[1][1], newPosition[1][2])
            candidateDecidedBalloons = decidedBalloons[:]
            candidateDecidedBalloons.append(candidateBalloon)
            s = getScore(candidateDecidedBalloons)

            if s > scoreMax:
                bestCandidate = candidateBalloon
                scoreMax = s
                bestMove = newPosition[0]

        decidedBalloons.append(bestCandidate)
        moves.append(bestMove)
        score += scoreMax

    return (decidedBalloons, moves, score)


