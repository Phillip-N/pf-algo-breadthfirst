class Maze(object):
# O is defined as the start of the maze object
# X is defined as the end
# # is defined as the obstacles

	def __init__(self, maze):
		self.maze = maze
		self.ppath = []
		self.solutionFound = False
		
	# Finds the start and end nodes in maze
	def findStartEnd(self):
		for i in range(len(self.maze)):
			for y in range(len(self.maze[0])):
				if self.maze[i][y] == 'O':
					self.start = [i, y]
				elif self.maze[i][y] == 'X':
					self.end = [i, y]

	# Finds the valid moves based on an iteration of the maze
	# and checking for '#' obstacles
	def findppath(self):
		for i in range(len(self.maze)):
			for y in range(len(self.maze[0])):
				if self.maze[i][y] != '#':
					self.ppath.append([i, y])
					
	# Prints the maze based on the path that reaches end node
	def printmaze(self, path):
		for i in range(len(self.maze)):
			for y in range(len(self.maze[0])):
				if ([i, y]) in path:
					if y == len(self.maze[0])-1:
						print('O')
					else:
						print('O', end=' ')
				else:
					if y == len(self.maze[0])-1:
						print(self.maze[i][y])
					else:
						print(self.maze[i][y], end=' ')

	# Finds the shortest path to the end node by iterating through
	# all possible moves
	def findpath(self):
		self.findStartEnd()
		self.findppath()
		
		queue = list()
		queue.append(self.start)
		visited_nodes = list()
		turn = 0
		
		while self.solutionFound == False:
			if turn >= 1:
				step = queue.pop(0)
				lastcoord = step[-1]
				i = lastcoord[0]
				y = lastcoord[1]
			else:
				lastcoord = None
				step = list()
				step.append(queue.pop(0))
				i = step[0][0]
				y = step[0][1]

			for new_pos in [(1,0), (-1,0), (0,1), (0,-1)]:
				move = [new_pos[0] + i, new_pos[1] + y]
				
				# Checks if move is valid and non duplicate
				if ((move in self.ppath) and (move != lastcoord) and
				move not in visited_nodes):
					new_path = step.copy()
					new_path.append(move)
					visited_nodes.append(move)
					
					if move == self.end:
						self.solutionFound = True
						self.printmaze(new_path)
						print('\n')
					else:
						queue.append(new_path)
					
			turn += 1

# test maze 1
maze = [['O', ' ', '#', '#', '#', '#'],
		['#', ' ', '#', ' ', ' ', '#'],
		['#', ' ', '#', ' ', ' ', ' '],
		['#', ' ', '#', ' ', '#', ' '],
		['#', ' ', '#', ' ', '#', ' '],
		['#', ' ', ' ', ' ', '#', ' '],
		['#', '#', '#', '#', '#', 'X']]

# test maze 2
maze2 = [['#', '#', '#', '#', '#', 'X'],
		[' ', '#', ' ', '#', ' ', ' '],
		[' ', '#', ' ', '#', ' ', '#'],
		[' ', ' ', ' ', '#', ' ', '#'],
		[' ', '#', ' ', '#', ' ', '#'],
		[' ', '#', ' ', ' ', ' ', '#'],
		['O', '#', '#', '#', '#', '#']]	


mymaze = Maze(maze)
mymaze.findpath()

mymaze2 = Maze(maze2)
mymaze2.findpath()

