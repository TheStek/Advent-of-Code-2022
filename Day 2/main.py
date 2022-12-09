play_scores = {'rock': 1, 'paper': 2, 'scissors': 3}

def check_win(op, player):
	if op == player:
		return 3
	if op == 'rock':
		if player == 'scissors':
			return 0
		if player == 'paper':
			return 6

	if op == 'paper':
		if player == 'rock':
			return 0
		if player == 'scissors':
			return 6

	if op == 'scissors':
		if player == 'paper':
			return 0
		if player == 'rock':
			return 6


op_play = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
player_play = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}

with open('input.txt', 'r') as file:
	data = file.read().split('\n')[:-1]

games = list(map(lambda x: (op_play[x[0]], player_play[x[2]]), data))


score_from_play = list(map(lambda x: play_scores[x[1]], games))
score_from_result = list(map(lambda x: check_win(*x), games))

print(sum(score_from_result) + sum(score_from_play))


mapping_2 = {
'A X' : ('rock', 'scissors'),
'A Y' : ('rock', 'rock'),
'A Z' : ('rock', 'paper'),
'B X' : ('paper', 'rock'),
'B Y' : ('paper', 'paper'),
'B Z' : ('paper', 'scissors'),
'C X' : ('scissors', 'paper'),
'C Y' : ('scissors', 'scissors'),
'C Z' : ('scissors', 'rock'),
}

games_2 = list(map(lambda x: mapping_2[x], data))
score_from_play2 = list(map(lambda x: play_scores[x[1]], games_2))
score_from_result2 = list(map(lambda x: check_win(*x), games_2))

print(sum(score_from_result2) + sum(score_from_play2))