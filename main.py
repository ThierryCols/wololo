from graphe import *

from balloon import *

from decision import *



if __name__ == "__main__":
    print('Buiding graph...')
    g = Graph()
    print('Graph Built !')
    balloons = Balloon()
    graphe = Graphe()

    turns = {}

    currentBalloons = initBalloons

    for turn in range(0, 400):
        (currentBalloons, moves, score) = decide(currentBalloons)
        turns[turn] = {}
        turns[turn]['B'] = moves
        turns[turn]['Score'] = score
        print('score at turn '+str(turn)+' : '+str(score))



