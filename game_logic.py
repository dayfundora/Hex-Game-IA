EMPTY = '.'
WHITE = 'W'
BLACK = 'B'
PLAYER = [WHITE, BLACK]

class Game:
	""" White should connect left side with right side.
		Black should connect upper side with lower side.
		White makes first move.

		White winning example:
		. . B .
		 W W B W
		  . W W B
		   . B . .
	"""
	def __init__(self, size):
		self.size = size
		self.board = [[EMPTY] * size for i in range(size)]
		self.ds = [-1] * (size * size + 4)
		self.turn = 0

	# Disjoint set

	def root(self, a):
		if self.ds[a] < 0:
			return a
		else:
			self.ds[a] = self.root(self.ds[a])
			return self.ds[a]

	def join(self, a, b):
		a, b = self.root(a), self.root(b)
		if a == b:
			return False
		if self.ds[a] < self.ds[b]:
			a, b = b, a
		self.ds[b] += self.ds[a]
		self.ds[a] = b
		return True

	# End disjoint set

	def current(self):
		return PLAYER[self.turn]

	def checkInside(self, x, y, empty = False):		
		return 0 <= x and x < self.size and 0 <= y and y < self.size

	def __getitem__(self, pos):
		x, y = pos
		GameError.test(self.checkInside(x, y), "Invalid move. Position <%d;%d> out of range."%(x, y))
		return self.board[x][y]

	def neighbour(self, x, y):
		self[x, y]
		neighborhood = [(-1, 1), (0, 1), (1, 0), (1, -1), (0, -1), (-1, 0)]

		for neig in neighborhood:
			nx, ny = x + neig[0], y + neig[1]
			if self.checkInside(nx, ny):
				yield nx, ny

	def position(self, x, y):
		return self.size * x + y + 4

	def play(self, x, y):
		value = self[x, y]
		GameError.test(value == EMPTY, "Invalid move. Position <%d;%d> is not empty."%(x, y))

		self.board[x][y] = PLAYER[self.turn]
		
		if self.turn == 0:			
			if y == 0:
				self.join(0, self.position(x, y))
			elif y + 1 == self.size:
				self.join(1, self.position(x, y))
		else:
			if x == 0:
				self.join(2, self.position(x, y))
			elif x + 1 == self.size:
				self.join(3, self.position(x, y))

		for nx, ny in self.neighbour(x, y):
			if self[nx, ny] == self[x, y]:
				self.join(self.position(nx, ny), self.position(x, y))

		self.turn ^= 1

	def clone_play(self, x, y):
		clone = self.__clone__()
		clone.play(x, y)
		return clone

	def winner(self):
		if self.root(0) == self.root(1):
			return PLAYER[0]
		if self.root(2) == self.root(3):
			return PLAYER[1]
		return EMPTY

	def __clone__(self):
		game = Game(self.size)
		game.board = [row[:] for row in self.board]
		game.ds = self.ds[:]
		game.turn = self.turn
		return game

	def __str__(self):
		ans = ""
		for i in range(self.size):
			ans += " " * i
			for j in range(self.size):
				ans += " %s"%self[i, j]
			ans += "\n"
		return ans

	def __repr__(self):
		return self.__str__()

class GameError(BaseException):
	def test(value, e):
		# Assert
		if not value:
			raise GameError(e)

def testGame(SIZE = 4):
	game = Game(SIZE)
	print(game)
	while game.winner() == EMPTY:
		x, y = list(map(int, input().split()))
		try:
			game.play(x, y)
		except GameError as e:
			print(e)
		print(game)
	print("WINNER: ", game.winner())

if __name__ == '__main__':
	testGame()