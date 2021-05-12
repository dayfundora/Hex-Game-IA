from game_logic import *

def play(game, player):
	for i in range(game.size):
		for j in range(game.size):
			if game[i, j] == EMPTY:
				return i, j