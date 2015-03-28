from graphe import *

from balloon import *

from decision import *

def initBalloons():
    listBalloon = []
    initMoves = []

    for b in range(0, 53):
        listBalloon.append(Balloon(b, 24, 167, 0))
        initMoves.append(0)

    return(listBalloon, initMoves, 0)

if __name__ == "__main__":
    print('Buiding graph...')
    graphe = Graph()
    print('Graph Built !')

    turns = {}

    (currentBalloons, moves, score) = initBalloons()



    for turn in range(0, 400):
        (currentBalloons, moves, score) = decide(currentBalloons, graphe)
        turns[turn] = {}
        turns[turn]['B'] = moves
        turns[turn]['Score'] = score
        print('score at turn '+str(turn)+' : '+str(score))



