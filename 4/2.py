import json

with open("input.txt") as file:
	total = 0
	copies = {}

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
		
		orig_card = i + 1
		print(orig_card)

		done = False
		
		for c in card_map:
			if not done:
				if orig_card in copies:
					copies[orig_card] += 1
				else:
					copies[orig_card] = 1
				done = True

		if orig_card in copies:
			for j in range(copies[orig_card]):
				curr_card = i + 2
				for c in card_map:
					if card_map[c] > 1:
						if curr_card in copies:
							copies[curr_card] += 1
						else:
							copies[curr_card] = 1
						
						curr_card += 1
		else:
			curr_card = i + 2

			for c in card_map:
				if card_map[c] > 1:
					if curr_card in copies:
						copies[curr_card] += 1
					else:
						copies[curr_card] = 1
					
					curr_card += 1

	for copy in copies:
		total += copies[copy]
	
	print(total)