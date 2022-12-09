class Folder:
	folders = []
	def __init__(self, name, parent):
		self.name = name
		self.parent = parent
		self.contents = {}
		Folder.folders.append(self)

	def add_file(self, filesize, filename):
		self.contents[filename] = filesize

	def add_folder(self, folder_name):
		sub_folder = Folder(folder_name, self)
		self.contents[folder_name] = sub_folder

	def get_total_size(self):
		size = 0
		for item in self.contents.keys():
			if type(self.contents[item]) == Folder:
				size += self.contents[item].get_total_size()
			else:
				size += self.contents[item]
		return size

	def print_structure(self, depth = 0):
		print(f"{'-' * depth}dir {self.name}")
		for k in self.contents.keys():
			if type(self.contents[k]) == Folder:
				self.contents[k].print_structure(depth + 1)
			else:
				print(f"{'-' * (depth + 1)}{k}")


with open('input.txt', 'r') as file:
	data = file.read().split('\n')

root = Folder('root', None)
current_dir = root


for line in data:
	if line == '':
		continue
	if line[:4] == '$ cd':
		destination = line.split(' ')[-1]
		if destination == '/':
			current_dir = root
			continue
		if destination == '..':
			current_dir = current_dir.parent
			continue
		current_dir = current_dir.contents[destination]
		continue


	if line == '$ ls':
		continue

	try:
		p1, p2 = line.split(' ')
	except:
		print(line)

	if p1 == 'dir':
		current_dir.add_folder(p2)
		continue

	current_dir.add_file(int(p1), p2)

sizes = list(map(lambda x: x.get_total_size(), Folder.folders))
print(sum(filter(lambda x: x<=100000, sizes)))



total_used = root.get_total_size()
remaining_free = 70000000 - total_used
needed_to_delete = 30000000 - remaining_free

print(sorted(filter(lambda x: x>= needed_to_delete, sizes)))

