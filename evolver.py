from mancala import Board
from brain import Brain
from math import floor

verbosity = 0

class Evolver:


    def compete(self, brain1: Brain, brain2: Brain):

        board = Board()
        brain1.set_board(board)
        brain2.set_board(board)

        brain1.set_player_num(1)
        brain2.set_player_num(2)

        print ("{} is playing against {}".format(brain1.getName(), brain2.getName()))

        winner = None
        full_game_played  = False
        move_count = 0

        while winner == None:
            (move, confidence) = brain1.predict()
            if (verbosity > 4):
                print("\n\nP1 move is {} with {}".format(move, confidence))
            if not move in board.possible_player_moves():
                winner = 2
                continue
            has_move = board.make_player_move(move, 1)
            if (verbosity > 4):
                board.print()

            move_count += 1

            (move, confidence) = brain2.predict()
            if (verbosity > 4):
                print("\n\nP2 move is {} with {}".format(move, confidence))
            if not move in board.get_opponent_board().possible_player_moves():
                winner = 1
                continue
            has_move = board.make_player_move(move, 2)
            if (verbosity > 4):
                board.print()

            move_count += 1

        if winner == None:
            full_game_played = True
            ending = " with a score of {} to {} after a full game".format(board.player_points, board.opponent_points)
            if board.player_points > board.opponent_points:
                winner = 1
            else:
                winner = 2
        else:
            ending = "by disqualification after {} moves. Score was {} to {}".format(move_count, board.player_points, board.opponent_points)


        if winner == 1:
            name = brain1.getName()
            brain1.record_win()
            brain2.record_loss()
        else:
            name = brain2.getName()
            brain2.record_win()
            brain1.record_loss()



        print ("{} wins {}".format(name, ending) )

        return winner



    def find_top_brains(self, brains, percentage = .25 ):
        winner_pool_size = round(len(brains) * percentage)
        loss_ordering = []

        while len(brains) > 1:
            print("\n\nStarting round of {}".format(len(brains)))
            next_round_brains = []
            for x in range(floor(len(brains) / 2)):
                b1 = brains[x * 2]
                b2 = brains[(x * 2) + 1]
                winner = self.compete(b1, b2)
                if winner == 1:
                    next_round_brains.append(b1)
                    loss_ordering.append(b2)
                else:
                    next_round_brains.append(b2)
                    loss_ordering.append(b1)
            brains = next_round_brains

        loss_ordering.append(brains[0]) # add the one that never lost!

        return loss_ordering[-1 * winner_pool_size:]