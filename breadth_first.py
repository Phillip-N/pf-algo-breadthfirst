maze = [['O', ' ', '#', '#', '#', '#'],
		['#', ' ', '#', ' ', ' ', '#'],
		['#', ' ', ' ', ' ', ' ', '#'],
		['#', ' ', '#', ' ', ' ', '#'],
		['#', ' ', '#', ' ', ' ', '#'],
		['#', ' ', '#', ' ', ' ', ' '],
		['#', '#', '#', '#', '#', 'X']]


queue = list()
ppath = []
start = list()
end = list()
turn = 0
solutionFound = False

# Find start and end positions
for i in range(len(maze)):
	for y in range(len(maze[0])):
		if maze[i][y] == 'O':
			start = [i, y]
		elif maze[i][y] == 'X':
			end = [i, y]

# Definine possible move restrictions
for i in range(len(maze)):
	for y in range(len(maze[0])):
		if maze[i][y] != '#':
			ppath.append([i, y])
				
queue.append(start)
		
def possiblesteps(q):
	global solutionFound
	global turn
	
	if turn >= 1:
		step = q.pop(0)
		lastcoord = step[-1]
		i = lastcoord[0]
		y = lastcoord[1]
	else:
		step = list()
		step.append(q.pop(0))
		i = step[0][0]
		y = step[0][1]
	
	
	# Possible steps (up down left right)
	if (([i+1, y]) in ppath):
		# if checkend == true break and print, else keep going
		if checkEnd([i+1, y], end) == True:
			solutionFound = True
			new_path = step.copy()
			new_path.append([i+1, y])
			printmaze(maze, new_path)
		else:
			new_path = step.copy()
			new_path.append([i+1, y])
			q.append(new_path)
				
	if ([i-1, y]) in ppath:
		if checkEnd([i-1, y], end) == True:
			solutionFound = True
			new_path = step.copy()
			new_path.append([i-1, y])
			printmaze(maze, new_path)			
		else:
			new_path = step.copy()
			new_path.append([i-1, y])
			q.append(new_path)
			
	if ([i, y+1]) in ppath:
		if checkEnd([i, y+1], end) == True:
			solutionFound = True
			new_path = step.copy()
			new_path.append([i, y+1])
			printmaze(maze, new_path)
		else:
			new_path = step.copy()
			new_path.append([i, y+1])
			q.append(new_path)
	
	if ([i, y-1]) in ppath:
		if checkEnd([i, y-1], end) == True:
			solutionFound = True
			new_path = step.copy()
			new_path.append([i, y-1])
			printmaze(maze, new_path)
		else:
			new_path = step.copy()
			new_path.append([i, y-1])
			q.append(new_path)

			
	
def checkEnd(coord, end):
	if coord == end:
		return True
	else:
		return False
		
def printmaze(maze, path):
	for i in range(len(maze)):
		for y in range(len(maze[0])):
			if ([i, y]) in path:
				if y == len(maze[0])-1:
					print('+')
				else:
					print('+', end=' ')
			else:
				if y == len(maze[0])-1:
					print(maze[i][y])
				else:
					print(maze[i][y], end=' ')
				
def pathfind(q):
	global solutionFound
	global turn
	while solutionFound == False:
		possiblesteps(q)
		turn += 1 

		
pathfind(queue)
