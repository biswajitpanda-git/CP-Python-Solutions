import sys

input_data = sys.stdin.read().split()
index = 0

n =int(input_data[index])
index += 1
arr = list(map(abs, map(int, input_data[index:index+n])))
req_val = min(arr)
print(req_val)
