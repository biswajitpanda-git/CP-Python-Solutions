import sys

input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1

for _ in range(t):
	a = int(data[index])
	b = int(data[index + 1])
	c = int(data[index + 2])
	index += 3

	if c % 2 == 1:  # odd
		if b > a:
			print("Second")  # Katie wins
		else:
			print("First")  # Anna wins
	else:  # even
		if a > b:
			print("First")
		else:
			print("Second")