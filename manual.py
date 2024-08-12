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
