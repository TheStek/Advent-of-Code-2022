def get_priority(item):
	if item == item.upper():
		return ord(item) - ord('A') + 27
	else:
		return ord(item) - ord('a') + 1

def get_compartments(rucksack):
	items = list(map(get_priority, rucksack))
	return items[:len(items)//2], items[len(items)//2:]

def get_sum_priorities_of_common(rucksack):
	comp_1, comp_2 = get_compartments(rucksack)
	return sum(set(comp_1).intersection(comp_2))

with open('input.txt', 'r') as file:
	rucksacks = file.read().split('\n')

print(sum(map(get_sum_priorities_of_common, rucksacks)))

# ----------- Part 2 ----------

def get_common_between_group(item_groups):
	return sum(set(item_groups[0]).intersection(item_groups[1]).intersection(item_groups[2]))


N = len(rucksacks)
total = 0
for i in range(N//3):
	group = [list(map(get_priority, rucksacks[i*3 + x])) for x in range(3)]
	total += get_common_between_group(group)

print(total)
