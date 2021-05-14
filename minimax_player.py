# Player Template
# IMPORTANT: 	This module must have a function called play
# 				that receives a game and return a tuple of
#				two integers who represent a valid move on
#				the game.

from game_logic import *
from minimax import minimax

# game_logic
#
# 	EMPTY		
#	PLAYER[0]	
#	PLAYER[1]

# game
# 	-> current (W or B)
#		It refers to the player who must play in
#		this turn.
#	-> indexing
#		game[i,j] return the player who have played
#		on position <i;j> (compare with PLAYER[0] 
#		and PLAYER[1]). EMPTY if none player have
#		played there.
#	-> neighbour
#		creates an iterator that yields all 
#		coordinates <x;y> who are neighbour of 
#		current coordinates.
#
#		for nx, ny in game.neighbour(x, y):
#			print(nx, ny)


def play(game, player):
	# Code Here
	# Random player implementation (just delete it)

	return minimax(game, player, 3, heuristic_coneccted, moves)


def moves(game, player):
	for x in range(game.size):
		for y in range(game.size):
			if game[x, y] == EMPTY:
				yield (x, y)
def heuristic_coneccted(game, player):
    oponent='W' if player=='B' else 'B'
    
    ccp=countBetterConnected(game,player)
    cco=countBetterConnected(game,oponent)
    
    return (cco-ccp)/max(ccp,cco)

def getRelevantNeighbors(game, player, x, y):
    relevantNeighborhoodWhite = [(-1,1),(0,1),(1,-1),(0,-1)]
    relevantNeighborhoodBlack = [(1,-1),(1,0),(-1,-1),(-1,0)]
    neighborhood=[]
    
    if player == 'W':
        neighborhood=relevantNeighborhoodWhite
    else:
        neighborhood=relevantNeighborhoodBlack
    for neig in neighborhood:
        nx, ny = x+ neig[0], y + neig[1]	
        if game.checkInside(nx, ny):
            yield nx, ny

def countBetterConnected(game, player):
    counted = set()
    connected = 0
    
    for i in range(game.size):
        for j in range(game.size):
            if game[i,j] == player:
                neighbors = getRelevantNeighbors(game,player,i,j)
                for n in neighbors:
                    r, c= n
                    if game[i,j] == player and n not in counted:
                        counted.add((r,c))
                        connected += 1
    return connected

def countConnected(game, player):
    counted = set()
    connected = 0
    
    for i in range(game.size):
        for j in range(game.size):
            if game[i,j] == player:
                neighbors = game.neighbour(i,j)
                for n in neighbors:
                    r, c= n
                    if game[i,j] == player and n not in counted:
                        counted.add((r,c))
                        connected += 1
    return connected