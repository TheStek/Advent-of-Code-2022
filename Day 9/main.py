import numpy as np

with open('input.txt', 'r') as file:
	data = file.read().split('\n')[:-1]

test = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''.split('\n')


def move(direction, head_coords, tail_coords, head = True):
	if head:
		if direction == 'U':
			head_coords[1] += 1
		elif direction == 'L':
			head_coords[0] -= 1
		elif direction == 'D':
			head_coords[1] -= 1
		elif direction == 'R':
			head_coords[0] += 1


	difference = head_coords - tail_coords

	# If head and tail are already touching do nothing
	if np.linalg.norm(difference) <= np.linalg.norm((1, 1)):
		
		return head_coords, tail_coords


	if difference[0] == 2 and difference[1] == 0:
		tail_coords[0] += 1
		
		return head_coords, tail_coords

	if difference[0] == -2 and difference[1] == 0:
		tail_coords[0] -= 1
		
		return head_coords, tail_coords

	if difference[1] == 2 and difference[0] == 0:
		tail_coords[1] += 1
		
		return head_coords, tail_coords

	if difference[1] == -2 and difference[0] == 0:
		tail_coords[1] -= 1
		
		return head_coords, tail_coords


	tail_coords += np.sign(difference)
	
	return head_coords, tail_coords

def part_1(commands = data):
	head_pos = np.array((0, 0))
	tail_pos = np.array((0, 0))

	tail_trail = [tail_pos.copy()]
	for command in data:
		direction, n = command.split(' ')
		# print(direction, n)
		for i in range(int(n)):
			head_pos, tail_pos = move(direction, head_pos, tail_pos)
			tail_trail.append(tail_pos.copy())
			# print(head_pos, tail_pos)

	print(len(np.unique(tail_trail, axis = 0)))



def part_2(commands = data):
	rope = [np.array((0, 0)) for i in range(10)]

	tail_trail = [rope[-1].copy()]
	for command in data:
		direction, n = command.split(' ')
		for i in range(int(n)):
			for h, t in zip(range(10), range(10)[1:]):
				rope[h], rope[t] = move(direction, rope[h], rope[t], h == 0)
			
			tail_trail.append(rope[-1].copy())
	print(rope)
	print(len(np.unique(tail_trail, axis = 0)))

part_1()
part_2()
