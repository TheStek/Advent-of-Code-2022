with open('input.txt', 'r') as file:
	data = file.read().split('\n')

elves = [[]]

for entry in data:
	if entry == '':
		elves.append([])
	else:
		elves[-1].append(int(entry))

totals = list(map(sum, elves))
print(max(totals))
print(sum(sorted(totals)[-3:]))