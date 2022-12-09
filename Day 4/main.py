def get_range(string):
	start, end = string.split('-')
	return list(range(int(start), int(end) + 1))

def check_containing_ranges(r1, r2):
	s1, e1 = r1.split('-')
	s2, e2 = r2.split('-')

	if int(s1) <= int(s2) and int(e1) >= int(e2):
		return True

	return False
	


with open('input.txt', 'r') as file:
	data = file.read().split('\n')

print(data[0].split(',')[0].split('-'))


def check_pair(line):
	if line == '':
		return 0
	l1, l2 = line.split(',')
	if check_containing_ranges(l1, l2) or check_containing_ranges(l2, l1):
		return 1
	return 0

print(sum(map(check_pair, data)))


def check_overlap_pair(line):
	if line == '':
		return 0
	r1, r2 = line.split(',')
	if len(set(get_range(r1)).intersection(get_range(r2))) > 0:
		return 1
	return 0

print(sum(map(check_overlap_pair, data)))