product_sum = 0

with open("input.txt") as file:
	for i, line in enumerate(file):
		line = line.rstrip()
		line = line.split(': ')[1]
		
		id = i + 1

		max_red = 0
		max_green = 0
		max_blue = 0
		product = 0
		
		for subgame in line.split('; '):
			for draw in subgame.split(', '):
				num = draw.split(' ')[0]
				color = draw.split(' ')[1]

				if color == "red":
					max_red = max(int(num), max_red)
				elif color == "green":
					max_green = max(int(num), max_green)
				elif color == "blue":
					max_blue = max(int(num), max_blue)
		
		product = max_red * max_green * max_blue
		product_sum += product

print(product_sum)