from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import tensorflow
import names
import numpy
from random import random




class Brain:

    first = None
    last = None
    generation = 0

    def __init__(self, model = None, wins = None, losses = None, first = None, last = None, generation=None):

        if first == None:
            self.first = names.get_first_name()
        else:
            self.first = first
        if last == None:
            self.last = names.get_last_name()
        else:
            self.last = last
        self.name = "{} {} ({})".format(self.first, self.last, self.generation)

        if generation != None:
            self.generation = generation

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

    def record_loss(self):
        self.losses += 1

    def set_board(self,board):
        self.board = board

    def set_player_num(self, player_num):
        self.player_num = player_num

    def create_model(self, hidden_node_count=28, hidden_node_count2=None):
        input_layer = tensorflow.keras.Input(shape=(122,))

        hidden_layer = Dense(hidden_node_count)(input_layer)

        output_layer = Dense(6, activation='softmax')(hidden_layer)

        return tensorflow.keras.Model(inputs=input_layer, outputs=output_layer)

    def get_game_state(self):
        if self.player_num == 1:
            return self.board.getState()
        else:
            return self.board.get_opponent_board().getState()


    def predict (self):
        state = self.get_game_state()
        inputs = []
        # 0 and 7 are the points, the others are the spaces
        inputs.append (float( state[0] ) / 50.0)
        inputs.append (float( state[7] ) / 50.0)
        for stone_count in state[1:7]:
            for i in range(10):
                if stone_count == i:
                    inputs.append(1)
                else:
                    inputs.append(0)
        for stone_count in state[8:]:
            for i in range(10):
                if stone_count == i:
                    inputs.append(1)
                else:
                    inputs.append(0)


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

    def getNewMutant(self, mutation_chance = .25, max_mutation = .1) -> tensorflow.keras.Model:
        new_mutant_weights = tensorflow.keras.models.clone_model( self.model )
        new_mutant_weights.set_weights(self.model.get_weights())

        w = new_mutant_weights.get_weights()

        for i in range(len(w)):
            if type(w[i]) == numpy.ndarray:
                for j in range(len(w[i]) ):
                    if type(w[i][j]) == numpy.ndarray:
                        if type(w[i][j]) == numpy.ndarray:
                            for k in range(len(w[i][j]) ):
                                if random() < mutation_chance:
                                    w[i][j][k] = max (-1, min( 1,  w[i][j][k] + (random() * max_mutation * 2) - max_mutation))

        new_mutant_weights.set_weights(w)

        mutant = Brain(new_mutant_weights, wins=0, losses=0, first=self.first, last=self.last, generation=self.generation + 1)
        return mutant


    def __str__(self):
        return "{} ({} wins and {} losses)".format(self.name, self.wins, self.losses)