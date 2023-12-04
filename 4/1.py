with open("input.txt") as file:
	total = 0

	for i, line in enumerate(file):
		line = line.rstrip()
		line = line.split(': ')[1]

		card_map = {}

		for winner in line.split(' | ')[0].split():
			if winner in card_map:
				card_map[winner] += 1
			else:
				card_map[winner] = 1
		
		for card in line.split(' | ')[1].split():

			if card in card_map:
				card_map[card] += 1
			else:
				card_map[card] = 1
		
		matches = 0

		for c in card_map:
			if card_map[c] > 1:
				if matches == 0:
					matches = 1
					print(c)
				else:
					matches *= 2
		
		total += matches

	print(total)