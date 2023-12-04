valid_games = 0

with open("input.txt") as file:
	for i, line in enumerate(file):
		line = line.rstrip()
		line = line.split(': ')[1]
		game_bad = False
		
		id = i + 1

		for subgame in line.split('; '):
			for draw in subgame.split(', '):
				num = draw.split(' ')[0]
				color = draw.split(' ')[1]

				if color == "red" and int(num) > 12:
					game_bad = True
				elif color == "green" and int(num) > 13:
					game_bad = True
				elif color == "blue" and int(num) > 14:
					game_bad = True
			
			if game_bad:
				break
		
		if game_bad:
			continue
		else:
			valid_games += id

print(valid_games)