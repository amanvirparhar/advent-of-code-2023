def checkAround(currNum, lines, i, j):
	
	if currNum == "475":
		print("left: " + lines[i][j - len(currNum)])
		print("right: " + lines[i][j + 1])

		print("up")
		if i - 1 >= 0:
			for char in lines[i - 1][max(0, j - len(currNum)):min(j + 2, len(lines[i - 1]))]:
				print(char)
		
		print("down")
		if i + 1 < len(lines):
			for char in lines[i + 1][max(0, j - len(currNum)):min(j + 2, len(lines[i - 1]))]:
				print(char)

		print()
		print()
		print()
				

	if j - len(currNum) >= 0 and not lines[i][j - len(currNum)].isdigit() and lines[i][j - len(currNum)] != '.':
		return True
	
	if j + 1 < len(lines[i]) and not lines[i][j + 1].isdigit() and lines[i][j + 1] != '.':
		return True 

	if i - 1 >= 0:
		for char in lines[i - 1][max(0, j - len(currNum)):min(j + 2, len(lines[i - 1]))]:
			if not char.isdigit() and char != '.':
				return True

	if i + 1 < len(lines):
		for char in lines[i + 1][max(0, j - len(currNum)):min(j + 2, len(lines[i - 1]))]:
			if not char.isdigit() and char != '.':
				return True

	if currNum == "475": print("RETURNED FALSE")
	
	return False

total = 0

with open('input.txt') as f:
	lines = f.readlines()

	for i, line in enumerate(lines):
		line = line.rstrip('\n')
		currNum = ""

		for j, char in enumerate(line):
			if char.isdigit():
				currNum += char
			else:
				if currNum != "" and checkAround(currNum, lines, i, j - 1):
					total += int(currNum)
				currNum = ""
		
		if currNum != "" and checkAround(currNum, lines, i, j):
			total += int(currNum)

print(total)