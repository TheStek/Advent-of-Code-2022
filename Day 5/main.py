import re

with open('input.txt', 'r') as file:
	data = file.read().split('\n')
change_point = list(filter(lambda x: x[1] == '', zip(range(len(data)), data)))[0][0]
setup = data[:change_point]

stack_list = []
for i in range(len(setup[-1])):
	stack_list.append([setup[x][i] for x in range(len(setup))])

stack_list = list(filter(lambda x: x[-1] != ' ', stack_list))
stack_list = list(map(lambda y: list(filter(lambda x: x != ' ', y)), stack_list))

stacks = {stack[-1]: stack[:-1] for stack in stack_list}

steps = data[change_point:]
step_nums = list(map(lambda x: re.findall('\d+', x), steps))
step_nums = list(filter(lambda x: len(x) ==  3, step_nums))


def perform_step(step):
	for i in range(int(step[0])):
		if len(stacks[step[1]]) != 0:
				stacks[step[2]].insert(0, stacks[step[1]][0])
				stacks[step[1]] = stacks[step[1]][1:]


def perform_step_multiple(step):
	n = int(step[0])
	items_to_move = stacks[step[1]][:n]
	stacks[step[1]] = stacks[step[1]][n:]
	stacks[step[2]] = items_to_move	+ stacks[step[2]]




for step in step_nums:
	perform_step_multiple(step)

for k in stacks.keys():
	print(k, stacks[k])
print(''.join([stacks[k][0] for k in stacks.keys()]))
