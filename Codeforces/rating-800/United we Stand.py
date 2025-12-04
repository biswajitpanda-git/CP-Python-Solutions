import sys

input = sys.stdin.read

data = input().split()

index = 0

t = int(data[index]) # Number of test cases
index += 1

for _ in range(t):
	n = int(data[index]) # Length of array a
	index += 1
	a = list(map(int, data[index:index + n])) # Array a of length n
	index += n

	# Find the maximum element in array a
	mx = max(a)
	b = [] # Array b
	c = [] # Array c

	# Distribute elements into b and c
	for value in a:
		if value != mx:
			b.append(value) # Add to b if not the maximum
		else:
			c.append(value) # Add to c if it is the maximum

	# Check if array b is empty, meaning all elements were the same
	if len(b) == 0:
		print(-1) # No valid distribution possible
	else:
		# Output the sizes of arrays b and c
		print(len(b), len(c))
		# Output elements of array b
		print(' '.join(map(str, b)))
		# Output elements of array c
		print(' '.join(map(str, c)))

# Time Complexity (TC): O(n) = O(100)
# Space Complexity (SC): O(n) = O(100)