from game_logic import *
from importlib import import_module as load

SIZE = 4		# Size of the board

PLAYERS = [	'random_player',
			'rush_player',
			'minimax_player',
			]

#TODO: MAX_TIME Not implemented yet
MAX_TIME = 5	# Max time (seconds) of execution of play function per player
TOT_GAMES = 5 	# Tot games between players per color

# Log customization
PRINT_LOG = True
ACTIVE_LOG = True
OVERWRITE_LOG = False

class Player:
	def __init__(self, name, play_function):
		self.name = name
		self.play = play_function

def log(message):
	if PRINT_LOG:
		print(message)

	if ACTIVE_LOG:
		logfile = open('log.txt', 'a')
		logfile.write("%s\n"%message)
		logfile.close()

def fightLog(player1, player2, winner, message = ""):
	log("%s vs %s (Winner: %s) %s"%(player1.name, player2.name, winner.name, message))

def fight(player1, player2):
	game = Game(SIZE)
	players = player1, player2

	while game.winner() == EMPTY:
		cur_player = players[game.turn]
		# try:
			#TODO: Establish time limit of play execution
		move = cur_player.play(game.__clone__(), game.current())
		game.play(*move)
		# except BaseException as e:
		# 	fightLog(player1, player2, player1 if game.turn == 1 else player2, ">>> Error: %s"%e)

	val = game.winner() == WHITE
	fightLog(player1, player2, player1 if val else player2)
	return val

def tourney():
	if OVERWRITE_LOG:
		logfile = open("log.txt", 'w')
		logfile.close()

	tot = len(PLAYERS)

	log("===============")
	log("Tourney")
	log("===============")

	players = []
	points = [0] * tot
	for p in PLAYERS:
		mod = load(p)
		players.append(Player(p, mod.play))

	for i in range(tot):
		for j in range(i + 1, tot):
			
			for k in range(TOT_GAMES):
				if fight(players[i], players[j]):
					points[i] += 1
				else:
					points[j] += 1
			
			for k in range(TOT_GAMES):
				if fight(players[j], players[i]):
					points[j] += 1
				else:
					points[i] += 1

	ranking = sorted([(points[i], players[i].name) for i in range(tot)], reverse = True)
	log('')
	log("Ranking:")
	for pnt, ply in ranking:
		log("%s %d"%(ply, pnt))
	log('')

if __name__ == '__main__':
	tourney()