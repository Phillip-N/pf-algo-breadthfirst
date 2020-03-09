class Maze(object):
# O is defined as the start of the maze object
# X is defined as the end
# # is defined as the obstacles

	def __init__(self, maze):
		self.maze = maze
		self.ppath = []
		self.solutionFound = False
		
	def findStartEnd(self):
		for i in range(len(self.maze)):
			for y in range(len(self.maze[0])):
				if self.maze[i][y] == 'O':
					self.start = [i, y]
				elif self.maze[i][y] == 'X':
					self.end = [i, y]

	def findppath(self):
		for i in range(len(self.maze)):
			for y in range(len(self.maze[0])):
				if self.maze[i][y] != '#':
					self.ppath.append([i, y])
					
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
		print('\n')

	def findpath(self):
		self.findStartEnd()
		self.findppath()
		
		queue = list()
		queue.append(self.start)
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

			# Possible steps (up down left right)
			if (([i+1, y]) in self.ppath) and ([i+1, y] != lastcoord):
				# if checkend == true break and print, else keep going
				if ([i+1, y]) == self.end:
					self.solutionFound = True
					new_path = step.copy()
					new_path.append([i+1, y])
					self.printmaze(new_path)
				else:
					new_path = step.copy()
					new_path.append([i+1, y])
					queue.append(new_path)
						
			if ([i-1, y]) in self.ppath and ([i-1, y] != lastcoord):
				if ([i-1, y]) == self.end:
					self.solutionFound = True
					new_path = step.copy()
					new_path.append([i-1, y])
					self.printmaze(new_path)			
				else:
					new_path = step.copy()
					new_path.append([i-1, y])
					queue.append(new_path)
					
			if ([i, y+1]) in self.ppath and ([i, y+1] != lastcoord):
				if ([i, y+1]) == self.end:
					self.solutionFound = True
					new_path = step.copy()
					new_path.append([i, y+1])
					self.printmaze(new_path)
				else:
					new_path = step.copy()
					new_path.append([i, y+1])
					queue.append(new_path)
			
			if ([i, y-1]) in self.ppath and ([i, y-1] != lastcoord):
				if ([i, y-1]) == self.end:
					self.solutionFound = True
					new_path = step.copy()
					new_path.append([i, y-1])
					self.printmaze(new_path)
				else:
					new_path = step.copy()
					new_path.append([i, y-1])
					queue.append(new_path)

			turn += 1

maze = [['O', ' ', '#', '#', '#', '#'],
		['#', ' ', '#', ' ', ' ', '#'],
		['#', ' ', '#', ' ', ' ', ' '],
		['#', ' ', '#', ' ', '#', ' '],
		['#', ' ', '#', ' ', '#', ' '],
		['#', ' ', ' ', ' ', '#', ' '],
		['#', '#', '#', '#', '#', 'X']]

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


