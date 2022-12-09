with open('input.txt', 'r') as file:
	data = file.read()



def find_start_of_message(n, data=data):
	character_buffer = []

	for i in range(len(data)):
		if len(character_buffer) < n:
			character_buffer.append(data[i])
			continue

		character_buffer.append(data[i])
		character_buffer = character_buffer[1:]

		if len(set(character_buffer)) == len(character_buffer):
			print(i + 1)
			break

find_start_of_message(4)

find_start_of_message(14)
