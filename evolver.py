from mancala import Board
from brain import Brain


class Evolver:


    def compete(self, brain1: Brain, brain2: Brain):

        board = Board()
        brain1.set_board(board)
        brain2.set_board(board)

        brain1.set_player_num(1)
        brain2.set_player_num(2)

        winner = None

        while winner == None:
            (move, confidence) = brain1.predict()
            print("\n\nP1 move is {} with {}".format(move, confidence))
            if not move in board.possible_player_moves():
                winner = 2
                continue
            has_move = board.make_player_move(move, 1)
            board.print()

            (move, confidence) = brain2.predict()
            print("\n\nP2 move is {} with {}".format(move, confidence))
            if not move in board.get_opponent_board().possible_player_moves():
                winner = 1
                continue
            has_move = board.make_player_move(move, 2)
            board.print()

        print ("Player {} wins!".format(winner))