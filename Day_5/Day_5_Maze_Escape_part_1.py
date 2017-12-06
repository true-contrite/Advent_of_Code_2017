def get_array(filename):

	array = []

	with open(filename) as inputfile:

		for line in inputfile:

			array.append(int(line.rstrip()))

	return array

def maze_escape(maze):

	exit_cond = False
	current_index = 0
	count = 0

	try:

		mark = current_index
		current_index += maze[current_index]
		maze[mark] += 1
		count += 1

	except:

		return count 







array = get_array("input_maze.txt")
print(maze_escape(array))