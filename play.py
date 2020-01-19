from mancala import Board
from brain import Brain
from evolver import Evolver

if __name__ == '__main__':



    brain1 = Brain()
    brain2 = Brain()

    evolver = Evolver()
    evolver.compete(brain1, brain2)

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
