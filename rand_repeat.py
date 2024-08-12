import random
win, lose = 0, 0
for game in range(10000):
	marked = []
	bingo = 0
	for turn in range(16):
		while True:
			num = random.randrange(1, 25)
			if not num in marked:
				marked.append(num)
				break
	for i in range(5):
		row = []
		for j in range(5):
			row.append(i*5+j+1)
		if all(item in marked for item in row):
			bingo += 1
	for i in range(5):
		column = []
		for j in range(5):
			column.append(i+1+j*5)
		if all(item in marked for item in column):
			bingo += 1
	diag1 = [1, 7, 13, 19, 25]
	diag2 = [5, 9, 13, 17, 21]
	if all(item in marked for item in diag1):
		bingo += 1
	if all(item in marked for item in diag2):
		bingo += 1
	if bingo == 4:
		win += 1
	else:
		lose += 1
print(win, end = ' ')
print(lose)
input()