import random
def grid():
	for i in range(26):
		print(end = '-')
	print()
def board():
	for i in range(5):
		grid()
		for j in range(5):
			t = i*5+j+1
			if t in marked:
				print(end = '| ｘ ')
			elif t < 10:
				print('| 0%d' % (t), end = ' ')
			else:
				print('| %d' % (t), end = ' ')
		print('|')
	grid()
marked = []
board()
for turn in range(8):
	marked.append(int(input('turn %d\nchoose a number\n' % (turn+1))))
	while True:
		num = random.randrange(1, 25)
		if not num in marked:
			marked.append(num)
			break
	board()
bingo = 0
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
	print('win')
else:
	print('lose')
