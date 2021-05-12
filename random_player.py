from game_logic import *
import random

def play(game, player):
	available_moves = []
	
	for i in range(game.size):
		for j in range(game.size):
			if game[i, j] == EMPTY:
				available_moves.append((i,j))

	return random.choice(available_moves)