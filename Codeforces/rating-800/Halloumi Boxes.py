import sys

input = sys.stdin.read
data = input().split()
index = 0

t = int(data[index]) # Read the number of test cases
index += 1

for _ in range(t):
	n = int(data[index]) # Read the number of boxes
	k = int(data[index + 1]) # Read the maximum length of subarray that can be reversed
	index += 2

	a = list(map(int, data[index:index + n])) # List to store the numbers on the boxes
	index += n

	# Create a copy of the original list
	copy_a = a[:]
	copy_a.sort() # Sort the copied list in non-decreasing order

	# Check if the original list is already sorted or if k > 1
	if copy_a == a or k > 1:
		print("YES") # If true, print "YES"
	else:
		print("NO") # Otherwise, print "NO"

# Time Complexity (TC): O(nlogn) = O(100log2(100)) = 100*7 = 700
# Space Complexity (SC): O(n)