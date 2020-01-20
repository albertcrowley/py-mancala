from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import tensorflow
import names



class Brain:

    def __init__(self, model = None, wins = None, losses = None):
        self.first = names.get_first_name()
        self.last = names.get_last_name()
        self.name = "{} {}".format(self.first, self.last)


        self.wins = wins
        self.losses = losses

        if self.wins == None: self.wins = 0
        if self.losses == None: self.losses = 0

        if model == None:
            self.model = self.create_model()
        else:
            self.model = model

    def get_record(self):
        return (self.wins, self.losses)

    def record_win(self):
        self.wins += 1
        print ("{} recording win number {}".format(self.last, self.wins))

    def record_loss(self):
        self.losses += 1

    def set_board(self,board):
        self.board = board

    def set_player_num(self, player_num):
        self.player_num = player_num

    def create_model(self, hidden_node_count=28, hidden_node_count2=28):
        input_layer = tensorflow.keras.Input(shape=(14,))

        hidden_layer = Dense(hidden_node_count)(input_layer)
        hidden_layer2 = Dense(hidden_node_count2)(hidden_layer)

        output_layer = Dense(6, activation='softmax')(hidden_layer2)

        return tensorflow.keras.Model(inputs=input_layer, outputs=output_layer)

    def get_game_state(self):
        if self.player_num == 1:
            return self.board.getState()
        else:
            return self.board.get_opponent_board().getState()


    def predict (self):
        inputs = [ min(x / 10.0, 1.0) for x in self.get_game_state() ]

        ys = self.model.predict( [  inputs ] )

        move = -1
        best = 0
        for i in range( len(ys[0])):
            if ys[0][i] > best:
                best = ys[0][i]
                move = i

        return (move, best)

    def getName(self):
        return self.name

    def __str__(self):
        return "{} ({} wins and {} losses)".format(self.name, self.wins, self.losses)