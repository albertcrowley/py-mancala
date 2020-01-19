from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import tensorflow




class Brain:

    def __init__(self, model = None):
        if model == None:
            self.model = self.create_model()
        else:
            self.model = model


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
