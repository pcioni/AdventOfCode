import sys

def parseInput(filename):
    f = open(filename, "r")
    return f.readlines()[0].split(', ')

instructions = parseInput(sys.argv[1])
direction = 0
directions = [(1,0), (0,1), (-1,0), (0,-1)]
location = [0,0]

for command in instructions:
	turn = command[0]
	if turn == 'L':
		direction -= 1
	elif turn == 'R':
		direction += 1

	amount = int(command[1:])
	location[0] += directions[direction % 4][0] * amount
	location[1] += directions[direction % 4][1] * amount

print abs(location[0]) + abs(location[1])