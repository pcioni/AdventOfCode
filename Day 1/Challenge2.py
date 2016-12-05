import sys

# Takes in input location and returns list of instructions
def parseInput(filename):
    f = open(filename, "r")
    return f.readlines()[0].split(', ')

instructions = parseInput(sys.argv[1])
location = (0,0)
visited = [ (0,0) ]
direction = 0
directions = [(1,0), (0,1), (-1,0), (0,-1)]

for movement in instructions:
	turn = movement[0]
	if turn == 'L':
		direction -= 1
	elif turn == 'R':
		direction += 1

	amount = int(movement[1:len(movement)])

	for x in range(0, amount):
		# lol
		location = ( location[0] + (directions[direction % 4][0] * 1) , location[1] + (directions[direction % 4][1] * 1) )

		if location in visited:
			print abs(location[0]) + abs(location[1])
			exit()

		visited.append(location)
