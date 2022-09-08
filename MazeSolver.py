##Nmae:Jinhao Zhong NSID:jiz263  student#:11204178 Cmpt145  L05

def readfile(file):
    square =[]
    with open(file, "r") as maze:
        for line in maze:
            data = line.split()
            square.append(data)
        maze.close()
    cols = len(square[0])
    rows = len(square)

    return square,rows,cols

def makemaze(maze):
	for x in range(len(maze)):
		for y in range(len(maze[0])):
			print(Maze[x][y])
		print('')
