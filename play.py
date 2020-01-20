from mancala import Board
from brain import Brain
from evolver import Evolver
from math import floor

if __name__ == '__main__':

    pool_size = 128
    iterations = 25

    brains = []

    evolver = Evolver()

    for loop in range(iterations):
        while len(brains) < pool_size:
            brains.append( Brain() )

        brains = evolver.find_top_brains(brains)

        print ("***********************\n  Iteration {} winners\n***********************")
        for b in brains:
            print (b)

    # while True:
    #     (move, confidence) = brain1.predict()
    #     print("\n\nP1 move is {} with {}".format(move, confidence))
    #     has_move = board.make_player_move(move,1)
    #     board.print()
    #
    #     (move, confidence) = brain2.predict()
    #     print("\n\nP2 move is {} with {}".format(move, confidence))
    #     has_move = board.make_player_move(move,2)
    #     board.print()
    #

    # try:
    #     board.print()
    #     while True:
    #         (move, confidence) = brain1.predict()
    #         has_move = board.make_player_move(move)
    #         board.print()
    # except Exception as e:
    #     print (e)
    #     print('Wrong move: ', move)


    # while False:
    #     move = brain1.predict()
    #     for best_move in board.find_best_move(5):
    #         print(best_move)
    #     board = player_move(board)
    #     board = opponent_move(board)
    #
    #     if board.no_more_moves():
    #         print("Games ended")
    #         break
